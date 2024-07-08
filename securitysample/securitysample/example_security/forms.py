
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import bcrypt

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = bcrypt.hashpw(self.cleaned_data["password1"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = bcrypt.hashpw(self.cleaned_data["password1"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name')