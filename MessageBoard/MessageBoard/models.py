from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= 'message'

    def __str__(self):
        return str(self.title)