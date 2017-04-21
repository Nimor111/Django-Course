from django.contrib import admin
from store.models import Pet


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
