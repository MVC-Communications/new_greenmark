from random import choices
from django.db import models
from django.contrib.auth.models import User


ENVIRON_COMM_CHOICES = (
    ('suggestion','suggestion'),
    ('positive feedback','positive feedback'),
    ('complaints','complaints'),
    ('requests', 'requests')
)

IMPACTS_CHOICES = (
    ('Land','Land'),
    ('Air','Air'),
    ('Water','Water'),
    ('Land & Air','Land & Air'),
    ('Land & Water','Land & Water'),
    ('Air & Water','Air & Water'),
    ('Land, Air & Water','Land, Air & Water')
)

PROBABILITY_CHOICES = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low')
)

IF_OCCURS_CHOICES = (
    ('Major','Major'),
    ('Medium','Medium'),
    ('Minor','Minor')
)

YES_OR_NO = (
    ('Yes','Yes'),
    ('No','No')
)

PERSON_RESP_FOR_ENV_COMP = (
    ('Same as key decision maker','Same as key decision maker'),
    ('Same as environmental manager','Same as environmental manager'),
    ('Other','Other')
)

CURRENT_OBJECTIVES_OPTIONS = (
    ('Reduce energy use','Reduce energy use'),
    ('Increase the efficient use of resources materials','Increase the efficient use of resources materials'),
    ('Environmental training to employees','Environmental training to employees')
)

COMM_SUBJECT_OPTIONS = (
    ('Government & Other Compliance Obligations','Government & Other Compliance Obligations'),
    ('Environmental Aspects and Impacts','Environmental Aspects and Impacts'),
    ('Environmental Policy','Environmental Policy'),
    ('Objectives, Procedures','Objectives, Procedures'),
    ('Emergency Response Procedures','Emergency Response Procedures'),
    ('Training schedules','Training schedules'),
    ('Nonconformities, blanks and filled','Nonconformities, blanks and filled'),
    ('Quarterly Audits and Annual Management Review','Quarterly Audits and Annual Management Review'),
    ('Other relevant Information','Other relevant Information')
)

RECORDS_TYPE_OPTIONS = (
    ('This document (current year EMS)','This document (current year EMS)'),
    ('Prior year/s ISO 14001:2015 EMS','Prior year/s ISO 14001:2015 EMS'),
    ('Regulatory permits and records','Regulatory permits and records'),
    ('Other Compliance Obligations agreements','Other Compliance Obligations agreements'),
    ('Policy Statement','Policy Statement'),
    ('Objectives Planning Sheets (completed)','Objectives Planning Sheets (completed)'),
    ('Emergency Response Procedures','Emergency Response Procedures'),
    ('Other Operational Procedures','Other Operational Procedures'),
    ('Training Procedures','Training Procedures'),
    ('Quarterly Audits and Annual Review','Quarterly Audits and Annual Review'),
    ('Other documents','Other documents')
)

class BussInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_of_aggrement = models.DateField()
    buss_name = models.CharField(max_length=50)
    # buss_logo = models.ImageField(upload_to='media/BusinessLogos')
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=50)
    # location1 = models.CharField(max_length=70)
    # location2 = models.CharField(max_length=70, blank=True)
    # location3 = models.CharField(max_length=70, blank=True)
    # location4 = models.CharField(max_length=70, blank=True)
    keydecider_name = models.CharField(max_length=30)
    keydecider_title = models.CharField(max_length=30)
    keydecider_email = models.CharField(max_length=30)
    keydecider_signature = models.CharField(max_length=30)
    envmanager_name = models.CharField(max_length=30)
    envmanager_title = models.CharField(max_length=30)
    envmanager_email = models.CharField(max_length=30)
    envmanager_signature = models.CharField(max_length=30)
    otherresp_person_name = models.CharField(max_length=30, blank=True)
    otherresp_person_title = models.CharField(max_length=30, blank=True)
    otherresp_person_email = models.CharField(max_length=30, blank=True)
    otherresp_person_signature = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        pass 


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        pass 

class EnvCompOblig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    person_rep = models.CharField(max_length=50, choices=PERSON_RESP_FOR_ENV_COMP, blank=True, null=True)
    comp_oblig_name_1 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_1 = models.TextField(blank=True, null=True)
    comp_oblig_name_2 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_2 = models.TextField(blank=True, null=True)
    comp_oblig_name_3 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_3 = models.TextField(blank=True, null=True)
    comp_oblig_name_4 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_4 = models.TextField(blank=True, null=True)
    comp_oblig_name_5 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_5 = models.TextField(blank=True, null=True)
    comp_oblig_name_6 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_6 = models.TextField(blank=True, null=True)
    comp_oblig_name_7 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_7 = models.TextField(blank=True, null=True)
    comp_oblig_name_8 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_8 = models.TextField(blank=True, null=True)
    comp_oblig_name_9 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_9 = models.TextField(blank=True, null=True)
    comp_oblig_name_10 = models.CharField(max_length=50, blank=True, null=True)
    comp_oblig_description_10 = models.TextField(blank=True, null=True)
    env_comm_option = models.CharField(max_length=50, choices=ENVIRON_COMM_CHOICES, blank=True, null=True)
    env_comm_description = models.TextField(blank=True, null=True)

    def __str__(self):
        pass 

class AspImpact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_1 = models.CharField(max_length=50, blank=True, null=True)
    aspect_1 = models.CharField(max_length=50, blank=True, null=True)
    impact_1 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_2 = models.CharField(max_length=50, blank=True, null=True)
    aspect_2 = models.CharField(max_length=50, blank=True, null=True)
    impact_2 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_3 = models.CharField(max_length=50, blank=True, null=True)
    aspect_3 = models.CharField(max_length=50, blank=True, null=True)
    impact_3 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_4 = models.CharField(max_length=50, blank=True, null=True)
    aspect_4 = models.CharField(max_length=50, blank=True, null=True)
    impact_4 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_5 = models.CharField(max_length=50, blank=True, null=True)
    aspect_5 = models.CharField(max_length=50, blank=True, null=True)
    impact_5 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_6 = models.CharField(max_length=50, blank=True, null=True)
    aspect_6 = models.CharField(max_length=50, blank=True, null=True)
    impact_6 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_7 = models.CharField(max_length=50, blank=True, null=True)
    aspect_7 = models.CharField(max_length=50, blank=True, null=True)
    impact_7 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_8 = models.CharField(max_length=50, blank=True, null=True)
    aspect_8 = models.CharField(max_length=50, blank=True, null=True)
    impact_8 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_9 = models.CharField(max_length=50, blank=True, null=True)
    aspect_9 = models.CharField(max_length=50, blank=True, null=True)
    impact_9 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)
    activity_10 = models.CharField(max_length=50, blank=True, null=True)
    aspect_10 = models.CharField(max_length=50, blank=True, null=True)
    impact_10 = models.CharField(max_length=50, choices=IMPACTS_CHOICES, blank=True, null=True)

    def __str__(self):
        pass 

class EnvThreats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    threat1 = models.CharField(max_length=50, blank=True, null=True)
    impact1 = models.CharField(max_length=20, choices=IMPACTS_CHOICES, blank=True, null=True)
    probability1 = models.CharField(max_length=20, choices=PROBABILITY_CHOICES, blank=True, null=True)
    if_occurs1 = models.CharField(max_length=20, choices=IF_OCCURS_CHOICES, blank=True, null=True)
    threat2 = models.CharField(max_length=50, blank=True, null=True)
    impact2 = models.CharField(max_length=20, choices=IMPACTS_CHOICES, blank=True, null=True)
    probability2 = models.CharField(max_length=20, choices=PROBABILITY_CHOICES, blank=True, null=True)
    if_occurs2 = models.CharField(max_length=20, choices=IF_OCCURS_CHOICES, blank=True, null=True)
    threat3 = models.CharField(max_length=50, blank=True, null=True)
    impact3 = models.CharField(max_length=20, choices=IMPACTS_CHOICES, blank=True, null=True)
    probability3 = models.CharField(max_length=20, choices=PROBABILITY_CHOICES, blank=True, null=True)
    if_occurs3 = models.CharField(max_length=20, choices=IF_OCCURS_CHOICES, blank=True, null=True)
    threat4 = models.CharField(max_length=50, blank=True, null=True)
    impact4 = models.CharField(max_length=20, choices=IMPACTS_CHOICES, blank=True, null=True)
    probability4 = models.CharField(max_length=20, choices=PROBABILITY_CHOICES, blank=True, null=True)
    if_occurs4 = models.CharField(max_length=20, choices=IF_OCCURS_CHOICES, blank=True, null=True)
    threat5 = models.CharField(max_length=50, blank=True, null=True)
    impact5 = models.CharField(max_length=20, choices=IMPACTS_CHOICES, blank=True, null=True)
    probability5 = models.CharField(max_length=20, choices=PROBABILITY_CHOICES, blank=True, null=True)
    if_occurs5 = models.CharField(max_length=20, choices=IF_OCCURS_CHOICES, blank=True, null=True)

    def __str__(self):
        pass 


class Objectives(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objective_1 = models.CharField(max_length=50, null=True, blank=True)
    procedure_1 = models.CharField(max_length=50, null=True, blank=True)
    result_1 = models.CharField(max_length=50, null=True, blank=True)
    start_date_1 = models.CharField(max_length=50, null=True, blank=True)
    objective_2 = models.CharField(max_length=50, null=True, blank=True)
    procedure_2 = models.CharField(max_length=50, null=True, blank=True)
    result_2 = models.CharField(max_length=50, null=True, blank=True)
    start_date_2 = models.CharField(max_length=50, null=True, blank=True)
    objective_3 = models.CharField(max_length=50, null=True, blank=True)
    procedure_3 = models.CharField(max_length=50, null=True, blank=True)
    result_3 = models.CharField(max_length=50, null=True, blank=True)
    start_date_3 = models.CharField(max_length=50, null=True, blank=True)
    objective_4 = models.CharField(max_length=50, null=True, blank=True)
    procedure_4 = models.CharField(max_length=50, null=True, blank=True)
    result_4 = models.CharField(max_length=50, null=True, blank=True)
    start_date_4 = models.CharField(max_length=50, null=True, blank=True)
    objective_5 = models.CharField(max_length=50, null=True, blank=True)
    procedure_5 = models.CharField(max_length=50, null=True, blank=True)
    result_5 = models.CharField(max_length=50, null=True, blank=True)
    start_date_5 = models.CharField(max_length=50, null=True, blank=True)
    objective_6 = models.CharField(max_length=50, null=True, blank=True)
    procedure_6 = models.CharField(max_length=50, null=True, blank=True)
    result_6 = models.CharField(max_length=50, null=True, blank=True)
    start_date_6 = models.CharField(max_length=50, null=True, blank=True)
    objective_7 = models.CharField(max_length=50, null=True, blank=True)
    procedure_7 = models.CharField(max_length=50, null=True, blank=True)
    result_7 = models.CharField(max_length=50, null=True, blank=True)
    start_date_7 = models.CharField(max_length=50, null=True, blank=True)
    objective_8 = models.CharField(max_length=50, null=True, blank=True)
    procedure_8 = models.CharField(max_length=50, null=True, blank=True)
    result_8 = models.CharField(max_length=50, null=True, blank=True)
    start_date_8 = models.CharField(max_length=50, null=True, blank=True)
    objective_9 = models.CharField(max_length=50, null=True, blank=True)
    procedure_9 = models.CharField(max_length=50, null=True, blank=True)
    result_9 = models.CharField(max_length=50, null=True, blank=True)
    start_date_9 = models.CharField(max_length=50, null=True, blank=True)
    objective_10 = models.CharField(max_length=50, null=True, blank=True)
    procedure_10 = models.CharField(max_length=50, null=True, blank=True)
    result_10 = models.CharField(max_length=50, null=True, blank=True)
    start_date_10 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        pass 

class CompanyPolicy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_objectives = models.CharField(max_length=50, choices=CURRENT_OBJECTIVES_OPTIONS, null=True, blank=True)
    existing_policy = models.TextField(null=True, blank=True)

    def __str__(self):
        pass 

class EmergencyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    procedure_1 = models.CharField(max_length=50, null=True, blank=True)
    internal_contact_1 = models.CharField(max_length=50, null=True, blank=True)
    external_contact_1 = models.CharField(max_length=50, null=True, blank=True)
    procedure_2 = models.CharField(max_length=50, null=True, blank=True)
    internal_contact_2 = models.CharField(max_length=50, null=True, blank=True)
    external_contact_2 = models.CharField(max_length=50, null=True, blank=True)
    procedure_3 = models.CharField(max_length=50, null=True, blank=True)
    internal_contact_3 = models.CharField(max_length=50, null=True, blank=True)
    external_contact_3 = models.CharField(max_length=50, null=True, blank=True)
    procedure_4 = models.CharField(max_length=50, null=True, blank=True)
    internal_contact_4 = models.CharField(max_length=50, null=True, blank=True)
    external_contact_4 = models.CharField(max_length=50, null=True, blank=True)
    procedure_5 = models.CharField(max_length=50, null=True, blank=True)
    internal_contact_5 = models.CharField(max_length=50, null=True, blank=True)
    external_contact_5 = models.CharField(max_length=50, null=True, blank=True)
    procedure_6 = models.CharField(max_length=50, null=True, blank=True)
    internal_contact_6 = models.CharField(max_length=50, null=True, blank=True)
    external_contact_6 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        pass 

class Trainers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer_name = models.CharField(max_length=50)
    trainer_email = models.CharField(max_length=50)
    trainee_name = models.CharField(max_length=50)
    trainee_email = models.CharField(max_length=50)

    def __str__(self):
        pass 

# communications
class Communications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_1 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_1 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_1 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_1 = models.CharField(max_length=50, null=True, blank=True)
    when_1 = models.CharField(max_length=50, null=True, blank=True)
    subject_2 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_2 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_2 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_2 = models.CharField(max_length=50, null=True, blank=True)
    when_2 = models.CharField(max_length=50, null=True, blank=True)
    subject_3 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_3 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_3 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_3 = models.CharField(max_length=50, null=True, blank=True)
    when_3 = models.CharField(max_length=50, null=True, blank=True)
    subject_4 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_4 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_4 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_4 = models.CharField(max_length=50, null=True, blank=True)
    when_4 = models.CharField(max_length=50, null=True, blank=True)
    subject_5 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_5 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_5 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_5 = models.CharField(max_length=50, null=True, blank=True)
    when_5 = models.CharField(max_length=50, null=True, blank=True)
    subject_6 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_6 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_6 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_6 = models.CharField(max_length=50, null=True, blank=True)
    when_6 = models.CharField(max_length=50, null=True, blank=True)
    subject_7 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_7 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_7 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_7 = models.CharField(max_length=50, null=True, blank=True)
    when_7 = models.CharField(max_length=50, null=True, blank=True)
    subject_8 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_8 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_8 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_8 = models.CharField(max_length=50, null=True, blank=True)
    when_8 = models.CharField(max_length=50, null=True, blank=True)
    subject_9 = models.CharField(max_length=50, choices=COMM_SUBJECT_OPTIONS, null=True, blank=True)
    how_comm_9 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_9 = models.CharField(max_length=50, null=True, blank=True)
    who_receives_9 = models.CharField(max_length=50, null=True, blank=True)
    when_9 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        pass


# DOCUMENTATION
class Documentation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    records_type_1 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_1 = models.CharField(max_length=50, null=True, blank=True)
    other_location_1 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_1 = models.CharField(max_length=50, null=True, blank=True)
    comments_1 = models.TextField(null=True, blank=True)
    records_type_2 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_2 = models.CharField(max_length=50, null=True, blank=True)
    other_location_2 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_2 = models.CharField(max_length=50, null=True, blank=True)
    comments_2 = models.TextField(null=True, blank=True)
    records_type_3 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_3 = models.CharField(max_length=50, null=True, blank=True)
    other_location_3 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_3 = models.CharField(max_length=50, null=True, blank=True)
    comments_3 = models.TextField(null=True, blank=True)
    records_type_4 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_4 = models.CharField(max_length=50, null=True, blank=True)
    other_location_4 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_4 = models.CharField(max_length=50, null=True, blank=True)
    comments_4 = models.TextField(null=True, blank=True)
    records_type_5 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_5 = models.CharField(max_length=50, null=True, blank=True)
    other_location_5 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_5 = models.CharField(max_length=50, null=True, blank=True)
    comments_5 = models.TextField(null=True, blank=True)
    records_type_6 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_6 = models.CharField(max_length=50, null=True, blank=True)
    other_location_6 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_6 = models.CharField(max_length=50, null=True, blank=True)
    comments_6 = models.TextField(null=True, blank=True)
    records_type_7 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_7 = models.CharField(max_length=50, null=True, blank=True)
    other_location_7 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_7 = models.CharField(max_length=50, null=True, blank=True)
    comments_7 = models.TextField(null=True, blank=True)
    records_type_8 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_8 = models.CharField(max_length=50, null=True, blank=True)
    other_location_8 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_8 = models.CharField(max_length=50, null=True, blank=True)
    comments_8 = models.TextField(null=True, blank=True)
    records_type_9 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_9 = models.CharField(max_length=50, null=True, blank=True)
    other_location_9 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_9 = models.CharField(max_length=50, null=True, blank=True)
    comments_9 = models.TextField(null=True, blank=True)
    records_type_10 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_10 = models.CharField(max_length=50, null=True, blank=True)
    other_location_10 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_10 = models.CharField(max_length=50, null=True, blank=True)
    comments_10 = models.TextField(null=True, blank=True)
    records_type_11 = models.CharField(max_length=50, choices=RECORDS_TYPE_OPTIONS, null=True, blank=True)
    main_location_11 = models.CharField(max_length=50, null=True, blank=True)
    other_location_11 = models.CharField(max_length=50, null=True, blank=True)
    person_resp_11 = models.CharField(max_length=50, null=True, blank=True)
    comments_11 = models.TextField(null=True, blank=True)

    def __str__(self):
        pass


class AuditReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objective_1 = models.CharField(max_length=50, null=True, blank=True)
    start_date_1 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_1 = models.CharField(max_length=50, null=True, blank=True)
    comment_1 = models.TextField(null=True, blank=True)
    objective_2 = models.CharField(max_length=50, null=True, blank=True)
    start_date_2 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_2 = models.CharField(max_length=50, null=True, blank=True)
    comment_2 = models.TextField(null=True, blank=True)
    objective_3 = models.CharField(max_length=50, null=True, blank=True)
    start_date_3 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_3 = models.CharField(max_length=50, null=True, blank=True)
    comment_3 = models.TextField(null=True, blank=True)
    objective_4 = models.CharField(max_length=50, null=True, blank=True)
    start_date_4 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_4 = models.CharField(max_length=50, null=True, blank=True)
    comment_4 = models.TextField(null=True, blank=True)
    objective_5 = models.CharField(max_length=50, null=True, blank=True)
    start_date_5 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_5 = models.CharField(max_length=50, null=True, blank=True)
    comment_5 = models.TextField(null=True, blank=True)
    objective_6 = models.CharField(max_length=50, null=True, blank=True)
    start_date_6 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_6 = models.CharField(max_length=50, null=True, blank=True)
    comment_6 = models.TextField(null=True, blank=True)
    objective_7 = models.CharField(max_length=50, null=True, blank=True)
    start_date_7 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_7 = models.CharField(max_length=50, null=True, blank=True)
    comment_7 = models.TextField(null=True, blank=True)
    objective_8 = models.CharField(max_length=50, null=True, blank=True)
    start_date_8 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_8 = models.CharField(max_length=50, null=True, blank=True)
    comment_8 = models.TextField(null=True, blank=True)
    objective_9 = models.CharField(max_length=50, null=True, blank=True)
    start_date_9 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_9 = models.CharField(max_length=50, null=True, blank=True)
    comment_9 = models.TextField(null=True, blank=True)
    objective_10 = models.CharField(max_length=50, null=True, blank=True)
    start_date_10 = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    achievement_10 = models.CharField(max_length=50, null=True, blank=True)
    comment_10 = models.TextField(null=True, blank=True)

    def __str__(self):
        pass