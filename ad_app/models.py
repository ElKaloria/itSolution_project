from django.db import models

# Create your models here.


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    amount_of_views = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title
