# Generated by Django 2.0 on 2018-02-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0015_suddenaccelreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suddenaccelreport',
            name='accident_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suddenaccelreport',
            name='buy_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suddenaccelreport',
            name='make_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]