from django.contrib import admin

from .models import *

class AgreementDocAdmin(admin.ModelAdmin):
    pass

class BussInfoAdmin(admin.ModelAdmin):
    pass

class KeyDecisionMakerAdmin(admin.ModelAdmin):
    pass

class EnvironManagerAdmin(admin.ModelAdmin):
    pass

class OtherResponsiblePersonAdmin(admin.ModelAdmin):
    pass

class EnvCompObligAdmin(admin.ModelAdmin):
    pass

class EnvCommAdmin(admin.ModelAdmin):
    pass


admin.site.register(AgreementDoc, AgreementDocAdmin)
admin.site.register(BussInfo, BussInfoAdmin)
admin.site.register(KeyDecisionMaker, KeyDecisionMakerAdmin)
admin.site.register(EnvironManager, EnvironManagerAdmin)
admin.site.register(OtherResponsiblePerson, OtherResponsiblePersonAdmin)
admin.site.register(EnvCompOblig, EnvCompObligAdmin)
admin.site.register(EnvComm, EnvCommAdmin)
    
