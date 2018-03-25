from django.shortcuts import render, HttpResponse, redirect
from apps.validate.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
import bcrypt

def index(request):
    return redirect('/main')

def main(request):
    if 'username' in request.session: del request.session['username']
    return render(request, 'validate/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.register(request.POST)
        if len(errors):
            for tag, error in errors.items(): messages.error(request, error, extra_tags=tag)
            context = {"error": 1}
            for key, value in request.POST.items(): context[key] = value
            return render(request, 'validate/index.html', context)
        else:
            User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],
                                email=request.POST['email'], birthdate=request.POST['bdate'],
                                password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
            request.session['username'] = request.POST['email']
            return redirect('/success')
    return redirect('/')

def login(request):
    if request.method =='POST':
        errors = User.objects.login(request.POST)
        if len(errors):
            for tag, error in errors.items(): messages.error(request, error, extra_tags=tag)
            context = {"email": request.POST['email'], "error": 2}
            return render(request, 'validate/index.html', context)
        else:
            request.session['username'] = request.POST['email']
            return redirect('/success')
    return redirect('/')

def success(request):
    if 'username' in request.session:
        return redirect(reverse('trips:index'))
    else: return redirect('/')
