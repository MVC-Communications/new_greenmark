from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import *
from .forms import *

@login_required
def iso_step_one(request):
    user = request.user
    formA = BussInfoForm
    if request.method == "POST":
        formA = BussInfoForm(request.POST)
        if formA.is_valid():
            a = formA.save(commit=False)
            a.user = user
            a.save()
            return redirect("main:print_doc")
    context = {
        'user': user,
        'formA': formA        
    }
    return render(request, 'main/iso_form.html', context)

@login_required
def print_doc(request):
    user = request.user
    modelA = BussInfo.objects.filter(user=request.user)
    context = {
        'user': user,
        'modelA': modelA,
    }
    return render(request, 'main/print_doc.html', context)

