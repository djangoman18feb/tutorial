from django.shortcuts import HttpResponse, render, redirect
from .forms import RegistrationForm
# Create your views here.

def home(request):
    return HttpResponse('i am home')

def login(request):
    return render(request, template_name='accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

