# Generated by Django 2.0 on 2018-02-26 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0014_auto_20180223_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuddenAccelReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_at', models.DateField()),
                ('make_at', models.DateField()),
                ('accident_at', models.DateField()),
                ('detail', models.TextField()),
                ('source', models.CharField(max_length=200)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sudden_accels', to='desucar.Car')),
            ],
        ),
    ]