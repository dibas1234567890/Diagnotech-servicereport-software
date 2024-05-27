from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import redirect

def group_required(group_name):
    def in_group(user):
        if user.groups.filter(name=group_name).exists():
            return True
        return False
    return user_passes_test(in_group)
