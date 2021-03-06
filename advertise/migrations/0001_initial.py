# Generated by Django 3.1 on 2020-08-18 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='ilan başlığı')),
                ('description', models.TextField(max_length=500, verbose_name='ilan açıklaması')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Fiyat')),
                ('square_meter', models.PositiveIntegerField(default=0, verbose_name='Metrekaresi')),
                ('number_of_rooms', models.PositiveIntegerField(choices=[(0, '1+0'), (1, '1+1'), (2, '2+0'), (3, '2+1'), (4, '2+2'), (5, '3+1'), (6, '3+2'), (7, '4+1'), (8, '4+2'), (9, '5+1'), (10, '5+2'), (11, '6+1'), (12, '6+2'), (13, '7+1'), (14, '7+2')], verbose_name='Oda sayısı')),
                ('building_age', models.PositiveIntegerField(choices=[(0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5-10 Arası'), (5, '11-15 Arası'), (6, '16-20 Arası'), (7, '20-25 Arası'), (8, '25-30 Arası'), (9, '30-40 Arası'), (10, '40-50 Arası')], verbose_name='Bina Yaşı')),
                ('floor', models.PositiveIntegerField(choices=[(0, 'Bodrum Kat'), (1, 'Zemin Kat'), (2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7'), (9, '8'), (10, '9'), (11, '10'), (12, '11'), (13, '12'), (14, '13'), (15, '14'), (16, '15'), (17, '16'), (18, '17'), (19, '18'), (20, '19'), (21, '20')], verbose_name='Bulunduğu Kat')),
                ('number_of_floors', models.PositiveIntegerField(choices=[(2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5'), (7, '6'), (8, '7'), (9, '8'), (10, '9'), (11, '10'), (12, '11'), (13, '12'), (14, '13'), (15, '14'), (16, '15'), (17, '16'), (18, '17'), (19, '18'), (20, '19'), (21, '20')], verbose_name='Kat sayısı')),
                ('number_of_bathrooms', models.PositiveIntegerField(choices=[(0, 'Yok'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], verbose_name='banyo sayısı')),
                ('heating', models.PositiveIntegerField(choices=[(0, 'Yok'), (1, 'Soba'), (2, 'Doğalgaz Sobası'), (3, 'Kat Kaloriferi'), (4, 'Merkezi Isıtıcı'), (5, 'Doğalgaz'), (6, 'Klima'), (7, 'Şömine')], verbose_name='Isınma Durumu')),
                ('balcony_exists', models.BooleanField(default=False, verbose_name='Balkon Durumu')),
                ('using_status', models.PositiveIntegerField(choices=[(0, 'Boş'), (1, 'Kiracılı'), (2, 'Mülk Sahibi')], verbose_name='Kullanım Durumu')),
                ('housing_shape', models.PositiveIntegerField(choices=[(1, 'Birinci El(Sıfır)'), (2, 'İkinci El')], verbose_name='Konut Şekli')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='İlan oluşturma zamanı')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='ilan güncellenme zamanı')),
                ('status', models.PositiveIntegerField(choices=[(0, 'Aktif'), (1, 'Kiralandı'), (2, 'Satıldı')], verbose_name='Aktiflik Durumu')),
                ('visibility', models.PositiveIntegerField(choices=[(0, 'Herkes'), (1, 'Sadece Ben')], verbose_name='İlan Görünürlüğü')),
            ],
        ),
        migrations.CreateModel(
            name='ExteriorFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Frontal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='InteriorFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Landscape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SuitableForDisabled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertiseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('advertiseForeign', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='advertise.advertise')),
            ],
        ),
        migrations.AddField(
            model_name='advertise',
            name='exterior_feature',
            field=models.ManyToManyField(to='advertise.ExteriorFeature'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='frontal',
            field=models.ManyToManyField(to='advertise.Frontal'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='interior_feature',
            field=models.ManyToManyField(to='advertise.InteriorFeature'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='landscape',
            field=models.ManyToManyField(to='advertise.Landscape'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='locality',
            field=models.ManyToManyField(to='advertise.Locality'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertise',
            name='sutiable_for_disabled',
            field=models.ManyToManyField(to='advertise.SuitableForDisabled'),
        ),
        migrations.AddField(
            model_name='advertise',
            name='transportation',
            field=models.ManyToManyField(to='advertise.Transportation'),
        ),
    ]
