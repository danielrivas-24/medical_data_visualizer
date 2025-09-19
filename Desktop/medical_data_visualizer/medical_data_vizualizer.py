import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    g.set_axis_labels("variable", "total")
    g._legend.set_title("value")
    
    fig = g.fig
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    df_heat = df.copy()
    df_heat = df_heat[df_heat['ap_lo'] <= df_heat['ap_hi']]
    h_low = df_heat['height'].quantile(0.025)
    h_high = df_heat['height'].quantile(0.975)
    df_heat = df_heat[(df_heat['height'] >= h_low) & (df_heat['height'] <= h_high)]

    w_low = df_heat['weight'].quantile(0.025)
    w_high = df_heat['weight'].quantile(0.975)
    df_heat = df_heat[(df_heat['weight'] >= w_low) & (df_heat['weight'] <= w_high)]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, vmax=.3, vmin=-0.1, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    fig.savefig('heatmap.png')
    return fig