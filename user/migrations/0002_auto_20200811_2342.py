# Generated by Django 3.1 on 2020-08-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='educational_status',
            field=models.PositiveIntegerField(choices=[(0, 'İlkokul'), (1, 'Ortaokul'), (2, 'Lise'), (3, 'Üniversite'), (4, 'Yüksek Lisans / Doktora')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.PositiveIntegerField(choices=[(1, 'Erkek'), (0, 'Kadın')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='martial_status',
            field=models.PositiveIntegerField(choices=[(1, 'Bekar'), (0, 'Evli')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.PositiveIntegerField(choices=[(0, 'Özel Sektör'), (1, 'Öğrenci'), (2, 'Kamu Çalışanı'), (3, 'Serbest Meslek'), (4, 'Ev Hanımı'), (5, 'Emekli'), (6, 'Çalışmıyorum'), (7, 'Çiftçi')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(to='user.Interest'),
        ),
    ]
