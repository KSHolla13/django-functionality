# Generated by Django 4.0.1 on 2022-01-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_alter_info_firstname_alter_info_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='firstname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
