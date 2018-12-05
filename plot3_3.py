# -*- coding: utf-8 -*-
def plot33 (df):
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 40})
    df.plot.bar(figsize=(40,10))
    plt.xlabel('States')
    plt.ylabel('Number of recorded year')
    plt.title('Number of recorded year for per state')
    plt.show()
    