# Generated by Django 4.0.4 on 2022-05-21 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PerTakip', '0003_alter_perizindurum_id_alter_pertakipkayit_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perizindurum',
            name='PerAdiSoyadi',
            field=models.CharField(blank=True, max_length=250, verbose_name='Personel Adı-Soyadı'),
        ),
    ]
