from django.shortcuts import render
from .models import chaiVarity  #use this to fetch data from database 
from django.shortcuts import get_object_or_404
#after create app named chai go to settings.py and add 'chai' in INSTALLED_APPS

# Create your views here.

def all_chai(request):
    chais=chaiVarity.objects.all()  #fetch all chaiVarity objects from database
    return render(request,"chai/app1.html",{'chais':chais})
    return render(request,"chai/app1.html")


#Now create a detail view for each chai variety
def chai_detail(request,chai_id):
    chai=get_object_or_404(chaiVarity,pk=chai_id)
    return render(request,"chai/next_page.html",{'chai':chai})