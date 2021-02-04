# Generated by Django 3.0.1 on 2020-09-10 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0009_remove_students_session_year_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='session_year_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management_app.SessionYearModel'),
            preserve_default=False,
        ),
    ]
