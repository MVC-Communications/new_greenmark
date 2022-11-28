from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group


from main.models import *
from main.forms import *
from .forms import NewUserForm

def homepage(request):
    return render(request, "accounts/home.html")

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

@login_required
def dashboard(request):
	modelA = BussInfo.objects.filter(user=request.user)
	modelB = EnvThreats.objects.filter(user=request.user)
	modelC = AuditReview.objects.filter(user=request.user)
	context = {
        'modelA': modelA,
        'modelB': modelB,
		'modelC': modelC,
    }
	return render(request, "accounts/dashboard.html", context)

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
	users = User.objects.all().order_by("-id")
	modelA = BussInfo.objects.all().order_by("-id")
	modelC = AuditReview.objects.all().order_by("-id")
	context = {
		'users': users,
		'modelA': modelA,
		'modelC': modelC,
	}
	return render(request, "accounts/admin_dashboard.html", context)


@login_required
@user_passes_test(is_admin)
def admin_view_iso(request, pk):
	user = User.objects.get(id=pk)
	modelA = BussInfo.objects.filter(id=pk)
	modelB = EnvCompOblig.objects.filter(id=pk)
	modelC = AspImpact.objects.filter(id=pk)
	modelD = EnvThreats.objects.filter(id=pk)
	modelE = Objectives.objects.filter(id=pk)
	modelF = CompanyPolicy.objects.filter(id=pk)
	modelG = EmergencyResponse.objects.filter(id=pk)
	modelH = Communications.objects.filter(id=pk)
	modelI = Documentation.objects.filter(id=pk)
	modelJ = AuditReview.objects.filter(id=pk)
	modelK = Location.objects.filter(id=pk)
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
	return render(request, 'accounts/admin_view_iso.html', context)



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("accounts:dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})

# my_admin_group = Group.objects.get_or_create(name='ADMIN')



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				if is_admin(request.user):
					return redirect("accounts:admin-dashboard")
				else:
					return redirect("accounts:dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("accounts:homepage")