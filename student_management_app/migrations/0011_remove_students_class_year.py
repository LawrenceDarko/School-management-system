# Generated by Django 3.0.1 on 2020-09-10 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0010_students_session_year_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='class_year',
        ),
    ]
