from django.shortcuts import render
from django.views.generic import TemplateView
from articles.models import Article
from articles.forms import ArticleSearchForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter
# Create your views here.

class ArticlesFilter(BaseFilter):
    search_fields = {
        'search_text' : ['title', ],
        'search_date_exact' : { 'operator' : '__exact', 'fields' : ['date'] },
        'search_date_min' : { 'operator' : '__gte', 'fields' : ['date'] },
        'search_date_max' : { 'operator' : '__lte', 'fields' : ['date'] },

    }

class Home(SearchListView):
    model = Article
    paginate_by = 30
    template_name = "home.html"
    form_class = ArticleSearchForm
    filter_class = ArticlesFilter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'home'
        context["articles"] = Article.objects.filter(featured=True).order_by('-published')[:3]
        return context
    
class About(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'about'
        return context

    

class Contact(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'contact us'
        return context

    

class Pricing(TemplateView):
    template_name = "pricing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'pricing'
        return context

    

class Faq(TemplateView):
    template_name = "faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'faq'
        return context

    