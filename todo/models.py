from django.db import models
from django.utils import timezone


class List(models.Model):
    item_no = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    reminder_date = models.DateTimeField(
            blank=True, null=True)

    def add(self):
        self.reminder_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
