# Generated by Django 3.1.6 on 2021-05-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0006_appoinment_doctorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoinment',
            name='doctorid',
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='doctor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='patient',
            field=models.CharField(max_length=50),
        ),
    ]
