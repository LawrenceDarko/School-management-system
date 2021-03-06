from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SchoolHistory, StaffInfo
from .models  import Home, Footer, AdministratorHistory
# Create your views here.

def about(request):

    schoolhistoryinfo = SchoolHistory.objects.all().first()
    administratorhistory = AdministratorHistory.objects.all().first()
    staffinformation = StaffInfo.objects.all()
    homeinfo = Home.objects.all().first()
    footerinfo = Footer.objects.all().first()

    template = 'educore/about.html'

    context = {'school_history_info':schoolhistoryinfo, 'admin_info': administratorhistory, 'staff_information':staffinformation, 'home_info':homeinfo, 'footer_info':footerinfo}

    return render(request, template, context)