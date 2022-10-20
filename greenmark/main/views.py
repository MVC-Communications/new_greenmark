from django.shortcuts import render, redirect

from .models import *
from .forms import *

def iso_step_one(request):
    formA = BussInfoForm
    formB = AgreementDocForm
    formC = KeyDecisionMakerForm
    formD = EnvironManagerForm
    formE = OtherResponsiblePersonForm
    if request.method == "POST":
        formA = BussInfoForm(request.POST, request.FILES)
        formB = AgreementDocForm(request.POST)
        formC = KeyDecisionMakerForm(request.POST)
        formD = EnvironManagerForm(request.POST)
        formE = OtherResponsiblePersonForm(request.POST)
        a_valid = formA.is_valid()
        b_valid = formB.is_valid()
        c_valid = formC.is_valid()
        d_valid = formD.is_valid()

        if a_valid and b_valid and c_valid and d_valid:
            a = formA.save()
            b = formB.save()
            c = formC.save()
            d = formD.save()
            e = formE.save()
            return redirect("main:print_doc")
    context = {
        'formA': formA,
        'formB': formB,
        'formC': formC,
        'formD': formD,
        'formE': formE,
    }
    return render(request, 'main/iso_form.html', context)


def print_doc(request):
    return render(request, 'main/print_doc.html')