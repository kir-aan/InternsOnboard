# Generated by Django 2.2.4 on 2019-08-12 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InternsOnboardMain', '0007_auto_20190812_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshippost',
            name='Uploader_info',
        ),
    ]
