from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
