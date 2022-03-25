from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core import serializers

from localusers.models import CustomUser, UserImage

users = CustomUser.objects.all()
User = serializers.serialize('json', users)


class RegistrationForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    telephone = forms.IntegerField()
    address = forms.CharField(max_length=100, label="Your Address")

    def save(self, request):
        user = super(RegistrationForm, self).save(request)
        user.telephone = self.cleaned_data['telephone']
        user.address = self.cleaned_data['address']
        user.save()
        return user


class SocialRegistrationForm(SocialSignupForm):
    def __init__(self, *args, **kwargs):
        super(SocialRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    telephone = forms.IntegerField()
    address = forms.CharField(max_length=100, label="Your Address")
    
    def save(self, request):
        user = super(SocialRegistrationForm, self).save(request)
        user.telephone = self.cleaned_data['telephone']
        user.address = self.cleaned_data['address']
        user.save()
        return user


class ProfileUpdateForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    password = forms.CharField(
        help_text="",
        required=False,
        widget=forms.HiddenInput()
    )

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',
                'email', 'telephone', 'address')


class AdminProfileUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(AdminProfileUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    password = forms.CharField(
        help_text="",
        required=False,
        widget=forms.HiddenInput(

        )
    )

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',
                'telephone', 'address', 'is_active', 'is_staff')


class UserImageForm(forms.ModelForm):

    class Meta:
        model = UserImage
        fields = ('image',)