from django.db import models
from datetime import datetime
# Create your models here.


class Invites(models.Model):
    sender_subs = models.ForeignKey('Subscribers', on_delete=models.DO_NOTHING, related_name='sender')
    recipient_subs = models.ForeignKey('Subscribers', on_delete=models.DO_NOTHING, related_name='recipient')
    STATUS_CHOICES = [(0, 'not active'),
                      (1, 'active'),
                      (2, 'accepted')]

    status = models.IntegerField(default='active', choices=STATUS_CHOICES)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(year=2999,
                                                     month=12,
                                                     day=31,
                                                     hour=12))

    def __str__(self):
        return f'From {self.sender_subs_id} to {self.recipient_subs_id}'


class Subscribers(models.Model):
    phone = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone