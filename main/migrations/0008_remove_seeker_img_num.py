# Generated by Django 3.1.6 on 2021-06-02 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210602_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeker',
            name='img_num',
        ),
    ]
