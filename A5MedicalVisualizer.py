# -*- coding: utf-8 -*

## Librerias necesarias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Importe de datos
df = pd.read_csv("medical_examination.csv")

# Añadiendo columna "overweight" sobrepeso
## Aplicando 1 si es sobrepeso
df["overweight"] = (df["weight"] / (df["height"]/100)**2).apply(
    lambda x:1 if x >25 else 0
    )

# Normalizar los datos haciendo los valores 1 siempre malo y 0 bueno
## Si el valor de cholesterol o gluc es 1, haga el valor 0. 
## Si el valor es más de 1, haga el valor 1.
df["cholesterol"] = df["cholesterol"].apply(lambda x:0 if x==1 else 1)
df["gluc"] = df["gluc"].apply(lambda x:0 if x==1 else 1)

def draw_cat_plot():
    """Crear un dataframe pd.melt solo para los valores de:
         cholesterol, gluc, smoke, alco, active, overweight
    """
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=[
        "cholesterol", "gluc", "smoke", "alco", "active", "overweight"
        ])
    
    # conjunto de datos divididos por cardio
    df_cat["total"] = 1 # Util para el recuento
    df_cat = df_cat.groupby(
        ["cardio", "variable","value"], as_index=False).count()

    # Grafica de catplot usando sns.catplot()
    fig = sns.catplot(x="variable", y="total", 
                      data=df_cat, hue="value", kind="bar", col="cardio").fig 
    
    fig.savefig("catplot.png")
    return fig

def draw_scatter_plot():
    fig = sns.relplot(x="weight", y="height", 
                      hue="active", style="gender", data=df)
    return fig

def draw_heat_map():
    # tratamiento de datos erroneos o sospechosos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)) 
        ] 
    ## Calculo de la matriz de correlaciones
    corr = df_heat.corr(method='pearson')
    
    ## mask para el triangulo superior
    mask = np.triu(corr)
    
    ## Configuracion para la figura
    fig, ax = plt.subplots(figsize=(12, 12))
    
    ## 'dibujar' el heatmap 
    sns.heatmap(
        corr, linewidths=1, annot=True, square=True, 
        mask=mask, fmt='.1f',
        center=0.08, cbar_kws={'shrink':0.5}
        )
    #fig.savefig('heatmap.png')
    
    return fig
    