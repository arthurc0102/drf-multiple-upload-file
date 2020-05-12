from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Attachment(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    file = models.FileField()

    def __str__(self):
        return f'{self.post_id}\'s file'
