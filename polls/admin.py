from django.contrib import admin
from .models import TopFollowers


# Register your models here.


@admin.register(TopFollowers)
class TopFollowersAdmin(admin.ModelAdmin):
    pass
