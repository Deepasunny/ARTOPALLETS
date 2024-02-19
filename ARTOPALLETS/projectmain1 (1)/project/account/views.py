from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from account.forms import RegistrationForm
from .models import Customisation
from .models import Feedback

def home(request):
    return render(request, 'home.html')


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})



def customization(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        emailid = request.POST.get('emailid')
        suggestion = request.POST.get('suggestion')
        customisation = Customisation(fname=fname, lname=lname, emailid=emailid, suggestion=suggestion)
        customisation.save()
        return HttpResponse("Data Saved")

    else:
        return render(request, 'customization.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phonenumber=request.POST.get('phonenumber')
        feedback = Feedback(name=name, email=email, message=message,phonenumber=phonenumber)
        feedback.save()
        return HttpResponse("Data Saved")
    else:
        return render(request, 'feedback.html')
    
    

def payment_success(request):
    # Process the form submission and any other required logic
    # ...

    # Set a success message
    messages.success(request, "Payment is successful.")

    # Render the success page
    return render(request, 'payment_success.html')
from django.contrib import messages

