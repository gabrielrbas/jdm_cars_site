# Generated by Django 3.2.3 on 2021-05-25 18:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.CharField(blank=True, max_length=255)),
                ('date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('source', models.ImageField(upload_to='photos/%Y/%m/')),
            ],
        ),
    ]
