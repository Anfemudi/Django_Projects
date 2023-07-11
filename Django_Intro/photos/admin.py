from django.contrib import admin
from photos import models

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name','owner_name','license','visibility')
    list_filter=('license','visibility')
    search_fields=('name','description')

    def owner_name(self,obj):
        return (obj.owner.first_name + u' '+obj.owner.last_name)
    ## method attributes 
    ## short description means the name of the column
    ## admin_order_field menas order by the column when clicked
    owner_name.short_description = u'Owner'
    owner_name.admin_order_field = 'owner'

    ##Fieldsets is a tuple , that is why it needs tu add a , at the end of each tuple
    fieldsets= (
        (None,{
            'fields':('name',),
            'classes':('wide',)
        }),
        ('Description & Author',{
            'fields':('description','owner'),
            'classes':('wide',)
        }),
        ('Extra',{
            'fields': ('url','license','visibility'),
            'classes': ('wide','collapse')
        })
    )

admin.site.register(models.Photo,PhotoAdmin)


