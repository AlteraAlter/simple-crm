from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.


def main(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.success(request, 'There is an error, please try again')
            return redirect('home')

    return render(request, 'dev/home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have succsessfully Registered')
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'dev/register.html', {'form': form})
    return render(request, 'dev/register.html', {'form': form})


def record_details(request, slug):
    record = get_object_or_404(Record, slug=slug)

    return render(request, 'dev/details.html', {'record': record})


def delete_record(request, slug):
    record = get_object_or_404(Record, slug=slug)
    record.delete()
    messages.success(request, 'Record deleted')

    return redirect('home')
