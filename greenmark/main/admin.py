from django.contrib import admin

from .models import *

class BussInfoAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'year_of_aggrement', 'buss_name',
    'phone', 'website', 'keydecider_name', 'keydecider_title',
    'keydecider_email', 'keydecider_signature', 'envmanager_name',
    'envmanager_title', 'envmanager_email', 'envmanager_signature',
    'otherresp_person_name', 'otherresp_person_title', 
    'otherresp_person_email', 'otherresp_person_signature')

class EnvCompObligAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'person_rep', 'comp_oblig_name_1',
    'comp_oblig_description_1', 'comp_oblig_name_2', 
    'comp_oblig_description_2', 'env_comm_option', 
    'env_comm_description')

class AspImpactAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'activity_1', 'aspect_1', 'impact_1',
    'activity_2', 'aspect_2', 'impact_2')

class EnvThreatsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'threat1', 'impact1', 'probability1',
    'if_occurs1', 'threat2', 'impact2', 'probability2', 'if_occurs2')

class ObjectivesAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'objective_1', 'procedure_1', 
    'result_1', 'start_date_1') 

class CompanyPolicyAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'current_objectives', 'existing_policy')

class EmergencyResponseAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'procedure_1', 'internal_contact_1',
    'external_contact_1', 'procedure_2', 'internal_contact_2')


class CommunicationsAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'subject_1', 'how_comm_1', 
    'person_resp_1', 'who_receives_1', 'when_1')

class DocumentationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'records_type_1', 'main_location_1',
    'other_location_1', 'person_resp_1', 'comments_1')

class AuditReviewAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'objective_1', 'start_date_1', 
    'achievement_1', 'comment_1')

class LocationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('user', 'location', 'phone', 'address')




admin.site.register(BussInfo, BussInfoAdmin)
admin.site.register(EnvCompOblig, EnvCompObligAdmin)
admin.site.register(AspImpact, AspImpactAdmin)
admin.site.register(EnvThreats, EnvThreatsAdmin)
admin.site.register(Trainers)
admin.site.register(Objectives, ObjectivesAdmin)
admin.site.register(CompanyPolicy, CompanyPolicyAdmin)
admin.site.register(EmergencyResponse, EmergencyResponseAdmin)
admin.site.register(Communications, CommunicationsAdmin)
admin.site.register(Documentation, DocumentationAdmin)
admin.site.register(AuditReview, AuditReviewAdmin)
admin.site.register(Location, LocationAdmin)