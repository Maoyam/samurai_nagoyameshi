# Generated by Django 4.2.6 on 2024-03-08 07:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commondb', '0021_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=100, verbose_name='所在地'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondb.area', verbose_name='エリア'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondb.genre', verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_images', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='information',
            field=models.CharField(max_length=300, verbose_name='お店の説明'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, verbose_name='店舗名'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name_alphabet',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]+$')], verbose_name='店舗名アルファベット表記'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price_high',
            field=models.CharField(max_length=5, verbose_name='上限価格'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='price_low',
            field=models.CharField(max_length=5, verbose_name='下限価格'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='time',
            field=models.CharField(max_length=100, verbose_name='営業時間'),
        ),
    ]