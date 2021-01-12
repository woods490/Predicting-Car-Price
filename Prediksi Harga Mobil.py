import pandas as pd                                  #Proses Data
import numpy as np                                   #Arrays
import matplotlib.pyplot as plt                      #Visualisasi
import seaborn as sns                                #Visualisasi
from termcolor import colored as cl                  #Pewarnaan Text
from sklearn.model_selection import train_test_split #Data Split Training dan Tests
from sklearn.linear_model import LinearRegression    #Algoritma Regresi Linear
from sklearn import preprocessing
from collections import defaultdict


#Import CSV Data yang Ingin Dilakukan Peramalan
data = pd.read_csv(r'C:\Users\Acer\Downloads\cars_data_modified.csv')
data = data.fillna(data.mean())

#Data Split Training dan Tests
select = ["make","body-style","fuel-type", "horsepower", "city-mpg", "highway-mpg"] #Kolom yang Digunakan untuk Regresi Linear
x = data[select]
y = data['price']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print("===== SPLITTED DATA =====")
print()
print(x_train,"==============\n", x_test,"==============\n",y_train,"==============\n", y_test)
print()

#Menghitung Regresi Linear
data_reg = LinearRegression()
data_reg.fit(x_train, y_train)
print("Slope/koefisien (m):", end=" ") #Menghitung M
print(data_reg.coef_)
print()
print("Intercept (b):", end=" ")       #Menghitung b
print(data_reg.intercept_)
print()
test_score = data_reg.score(x_test, y_test)
print("Score Model: %.2f" % test_score, '= %.2f' % (test_score*100),'%')
print()

#Menghitung Prediksi Harga
print("Kategorisasi mobil berdasarkan merk: ")
print()
print("toyota: 1")
print("nissan: 2")
print("mazda: 3")
print("honda: 4")
print("mitsubishi: 5")
print("subaru: 6")
print("volkswagen: 7")
print("peugot: 8")
print("volvo: 9")
print("dodge: 10")
print("bmw: 11")
print("mercedes-benz: 12")
print("plymouth: 13")
print("saab: 14")
print("audi: 15")
print("porsche: 16")
print("alfa-romero: 17")
print("chevrolet: 18")
print("jaguar: 19")
print("isuzu: 20")
print("renault: 21")
print("mercury: 22")
print()
make = float(input('Masukkan merk mobil (Contoh: Masukkan 1 untuk Toyota): '))
print()
print("Kategorisasi mobil berdasarkan body-style: ")
print("sedan: 1")
print("hatchback: 2")
print("wagon: 3")
print("hardtop: 4")
print("convertible: 5")
print()
bodystyle = float(input('Masukkan body-type mobil (Contoh: Masukkan 3 untuk Wagon): '))
print()
print("Kategorisasi mobil berdasarkan fuel-type: ")
print("gas: 1")
print("diesel: 2")
print()
fuelstyle = float(input('Masukkan fuel-style mobil (Contoh: Masukkan 1 untuk gas / bensin): '))
print()
horsepower = float(input('Masukkan horsepower mobil: '))
print()
citympg = float(input('Masukkan konsumsi bahan bakar dalam kota (miles per gallon): '))
print()
highwaympg = float(input('Masukkan konsumsi bahan bakar dalam tol (miles per gallon): '))
print()
variable:dict = {     
    "make"              : make,
    "body-style"        : bodystyle,
    "fuel-type"         : fuelstyle,
    "horsepower"        : horsepower,
    "city-mpg"          : citympg,
    "highway-mpg"       : highwaympg,
    "key"               : ["make", "body-style", "fuel-type", "horsepower", "city-mpg",
                           "highway-mpg"]
    }
print("Variable predict: ")
sdtin = []
for i in variable["key"]:
    sdtin.append(variable[i])
    print("\t>",i+' =', variable[i])
data_predict = data_reg.predict([sdtin])
print("Price Predict: $", int(round(data_predict[0],0)))
