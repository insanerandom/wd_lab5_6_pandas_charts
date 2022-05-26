import numpy as np #numpy 1.22.3
import pandas as pd
import matplotlib.pyplot as plt #matplotlib 3.5.1
from PIL import Image #pillow 9.0.1

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

#Zadanie1
#Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
print("Zadanie 1")
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, header=0)
# a = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(a)
# wykres = a.plot()
# wykres.set_xlabel('Rok')
# wykres.set_ylabel('Liczba')
# plt.xticks(np.arange(df['Rok'].min(), df['Rok'].max() + 1, 1))
# wykres.legend()
# wykres.set_title('Liczba urodzonych dzieci dla kazdego roku')
# # plt.show()
# print("########################")

# #Zadanie 2
# #Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
# print("Zadanie 2")
# a = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(a)
# a.plot(kind='bar', xlabel='Plec', ylabel='Liczba', rot=0, legend=True, title='Liczba urodzonych chlopcow i dziewczynek.')
# # plt.show()
print("########################")

#Zadanie 3
#Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5
#latach z datasetu.
print("Zadanie 3")
k = df.loc[(df['Rok'] >= 2012) & (df['Plec'] == 'K'), 'Liczba'].sum()
print(k)
m = df.loc[(df['Rok'] >= 2012) & (df['Plec'] == 'M'), 'Liczba'].sum()
print(m)
print("########################")
a = df.where(df['Rok'] >= 2012).groupby(['Plec']).agg({'Liczba':['sum']})
print(a)
a.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
plt.legend(loc="lower right")
plt.title("Ilosc urodzonych chlopcow i dziewczynek w ostatnich 5 latach")
plt.show()
print("########################")

#Zadanie 4
#Wyświetl za pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych
#sprzedawców (zbiór danych zamówienia.csv).

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df)
a = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
print(a)
a.plot(kind='bar', xlabel='Sprzedawca', ylabel='Ilosc zamowien', rot=0, legend=True, title='Ilosc zlozonych zamowien przez poszczegolnych sprzedawcow')
plt.show()