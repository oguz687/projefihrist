from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fihrist.models import Personel, Yetki, MudurlukYetki, AmirlikYetki, Mudurluk, Amirlik

# class CustomUserAdmin(admin.ModelAdmin):
#
#     model = Personel
#     list_display = ['isim', 'sicil','tc','adres','mudurluk','amirlik','yetki','amirlik_yetki','mudurluk_yetki','foto']

class PersonelAdmin(admin.ModelAdmin):
    list_display = ('isim', 'sicil','tc','adres','mudurluk','amirlik','yetki','amirlik_yetki','mudurluk_yetki','foto')

admin.site.register(Personel,PersonelAdmin)
admin.site.register(Yetki)
admin.site.register(MudurlukYetki)
admin.site.register(AmirlikYetki)
admin.site.register(Mudurluk)
admin.site.register(Amirlik)