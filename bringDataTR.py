def bringData():

    from selenium import webdriver
    import pandas as pd
    import time

    options = webdriver.ChromeOptions()
    
    options.add_argument('headless')

    url = "https://covid19.saglik.gov.tr/"

    driver = webdriver.Chrome(options = options)
    driver.get(url)

    time.sleep(1)
    item = driver.find_element_by_xpath('//*[@id="post-carosel-6"]/div/div[4]/div/table/tbody').text

    data = item.replace(",",".")

    # Veriler : İllere Göre Haftalık Vaka Sayısı (100 binde)
    ss = pd.Series(data.splitlines()).str.split(expand = True).rename(columns = {0: "Sehir Adi", 1:"Vaka Sayisi"})

    #splitlines, split metodu bir dizedeki kelimeleri boşluklardan ayırır ve bir dizeler listesi verir.
    #string.SplitYöntemi, giriş dizesini bir veya daha fazla sınırlayıcı temelinde bölerek bir alt dizeler dizisi oluşturur.
    #data'yi newline'lardan ayırarak 81 elemanlı bir listeye dönüştürüyoruz,
    # pd.Series'e paslıyoruz.
    # Sonra oradaki str.split'ten yararlanarak her veriyi,
    # "il-vaka" gibi bölüyoruz; expand=True bölüm sayısı kadar yeni sütuna koymayı sağlıyor.
    # Sonrasında sütunları yeniden adlandırıyoruz.

    ss.to_csv('verilerim.csv') # csv dosyasına yazdırıyoruz.
