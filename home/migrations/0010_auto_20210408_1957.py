# Generated by Django 3.1.5 on 2021-04-08 12:57

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210408_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='divisi',
            field=models.CharField(default='Development', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jabatan',
            field=models.CharField(default='Supervisor', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='jenis_kelamin',
            field=models.CharField(default='Pria', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]