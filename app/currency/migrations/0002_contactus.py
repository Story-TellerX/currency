# Generated by Django 3.2.3 on 2021-05-25 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=2500)),
            ],
        ),
    ]
