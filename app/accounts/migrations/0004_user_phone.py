# Generated by Django 3.2.3 on 2021-08-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=11, null=True),
        ),
    ]
