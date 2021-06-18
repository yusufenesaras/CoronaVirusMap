
def vaka_Sayisi_renk(vaka):
    if vaka < 200000:
        return "green"

    elif vaka < 450000:
        return "white"

    elif vaka < 1750000:
        return "orange"

    else:
        return "red"


def vaka_sayisi_yaricap(vaka):
    if vaka < 200000:
        return 40000

    elif vaka < 450000:
        return 100000

    elif vaka < 1750000:
        return 200000

    else:
        return 400000


def olum_orani_yaricap(vaka,vefat):
    if (vefat/vaka) * 100 < 2.5:
        return 40000

    elif (vefat/vaka) * 100 < 5:
        return 100000

    elif (vefat/vaka) * 100 < 7.5:
        return 200000

    else:
        return 400000


def olum_orani_renk(vaka,vefat):
    if (vefat/vaka) * 100 < 2.5:
        return "green"

    elif (vefat/vaka) * 100 < 5:
        return "white"

    elif (vefat/vaka) * 100 < 7.5:
        return "orange"

    else:
        return "red"


def aktif_vaka_renk(aktif):
    if aktif < 100000:
        return "green"

    elif aktif < 250000:
        return "white"

    elif aktif < 750000:
        return "orange"

    else:
        return "red"


def aktif_vaka_yaricap(aktif):
    if aktif < 100000:
        return 40000

    elif aktif < 300000:
        return 100000

    elif aktif < 750000:
        return 200000

    else:
        return 400000


def test_orani_yaricap(nufus,test):
    if (test / nufus) * 100 < 2.5:
        return 400000

    elif (test / nufus) * 100 < 5:
        return 200000

    elif (test / nufus) * 100 < 7.5:
        return 100000

    else:
        return 40000


def test_orani_renk(nufus,test):
    if (test / nufus) * 100 < 2.5:
        return "red"

    elif (test / nufus) * 100 < 5:
        return "orange"

    elif (test / nufus) * 100 < 7.5:
        return "white"

    else:
        return "green"

#TR
def tr_renklendir(sayi):
    if sayi < 30.000:
        return "green"
    elif 30.000 <= sayi < 70.000:
        return "blue"
    elif 70.000 <= sayi < 110.000:
        return "orange"
    else:
        return "red"


def risk(sayi):
    if sayi < 30.000:
        return "Düşük Risk"
    elif 30.000 <=sayi <70.000:
        return "Orta Risk"
    elif 70.000 <= sayi < 110.000:
        return "Yüksek Risk"
    else:
        return "Çok Yüksek Risk"


#TR circle ile kullanmak için açılması gereken metot.
"""def tr_vaka_sayisi_yaricap(vaka):
    if vaka < 50000:
        return 40000
    elif 50000 <= vaka < 150000:
        return 100000
    elif 150000 <= vaka < 300000:
        return 200000
    else:
        return 300000"""