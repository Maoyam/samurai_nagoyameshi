# Generated by Django 4.2.6 on 2024-03-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondb', '0025_reguration_name_alter_reguration_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguration',
            name='text',
            field=models.TextField(default='', max_length=1000, verbose_name='規約本文'),
        ),
    ]