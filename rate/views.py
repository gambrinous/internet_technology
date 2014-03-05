# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from rate.models import Rate, Course


def index(request):
    context = RequestContext(request)
    top_five_list = UniCourse.objects.order_by('-rating')[:5]
    worst_five_list = UniCourse.objects.order_by('rating')[:5]
    latest_list = Rate.objects.order_by('-date')[:5]
    context_dict = {'topfive': top_five_list, 'worstfive': worst_five_list, 'latestfive': latest_list}
    return render_to_response('rate/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Here is the about page."}
    return render_to_response('rate/about.html', context_dict, context)


def contact(request):
    context = RequestContext(request)
    return render_to_response('rate/contact.html', context)