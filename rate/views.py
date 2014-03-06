# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from rate.models import Rate, Course
from rate.forms import UserForm

def index(request):
    context = RequestContext(request)
    top_five_list = Course.objects.order_by('-stored_average_rating')[:5]
    worst_five_list = Course.objects.order_by('stored_average_rating')[:5]
    latest_list = Rate.objects.order_by('-date')[:5]
    context_dict = {'topfive': top_five_list, 'worstfive': worst_five_list, 'latestfive': latest_list}
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
        return render_to_response('rango/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rate/')

def register(request):

    if not request.user.is_authenticated():

        # Like before, get the request's context.
        context = RequestContext(request)

        # A boolean value for telling the template whether the registration was successful.
        # Set to False initially. Code changes value to True when registration succeeds.
        registered = False

        # If it's a HTTP POST, we're interested in processing form data.
        if request.method == 'POST':
            # Attempt to grab information from the raw form information.
            # Note that we make use of both UserForm and UserProfileForm.
            user_form = UserForm(data=request.POST)

            # If the two forms are valid...
            if user_form.is_valid():
                # Save the user's form data to the database.
                user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()


                # Update our variable to tell the template registration was successful.
                registered = True

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            # They'll also be shown to the user.
            else:
                print user_form.errors,

        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        else:
            user_form = UserForm()

        return render_to_response('rate/register.html', {'user_form': user_form, 'registered': registered}, context)
    else:
        return HttpResponse("You are already registered and signed in.")

def restricted(request):
    if not request.user.is_authenticated():
        return HttpResponse("Since you're logged in, you cannot see this page!")
    else:
        return render_to_response('rate/restricted.html')

def underConstruction(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "Under Construction"}
    return render_to_response('rate/underConstruction.html', context_dict, context)

def test(request):
    context = RequestContext(request)
    return render_to_response('rate/test.html', context)
