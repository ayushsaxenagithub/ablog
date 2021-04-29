from django.contrib import admin
from django.urls import path,include
from .import views
from .views import HomeView,ArticleDetailView,AddPost,UpdatePost,DeletePost,AddCategory,CategoryView,ShowProfileView,AddComment

urlpatterns = [
    #path('', views.home,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/',AddPost.as_view(),name='add_post'),
    path ('article/update/<int:pk>', UpdatePost.as_view (), name='update_post'),
    path ('article/remove/<int:pk>', DeletePost.as_view (), name='delete_post'),
    path('add_category/',AddCategory.as_view(),name='add_category'),
    path ('category/<str:ctv>/', views.CategoryView, name='category'),
    path ('category-list/', CategoryView, name='category'),
    path ('like/<int:pk>/', views.LikeView, name='like_post'),
    path ('show_profile/<int:pk>', ShowProfileView.as_view (), name='show_profile'),
    path ('article/<int:pk>/add_comment/', AddComment.as_view (), name='add_comment'),

]