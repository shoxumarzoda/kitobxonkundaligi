from django import template
from main.models import *
from django.contrib.auth.models import User
register = template.Library()


@register.simple_tag()
def get_top_books():
    return Book.objects.all()


@register.simple_tag()
def get_top_users():
    return User.objects.all()
