from .models import Category
def Menu_links(request):
    links = Category.objects.all()
    return dict(links=links)