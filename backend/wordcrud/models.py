from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']
