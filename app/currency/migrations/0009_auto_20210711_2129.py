# Generated by Django 3.2.3 on 2021-07-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_remove_rate_type_curr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='type_curr_new',
        ),
        migrations.AddField(
            model_name='rate',
            name='type_curr',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Dollar'), (1, 'Euro')], default=0),
            preserve_default=False,
        ),
    ]
