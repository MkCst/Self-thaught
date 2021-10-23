# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 18:25:17 2021

@author: PC
"""


# Demographic data
import pandas as pd

df = pd.read_csv("adult_data.csv")

# Primeros y ultimos registros del archivo
print(df.head(3))
print(df.tail(3))
print("Info filas, columnas:\t",df.shape)


# Cuantas personas de cada raza estan en el conjunto de datos
race = df["race"] #Selecciona solo la columna 'race'
race_count = df["race"].value_counts()
print(race) 
print("\n\nCuenta los elementos de cada etiqueta\n",race_count)

# Edad media de los hombres
average_age_men = round(df[df["sex"]=="Male"]["age"].mean(),1)
print(average_age_men)

# Porcentaje de personas que tienen una licenciatura
num_bachelors = len(df[df["education"]=="Bachelors"])
total  = len(df)
percent_bachelors = round(num_bachelors/total*100, 1)
print(percent_bachelors)


# Porcentaje de personas con educacion avanzada que gana mas de 50k
# Porcentaje de personas sin educacion avanzada ganan mas de 50k
higher_education = df[df["education"].isin(["Bachelors","Masters","Doctorate"])]
lower_education = df[~df["education"].isin(["Bachelors","Masters","Doctorate"])]

hgh_education_rich = len(higher_education[higher_education.salary == ">50K"])
percent_educate_rich = round( hgh_education_rich/ len(higher_education)*100, 1)

lwr_education_rich = len(lower_education[lower_education.salary == ">50K"])
percent_lower_educate_rich = round( lwr_education_rich/ len(lower_education)*100, 1)

# Horas minimas trabajadas por personas a la semana
min_work_hours = df["hours-per-week"].min()

# Porcentaje de personas que trabajan el minimo y ganan mas de 50k
num_min_workers = df[df["hours-per-week"] == min_work_hours]
min_work_rich = round(len(num_min_workers[num_min_workers.salary == ">50K"]) /
                      len(num_min_workers)*100, 1)

# Que pais tiene  el mas alto porcentaje de personas cuyo ingreso es >50k
country_count = df["native-country"].value_counts()
country_rich_count = df[df["salary"]==">50K"]["native-country"].value_counts()

highest_earning_country = (country_rich_count / country_count *100).idxmax()
highest_earning_country_percentage = round(
        (country_rich_count / country_count *100).max(), 1
    )


# Que pais tiene  el menor porcentaje de personas cuyo ingreso es >50k

country_rich_count = df[df["salary"]==">50K"]["native-country"].value_counts()

lower_earning_country = (country_rich_count / country_count *100).idxmin()
lower_earning_country_percentage = round(
        (country_rich_count / country_count *100).min(), 1
    )


# Identificar la ocupacion mas popular con un ingreso >50K en la INDIA
people_of_india = df[(df["native-country"] =="India") & (df["salary"]==">50K")]
occupation_counts = people_of_india["occupation"].value_counts()
top_in_occupation = occupation_counts.idxmax()


