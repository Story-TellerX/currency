# Generated by Django 3.2.3 on 2021-07-14 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_auto_20210714_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='code_name',
            field=models.CharField(default='privatbank', max_length=64),
        ),
    ]