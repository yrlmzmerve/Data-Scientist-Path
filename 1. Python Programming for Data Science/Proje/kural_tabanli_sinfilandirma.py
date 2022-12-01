
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama


# İş Problemi
"""Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
seviye tabanlı (level based) yeni müşteri tanımları (persona)
oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
istemektedir.

Örneğin:
Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
isteniyor.
"""
# Veri Seti Hikayesi
"""Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. 
Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
kullanıcı birden fazla alışveriş yapmış olabilir."""

"""
PRICE – Müşterinin harcama tutarı
SOURCE – Müşterinin bağlandığı cihaz türü
SEX – Müşterinin cinsiyeti
COUNTRY – Müşterinin ülkesi
AGE – Müşterinin yaşı
"""

# Görev 1: Aşağıdaki Soruları Yanıtlayınız

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd

df = pd.read_csv("Proje/Kural Tabanlı Sınıflandırma/persona.csv")
df.head()
df.shape # (5000, 5) : 5000 satır veri var

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].unique() # array(['android', 'ios'], dtype=object)
df["SOURCE"].value_counts()
# android    2974
# ios        2026

#  Soru 3: Kaç unique PRICE vardır?

df["PRICE"].unique() # array([39, 49, 29, 19, 59,  9], dtype=int64)
df["PRICE"].nunique() # 6

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

# 1.yol
df.groupby("PRICE").agg({"PRICE":"count"})

# 2.yol
df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df.groupby("COUNTRY").agg({"COUNTRY":"count"})

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY").agg({"PRICE":"sum"})

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

df.groupby("SOURCE").agg({"SOURCE":"count"})

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY").agg({"PRICE":"mean"})

#Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE").agg({"PRICE":"mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":"mean"})

# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE":"mean"})

# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# • Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE",ascending=False)
agg_df

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

# • Üçüncü sorunun çıktısında yer alan
# PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.

# indexi resetleme

agg_df.reset_index()
agg_df.head()


# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.

df.AGE.dtype #dtype('int64')

