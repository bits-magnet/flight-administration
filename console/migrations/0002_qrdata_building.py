# Generated by Django 2.2.4 on 2019-08-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrdata',
            name='building',
            field=models.IntegerField(default=0),
        ),
    ]
