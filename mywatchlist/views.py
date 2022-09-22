from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist_item = MyWatchList.objects.all()
    udahnonton = 0
    belumnonton = 0

    for i in data_mywatchlist_item:
        if i.watched == True:
            udahnonton += 1
        elif i.watched == False:
            belumnonton += 1
            
    context ={
        'list_item' : data_mywatchlist_item,
        'name': 'Nicolas Ananda',
        'NPM' : '2106720973',
        'udahnonton' : udahnonton,
        'belumnonton' : belumnonton,
    }
    
    return render(request,"mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   

def show_xml_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
