# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:40:03 2020

@author: arthu
"""

import pandas as pd
import datetime as dtime
from datetime import timedelta
from itertools import compress
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def generate_TS_periods(dt_start, per, timezone='Europe/Paris', frequency='H', output='tuple'):
    """ generate a timeserie starting at a defined timestamp, with detailed periods, timezone & frequency.
    Return a tuple containing (serie of timestamps, serie of offset) """
    
    # Generate a serie twice the length requested, convert it to requested timezone
    delta_1D = dtime.timedelta(days=1)
    dti = pd.date_range(dt_start - delta_1D, periods=per*2, freq=frequency)
    dti_zone = dti.tz_localize(tz='UTC').tz_convert(tz=timezone)
    
    # Extract timestamp & offset info of the requested timezone serie
    timestamp_zone = pd.to_datetime([str(dt)[0:19] for dt in dti_zone],format='%Y-%m-%d %H:%M:%S')
    offset_zone = [int(str(dt)[-4]) for dt in dti_zone]
    
    # Slice the series to keep only dates >= dt_start and the requested number of periods
    loc_target = timestamp_zone>=dt_start
    timestamp_zone = timestamp_zone[loc_target]
    offset_zone = list(compress(offset_zone, loc_target))
    timestamp_zone = timestamp_zone[0:per]
    offset_zone = offset_zone[0:per]

    if output == 'dataframe':
        df = pd.DataFrame(index= timestamp_zone, columns = ['Offset'])
        df['Offset'] = offset_zone
        return df
    
    elif output=='tuple':
        return (timestamp_zone, offset_zone)
    
    else:
        print('Ouptut type ' + output + ' unknown.')


def generate_TS_frame(dt_start, dt_end, timezone='Europe/Paris', frequency='H', output='tuple'):
    """ generate a timeserie on the defined timezone, with detailed frequency """
    
    # Generate a serie twice the length requested, convert it to requested timezone
    delta_1D = dtime.timedelta(days=1)
    dti = pd.date_range(dt_start - delta_1D, dt_end + delta_1D, freq=frequency)
    dti_zone = dti.tz_localize(tz='UTC').tz_convert(tz=timezone)
    
    # Extract timestamp & offset info of the requested timezone serie
    timestamp_zone =pd.to_datetime([str(dt)[0:19] for dt in dti_zone],format='%Y-%m-%d %H:%M:%S')
    offset_zone =[int(str(dt)[-4]) for dt in dti_zone]
    
    # Slice the series to keep only dates >= dt_start and the requested number of periods
    loc_target = (timestamp_zone>=dt_start) & (timestamp_zone<dt_end)
    timestamp_zone = timestamp_zone[loc_target]
    offset_zone = list(compress(offset_zone, loc_target))
    
    if output == 'dataframe':
        df = pd.DataFrame(index= timestamp_zone, columns = ['Offset'])
        df['Offset'] = offset_zone
        return df
    
    elif output=='tuple':
        return (timestamp_zone, offset_zone)
    
    else:
        print('Ouptut type ' + output + ' unknown.')


def switch_granularity(df_in, granularity, method = 'ffill'):
    """ tranform one dataframe timeserie index granularity"""
    
    agg_method = ['ffill','bfill','mean','sum','min','max']
    interpol_method = ['linear']
    
    if method in agg_method:
        df_resampled = df_in.resample(granularity).agg(method)
    elif method in interpol_method:
        df_resampled = df_in.resample(granularity).interpolate(method)
    else:
        print('Sorry method ' + method + ' unknown.')
        df_resampled = df_in.resample(granularity).asfreq()
        
    return df_resampled
    

if __name__ == "__main__":

    [ts_1H, offset] = generate_TS_periods(dtime.datetime(day=1, month=1, year=2020), 366*24)
    
    df1 = generate_TS_periods(dtime.datetime(day=1,month=1,year=2020),
                             366*24*4, frequency='15min', output='dataframe')
    
    df2 = generate_TS_frame(dtime.datetime(day=1,month=1,year=2020),dtime.datetime(day=1,month=2,year=2020),
                             frequency='30s', output='dataframe')
    
    df3 = generate_TS_frame(dtime.datetime(day=1,month=1,year=2020),dtime.datetime(day=1,month=1,year=2025),
                             frequency='1h', output='dataframe')
    
    df_error = generate_TS_frame(dtime.datetime(day=1,month=1,year=2020),dtime.datetime(day=1,month=1,year=2025),
                             frequency='1h', output='SoupeAuxChoux')
    
    df2['Test_Range'] = range(df2.shape[0])
    
    df2_RS_large = switch_granularity(df2, '1min','sum')
    df2_RS_small = switch_granularity(df2, '10s','linear')
    
    df_test = pd.read_csv('../../data/MarketData/ETFs/aadr.us.txt')
    df_test['Date'] = pd.to_datetime(df_test['Date'],format='%Y-%m-%d %H:%M')
    df_test.set_index('Date',inplace=True)
    df_test_RS = switch_granularity(df_test,'MS','mean')
