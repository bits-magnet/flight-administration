# Generated by Django 2.2.4 on 2019-12-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0002_auto_20191208_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(default='', max_length=50)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_from', to='console.Airports'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_to', to='console.Airports'),
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
    ]
