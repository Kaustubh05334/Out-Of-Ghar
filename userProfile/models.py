from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=300,blank=True)
    def __str__(self):
        return self.message