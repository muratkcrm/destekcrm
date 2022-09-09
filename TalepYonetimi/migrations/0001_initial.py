# Generated by Django 3.1.4 on 2020-12-01 07:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DestekTalebiKayit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DestekTalebiKonu', models.CharField(max_length=100, verbose_name='Talep Konusu')),
                ('DestekTalebiKisi', models.CharField(blank=True, max_length=100, null=True, verbose_name='Talep Eden Kişi')),
                ('DestekTalebiKisiTelefon', models.CharField(blank=True, max_length=100, null=True, verbose_name='İletişim')),
                ('DestekTalebiDurumu', models.CharField(choices=[('Kapalı', 'Kapalı'), ('Açık', 'Açık')], default=1, max_length=50, verbose_name='Talep Durumu')),
                ('DestekTalebiAciklama', models.TextField()),
                ('DestekTalebiDosya', models.FileField(blank=True, null=True, upload_to='Dosya/', verbose_name='Talep ile ilgili dosya ekle')),
                ('DestekTalebiBaslamaTarihi', models.DateField(auto_now_add=True, null=True)),
                ('DestekTalebiKayitTarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('DestekTalebiKapanmaTarihi', models.DateTimeField(auto_now=True, null=True)),
                ('DestekTalebiAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('DestekTalebiTfsId', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tfs Id')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DestekTalebiTuru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DestekTalebiAdi', models.CharField(max_length=30)),
                ('DestekTalebiAciklama', models.CharField(max_length=150)),
                ('DestekTalebiAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KategoriAdi', models.CharField(max_length=50, verbose_name='Kategori Adı')),
                ('KategoriAciklama', models.CharField(blank=True, max_length=150, null=True, verbose_name='Kategori Açıklama')),
                ('KategoriAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Kurumlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KurumAdi', models.CharField(max_length=250)),
                ('KurumAdres', models.CharField(blank=True, max_length=250, null=True)),
                ('KurumIl', models.CharField(blank=True, max_length=50, null=True)),
                ('KurumEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('KurumYetkili', models.CharField(blank=True, max_length=150, null=True)),
                ('KurumTelefon', models.CharField(blank=True, max_length=50, null=True)),
                ('KurumAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('KurumCreate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Uygulama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UygulamaAdi', models.CharField(max_length=30, verbose_name='Ürün/Modül Adı')),
                ('UygulamaAciklama', models.CharField(max_length=150, verbose_name='Ürün/Modül Açıklama')),
                ('UygulamaAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('UygulamaCreated', models.DateTimeField(editable=False)),
                ('UygulamaModified', models.DateTimeField()),
                ('UygulamaModifiedby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
                ('UygulamaUser', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='KurumBirimi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BirimAdi', models.CharField(max_length=250)),
                ('BirimAdresi', models.CharField(blank=True, max_length=250, null=True)),
                ('BirimEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('BirimYetkili', models.CharField(blank=True, max_length=150, null=True)),
                ('BirimTelefon', models.CharField(blank=True, max_length=50, null=True)),
                ('BirimAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('BirimCreate', models.DateTimeField(auto_now_add=True, null=True)),
                ('KurumAdi', models.ForeignKey(help_text='Birimin üst kurum adı seçimi yapılır.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kurumlar', to='TalepYonetimi.kurumlar')),
            ],
            options={
                'ordering': ['KurumAdi', 'BirimAdi', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Kisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KisiAdiSoyadi', models.CharField(max_length=250, verbose_name='Adı Soyadı')),
                ('KisiTelefon', models.CharField(blank=True, max_length=50, null=True)),
                ('KisiEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('KisiAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('KisiBirimAdi', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='KurumAdi', chained_model_field='KurumAdi', on_delete=django.db.models.deletion.DO_NOTHING, to='TalepYonetimi.kurumbirimi', verbose_name='Birim Adı')),
                ('KisiUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('KurumAdi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TalepYonetimi.kurumlar', verbose_name='Kurum Adı')),
            ],
            options={
                'verbose_name_plural': 'Kişi Kayıtları',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Duyurular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DuyuruTarihi', models.DateTimeField(auto_now_add=True)),
                ('DuyuruBaslik', models.CharField(default='', max_length=250, verbose_name='Duyurunun Konusu')),
                ('DuyuruAciklama', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Duyuru Metni')),
                ('DuyuruUygulama', models.CharField(choices=[('0', 'Hepsi'), ('1', 'GorevTakip'), ('2', 'TalepYonetim'), ('3', 'Satis')], default=0, max_length=50, verbose_name='Talep Durumu')),
                ('DuyuruAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('DuyuruUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Duyurular',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='DestekTalebiNotlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DestekTalebiNotlarKonu', models.CharField(max_length=50, verbose_name='Konu')),
                ('Metin', ckeditor.fields.RichTextField(help_text='Çağrı ile İlgili Tüm Notlarınızı ekleyebilirsiniz..', max_length=2000, null=True, verbose_name='İçerik')),
                ('OlusturmaTarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('DestekTalebiNotDosya', models.FileField(blank=True, null=True, upload_to='Notlar/', verbose_name='Çağrı Notlarına Dosya Ekle')),
                ('DestekTalebiNotAktif', models.BooleanField(default=True, verbose_name='silmek için Onayı kaldırın..!!!')),
                ('DestekTalebiKayit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DestekTalebiNotlar', to='TalepYonetimi.destektalebikayit')),
                ('DestekTalebiNotUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cağrı Notları',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='destektalebikayit',
            name='DestekTalebiBirim',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='DestekTalebiKurum', chained_model_field='KurumAdi', on_delete=django.db.models.deletion.DO_NOTHING, to='TalepYonetimi.kurumbirimi', verbose_name='Birim Adı'),
        ),
        migrations.AddField(
            model_name='destektalebikayit',
            name='DestekTalebiKategori',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TalepYonetimi.kategori', verbose_name='Destek Kaynağı'),
        ),
        migrations.AddField(
            model_name='destektalebikayit',
            name='DestekTalebiKurum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TalepYonetimi.kurumlar', verbose_name='Kurum Adı'),
        ),
        migrations.AddField(
            model_name='destektalebikayit',
            name='DestekTalebiTuruAdi',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='TuruAdi', to='TalepYonetimi.destektalebituru', verbose_name='Talep Türü'),
        ),
        migrations.AddField(
            model_name='destektalebikayit',
            name='DestekTalebiUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Kullanici', to=settings.AUTH_USER_MODEL, verbose_name='Talebi Açan Kullanıcı'),
        ),
        migrations.AddField(
            model_name='destektalebikayit',
            name='DestekTalebiUygulama',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TalepYonetimi.uygulama', verbose_name='Uygulama Adı'),
        ),
    ]