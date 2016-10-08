# -*- coding:utf-8 -*-

from django.forms import ModelForm
from models import AdminComment

class CommentForm(ModelForm):
    class Meta:
        model = AdminComment
        fields = ['text']