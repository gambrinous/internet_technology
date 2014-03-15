# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from rate.models import Rate, Course, University
from rate.forms import UserForm


def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        university_option = request.POST['university_options']
        course_option = request.POST['course_options']
        level_option = request.POST['level_options']
        year_option = request.POST['year_options']

        the_course = Course.objects.filter(university=university_option).filter(title=course_option).filter(level=level_option).filter(year=year_option)
        if the_course:
            for j in the_course:
                j.url = j.title.replace(' ','_')
            return HttpResponseRedirect('course/'+j.url)
        else:
            return HttpResponse('There is no such course. Please <a href="/rate/contact/">contact</a> the administrator to request it, or go back to <a href="/rate/">main page</a>.')
    else:
        top_five_list = Course.objects.order_by('-stored_average_rating')[:5]
        worst_five_list = Course.objects.order_by('stored_average_rating')[:5]
        latest_list = Course.objects.order_by('-date')[:5]
        university_list = University.objects.order_by('name')
        course_list = Course.objects.values('title').distinct()
        year_list = Course.objects.values('year').distinct()
        context_dict = {'topfive': top_five_list, 'worstfive': worst_five_list, 'latestfive': latest_list,
                        'universitylist': university_list, 'courselist': course_list, 'yearlist': year_list}

        for rate in top_five_list:
            rate.url = rate.title.replace(' ', '_')
        for rate in worst_five_list:
            rate.url = rate.title.replace(' ', '_')
        for rate in latest_list:
            rate.url = rate.title.replace(' ', '_')
        return render_to_response('rate/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Colossus 4.0 Team"}
    return render_to_response('rate/about.html', context_dict, context)


def contact(request):
    context = RequestContext(request)
    return render_to_response('rate/contact.html', context)


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rate/')
            else:
                return HttpResponse("Sorry your account is not enabled. Your University's domain is not confirmed yet.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('rate/login.html', {}, context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rate/')


def register(request):
    if not request.user.is_authenticated():
        context = RequestContext(request)
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.username = user.email
                user.save()
                registered = True
            else:
                print user_form.errors,
        else:
            user_form = UserForm()
        return render_to_response('rate/register.html', {'user_form': user_form, 'registered': registered}, context)
    else:
        return HttpResponse("You are already registered and signed in.")


def restricted(request):
    if request.user.is_authenticated():
        return HttpResponse("You cannot access this page!")
    else:
        return render_to_response('rate/restricted.html')


def underConstruction(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Under Construction"}
    return render_to_response('rate/underConstruction.html', context_dict, context)


def test(request):
    context = RequestContext(request)
    return render_to_response('rate/test.html', context)


def course(request, course_title_url):
    context = RequestContext(request)
    course_title = course_title_url.replace('_', ' ')
    context_dict = {'course_title': course_title}
    try:
        course = Course.objects.get(title=course_title)
        rate = Rate.objects.filter(course=course)
        context_dict['course'] = course
        context_dict['rate'] = rate

        flag = "yes"
        for u in rate:
            if u.student.email == request.user.email:
                flag = "no"

        context_dict['rateIt'] = flag
    except Course.DoesNotExist:
        pass

    course.url = course.title.replace(' ', '_')

    return render_to_response('rate/course.html', context_dict, context)


def rated_courses(request, type):
    context = RequestContext(request)
    if type == "top":
        list = Course.objects.order_by('-stored_average_rating')[:20]
        title = "Top Rated Courses"
    if type == "worst":
        list = Course.objects.order_by('stored_average_rating')[:20]
        title = "Worst Rated Courses"
    if type == "latest":
        list = Course.objects.order_by('-date')[:20]
        title = "Most Recent Rated Courses"

    university_list = University.objects.order_by('name')
    course_list = Course.objects.values('title').distinct()
    year_list = Course.objects.values('year').distinct()
    rates_list = Rate.objects.values('course', 'date')[:1]
    context_dict = {'list': list, 'title': title,
                    'universitylist': university_list, 'courselist': course_list, 'yearlist': year_list,
                    'rateslist': rates_list}

    for rate in list:
        rate.url = rate.title.replace(' ', '_')

    return render_to_response('rate/rated_courses.html', context_dict, context)

def rateIt(request, course_title_url):
    context = RequestContext(request)
    if request.user.is_authenticated():
        course_title = course_title_url.replace('_', ' ')
        context_dict = {'course_title': course_title}

        try:
            course = Course.objects.get(title=course_title)
            rate = Rate.objects.filter(course=course)
            context_dict['course'] = course
            context_dict['rate'] = rate
        except Course.DoesNotExist:
            pass
        return render_to_response('rate/rateIt.html', context_dict, context)
    else:
        return render_to_response('rate/restricted.html')
