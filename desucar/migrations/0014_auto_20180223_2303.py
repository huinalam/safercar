# Generated by Django 2.0 on 2018-02-23 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0013_auto_20180223_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('url', models.URLField()),
                ('join_required', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='communitydefect',
            name='solution',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='communitydefect',
            name='community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='desucar.Community'),
        ),
    ]
