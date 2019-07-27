from django.contrib import admin
from .models import Content_with_1_image
from .models import Content_with_2_image
from .models import Content_with_3_image,Photo,CSE_Faculty,ECE_Faculty
# Register your models here.
admin.site.register(Content_with_1_image)
admin.site.register(Content_with_2_image)
admin.site.register(Content_with_3_image)
admin.site.register(Photo)
admin.site.register(CSE_Faculty)
admin.site.register(ECE_Faculty)
