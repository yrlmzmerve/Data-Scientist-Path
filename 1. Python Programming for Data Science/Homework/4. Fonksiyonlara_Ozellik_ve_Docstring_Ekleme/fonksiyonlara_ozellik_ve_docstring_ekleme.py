# Görev 1 :  cat_summary() fonksiyonuna 1 özellik ekleyiniz.
# Bu özellik argümanla biçimlendirilebilir olsun.
# Var olan özelliğide argümanla kontrol edilebilir hale getirebilirsiniz.

# Fonksiyona arguman ile biçimlendirilebilen bir özellik eklemek ne demek?
# Örnek olarak aşağıdaki check_df fonksiyonuna
# argümanla biçimlendirilebilen 2 özellik eklenmiştir.
# Bu özellikler ile tail fonksiyonunun kaç gözlemi göstereceği ve quantile
# değerlerinin gösterilip gösterilmeyeceği fonksiyona özellik olarak girilmiştir.
# Bu özellikleri kullanıcı argümanlarla biçimlendirebilmektedir.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

# Görev 2 : Görev: check_df(), cat_summary() fonksiyonlarına
# 4 bilgi(uygunsa) barındıran numpy tarzı docstring yazınız.
# (task, params, return, example)

def check_df(dataframe, head=5):

    """
    Bu fonksiyon gelen dataframe ile ilgili genel bilgileri inceleme sağlar

    Parameters
    ----------
        dataframe : dataframe
        head : int

    Returns
    -------
        None

    Examples
    --------
        check_df(dataframe,3)

    """

    print("##################### Columns Size #####################")
    print(dataframe.columns.size)
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


def cat_summary(dataframe, col_name, plot=False):
    """
    Bu fonksiyon datafremdeki her bir column için içerdiği sınıf sayısının içerdiği eleman sayısını verir
    Parameters
    ----------
    dataframe : dataframe
    col_name : String
    plot

     Returns
    -------
        None

    Examples
    --------
        import seaborn as sns
        df = sns.load_dataset("titanic")
        cat_summary(df, "Survived", plot=True)


    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()

