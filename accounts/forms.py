# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member


class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False)
    city = forms.CharField(required=False)
    province = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'city',
            'province')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        else:
            user.save()  # Ensure the User is saved before proceeding

        # Ensure the related Member instance exists
        Member.objects.get_or_create(user=user)

        # Access and update the Member instance via user.member
        user.member.bio = self.cleaned_data.get('bio', '')
        user.member.profile_picture = self.cleaned_data.get('profile_picture', None)
        user.member.city = self.cleaned_data.get('city', '')
        user.member.province = self.cleaned_data.get('province', '')

        user.member.save()

        return user
