# Generated by Django 3.0.1 on 2020-09-10 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_auto_20200910_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='class_year',
        ),
    ]