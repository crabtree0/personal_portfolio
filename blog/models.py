from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    author = models.CharField(max_length=30)
    date = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title

