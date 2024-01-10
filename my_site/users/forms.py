from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .validators import russian_email
from django.core.validators import MinLengthValidator
from .models import Profile

#Регистрация пользователя
# class UserRegisterForm(UserCreationForm):
#     name = forms.CharField(max_length=100,
#                            validators = [MinLengthValidator(2)])
#     email = forms.EmailField(validators=[russian_email])
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password1', 'password2']
#update foto
#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ('photo')

#Заполнение и обновление профилей
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields  = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']