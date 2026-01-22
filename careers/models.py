from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title