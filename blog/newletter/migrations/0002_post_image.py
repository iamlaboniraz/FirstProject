# Generated by Django 2.1 on 2018-08-30 09:58

from django.db import migrations, models
import newletter.models


class Migration(migrations.Migration):

    dependencies = [
        ('newletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=newletter.models.update_location),
        ),
    ]
