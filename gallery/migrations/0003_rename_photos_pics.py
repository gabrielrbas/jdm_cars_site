# Generated by Django 3.2.3 on 2021-05-26 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_photos_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Pics',
        ),
    ]
