from django.db import models


# Create your models here.
class Yetki(models.Model):
    yetki_tipi = models.CharField(max_length=1, default=0)

    def __str__(self):
        return self.yetki_tipi


class AmirlikYetki(models.Model):
    LOCATOR_YES_NO_CHOICES = ((None, ''), (True, 'Var'), (False, 'Yok'))

    amirlik_yetki = models.BooleanField(choices=LOCATOR_YES_NO_CHOICES,
                                        max_length=3,
                                        blank=True, default=False, )
    amirlik_yetki_ismi = models.CharField(max_length=9)

    def __str__(self):
        return self.amirlik_yetki_ismi


class MudurlukYetki(models.Model):
    LOCATOR_YES_NO_CHOICES = ((None, ''), (True, 'Var'), (False, 'Yok'))

    mudurluk_yetki = models.BooleanField(choices=LOCATOR_YES_NO_CHOICES,
                                         max_length=3,
                                         blank=True, default=False, )
    mudurluk_yetki_ismi = models.CharField(max_length=9)

    def __str__(self):
        return self.mudurluk_yetki_ismi


class Amirlik(models.Model):
    amirlik = models.CharField(max_length=100)

    def __str__(self):
        return self.amirlik


class Mudurluk(models.Model):
    mudurluk = models.CharField(max_length=100)

    def __str__(self):
        return self.mudurluk


class Personel(models.Model):
    isim = models.CharField(max_length=200, unique=True)
    sicil = models.IntegerField()
    telefon = models.IntegerField()
    adres = models.TextField()
    tc = models.CharField(max_length=11)
    foto = models.ImageField(upload_to="fihrist/")
    mudurluk = models.ForeignKey(Mudurluk, on_delete=models.CASCADE, related_name='mudurlukr', )
    amirlik = models.ForeignKey(Amirlik, on_delete=models.CASCADE, related_name='amirlikr')
    amirlik_yetki = models.ForeignKey(AmirlikYetki, on_delete=models.CASCADE, related_name='amirr')
    mudurluk_yetki = models.ForeignKey(MudurlukYetki, on_delete=models.CASCADE, related_name='mudurr', )
    yetki = models.ForeignKey(Yetki, on_delete=models.CASCADE, related_name='yetkipersoneller', )

    def __str__(self):
        return self.isim


def ekle():
    from pathlib import Path
    import pandas as pd

    # from fihrist.models import Personel

    pathd = Path("C:\\Users\\oguzhan.ozturk\\Desktop\\xx\\calisan_data.csv")
    data = pd.read_csv(pathd)
    data2 = pd.DataFrame(data,columns=['Isimler', 'Soyisimler', 'TelefonTuru', 'Departman', 'Sehir', 'DogumTarihi', 'Maas','Telefon', 'mail'])
    personel=Personel()
    personel.objects.get_or_create(isim=data2["Isimler"],amirlik_yetki=0,amirlik=data2["Maas"],mudurluk_yetki=False,mudurluk=data2["Sehir"]
                                   ,tc=data2["Telefon"],telefon=data2["Telefon"],adres=data2["Departman"],sicil=data2["Telefon"])