from django.db import models
from django.conf import settings


class Customer(models.Model):
    SELLER_ACCOUNT_CHOICES = [
        ('pro', 'professional'),
        ('normal', 'normal')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    seller = models.CharField(max_length=200,
                              choices=SELLER_ACCOUNT_CHOICES, null=True, blank=True)

    def __str__(self):
        return  self.user.first_name + ' - ' + self.user.last_name
