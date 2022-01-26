from django.urls import path
from . import views

app_name = "base"   


urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("about/", views.About.as_view(), name="about"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("pricing/", views.Pricing.as_view(), name="pricing"),
    path("faq/", views.Faq.as_view(), name="faq"),
    
]