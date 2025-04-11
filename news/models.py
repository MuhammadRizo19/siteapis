from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='news/images/', blank=True, null=True)
    video = models.FileField(upload_to='news/videos/', blank=True, null=True)
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
