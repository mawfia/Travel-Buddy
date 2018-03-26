from django.shortcuts import render, HttpResponse, redirect
from apps.validate.models import User
from apps.trips.models import Trip
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
    if 'username' not in request.session: return redirect(reverse('validate:index'))

    user = User.objects.get(email=request.session['username'])
    context = {
                "user": user,
                "trips": Trip.objects.exclude(users=user)
              }
    return render(request, 'trips/trips.html', context)

def show(request, trip_id):
    if 'username' not in request.session: return redirect(reverse('validate:index'))

    user = User.objects.get(email=request.session['username'])
    trip = Trip.objects.filter(id=trip_id)[0]
    context = {
                "user": user,
                "trip": trip,
                "group": trip.users.all().exclude(id=user.id).exclude(id=trip.users.first().id)
              }
    return render(request, 'trips/trip.html', context)

def add(request):
    if 'username' not in request.session: return redirect(reverse('validate:index'))

    context = { "user": User.objects.filter(email=request.session['username'])[0]}
    return render(request, 'trips/new.html', context)

def join(request, trip_id):
    if 'username' not in request.session: return redirect(reverse('validate:index'))

    user = User.objects.get(email=request.session['username'])
    user.trips.add(Trip.objects.get(id=trip_id))
    user.save()

    return redirect(reverse('trips:index'))

def create(request):
    if 'username' not in request.session: return redirect(reverse('validate:index'))

    if request.method == 'POST':
        errors = Trip.objects.validator(request.POST)

        if len(errors):
            for tag, error in errors.items(): messages.error(request, error, extra_tags=tag)
            context = { "user": User.objects.filter(email=request.session['username'])[0]}
            for key, value in request.POST.items(): context[key] = value
            return render(request, 'trips/new.html', context)
        else:
            destination = request.POST['destination'].lower()
            u = User.objects.get(email=request.session['username'])
            Trip.objects.create(destination=destination, description=request.POST['description'], travel_date_from=request.POST['date_from'], travel_date_to=request.POST['date_to'])
            u.trips.add(Trip.objects.get(destination=destination))
    return redirect(reverse('trips:index'))
