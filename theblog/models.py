from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField



class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')



class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=RichTextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    website_url=models.URLField(null=True,blank=True)
    fb_url=models.URLField(null=True,blank=True)
    instagram_url=models.URLField(null=True,blank=True)
    twitter_url=models.URLField(null=True,blank=True)
    pinterest_url=models.URLField(null=True,blank=True)
    linkedin_url=models.URLField(null=True,blank=True)

    def __str__(self):
        return str(self.user)



class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField (max_length=255,default="A Awesome Blog")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    post_date=models.DateTimeField(blank=True,null=True,default=datetime.now)
    category=models.CharField(max_length=255,default="uncategorised")
    snippet=models.CharField(max_length=255,default="Click on link to read full Blog Post")

    def __str__(self):
        return self.title+'|'+str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=RichTextField(blank=True,null=True)
    date_added=models.DateTimeField( blank=True,default=datetime.now)
    def __str__(self):
        return '%s-%s'%(self.post.title,self.name)