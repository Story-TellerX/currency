# Generated by Django 3.2.3 on 2021-07-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0015_remove_rate_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='code_name',
            field=models.CharField(max_length=64),
        ),
    ]
