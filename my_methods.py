# -*- coding: utf-8 -*-

def reshape_data(df, entry, new_shape):
    '''
    Creates new column in the dataset to integrate EPA categories 
    for air quality (see reference for methodology)
    '''
    
    df = df.copy()
    data = df[entry].values
    data.reshape(*new_shape)
    return data

def classify_air_quality(df, lowerbound, upperbound, classification):
    '''
    Creates a column that classify the air quality according to EPA categories
    '''
    if lowerbound == 0:
        df.loc[(df.MAX_AQI >= lowerbound) & (df.MAX_AQI <= upperbound), ["EPA"]] = classification
    else:
        df.loc[(df.MAX_AQI > lowerbound) & (df.MAX_AQI <= upperbound), ["EPA"]] = classification

def groupby_and_sum(df, n_zeros=None):
    '''
    Groupby dataframes, sum along the columns and check null entries for years,
    filling them by zeros
    '''
    df = df.copy()
    groupby = df.groupby(['Year','EPA'])
    df = groupby["EPA"].count().unstack()
    df.fillna(0, inplace=True)
    if n_zeros is not None:
        y = [y for y in range(2000,2016)]
        Year = df.index.tolist()
        for i in y:
            if i not in Year:
                df.loc[i] = [0]*n_zeros
    df["SUM"] = df.sum(axis=1)
    return df

def make_percentages(df, entry):
    '''
    Return percentages
    '''
    df[entry] = (df[entry]/df["SUM"])
    
def make_df_and_column(df, classifications, c_slice, drop_2016=False, n_zeros=None):
    '''
    Rewrite dataframes using make_percentage and drop years
    '''
    df = groupby_and_sum(df.copy(), n_zeros=n_zeros)
    for c in classifications[:c_slice]:
        make_percentages(df, c)
    df = df.drop(['SUM'], axis=1)
    if drop_2016:
        df = df.drop(2016)
    df = df.sort_index()

    df_column = list(df.columns.values)
    
    return df, df_column

def get_average(df, AQI):
    '''
    Get the AQI average of a dataframe that was grouped by Year and City and unstack it
    '''
    return df.groupby(['Year','City']).mean()[AQI].unstack()