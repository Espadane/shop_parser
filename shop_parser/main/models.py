from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''Модель пользователя'''
    send_messages = models.BooleanField(default=False, verbose_name='Получать уведомления?')
    
    class Meta(AbstractUser.Meta):
        pass