from django.contrib import admin
from .models import Registration
from .models import contactus,postdata,Message
# Registration your models here.
admin.site.register(Registration)
admin.site.register(contactus)
admin.site.register(postdata)
admin.site.register(Message)
