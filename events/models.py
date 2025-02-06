from django.db import models

from users.models import CustomUser


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='events_images/', default='events_images/default.jpg')


    def __str__(self):
        return f"{self.title} ({self.location}) - {self.datetime.strftime('%d.%m.%Y %H:%M')}"