from pathlib import Path
import pandas as pd

from fihrist.models import Personel

pathd=Path("C:\\Users\\atessu\\Desktop\\xx\\calisan_data.csv")
data=pd.read_csv(pathd)
data2=pd.DataFrame(data,columns =['Isimler', 'Soyisimler','TelefonTuru','Departman','Sehir','DogumTarihi','Maas','Telefon','mail'])
personel=Personel.objects.get_or_create(isim=[""])
print(data2)