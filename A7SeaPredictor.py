# -*- coding: utf-8 -*-
"""
@author: MkCst
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    # Asignando nombre a los ejes
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    
    # Creaccion de primera linea
    res = linregress(x, y )
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r')
    
    # Creacion de la segunda linea
    new_df = df.loc[df['Year'] >=2000 ]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res_2 = linregress(new_x, new_y)
    x_pred2 = pd.Series([i for i in range(2000, 2050)])
    y_pred2 = res_2.slope * x_pred2 + res_2.intercept
    plt.plot(x_pred2, y_pred2, 'green')
    
    # Configuracion de grafico
    ## Etiquetas
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # guardar grafico
    #plt.savefig('sea_level_plot.png')
    return plt.gca()
    
    