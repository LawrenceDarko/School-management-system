from django.contrib import admin
from .models import Home, Course, NoticeImage, Notice, Footer, AdmitNotice, ResearchInfo, StudentNews, StudentNewsTwo, SchoolGallery, SchoolHistory, StaffInfo
# Register your models here.

admin.site.register(Home)
admin.site.register(Course)
admin.site.register(NoticeImage)
admin.site.register(Notice)
admin.site.register(AdmitNotice)
admin.site.register(ResearchInfo)
admin.site.register(StudentNews)
admin.site.register(StudentNewsTwo)
admin.site.register(Footer)

admin.site.register(SchoolGallery)

admin.site.register(SchoolHistory)
admin.site.register(StaffInfo)