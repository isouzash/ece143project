# -*- coding: utf-8 -*-
def plot32 (df):
    import matplotlib.pyplot as plt
    explode = [0.05, 0.05, 0.05, 0.05]
    colors = ['#a1d99b', '#FFF933', '#fdae6b', '#e6550d']
    df.plot(kind='pie', figsize=(12, 12),explode=explode, colors=colors, y = None, title = 'CA EPA', fontsize=15, legend = True, pctdistance=0.85 ,shadow=False, autopct='%.1f%%',startangle=20)
    plt.title('CA EPA Percentage', fontsize=22)
    plt.ylabel('', fontsize=16)
    