from django.urls import path
from .views import SignUpView,UserEditView,PasswordChangeView,EditProfileView
from django.contrib.auth import views as auth_views
from .import views
app_name='members'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path ('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path ('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path ('password/', PasswordChangeView.as_view (template_name='registration/change_password.html')),
    path ('password-success/', views.PasswordSuccess,name='password-success'),
    path ('<int:pk>/edit_profile_page/', EditProfileView.as_view(), name='edit-profile'),

]