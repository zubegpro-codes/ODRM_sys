from django.contrib import admin
from base.models import CustomUser, Comments, Report, Category

admin.site.register(CustomUser)
admin.site.register(Report)
admin.site.register(Category)
admin.site.register(Comments)