import os
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as wg
from pandas.plotting import lag_plot
from statsmodels.graphics.tsaplots import plot_acf
import seaborn as sns
%matplotlib inlinedef sample_data(lag,plot =False,figuretitle='Figure'):
    '''
    This function returns the sampled data with a given time lag.
    
    Argument:
    lag - a string specifying the time lag, e.g., '1W','1M', etc.
    
    Return - a dataframe contained sampled data.
    '''
    ts_week = ts.resample(lag).mean().interpolate()
    if plot:
        fig, ax = plt.subplots(2,2,figsize=(16.53,11.69))
        ts_week.plot(ax=ax[0,0],y='Settlement',marker='o',label='Sampled Data',markersize=3,color='r')
        ts_week.plot(ax=ax[0,1],y='Ground Level',marker='*',label='Ground Level',markersize=1)
        ts.plot(y='Settlement',kind='line',ax=ax[0,0],marker='*',linewidth=0,label = 'Original Data',c='k')
        lag_plot(ts_week.Settlement,lag=1,ax=ax[1,0],c='k',marker='*')
        plot_acf(ts_week.Settlement,ax=ax[1,1],color='k')
        ax[0,0].set_ylim([8,0])
        ts.Date.max()
        ax[0,0].set_ylabel('Settlement(m)')
        fig.savefig(os.path.join(r'./pdf',figuretitle+'.pdf'))
    return ts_week