#%%
import numpy as np
import pandas as pd
import researchpy
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from patsy import dmatrices
from statsmodels.stats.anova import AnovaRM

#%%
#prepare data 
np_data = np.random.randint(100, size=(30,4))
#%%
df = pd.DataFrame(np_data, columns=['g1','g2','g3','g4'])
#%%
g1_mean=df['g1'].mean()
g2_mean=df['g2'].mean()
g3_mean=df['g3'].mean()
g4_mean=df['g4'].mean()

#%%
boxplot = df.boxplot(column=['g1','g2','g3','g4'])

#%%
group_names = (['group1'] * 30) + (['group2'] * 30) +(['group3'] *30)
df_anova = pd.DataFrame({'group_name': group_names, 'score':np.random.randint(100,size=30*3)})
# %%
df_anova.groupby('group_name').mean()

# %%
boxplot= df_anova.boxplot(by='group_name')

# %%
lm = ols('score ~ group_name', data=df_anova).fit()

# %%
table = sm.stats.anova_lm(lm)
print(table)

# %%
moore = sm.datasets.get_rdataset('Moore', 'carData', cache=True)

# %%
data = moore.data

# %%
data = data.rename(columns = {"partner.status" : "partner_status"})

# %%
moore_lm = ols('conformity ~ C(fcategory, Sum) * C(partner_status, Sum)', data=data).fit()

# %%
table=sm.stats.anova_lm(moore_lm, typ=2)

# %%
