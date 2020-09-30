#%%
import numpy as np
import pandas as pd
import researchpy
import matplotlib.pyplot as plt
import share
#%%
from scipy.stats import chi2_contingency

# #np.random.seed(123)
# random_data = np.random.randint([0,1,1],[2,10,5],size=(10,3))
# df = pd.DataFrame(random_data,columns=['gender','learning_gain','learning_mood'])
# crosstab1, res1 = researchpy.crosstab(df['gender'],df['learning_gain'],test='chi-square')
# crosstab2, res2 = researchpy.crosstab(df['learning_mood'],df['learning_gain'],test='chi-square')

#%%
#import data 
control_group = pd.read_csv(share.CONTROL_GROUP)
experiment_group = pd.read_csv(share.EXPERIMENT_GROUP)

#%%
#get the expected data for displaying
control_results=control_group.drop(['username','gender','age'], axis=1).T
control_frequencies = control_results.apply(share.count_frequencies, axis=1).to_dict('split')
experiment_results = experiment_group.drop(['username', 'gender','age'], axis=1).T
experiment_frequencies = experiment_results.apply(share.count_frequencies, axis=1).to_dict('split')

#%% display the data as bar chart
category_names=['Strongly disagree','Disagree','Neither agree nor disagree', 'Agree', 'Strongly agree']
plot_control_data = share.create_data_plt(control_frequencies)
plot_experiment_data = share.create_data_plt(experiment_frequencies)

# %%
def display_bar_chart(dict_data, category_names):
    labels = list(dict_data.keys())
    data = np.array(list(dict_data.values()))
    data_cum = data.cumsum(axis=1)

    category_colors = plt.get_cmap('YlGnBu')(np.linspace(0.15,0.85,data.shape[1]))
    fig, ax = plt.subplots(figsize=(10,data.shape[0]))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names,category_colors)):
        widths = data[:,i]
        starts = data_cum[:,i]-widths
        ax.barh(labels,widths,left=starts,height=0.5,label=colname,color=color)
        xcenters=starts + widths/2
        r,g,b,_=color
        text_color='white' if r*g*b < -.5 else 'darkgrey'
        for y, (x,c) in enumerate(zip(xcenters,widths)):
            ax.text(x,y,str(int(c)),ha='center',va='center',color=text_color)

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0,1),loc='lower left', fontsize='small')

    plt.show()

display_bar_chart(plot_control_data, category_names)
display_bar_chart(plot_experiment_data, category_names)

# %%
#chi-square analysis
chi_exp = experiment_results.apply(share.count_frequencies, axis=1)[10:13]
chi_control = control_results.apply(share.count_frequencies, axis=1)[10:13]

chi_exp_ag = chi_exp.sum(axis=0)
chi_control_ag = chi_control.sum(axis=0)

chi = pd.concat([chi_exp_ag,chi_control_ag], axis=1, keys=['exp','con'])
chi2, p, dof, expected = chi2_contingency(chi)

# %%
#draw bar chart for one variable
data = chi_exp_ag.to_dict()
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(figsize=(5,3))
axs.bar(names,values)

#%%c
#check the chi-sqaure between perception1 and perception2
crosstab, res, expected = researchpy.crosstab(experiment_results.loc['perception1'], experiment_results.loc['perception2'], test='chi-square', expected_freqs=True)

# %%
