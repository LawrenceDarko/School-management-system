# Generated by Django 3.1.6 on 2021-02-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmitNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admit_essay', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='CourseImages/')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_head', models.CharField(max_length=150)),
                ('text_summary', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='WelcomeImage/')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('event_details', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to='NoticeImage/')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_title', models.CharField(max_length=100)),
                ('research_text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='SchoolGallery/')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proprietor_history', models.TextField(max_length=600)),
                ('proprietor_image', models.ImageField(blank=True, null=True, upload_to='StaffImages/')),
            ],
        ),
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_description', models.TextField(max_length=100)),
                ('staff_image', models.ImageField(blank=True, null=True, upload_to='StaffImages/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=20)),
                ('news_description', models.TextField(max_length=200)),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='NewsImages/')),
            ],
        ),
        migrations.CreateModel(
            name='StudentNewsTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=20)),
                ('news_description', models.TextField(max_length=200)),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='NewsImages/')),
            ],
        ),
    ]
