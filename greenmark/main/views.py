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
    form = BussInfoForm
    if request.method == "POST":
        form = BussInfoForm(request.POST)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect("")
    context = {'form':form}
    return render(request, 'main/iso_buss_info.html', context)

@login_required
def iso_step_one(request):
    user = request.user
    formA = BussInfoForm
    formB = AspImpactForm
    if request.method == "POST":
        formA = BussInfoForm(request.POST)
        formB = AspImpactForm(request.POST)
        if formA.is_valid() and formB.is_valid():
            a = formA.save(commit=False)
            a.user = user
            b = formB.save(commit=False)
            b.user = user
            a.save()
            b.save()
            return redirect("main:print_doc")
    context = {
        'user': user,
        'formA': formA,
        'formB': formB        
    }
    return render(request, 'main/iso_form.html', context)

@login_required
def print_doc(request):
    user = request.user
    modelA = BussInfo.objects.filter(user=request.user)
    modelB = AspImpact.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
        'modelB': modelB
    }
    return render(request, 'main/print_doc.html', context)

