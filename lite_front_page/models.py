from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " " + self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        ordering = ["-created_at"]