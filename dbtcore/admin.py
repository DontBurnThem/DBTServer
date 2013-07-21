from django.contrib import admin
from dbtcore.models import Book, Offer, DBTUser

class DBTUserModel(admin.ModelAdmin):
    fields= ('email', 'is_staff', 'is_superuser')

admin.site.register(Book)
admin.site.register(Offer)
admin.site.register(DBTUser, DBTUserModel)
