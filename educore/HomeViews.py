from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Home, Course, NoticeImage, Notice, AdmitNotice, ResearchInfo, StudentNews, Footer, StudentNewsTwo
# Create your views here.

# def home(request):
#     return render(request, 'Home/home.html')

def home(request):

    homeinfo = Home.objects.all().first()
    courseInfo = Course.objects.all()
    noticeimageinfo = NoticeImage.objects.all().first()
    noticeinfo = Notice.objects.all()
    admitnoticeinfo = AdmitNotice.objects.all().first()
    researchessay = ResearchInfo.objects.all().first()
    studentnewsinfo = StudentNews.objects.all()
    studentnewsinfotwo = StudentNewsTwo.objects.all()
    footerinfo = Footer.objects.all().first()

    template = 'educore/home.html'

    context = {'home_info':homeinfo, 'course_info':courseInfo, 'notice_image_info':noticeimageinfo, 'notice_info':noticeinfo, 'admit_notice_info':admitnoticeinfo, 'research_essay':researchessay, 'student_news_info':studentnewsinfo, 'student_news_info_two':studentnewsinfotwo, 'footer_info':footerinfo}

    return render(request, template, context)