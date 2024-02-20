from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.title