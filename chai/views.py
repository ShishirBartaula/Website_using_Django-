from django.shortcuts import render
from .models import chaiVarity
from .models import store
from .forms import chaiVarityForm 
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

#view for chai store
def chai_store_view(request):
    stores=None
     
    if request.method=="POST":
       form=chaiVarityForm(request.POST)
       if form.is_valid():
            chai_varity=form.cleaned_data['chai_varity']
            store=store.objects.filter(chai_varity=chai_varity)   
    else:    
        form=chaiVarityForm() 
    return render(request,"chai/chai_stores.html",{'stores':store,'form':form })