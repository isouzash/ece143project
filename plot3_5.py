# -*- coding: utf-8 -*-
def plot35 (df, gas):

    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 80})
    fig, ax = plt.subplots(figsize=(60,30))

    df.plot(ax=ax,linewidth=5)


    plt.xlabel('Year')
    plt.ylabel('Avg AQI')
    plt.title("Annual average "+gas+" AQI over time")
    import math
    xint = range(2007, math.ceil(2011)+1)
    plt.xticks(xint)

    leg = plt.legend()
    leg_lines = leg.get_lines()
    plt.setp(leg_lines, linewidth=15)
    plt.grid()
    plt.show()