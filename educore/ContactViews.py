from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models  import Home, Footer

# Create your views here.
def contact(request):
    
    footerinfo = Footer.objects.all().first()

    template = 'educore/contact.html'

    context = {'footer_info':footerinfo}

    return render(request, template, context)