from django.contrib import admin
from .models import Todo

# for administrative tasks
# display the models in the Django admin panel

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Todo, TodoAdmin)