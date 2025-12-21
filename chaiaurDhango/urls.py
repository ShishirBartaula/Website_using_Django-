"""
URL configuration for chaiaurDhango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin

#import settings and static for media files

from django.conf import settings
#Gives access to variables defined in settings.py, such as: MEDIA_URL and MEDIA_ROOT

from django.conf.urls.static import static
#creates URL patterns for serving static or media files during development.

#now write include for apps urls.py reference
from django.urls import path,include

from .import views #import  current views directory 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.Home,name="home"), # Root URl so empth ''
    path('privacy',views.privacy,name="privacy"),
    path('about/',views.About,name="about"),  #abou is the url path shoe in browser
    #views.About is the function written in views.py file
    #name="about" is the reference name 
    path('contact/',views.contact,name="contact"),

    # connect with apps urls.py by
    path('chai/',include('chai.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#this static function is used to serve media files during development only

# Maps URLs starting with MEDIA_URL
# To files stored inside MEDIA_ROOT
