from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserChangeForm
from .models import User

class UniversityApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    nationality = forms.CharField(max_length=100)
    high_school = forms.CharField(max_length=100)
    graduation_year = forms.IntegerField()
    gpa = forms.FloatField()
    course = forms.ChoiceField(choices=[
        ('Computer Science', 'Computer Science'),
        ('Business Administration', 'Business Administration'),
        ('Engineering', 'Engineering'),
        ('Medicine', 'Medicine'),
        ('Law', 'Law')
    ])
    # captcha = ReCaptchaField()


class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self)
        print(f"password={self.cleaned_data.get('password')}")
        # user.set_password(self.cleaned_data.get('password'))        

        if commit:
            user.save()
            
        return user




class LoginForm(Form):
    class Meta(Form):
        model = User
        fields = ['email', 'password']

