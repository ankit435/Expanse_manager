from django.contrib import admin
# from .models import ExpanseGroup, Expanse, ExpanseGroupUser, ExpanseUser

# admin.site.register([ExpanseGroup,Expanse,ExpanseGroupUser,ExpanseUser])

from .models import User ,Expanse,ExpanseGroup,ExpanseGroup,ExpanseGroupUser,LinkExpanseGroupUser
admin.site.register([User,Expanse,ExpanseGroup,ExpanseGroupUser,LinkExpanseGroupUser])