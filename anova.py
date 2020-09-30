#%%
import pandas as pd 
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot
import matplotlib.pyplot as plt
from scipy import stats
import share
import os


# %%
datafile = 'ToothGrowth.csv'
data = pd.read_csv(os.path.join(share.THESIS_PATH, datafile))

# %%
fig = interaction_plot(data.dose,data.supp,data.len, colors=['red','blue'],markers=['D','^'],ms=10) 

# %%
N = len(data.len)
df_a = len(data.supp.unique()) - 1
df_b = len(data.dose.unique()) - 1
df_axb = df_a * df_b
df_w = N - (len(data.supp.unique())*len(data.dose.unique()))
# %%
grand_mean = data['len'].mean()

# %%
# i = 0
# sum_square=0
# for l in data.supp:
#     xi_mean= data[data.supp == l].len.mean()
#     print(xi_mean)
#     square = (xi_mean-grand_mean)**2 
#     sum_square += square
#print('sum_square is {}', sum_square)

#sum of squares for the first factor supply
ssq_a = sum([(data[data.supp ==l].len.mean()-grand_mean)**2 for l in data.supp])
print('ssq_a for supply(VC,OJ) is {}', ssq_a)

# %%
#sum of squares for the second factor dose
ssq_b = sum([(data[data.dose==l].len.mean()-grand_mean)**2 for l in data.dose])
print('ssq_b for dose(0.5, 1, 2) is {}', ssq_b)

# %%
#sum of squares for the total 
ssq_t = sum((data.len - grand_mean)**2)
print('ssq_t for total, supply and dose, is {}',ssq_t)

# %%
#sum of squares within(error/residual)
vc = data[data.supp == 'VC']
oj = data[data.supp == 'OJ']
vc_dose_means = [vc[vc.dose == d].len.mean() for d in vc.dose]
oj_dose_means = [oj[oj.dose == d].len.mean() for d in oj.dose]
ssq_w = sum((oj.len - oj_dose_means)**2) + sum((vc.len - vc_dose_means)**2)

# %%
#sum of squares interaction of supply and dose
ssq_axb = ssq_t - ssq_a - ssq_b - ssq_w

# %%
#mean square  
ms_a = ssq_a / df_a
ms_b = ssq_b / df_b
ms_axb = ssq_axb / df_axb
ms_w = ssq_w/df_w

# %%
# F-test
f_a = ms_a/ms_w
f_b = ms_b/ms_w
f_axb = ms_axb/ms_w

# %%
#p-values
p_a = stats.f.sf(f_a, df_a, df_w)
p_b = stats.f.sf(f_b, df_b, df_w)
p_axb = stats.f.sf(f_axb, df_axb, df_w)

# %%
results = {'sum_sq':[ssq_a, ssq_b, ssq_axb, ssq_w],
           'df':[df_a, df_b, df_axb, df_w],
           'F':[f_a, f_b, f_axb, 'NaN'],
            'PR(>F)':[p_a, p_b, p_axb, 'NaN']}
columns=['sum_sq', 'df', 'F', 'PR(>F)']
aov_table1 = pd.DataFrame(results, columns=columns,
                          index=['supp', 'dose', 
                          'supp:dose', 'Residual'])


