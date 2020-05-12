from rest_framework import serializers

from .models import Post, Attachment


class AttachmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('id', 'file')
        read_only_fields = ('id',)


# Use `attachments` as field name both read and write
# update field type at `to_representation`
class PostSerializers(serializers.ModelSerializer):
    attachments = serializers.ListField(
        child=serializers.FileField(),
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'attachments',
            'create_at',
            'update_at',
        )
        read_only_fields = ('id', 'create_at', 'update_at')

    def create(self, validated_data):
        attachments = validated_data.pop('attachments')
        post = super().create(validated_data)

        Attachment.objects.bulk_create(
            [Attachment(post=post, file=file) for file in attachments],
        )

        return post

    def to_representation(self, instance):
        self.fields['attachments'] = AttachmentSerializers(many=True)
        return super().to_representation(instance)


# Use `files` for file upload
# and use `attachments` as response name
"""
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
"""
