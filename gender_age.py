#%%
import pandas as pd
import numpy as np
import share
import os
#%%
from scipy import stats 
# %% 
# collect data
df = pd.read_csv(os.path.join(share.THESIS_PATH, 'gender_age_score.csv'), sep=';')

# %% 
# calculate the grand_mean, sum of squares of SS-Total and its degree of freedom
grand_mean = df['Score'].mean()
ss_total = sum((df['Score'] - grand_mean)**2)
dof_total = df['Score'].count()-1

# %%
#calculate the sum of squares of SS-Gender, its mean square, and its degree of freedom
gender_mean = df.groupby('Gender').mean()['Score']
ss_gender = sum(((gender_mean - grand_mean) ** 2) * df.groupby('Gender')['Score'].count())
dof_gender = df['Gender'].nunique()-1
ms_gender = ss_gender / dof_gender

# %%
#calculate the sum of squares of SS-Age, its degree of square, and its mean square
age_mean = df.groupby('Age').mean()['Score']
ss_age = sum(((age_mean - grand_mean) ** 2) * df.groupby('Age')['Score'].count())
dof_age = df['Age'].nunique() - 1
ms_age = ss_age / dof_age

# %%
#calculate the sum of squares of within Age and Group, called SS Error, its degree of square, and its mean square 
within_group = df.groupby(['Age', 'Gender'])
ss_within = sum((df['Score'] - df.apply(lambda row: within_group.mean().loc[row['Age'],row['Gender']], axis=1)['Score']) ** 2)
dof_within = sum(within_group.apply(len)) - len(within_group)
ms_within = ss_within/dof_within

# %%
#calculate the sum of squares of interaction Age and Gender
ss_both = ss_total - ss_age - ss_gender - ss_within
dof_both = dof_total - dof_age - dof_gender - dof_within
ms_both = ss_both / dof_both

# %% calculate the F value
f_gender = ms_gender / ms_within
f_age = ms_age / ms_within
f_both = ms_both / ms_within

# %%
p_gender = 1 - stats.f.cdf(f_gender, dof_gender,dof_within)
p_age = 1 - stats.f.cdf(f_age, dof_age, dof_within)
p_both = 1 - stats.f.cdf(f_both, dof_both, dof_within)
# %%
# %%
#report results
d = {
    'type': ['Gender', 'Age', 'Interaction'],
    'ss': [ss_gender, ss_age, ss_both],
    'df':[dof_gender, dof_age, dof_both],
    'ms':[ms_gender, ss_age, ss_both],
     'f':[f_gender, f_age, f_both],
    'p':[p_gender, p_age, p_both]
}

df_results = pd.DataFrame(data=d)

# %%
#draw effects 