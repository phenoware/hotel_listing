from functools import wraps
from django.http import HttpResponseRedirect, HttpResponse
from dashboard.models import *
from partner.models import *
from hotels.models import *
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render,redirect


def check_vendor_account():
    def decorator(view_func):
        @wraps(view_func)
        def _is_logged_in(request, *args, **kwargs):
            if request.user.is_authenticated:
                if Partner.objects.filter(user_id = request.user.id).exists():
                    return view_func(request, *args, **kwargs)
                else:
                    logout(request)
                    messages.success(request, 'Yor are not authorised to access partner panel, Please contact with admin')
                    return HttpResponseRedirect('/partner/partner-login/')

            else:
                return view_func(request, *args, **kwargs)
        return _is_logged_in
    return decorator
