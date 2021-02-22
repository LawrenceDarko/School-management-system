# Generated by Django 3.1.6 on 2021-02-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrator_history', models.TextField(max_length=600)),
                ('administrator_image', models.ImageField(blank=True, null=True, upload_to='StaffImages/')),
            ],
        ),
    ]
