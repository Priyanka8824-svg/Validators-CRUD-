from django.shortcuts import render, HttpResponse, redirect
from .forms import PersonForm
from .models import Person

# Create your views here.

def homeview(request):

    return render(request,"app1/home.html",{})
def pview(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            p = form.cleaned_data.get('pid')
            n = form.cleaned_data.get('name')
            e = form.cleaned_data.get('email')
            d = form.cleaned_data.get('dob')
            a = form.cleaned_data.get('age')
            c = form.cleaned_data.get('city')
            print(p, n, e, d, a, c)

            return HttpResponse("Data Saved")
    return render(request,"app1/add_person.html",{"form":form})