from django.shortcuts import render, redirect
from .models import users

def index(request):
    context = {
        'all_users': users.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        users.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email_address=request.POST['email_address'],
            age=request.POST['age']
        )
    return redirect('/')