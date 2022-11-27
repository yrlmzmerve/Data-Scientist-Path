
#Virtual Environment Oluşturma

# Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
# conda create -n merve python=3

# Oluşturduğunuz environment'ı aktif ediniz
# conda activate merve

# Yüklü paketleri listeleyiniz
# conda list

# Environment içerisine Numpy'ın güncel versiyonunu ve
# Pandas'ın 1.4.1 versiyonunu aynı anda indiriniz
# conda install numpy pandas=1.4.1

# İndirilen Numpy'ın versiyonu nedir?
# conda list ile baktım : 1.23.3

# Pandas'ı upgrade ediniz. Yeni versiyonu nedir?
# conda upgrade pandas, 1.4.4

# Numpy'ı environmenttan siliniz.
# conda remove numpy

# Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz
# conda install seaborn matplotlib

# Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml
# dosyasını inceleyiniz
# conda env export > enviroment.yaml
# bunu çalıştırdıktan sonra bu .py dosyasının oldugu klasörde enviroment. yaml dosyası oluştuu gözlemlenir.
# bu dosyanın içinde enviromentlarımızın içindeki kütüphanelerin versiyonlarını içerir

# Oluşturduğunuz environment'i siliniz.
# Önce environment'i deactivate ediniz.
# conda deactivate
# sonra siliyoruz
# conda env remove -n merve
