# Generated by Django 3.2.3 on 2021-07-14 01:00

from django.db import migrations


def forwards(apps, schema_editor):
    Rate = apps.get_model('currency', 'Rate')
    Bank = apps.get_model('currency', 'Bank')

    monobank = Bank.objects.create(
        name='MonoBank',
        url='https://api.monobank.ua/bank/currency',
        original_url='https://www.monobank.ua/',
        number='0 800 205 205',
    )

    for rate in Rate.objects.all():
        if 'monobank' in rate.source.lower():
            rate.bank = monobank
        rate.save()

    vkurse = Bank.objects.create(
        name='Vkurse',
        url='http://vkurse.dp.ua/course.json',
        original_url='http://vkurse.dp.ua/',
        number='+38(067)989-22-95',
    )

    for rate in Rate.objects.all():
        if 'vkurse' in rate.source.lower():
            rate.bank = vkurse
        rate.save()

    iboxbank = Bank.objects.create(
        name='IBoxBank',
        url='https://app.iboxbank.online/api/currency/rate-only-base/UAH',
        original_url='https://iboxbank.online/ua/',
        number='0 (800) 500-178',
    )

    for rate in Rate.objects.all():
        if 'iboxbank' in rate.source.lower():
            rate.bank = iboxbank
        rate.save()

    grantbank = Bank.objects.create(
        name='GrantBank',
        url='https://ws.grant.ua/api/rates',
        original_url='https://www.grant.ua/ua/home/',
        number='+38(057)714-01-99',
    )

    for rate in Rate.objects.all():
        if 'grantbank' in rate.source.lower():
            rate.bank = grantbank
        rate.save()

    skybank = Bank.objects.create(
        name='SkyBank',
        url='https://tascombank.ua/api/currencies',
        original_url='https://tascombank.ua/',
        number='0 (800) 503 580',
    )

    for rate in Rate.objects.all():
        if 'skybank' in rate.source.lower():
            rate.bank = skybank
        rate.save()


def backwards(apps, schema_editor):
    print('HELLO FROM BACKWARDS')


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0013_bank_code_name'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
