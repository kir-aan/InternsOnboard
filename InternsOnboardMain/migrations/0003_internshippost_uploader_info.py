# Generated by Django 2.2.4 on 2019-08-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InternsOnboardMain', '0002_auto_20190806_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshippost',
            name='Uploader_info',
            field=models.CharField(editable=False, max_length=100, null=True),
        ),
    ]