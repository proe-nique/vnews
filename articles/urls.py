from django.urls import path
from . import views

app_name = "stories"   


urlpatterns = [
    path("article/<slug>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("list/", views.ArticleListView.as_view(), name="article_list"),
    path("delete/article<slug>/", views.ArticleDeleteView.as_view(), name="article_delete"),
    path("update/article<slug>/", views.ArticleUpdateView.as_view(), name="article_update"),
    path("create/article/<slug>/", views.ArticleCreateView.as_view(), name="article_create"),
    ############
    path("category/<slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
    path("category/list/", views.CategoryListView.as_view(), name="category_list"),
     ############
    path("tag/<slug>/", views.TagDetailView.as_view(), name="tag_detail"),
    path("tag/list/", views.TagListView.as_view(), name="tag_list"),

]