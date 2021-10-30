from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    context = {'contact': 'active'}
    if request.method == 'POST':
        cont_name = request.POST.get('Name', default='')
        cont_email = request.POST.get('Email', default='')
        cont_subject = request.POST.get('Subject', default='')
        cont_mess = request.POST.get('Message', default='')
        con = Contact(name = cont_name, email = cont_email, subject = cont_subject, message = cont_mess)
        con.save()
        messages.success(request, 'Your message has been sent. Thank you!')       
    return render(request, 'core/contact.html', context)
