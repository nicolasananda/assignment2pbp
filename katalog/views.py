from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    return render(request,"katalog.html", context)

data_katalog_item = CatalogItem.objects.all()
context ={
    'list_item' : data_katalog_item,
    'name': 'Nicolas Ananda',
    'NPM' : '2106720973'
}
