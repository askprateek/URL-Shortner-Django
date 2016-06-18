from django.db import models

# Create your models here.

class Urldb(models.Model):
    weburl = models.URLField()
    shortened_link = models.CharField(max_length=10)

    def __str__(self):
        return self.weburl
