# -*- coding: utf-8 -*-
def plot31(df):
    import matplotlib.pyplot as plt
    df.plot.bar(figsize=(15,10))
    plt.xlabel('States')
    plt.ylabel('Average MAX_AQI 2011-2015')
    plt.title('Top 10 States With Highest Average MAX_AQI 2011-2015')
    plt.show()
    