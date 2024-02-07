from django.shortcuts import render
# importing improved format of Django's built in user authentication usercreation forms from forms.py
from .forms import CreateUserForm, CustomAuthenticateForm
# allowing for handle requests and creating users
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.

def signupaccount(request):
    if request.method == 'GET':
        return render(request, "signupaccount.html", {'form': CreateUserForm})
    
    # handling POST methods
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # creates new user via their username and password into django's own set of Model and database table
                user = User.objects.create_user(request.POST['username'], email=request.POST['email'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            # if username/primary key has been taken, integrity error would be raised
            except IntegrityError as E:
                return render(request, "signupaccount.html", {'form': CreateUserForm, 'error': f'Username Has Been Taken. Choose another username.\n {E}'})

        # handling errors if user does not meet form's pre-requisites
        else:
            return render(request, "signupaccount.html", {'form': CreateUserForm, 'error': CreateUserForm.error_messages['password_mismatch']})
        


def loginaccount(request):
    if request.method == "GET":
        return render(request, "login.html", {'form': CustomAuthenticateForm})

    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user == None:
            return render(request, 'login.html', {'form': CustomAuthenticateForm, 'error': CustomAuthenticateForm.error_messages["invalid_login"]})
        
        else:
            login(request, user)
            return redirect('home')


@login_required
def logoutaccount(request):
    logout(request)
    return redirect("home")



