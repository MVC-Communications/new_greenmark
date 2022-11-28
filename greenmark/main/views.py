from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import *
from .forms import *

@login_required
def iso_start(request):
    return render(request, 'main/iso_plan.html')

@login_required
def iso_buss_info(request):
    user = request.user
    formA = BussInfoForm
    formB = EnvCompObligForm
    formC = AspImpactForm
    formD = LocationForm
    if request.method == "POST":
        formA = BussInfoForm(request.POST)
        formB = EnvCompObligForm(request.POST)
        formC = AspImpactForm(request.POST)
        formD = LocationForm(request.POST)
        if formA.is_valid() and formB.is_valid() and formC.is_valid() and formD.is_valid():
            a = formA.save(commit=False)
            a.user = user
            b = formB.save(commit=False)
            b.user = user
            c = formC.save(commit=False)
            c.user = user
            d = formD.save(commit=False)
            d.user = user
            a.save()
            b.save()
            c.save()
            d.save()
            return redirect("main:iso_step_two")
    context = {
        'user': user,
        'formA': formA,
        'formB': formB,
        'formC': formC,
        'formD': formD,  
    }
    return render(request, 'main/iso_buss_info.html', context)

@login_required
def iso_step_two(request):
    user = request.user
    buss_info = BussInfo.objects.filter(user=request.user)
    asp_imp = AspImpact.objects.filter(user=request.user)
    formA = EnvThreatsForm
    formB = ObjectivesForm
    formC = CompanyPolicyForm
    formD = EmergencyResponseForm
    formE = CommunicationsForm
    formF = DocumentationForm
    if request.method == "POST":
        formA = EnvThreatsForm(request.POST)
        formB = ObjectivesForm(request.POST)
        formC = CompanyPolicyForm(request.POST)
        formD = EmergencyResponseForm(request.POST)
        formE = CommunicationsForm(request.POST)
        formF = DocumentationForm(request.POST)
        a_valid = formA.is_valid()
        b_valid = formB.is_valid()
        c_valid = formC.is_valid()
        d_valid = formD.is_valid()
        e_valid = formE.is_valid()
        f_valid = formF.is_valid()
        if a_valid and b_valid and c_valid and d_valid and e_valid and f_valid:
            a = formA.save(commit=False)
            a.user = user
            b = formB.save(commit=False)
            b.user = user
            c = formC.save(commit=False)
            c.user = user
            d = formD.save(commit=False)
            d.user = user
            e = formE.save(commit=False)
            e.user = user
            f = formF.save(commit=False)
            f.user = user
            a.save()
            b.save()
            c.save()
            d.save()
            e.save()
            f.save()
            return redirect("main:iso_step_three")
    context = {
        'user': user,
        'buss_info': buss_info,
        'formA': formA,
        'formB': formB,
        'formC': formC,
        'formD': formD,
        'formE': formE,
        'formF': formF,
        'asp_imp': asp_imp,       
    }
    return render(request, 'main/iso_do.html', context)


@login_required
def iso_step_three(request):
    user = request.user
    formA = AuditReviewForm
    if request.method == "POST":
        formA = AuditReviewForm(request.POST)
        if formA.is_valid():
            a = formA.save(commit=False)
            a.user = user
            a.save()
            return redirect("main:iso_step_four")
    context = {
        'user': user,
        'formA': formA,       
    }
    return render(request, 'main/iso_check.html', context)


@login_required
def iso_step_four(request):
    user = request.user
    modelA = BussInfo.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
    }
    return render(request, 'main/iso_act.html', context)



# @login_required
# def iso_step_one(request):
#     user = request.user
#     formA = BussInfoForm
#     formB = AspImpactForm
#     if request.method == "POST":
#         formA = BussInfoForm(request.POST)
#         formB = AspImpactForm(request.POST)
#         if formA.is_valid() and formB.is_valid():
#             a = formA.save(commit=False)
#             a.user = user
#             b = formB.save(commit=False)
#             b.user = user
#             a.save()
#             b.save()
#             return redirect("main:print_doc")
#     context = {
#         'user': user,
#         'formA': formA,
#         'formB': formB        
#     }
#     return render(request, 'main/iso_form.html', context)

@login_required
def print_doc(request):
    user = request.user
    modelA = BussInfo.objects.filter(user=request.user)
    modelB = EnvCompOblig.objects.filter(user=request.user)
    modelC = AspImpact.objects.filter(user=request.user)
    modelD = EnvThreats.objects.filter(user=request.user)
    modelE = Objectives.objects.filter(user=request.user)
    modelF = CompanyPolicy.objects.filter(user=request.user)
    modelG = EmergencyResponse.objects.filter(user=request.user)
    modelH = Communications.objects.filter(user=request.user)
    modelI = Documentation.objects.filter(user=request.user)
    modelJ = AuditReview.objects.filter(user=request.user)
    modelK = Location.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
        'modelB': modelB,
        'modelC': modelC,
        'modelD': modelD,
        'modelE': modelE,
        'modelF': modelF,
        'modelG': modelG,
        'modelH': modelH,
        'modelI': modelI,
        'modelJ': modelJ,
        'modelK': modelK,
    }
    return render(request, 'main/print_doc.html', context)

@login_required
def view_plan(request):
    user = request.user
    modelA = BussInfo.objects.filter(user=request.user)
    modelB = EnvCompOblig.objects.filter(user=request.user)
    modelC = AspImpact.objects.filter(user=request.user)
    modelD = Location.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
        'modelB': modelB,
        'modelC': modelC,
        'modelD': modelD,
    }
    return render(request, 'main/view_plan.html', context)


@login_required
def view_do(request):
    user = request.user
    modelA = EnvThreats.objects.filter(user=request.user)
    modelB = Objectives.objects.filter(user=request.user)
    modelC = CompanyPolicy.objects.filter(user=request.user)
    modelD = EmergencyResponse.objects.filter(user=request.user)
    modelE = Communications.objects.filter(user=request.user)
    modelF = Documentation.objects.filter(user=request.user)
    asp_imp = AspImpact.objects.filter(user=request.user)
    buss_info = BussInfo.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
        'modelB': modelB,
        'modelC': modelC,
        'modelD': modelD,
        'modelE': modelE,
        'modelF': modelF,
        'asp_imp': asp_imp,
        'buss_info': buss_info,
    }
    return render(request, 'main/view_do.html', context)

@login_required
def view_check(request):
    user = request.user
    modelA = AuditReview.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
    }
    return render(request, 'main/view_check.html', context)


@login_required
def view_act(request):
    user = request.user
    modelA = BussInfo.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
    }
    return render(request, 'main/view_act.html', context)

