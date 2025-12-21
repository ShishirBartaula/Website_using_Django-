#this urls is reference to apps name chai 
#we need to connect this with project urls

from django.urls import path
from .import views #import  current views directory 
urlpatterns = [

     path('',views.all_chai,name="all_chai"),
#views ma function ko name all_chai x so
path('<int:chai_id>/',views.chai_detail,name="chai_detail"),

]