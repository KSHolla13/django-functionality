# Generated by Django 4.0.1 on 2022-01-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_alter_info_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='course',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='dist',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='door',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='gpa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='hobbies',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='institute',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='passed',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='picture',
            field=models.ImageField(null=True, upload_to='records'),
        ),
        migrations.AlterField(
            model_name='info',
            name='resume',
            field=models.FileField(null=True, upload_to='records'),
        ),
        migrations.AlterField(
            model_name='info',
            name='started',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='street',
            field=models.TextField(null=True),
        ),
    ]
