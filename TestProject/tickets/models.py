# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Ticket(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=500,verbose_name='Описание')
    #file
    user = models.ForeignKey(User)
    create_date = models.DateTimeField( verbose_name='Дата создания')
    status = models.BooleanField(default=False)


    def __unicode__(self):
        return self.title



class AdminComment(models.Model):
    text = models.CharField(max_length=300)
    #file
    ticket = models.ForeignKey(Ticket, default=None, related_name='admin_comments')
    user = models.ForeignKey(User,default=None)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

class UserComment(models.Model):
    text = models.CharField(max_length=300)
    #file
    ticket = models.ForeignKey(Ticket, default=None, related_name='user_comments')
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    #ava = models.ImageField(upload_to='avatars',blank=True)
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')

    def __unicode__(self):
        return self.user.get_full_name()
