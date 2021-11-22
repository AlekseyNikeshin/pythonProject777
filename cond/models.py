from django.db import models
from django.conf import settings
from django.utils import timezone

class Cond(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    type = models.CharField(max_length=15)
    price = models.CharField(max_length=15)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()


    def __str__(self):
        return self.title
# Create your models here.