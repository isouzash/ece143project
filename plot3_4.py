# -*- coding: utf-8 -*-
def plot34 (df,column,title):
    import matplotlib.pyplot as plt
    c = {}
    c['Good'] = 'green'
    c['Moderate'] = 'gold'
    c['Unhealthy'] = 'orange'
    c['Unhealthy for Sensitive Groups'] = 'red'
    c['Very Unhealthy'] = 'purple'
    
    color = []
    label = column
    for i in column:
        color.append(c[i])
    df.plot(kind = 'bar', stacked=True, title = 'Air quality measurements per year in ' + title,figsize=(40,10),width = 0.5, color = color, label=label)
    plt.xlabel('Year')
    plt.ylabel('% of measurements')
    plt.show()