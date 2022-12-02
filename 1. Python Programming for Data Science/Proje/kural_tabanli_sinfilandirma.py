
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

# * * * * * * * * *

# Görev 1: Aşağıdaki Soruları Yanıtlayınız

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd

df = pd.read_csv("Proje/persona.csv")
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


# * * * * * * * * *

# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE":"mean"})


# * * * * * * * * *

# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# • Çıktıyı agg_df olarak kaydediniz.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE":"mean"}).sort_values("PRICE",ascending=False)
agg_df


# * * * * * * * * *

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.

# • Üçüncü sorunun çıktısında yer alan
# PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.

# indexi resetleme

agg_df = agg_df.reset_index()
agg_df.head()

# * * * * * * * * *

# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
# • Age sayısal değişkenini kategorik değişkene çeviriniz.
#Aralıkları ikna edici şekilde oluşturunuz.
# • Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

df.AGE.dtype #dtype('int64')

#nereden böleceğimizi ayarlayalım.

bins = [0,18,23,30,40,agg_df["AGE"].max()]

#böldüklerimize karsılık gelecek kategorıklerı oluşturalım

age_labels=['0_18', '19_23', '24_30', '31_40', '41_'+ str(agg_df["AGE"].max())]

# şimdi birleştirelim

agg_df["age_cut"] = pd.cut(agg_df["AGE"], bins, labels=age_labels)


# * * * * * * * * *

# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# • Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# • Yeni eklenecek değişkenin adı: customers_level_based
# • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based
# değişkenini oluşturmanız gerekmektedir.

agg_df.head()

# dataframedeki tüm satırları getirme
for row in agg_df.values:
    print(row)


# COUNTRY, SOURCE, SEX ve age_cut değişkenlerinin değerlerini yan yana koymak ve alt tire ile birleştirme
[row[0].upper()+"_"+ row[1].upper()+"_"+ row[2].upper()+"_"+ row[5].upper()+"_" for row in agg_df.values]

#Veri setine ekleyelim
agg_df["customers_level_based"] = [row[0].upper()+"_"+ row[1].upper()+"_"+ row[2].upper()+"_"+ row[5].upper() for row in agg_df.values]
agg_df.head()

# gereksiz değişkenleri çıkaralım
agg_df = agg_df[["customers_level_based","PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"]: # DEU_ANDROID_MALE_24_30
    print(i)

for i in agg_df["customers_level_based"].values: # DEU_ANDROID_MALE_24_30
    print(i)

# bir çok aynı segmnet olabilir
# örn : DEU_ANDROID_MALE_24_30 segmentinden bir çok sayıda olabilir

agg_df["customers_level_based"].value_counts()
# BRA_ANDROID_MALE_24_30      7 tane var

#bu sebeple segmentlere göre group by yaptıktan sonra price ortalamalarını almalı
# ve segmentleri tekilleştirmeliyiz

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"})
agg_df.head()

# customers_level_based indexte duruyor bunu normal değikene çevirelim

agg_df = agg_df.reset_index()
agg_df.head()


agg_df.shape # 109 tane farklı persona var

# her bir personanın 1 tane olmasını bekeriz :
agg_df["customers_level_based"].value_counts()

# * * * * * * * * *
# Görev 7:
# Yeni müşterileri (personaları) segmentlere ayırınız

# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’aSEGMENT göre 4 segmente ayırınız.
# •Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# •Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D","C","B","A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE":"mean"})



# * * * * * * * * *

# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# 1• 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve
# ortalama ne kadar gelir kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"

agg_df.head()

# fancy indexle arama
agg_df[agg_df["customers_level_based"] == new_user]

#        customers_level_based      PRICE SEGMENT
# 72  TUR_ANDROID_FEMALE_31_40  41.833333       A


# 2• 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve
# ortalama ne kadar gelir kazandırması beklenir?


new_user_2 = "FRA_IOS_FEMALE_31_40"
agg_df[ agg_df["customers_level_based"] == new_user_2]

#    customers_level_based      PRICE SEGMENT
# 63  FRA_IOS_FEMALE_31_40  32.818182       C