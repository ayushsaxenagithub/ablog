from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DeleteView, CreateView,UpdateView,DetailView
from .models import Post, Category,Comment
from .forms import PostForm,AddComment
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect






def LikeView(request,pk):
     post=get_object_or_404(Post,id=request.Post.get('post_id'))
     post.likes.add(request.user)
     return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


def get_context_data(self,*args,**kwargs):
    cat_menu = Category.objects.all()
    context = super(HomeView, self).get_context_data( *args, **kwargs )
    context["cat_menu"]=cat_menu
    return context

def CategoryView(request,ctv):
    category_posts=Post.objects.filter(category=ctv)
    return render(request,'categories.html',{'ctv':ctv,'category_post':category_posts})


class ShowProfileView(DetailView):
    model = Post
    template_name = 'show_profile.html'
    success_url = reverse_lazy('home')


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    success_url = reverse_lazy('home')


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'


class AddComment(CreateView):
    model = Comment
    form_class = AddComment
    template_name = 'add_comments.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)


class AddCategory(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title','title_tag','body')
    success_url = reverse_lazy('home')



class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


