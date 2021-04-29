from dataclasses import fields
from ckeditor import widgets
from django import forms
from .models import Post,Category,Comment

choices = Category.objects.all().values_list('name','name')
choice_list=[]
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag','category','author','snippet','body','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Give a title to your content'}),
            'title_tag': forms.TextInput (attrs={'class': 'form-control'}),
            'author': forms.TextInput (attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            #'author': forms.Select (attrs={'class': 'form-label'}),
            'category': forms.Select (choices=choice_list,attrs={'class': 'form-label'}),
            'body': forms.Textarea (attrs={'class': 'form-control'}),
            'snippet': forms.Textarea (attrs={'class': 'form-control'}),
        }


class Editform (forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category','snippet', 'body')

        widgets = {
            'title': forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Give a title to your content'}),
            'title_tag': forms.TextInput (attrs={'class': 'form-control'}),
            'category': forms.Select (choices=choice_list,attrs={'class': 'form-label'}),
            #'author': forms.Select (attrs={'class': 'form-control'}),
            'body': forms.Textarea (attrs={'class': 'form-control'}),
            'snippet': forms.Textarea (attrs={'class': 'form-control'}),
        }

class AddComment (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput (attrs={'class': 'form-control','value':'','id':'name','type':'hidden'}),
            'body': forms.Textarea (attrs={'class': 'form-control'}),
        }

class Profile(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category','snippet', 'body')

        widgets = {
            'title': forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Give a title to your content'}),
            'title_tag': forms.TextInput (attrs={'class': 'form-control'}),
            'category': forms.Select (choices=choice_list,attrs={'class': 'form-label'}),
            #'author': forms.Select (attrs={'class': 'form-control'}),
            'body': forms.Textarea (attrs={'class': 'form-control'}),
            'snippet': forms.Textarea (attrs={'class': 'form-control'}),
        }

