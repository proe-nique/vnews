from . models import Article
import django_filters
from django_filters.filters import RangeFilter

# Creating Article filters
class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    date = RangeFilter()
    


    class Meta:
        model = Article
        fields = ['title', 'date']