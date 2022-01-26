from articles.models import Category
def engine(request):
    return {
       "site_name": 'v-news',
       'categories': Category.objects.all()
    }    