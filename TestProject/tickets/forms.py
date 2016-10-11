# -*- coding:utf-8 -*-

from django.forms import ModelForm
from models import AdminComment,Comment,UserComment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'attached_file']


class AdminCommentForm(ModelForm):
    class Meta:
        model = AdminComment
        fields = ['text', 'attached_file']


class UserCommentForm(ModelForm):
    class Meta:
        model = UserComment
        fields = ['text', 'attached_file']