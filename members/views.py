from django.shortcuts import render,get_object_or_404,reverse,_get_queryset
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.forms import ModelForm


from .forms import SignUpForm,EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile
from django.views.generic import CreateView,UpdateView,DetailView


def PasswordSuccess(request):
    return render(request,'registration/password_success.html')


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio','profile_pic','website_url','fb_url','instagram_url','twitter_url','pinterest_url','linkedin_url']
    success_url = reverse_lazy('home')



class PasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeView
    success_url = reverse_lazy('password-success')

class SignUpView (CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy ('login')
    template_name = 'registration/register.html'


class UserEditView(UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy ('home')
    template_name = 'registration/edit_profile.html'
    def get_object(self):
        return self.request.user


