# Generated by Django 2.2.4 on 2019-08-07 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentPortal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinternship',
            name='companyName',
        ),
        migrations.RemoveField(
            model_name='studentinternship',
            name='studentName',
        ),
    ]
