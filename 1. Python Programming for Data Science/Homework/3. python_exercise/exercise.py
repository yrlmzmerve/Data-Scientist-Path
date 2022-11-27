# Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
type(x)

y=3.2
type(y)

z=8j+18
type(z)

a="python"
type(a)

b= True
type(b)

c = 22 < 23
type(c)

l = [1,2,3,4]
type(l)

d = { "name" : "jake",
      "age":27,
      "adress":"downtown" }

type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"python", "machine learning", "data science" }
type(s) #set

# -----------------------------------------------

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
Beklenen_cikti = ['THE','GOAL','IS','TO','TURN','DATA','INTO','INFORMATION','AND','INFORMATION','INTO', 'INSIGHT']


text = text.upper().replace(",","").replace(".","").split(" ")
text

# -------------------------------------

# Görev 3:
#
# Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

type(lst)
# listenin eleman sayısına bak
print("Listenin uzunluğu: ", len(lst))

#Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print("0. indexteki eleman: {} , 10. indexteki eleman : {}".format(lst[0],lst[10]))

#Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
new_lst = lst[0:4]
print(new_lst)

# Sekizinci indeksteki elemanı siliniz.
lst.pop(8)

# pop() içine birdeğer vermezsek son elemanı siler

#: Yeni bir eleman ekleyiniz.
lst.append("MRV")
lst

# Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")
lst

# -------------------------------------

#Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dct = {"Chrictian" : ["America",18],
       "Daisy": ["England",12],
       "Antonio" : ["Spain", 22],
       "Dante" : ["Italy", 25]
       }

# Key değerlerine erişiniz
dct.keys()

#Value'lara erişiniz
dct.values()

#Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz
# 1.yol
dct["Daisy"] = ["England",13]
dct

# 2.yol
dct.update({"Daisy": ["England",18] })
dct

# 3.yol
dct["Daisy"][1]=8
dct

# Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dct["Ahmet"] = ["Turkey",24]
dct

# Antonio'yu dictionary'den siliniz.
dct.pop("Antonio")
dct

# -------------------------------------

# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2,13,35,78,98,3]

def fun_evenorodd(lst):

    even_list=[]
    odd_list=[]

    for index in range(len(l)):
        if l[index]%2==0:
            even_list.append(l[index])
        else:
            odd_list.append(l[index])

    return even_list,odd_list

even, odd = fun_evenorodd(l)
print("Even list: ",even)
print("Odd list: ",odd)

# -------------------------------------
# Görev 6: List Comprehension yapısı kullanarak
# car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns # colum isimlerini getirme

for column in df.columns:
    print(df[column].dtype)


df.columns = ["NUM_"+column.upper() if df[column].dtype!="O" else column.upper() for column in df.columns]
df.columns


# -------------------------------------
# Görev 7: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns
df = sns.load_dataset("car_crashes")


df.columns = [ column.upper()+"_FLAG" if "no" not in column else column.upper() for column in df.columns]
df.columns


# Görev 8: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# -------------------------------------
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]
new_cols = [ column for column in df.columns if column not in og_list ]
new_cols

new_cols_df = df[new_cols]
new_cols_df
