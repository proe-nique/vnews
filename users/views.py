from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.models import User
from . models import Profile
from articles.models import Article
# Create your views here.


class UserListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'blogs'
        return context
    
    


class UserDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'blog'
        context["article"] = Article.objects.select_related('user').filter(featured=True).first()
        return context
    
    



class UserUpdateView(UpdateView):
    model = Profile
    template_name = "update_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'update/blog'
        return context
    
    


class UserDeleteView(DeleteView):
    model = Profile
    template_name = "delete_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'delete/blog'
        return context
    
   
