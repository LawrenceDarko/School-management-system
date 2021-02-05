from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Footer, SchoolGallery
# Create your views here.

# def home(request):
#     return render(request, 'Home/home.html')

def gallery(request):

    schoolgallery = SchoolGallery.objects.all()

    footerinfo = Footer.objects.all().first()

    template = 'educore/gallery.html'

    context = {'footer_info':footerinfo, 'school_gallery':schoolgallery}

    return render(request, template, context)