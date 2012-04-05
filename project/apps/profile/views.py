# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


@login_required()
def profile_details(request):
    return HttpResponseRedirect(reverse('profiles_profile_detail',
                              kwargs={ 'username': request.user.username }))
