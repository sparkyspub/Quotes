from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, "Post/index.html")

def Reg(request):
    nologinerrors = True
    if len(request.POST['first_name']) < 2:
        messages.add_message(request, messages.ERROR, "Invalid input")
        nologinerrors = False
    if len(request.POST['last_name']) < 2:
        messages.add_message(request, messages.ERROR, "Invalid input")
        nologinerrors = False
    if not ALPHA_REGEX.match(request.POST['first_name']):
        messages.add_message(request, messages.ERROR, "First name can not have a number in it")
        nologinerrors = False
    if not ALPHA_REGEX.match(request.POST['last_name']):
        messages.add_message(request, messages.ERROR, "Last name can not have a number in it")
        nologinerrors = False
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.add_message(request, messages.ERROR,"Your email does not match")
        nologinerrors = False
    if request.POST['password'] < 8:
        messages.add_messages(request, messages.ERROR, "Your password is not long enough")
        nologinerrors = False
    if request.POST['password'] != request.POST['confirm']:
        messages.add_message(request, messages.ERROR, "Your passwords don't match")
        nologinerrors = False
    if nologinerrors == False:
        return redirect ('/')

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    User.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    email = request.POST['email'],
    password = request.POST['password'])
    request.session['first_name'] = request.POST['first_name']
    return render (request, 'Post/profile.html')

def SignIn(request):
    email = request.POST['email']
    password = request.POST['password']
    query = User.objects.filter(email = email)
    user = query[0]
    print query

    if user['password'] == password:
        return redirect('/success')
    else:
        messages.add_message(request, messages.ERROR, "invalid login or password")
        return redirect('/')

def success (request):
    return render (request, 'Post/profile.html')

def clear (request):
    if 'first_name' in request.session:
        del request.session['first_name']
    return redirect ('/')


def quotes (request):
    Quote.objects.create(quotes = request.POST['quotes'])
    return render (request, 'Post/profile.html')

def profile (request):
    context = {
    "quotes": Quote.objects.all()
    }
    print "====================================="
    return render (request, 'Post/profile.html', context)
