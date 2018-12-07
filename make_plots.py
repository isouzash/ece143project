# coding: utf-8

import matplotlib.pyplot as plt
import math
import numpy as np


def make_bar_plot(df, fontsize, figsize, ylabel, title):
    '''
    This function define font size, figure size, y label and title for bar plots
    '''
    plt.rcParams.update({'font.size': fontsize})
    df.plot.bar(figsize=figsize)
    plt.xlabel('States')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)

def plot32(df,title):
    '''
    This function plots pie charts
    '''
    explode = [0.05, 0.05, 0.05, 0.05]
    colors = ['#a1d99b', '#FFF933', '#fdae6b', '#e6550d']
    df.plot(kind='pie', figsize=(12, 12),explode=explode, colors=colors, y = None, title = 'CA EPA', fontsize=15, legend = True, pctdistance=0.85 ,shadow=False, autopct='%.1f%%',startangle=20)
    plt.title(title, fontsize=22)
    plt.ylabel('', fontsize=16)
    plt.show()


def plot34(df, column, title):
    '''
    This function plots stacked bar plots
    '''
    c = dict(zip(["Good", "Moderate", "Unhealthy", "Unhealthy for Sensitive Groups", "Very Unhealthy"],
                 ["green", "gold", "orange", "red", "purple"]))

    label = column
    color = [c[i] for i in column]

    df.plot(kind = 'bar', stacked=True, title = 'Air quality measurements per year in ' + title,
            figsize=(40,10),width = 0.5, color = color, label=label)
    plt.xlabel('Year')
    plt.ylabel('% of measurements')
    plt.xticks(rotation=45)
    plt.show()

def plot35 (df, gas):
    '''
    This function plots AQI over time
    '''
    plt.rcParams.update({'font.size': 80})
    fig, ax = plt.subplots(figsize=(60,30))

    df.plot(ax=ax,linewidth=15)


    plt.xlabel('Year')
    plt.ylabel('Avg AQI')
    plt.title("Annual average "+gas+" AQI over time")
    xint = range(2007, math.ceil(2011)+1)
    plt.xticks(xint)
    leg = plt.legend()
    leg_lines = leg.get_lines()
    plt.setp(leg_lines, linewidth=15)
    plt.grid()
    plt.show()

def plot36 (data, recipe):
    '''
    This function plots pie chart of USA air components
    '''
    plt.rcParams['font.size'] = 11.0
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=120)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                 horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Air Quality")

    plt.show()

    
def abbreviation(State_names):
    '''
    This function returns the abbreviation for State names
    '''
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'Country Of Mexico': 'CM', 
    'District Of Columbia': 'DC'
    }
    return [us_state_abbrev[key] for key in State_names]    