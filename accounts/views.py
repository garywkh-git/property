from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# from .views import (
#     CustomPasswordResetView,
#     CustomPasswordResetDoneView,
#     CustomPasswordResetConfirmView,
#     CustomPasswordResetCompleteView,
# )
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request, "accounts/login.html")

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('pages:index')

def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exist')
                return redirect("accounts:register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exist')
                    return redirect("accounts:register")
                else:    
                    user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect("accounts:login")
        else:
            messages.error(request, 'Passwords do not match')
            return redirect("accounts:register")
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.all().filter(user_id=request.user.id).order_by('-contact_date')
    context = {"contacts": user_contacts}
    return render(request, 'accounts/dashboard.html', context)




class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/custom_password_reset_email.html'
    subject_template_name = 'registration/custom_password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'