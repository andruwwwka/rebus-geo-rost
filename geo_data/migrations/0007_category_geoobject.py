# Generated by Django 2.2.3 on 2019-08-13 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_data', '0006_auto_20190707_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('radius', models.IntegerField(blank=True, verbose_name='Радиус действия категории в метрах')),
                ('power', models.BooleanField(default=True, verbose_name='Степень влияния')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
        ),
        migrations.CreateModel(
            name='GeoObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo_data.Category')),
            ],
        ),
    ]
