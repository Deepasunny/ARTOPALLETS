from django.contrib import admin


# Register your models here.
from.models import Customisation

admin.site.register(Customisation)

from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ('title', 'upload_date')

from django.contrib import admin
from .models import Feedback

admin.site.register(Feedback)


