# Generated by Django 3.1.6 on 2021-06-02 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210602_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='email',
        ),
    ]