# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.columns

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
print(df["sex"].value_counts())

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz
print(df.nunique())

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
print(df.pclass.nunique())

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
print(df[["pclass", "parch"]].nunique())

# Görev 6: embarked değişkeninin tipini kontrol ediniz.
# Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

print(df["embarked"].dtype)  # object
df["embarked"] = df["embarked"].astype("category")
print(df["embarked"].dtype)  # category

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.

# df[df["embarked"]=="C"]["embarked"]
df[df["embarked"] == "C"]

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] != "S"]

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df.loc[df["age"] < 30]
df.loc[df["age"] < 30, "age"]

# tüm bilgilerini getirme
df.loc[(df["age"] < 30) & (df["sex"] == "female")]

#  Yaşı 25 - 28 arası olan kadınların embarked ve classlarını getirme
df.loc[((df["age"] > 25) & (df["age"] < 28)) & (df["sex"] == "female"), ["class", "embark_town"]]

# Görev 10: Fare'i 500'den büyük veya
# yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
df.columns
df.fare.dtype

df.loc[(df["fare"] > 500) | (df["age"] > 70)]

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

df.isnull().values.any()  # hiç boş değer var mı ?

# Görev 12: who değişkenini dataframe’den çıkarınız.

df["who"]
df.drop("who", axis=1, inplace=True)

# Görev13:  deck değikenindeki boş değerleri
# deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz

df["deck"].unique()

mod = df["deck"].mode()[0]  # en çok tekrar eden değişken

df["deck"].fillna(mod, inplace=True)

# Görev 14: age değişkenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

df["age"].isnull().sum()  # 177 tane boş değer var
df["age"] = df["age"].fillna(df["age"].median())

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri
# kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz.
# (apply ve lambda yapılarını kullanınız)
import seaborn as sns

df = sns.load_dataset("titanic")


def age30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age30(x))

df.head()

# 2.yol
df["age_flag?2"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
df.head()

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

import seaborn as sns

df = sns.load_dataset("tips")
df.head()

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre
# total_bill değerinin sum, min, max ve mean değerlerini bulunuz.

df.columns
df["time"]

df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 19: Day ve time’a göre
# total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 20: Lunch zamanına ve kadın müşterilere ait
# total_bill ve tip değerlerinin
# day'e göre
# sum, min, max ve mean değerlerini bulunuz.

df.columns

df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day").agg(
    {"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})

# Görev 21: size'i 3'ten küçük,
# total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz.
# Her bir müşterinin ödediği totalbill ve tip in toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz.
# Bulduğunuz ortalamaların altında olanlara 0,
# üstünde ve eşit  olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
# Kadınlar için Female olanlarının ortalamaları,
# erkekler için ise Male olanların ortalamaları dikkate alınacktır.
# Parametre olarak cinsiyet ve total_bill
# alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)

f_avg = df[df["sex"] == "Female"]["total_bill"].mean()
m_avg = df[df["sex"] == "Male"]["total_bill"].mean()


def func(sex, total_bill):
    if sex == "Female":
        if (f_avg > total_bill):
            return 1
        else:
            return 0
    else:
        if (m_avg > total_bill):
            return 1
        else:
            return 0

df["total_bill_flag"] = df.apply(lambda x: func(x["sex"],x["total_bill"]),axis=1)
df.head()

# Görev 24: total_bill_flag değişkenini kullanarak
# cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.

df.groupby("sex").agg({"total_bill_flag":"count"})

df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag":"count"})

# Görev 25: Veriyi total_bill_tip_sum değişkenine
# göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

# Görev 22:de yaptıgımız değişken
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

temp_df = df.sort_values("total_bill_tip_sum",ascending=False)[:30]