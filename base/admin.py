from django.contrib import admin
from .models import Types,B_models,Engine,Customer,Order,Staff

# Register your models here.

class EngineInline(admin.TabularInline):
    model = Engine

class Modelsadmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['type_id']}),
        ('Model Name',{'fields':['name']}),
        ('Description',{'fields':['description']}),
        ('Base Prize',{'fields':['base_prize']}),
        ('Prize',{'fields':['prize']}),
        ('Quantity',{'fields':['quantity']}),
        ('Picture',{'fields':['image']})
    ]

    inlines=[EngineInline]

admin.site.register(Types)
admin.site.register(B_models,Modelsadmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Staff)
