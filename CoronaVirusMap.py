import folium
from folium import plugins
from folium.plugins import Draw
from branca import colormap as cm  #Bu kütüphane, haritaya özgü olmayan özellikleri barındıracak olan folium'dan bir yan ürün. Gelecekte bir HTML+JS nesil kütüphanesi olabilir.
import pandas as pd
import time
import bringDataTR,Methods

data = pd.read_excel("Data/world_coronavirus_cases.xlsx")
dataTr = pd.read_csv("Data/tr_enlem_boylam.csv")


bringDataTR.bringData()
time.sleep(1)
veriTrVaka = pd.read_csv("verilerim.csv")#,encoding="utf-8-sig")


#Sehir nüfüs ve bolge adlarını çektik.
ilBilgi = pd.read_excel("Data/SehirlerBolgeler.xlsx")
tr_nufus = list(ilBilgi["Nufus"])
tr_bolge_ad = list(ilBilgi["BolgeAd"])


enlemler = list(data["Enlem"])
boylamlar = list(data["Boylam"])
toplam_vaka = list(data["Toplam Vaka"])
vefatlar = list(data["Vefat Edenler"])
aktifVakalar = list(data["Aktif Vakalar"])
nufus = list(data["Nüfus"])
toplam_test = list(data["Toplam Test"])


t_enlemler = list(dataTr["tEnlem"])
t_boylamlar = list(dataTr["tBoylam"])

t_isimler = list(veriTrVaka["Sehir Adi"])
t_vakalar = list(veriTrVaka["Vaka Sayisi"])


linear = cm.LinearColormap(["green","blue","orange","red"],vmin=50,vmax=300)  #Tr color info


vaka_sayisi_haritasi = folium.FeatureGroup(name='Toplam Vaka Sayısı',show=False)
olum_orani_haritasi = folium.FeatureGroup(name="Ölüm Oranı",show=False)
aktif_vaka_haritasi = folium.FeatureGroup(name ="Aktif Vaka Sayısı",show=False)
test_orani_haritasi = folium.FeatureGroup(name="Test Oranı",show=False)
nufus_dagilim_haritasi = folium.FeatureGroup(name="Nüfus Dağılım Haritası",show=False)
tr_dagilim_haritasi = folium.FeatureGroup(name="Türkiye Vaka Haritası",show=False)
tr_sinir_haritasi = folium.FeatureGroup("Türkiye Sınır Dağılım Haritası",show=False)


draw = Draw(export=True)

world_map = folium.Map()


folium.TileLayer("Cartodb Positron").add_to(world_map)
folium.TileLayer("openstreetmap").add_to(world_map)
folium.TileLayer("Cartodb dark_matter").add_to(world_map)
folium.TileLayer("Stamen Terrain").add_to(world_map)


for enlem,boylam,vaka in zip(enlemler,boylamlar,toplam_vaka):
   vaka_sayisi_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                                radius=Methods.vaka_sayisi_yaricap(vaka),
                                                color=Methods.vaka_Sayisi_renk(vaka),
                                                fill_color=Methods.vaka_Sayisi_renk(vaka),
                                                fill_opacity=0.4))



for enlem,boylam,vaka,vefat in zip(enlemler,boylamlar,toplam_vaka,vefatlar):
   olum_orani_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                               radius=Methods.olum_orani_yaricap(vaka, vefat),
                                               color=Methods.olum_orani_renk(vaka, vefat),
                                               fill_color=Methods.olum_orani_renk(vaka, vefat),
                                               fill_opacity=0.4))



for enlem,boylam,aktif in zip(enlemler,boylamlar,aktifVakalar):
   aktif_vaka_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                               radius=Methods.aktif_vaka_yaricap(aktif),
                                               color=Methods.aktif_vaka_renk(aktif),
                                               fill_color=Methods.aktif_vaka_renk(aktif),
                                               fill_opacity=0.4))



for enlem,boylam,ulke_nufus ,test in zip(enlemler,boylamlar,nufus,toplam_test):
   test_orani_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                               radius=Methods.test_orani_yaricap(ulke_nufus, test),
                                               color=Methods.test_orani_renk(ulke_nufus, test),
                                               fill_color=Methods.test_orani_renk(ulke_nufus, test),
                                               fill_opacity=0.4))




for t_enlem,t_boylam,il,vaka in zip(t_enlemler,t_boylamlar,t_isimler,t_vakalar):
    tr_dagilim_haritasi.add_child(folium.Marker(location=[t_enlem,t_boylam], color = "red",
                                                icon=folium.Icon(color=Methods.tr_renklendir(sayi=vaka),
                                                                 icon='bar-chart',
                                                                 prefix='fa'),
                                                popup=Methods.risk(sayi=vaka),
                                                tooltip=["Sehir Adi:",il,
                                             "\nVaka Sayisi:",vaka]))




sehirIndex = veriTrVaka.set_index("Sehir Adi")
def vakaKontrol(vak):
    sonuc = (sehirIndex.loc[vak,'Vaka Sayisi'])
    return Methods.tr_renklendir(sonuc)



#Circle şeklinde yapmak için:
"""for t_enlem,t_boylam,il,vaka in zip(t_enlemler,t_boylamlar,t_isimler,t_vakalar):
   tr_dagilim_haritasi.add_child(folium.Circle(location=(t_enlem,t_boylam),
                                      radius=tr_vaka_sayisi_yaricap(vaka),
                                      color=Tr_renklendir(vaka),
                                      fill_color=Tr_renklendir(vaka),
                                      fill_opacity=0.4))"""


for enlem,boylam,ulke_nufus,test in zip(enlemler,boylamlar,nufus,toplam_test):
   test_orani_haritasi.add_child(folium.Circle(location=(enlem,boylam),
                                               radius=Methods.test_orani_yaricap(ulke_nufus, test),
                                               color=Methods.test_orani_renk(ulke_nufus, test),
                                               fill_color=Methods.test_orani_renk(ulke_nufus, test),
                                               fill_opacity=0.4))



nufus_dagilim_haritasi.add_child(folium.GeoJson(data=(open("Data/world.json", "r",
                                                           encoding="utf-8-sig").read()),
                                        style_function=lambda x: {"fillColor":"green"
                                        if x["properties"]["POP2005"] < 20000000
                                        else
                                        "white"
                                        if 20000000 <= x["properties"]["POP2005"] <= 50000000
                                        else
                                        "orange"
                                        if 50000000 <= x["properties"]["POP2005"] <= 100000000
                                        else
                                        "red"}))




tr_sinir_haritasi.add_child(folium.GeoJson(open("Data/turkey-il-sinirlar.json", "r",
                                                encoding="utf-8-sig").read(),
                                                style_function=lambda il:
                                                {'fillColor':vakaKontrol(il["properties"]["Name"])}))



miniMap = plugins.MiniMap(toggle_display=True)



world_map.add_child(vaka_sayisi_haritasi)
world_map.add_child(olum_orani_haritasi)
world_map.add_child(aktif_vaka_haritasi)
world_map.add_child(test_orani_haritasi)
world_map.add_child(nufus_dagilim_haritasi)
world_map.add_child(tr_dagilim_haritasi)
world_map.add_child(tr_sinir_haritasi)
world_map.add_child(miniMap)
world_map.add_child(linear)
world_map.add_child(draw)


world_map.add_child(folium.LayerControl(position="topright"))

world_map.save("world_map.html")