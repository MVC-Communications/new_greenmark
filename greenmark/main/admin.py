from django.contrib import admin

from .models import *

class BussInfoAdmin(admin.ModelAdmin):
    pass

class EnvCompObligAdmin(admin.ModelAdmin):
    pass

class AspImpactAdmin(admin.ModelAdmin):
    pass


admin.site.register(BussInfo, BussInfoAdmin)
admin.site.register(EnvCompOblig, EnvCompObligAdmin)
admin.site.register(AspImpact, AspImpactAdmin)
