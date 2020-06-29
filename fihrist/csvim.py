from pathlib import Path
import pandas as pd

def ekle():
    from pathlib import Path
    import pandas as pd

    from fihrist.models import Personel

    pathd = Path("C:\\Users\\oguzhan.ozturk\\Desktop\\xx\\calisan_data.csv")
    data = pd.read_csv(pathd)
    data2 = pd.DataFrame(data,columns=['Isimler', 'Soyisimler', 'TelefonTuru', 'Departman', 'Sehir', 'DogumTarihi', 'Maas','Telefon', 'mail'])
    personel=Personel()
    personel.objects.get_or_create(isim=data2["Isimler"],amirlik_yetki=0,amirlik=data2["Maas"],mudurluk_yetki=False,mudurluk=data2["Sehir"]
                                   ,tc=data2["Telefon"],telefon=data2["Telefon"],adres=data2["Departman"],sicil=data2["Telefon"])


if __name__ == "__main__":
    ekle()