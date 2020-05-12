from rest_framework import serializers

from .models import Post, Attachment


class AttachmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('id', 'file')
        read_only_fields = ('id',)


class PostSerializers(serializers.ModelSerializer):
    files = serializers.ListField(child=serializers.FileField(), write_only=True)  # noqa: E501
    attachments = AttachmentSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'files',
            'attachments',
            'create_at',
            'update_at',
        )
        read_only_fields = ('id', 'attachments', 'create_at', 'update_at')

    def create(self, validated_data):
        files = validated_data.pop('files')
        post = super().create(validated_data)
        Attachment.objects \
            .bulk_create([Attachment(post=post, file=file) for file in files])

        return post
