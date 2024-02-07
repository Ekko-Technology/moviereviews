# this file is used to customize the built-in user creationform and AuthenticationForm within django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

# creating a new form format called createuserform that extends the default built-in form placed in the argument
class CreateUserForm(UserCreationForm):
    # adding an email field within the user creation form
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    # super method is used to access methods of the parent class, in this case is the default UserCreationForm. 
    def __init__(self, *args, **kwargs):
        # this inherits and initializes any attributes from the parent class
        super(CreateUserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            # editing the original form page https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
            self.fields[fieldname].help_text = None
            # add bootstrap properties within each form field
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class CustomAuthenticateForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticateForm, self).__init__(*args, **kwargs)

        for fieldname in ["username","password"]:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
