# Generated by Django 3.0.6 on 2020-05-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegister', '0002_auto_20190805_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
