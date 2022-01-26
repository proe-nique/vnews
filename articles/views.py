from django.shortcuts import render
from . models import Article, Category, Tag
from . forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib import messages
from .filters import ArticleFilter

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.



class CategoryListView(ListView):
    model = Category
    paginate_by = 20
    context_object_name = 'categories'
    template_name = "categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(category=self.slug).order_by('-published')
        context["page_title"] = 'categories'
        return context
    


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = "category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'category'
        return context
    

class TagListView(ListView):
    model = Tag
    paginate_by = 20
    context_object_name = 'tags'
    template_name = "tags.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(tags=self.slug).order_by('-published')
        context["page_title"] = 'tags'
        return context
    


class TagDetailView(DetailView):
    model = Tag
    context_object_name = 'tag'
    template_name = "tag.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'tag'
        return context
    

class ArticleListView(ListView):
    model = Article
    paginate_by = 20
    context_object_name = 'articles'
    template_name = "articles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset()).order_by('-published')
        context["page_title"] = 'articles'
        return context
    


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'article'
        return context
    


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "create_article.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully created.")
        return super(ArticleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'create-article'
        return context
    


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "update_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'update-article'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully updated.")
        return super(ArticleUpdateView, self).form_valid(form)
    


class ArticleDeleteView(DeleteView):
    model = Article
    form_class = ArticleForm
    template_name = "delete_article.html"
    success_url = reverse_lazy('base:home')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'confirm delete article'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully Deleted.")
        return super(ArticleDeleteView, self).form_valid(form)

   
