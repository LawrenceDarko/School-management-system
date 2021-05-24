from django.db import models
from django.utils import timezone

# Create your models here.


class Home(models.Model):
    welcome_head = models.CharField(max_length=150)
    text_summary = models.TextField(max_length=700)
    image = models.ImageField(upload_to='WelcomeImage/', blank=True, null=True)

    def __str__(self):
        return self.welcome_head

    def snippet(self):
        return self.text_summary[:20]+'...'


class Course(models.Model):
    course_title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='CourseImages/', blank=True, null=True)

    def __str__(self):
        return self.course_title


class NoticeImage(models.Model):
    image_title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='NoticeImage/', blank=True, null=True)

    def __str__(self):
        return self.image_title


class Notice(models.Model):
    event_name = models.CharField(max_length=100)
    event_details = models.TextField(max_length=200)

    def __str__(self):
        return self.event_name


# class Admission(models.Model):
#     admission_essay = models.TextField(max_length=300)

class AdmitNotice(models.Model):
    admit_essay = models.TextField(max_length=600)

    def __str__(self):
        return self.admit_essay


class ResearchInfo(models.Model):
    research_title = models.CharField(max_length=100)
    research_text = models.TextField(max_length=500)

    def __str__(self):
        return self.research_title

# class Research(models.Model):
#     title = models.CharField(max_length=20)
#     research_essay = models.TextField(max_length=300)


class StudentNews(models.Model):
    news_title = models.CharField(max_length=50)
    news_description = models.TextField(max_length=200)
    news_image = models.ImageField(
        upload_to='NewsImages/', blank=True, null=True)

    def __str__(self):
        return self.news_title


class StudentNewsTwo(models.Model):
    news_title = models.CharField(max_length=50)
    news_description = models.TextField(max_length=200)
    news_image = models.ImageField(
        upload_to='NewsImages/', blank=True, null=True)

    def __str__(self):
        return self.news_title

# class News(models.Model):
#     title = models.CharField(max_length=20)
#     description = models.TextField(max_length=40)
#     image = models.ImageField(upload_to='NewsImages/', blank=True, null=True)


class Footer(models.Model):
    address = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class SchoolGallery(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(
        upload_to='SchoolGallery/', blank=True, null=True)

    def __str__(self):
        return self.title


class SchoolHistory(models.Model):
    proprietor_history = models.TextField(max_length=1000)
    proprietor_image = models.ImageField(
        upload_to='StaffImages/', blank=True, null=True)


class AdministratorHistory(models.Model):
    administrator_history = models.TextField(max_length=1000)
    administrator_image = models.ImageField(
        upload_to='StaffImages/', blank=True, null=True)


class StaffInfo(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_description = models.TextField(max_length=100)
    staff_image = models.ImageField(
        upload_to='StaffImages/', blank=True, null=True)

    def __str__(self):
        return self.staff_name
