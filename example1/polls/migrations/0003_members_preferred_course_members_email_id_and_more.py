# Generated by Django 4.1.2 on 2022-10-19 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_members_age_remove_members_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Preferred_course',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AddField(
            model_name='members',
            name='email_id',
            field=models.EmailField(default='SOME STRING', max_length=236),
        ),
        migrations.AddField(
            model_name='members',
            name='location',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
    ]
