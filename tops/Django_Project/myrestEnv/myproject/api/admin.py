from django.contrib import admin
from .models import *

# Register your models here.
#Serializers : to convert complex data type
#for example result of models instance,query set,filter data all these complex data convert into normal python data type.

#Deserialixers : to convert python data type value into complex data type.

class StudentAdmin(admin.ModelAdmin):
    list_display=("id","name","city")

admin.site.register(Student,StudentAdmin)
