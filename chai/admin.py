from django.contrib import admin
#This code registers a Django model with the Django admin panel
#  so it can be managed through the admin interface.
from .models import chaiVarity,chaiReview,store,chaiCertification
 #Imports the  chaiVariy model class name from models.py

# admin.site.register(chaiVarity)  #Registers the chaiVariy model with Django Admin

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 2  #Number of extra forms to display

class ChaiVarityAdmin(admin.ModelAdmin):
    inlines = [ChaiReviewInline]
    list_display = ('name', 'type', 'price', 'date_added','image','rating')
    search_fields = ('name', 'type')
    list_filter = ('type', 'date_added')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'opening_hours', 'contact_info')
    search_fields = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificationAdmin(admin.ModelAdmin):
    list_display = ('chai_certification','certificate_number', 'issued_date', 'valid_until')   


admin.site.register(chaiVarity, ChaiVarityAdmin)   
admin.site.register(store, StoreAdmin)
admin.site.register(chaiCertification, ChaiCertificationAdmin)