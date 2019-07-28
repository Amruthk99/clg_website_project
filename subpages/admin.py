from django.contrib import admin
from .models import Content_with_1_image
from .models import Content_with_2_image
from .models import Content_with_3_image,Photo
# Register your models here.
admin.site.register(Content_with_1_image)
admin.site.register(Content_with_2_image)
admin.site.register(Content_with_3_image)
admin.site.register(Photo)
