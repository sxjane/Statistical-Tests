#%%
import csv
import share
import pandas
from scipy import stats
import researchpy

# %%
control_df = pandas.read_csv(share.CHAT_MSG_CONTROL)
experiment_df = pandas.read_csv(share.CHAT_MSG_EXP).drop(columns='marker')

# %%
T2_control_df = control_df.loc[control_df['chat_id'] == 'T2']['num_msg']
T2_experiment_df = experiment_df.loc[experiment_df['chat_id'] == 'T2']['num_msg']
T2_df = pandas.DataFrame({'con_T2':T2_control_df,'exp_T2':T2_experiment_df})

# %%
T2_des, T2_res = researchpy.ttest(T2_df['exp_T2'], T2_df['con_T2'])

#%%
T3_control_df = control_df.loc[control_df['chat_id'] == 'T3']['num_msg']
T3_experiment_df = experiment_df.loc[experiment_df['chat_id'] == 'T3']['num_msg']
T3_df = pandas.DataFrame({'con_T3':T3_control_df,'exp_T3':T3_experiment_df})

#%%
T3_des, T3_res = researchpy.ttest(T3_df['con_T3'], T3_df['exp_T3'])

# %%
control_group = control_df.groupby('user_name')
control_group = control_group.apply(lambda df: df.iloc[[1,2]]['num_msg'].sum()).reset_index(drop=True)
# %%
experiment_group = experiment_df.groupby('user_name')
experiment_group = experiment_group.apply(lambda df: df.iloc[[1,2]]['num_msg'].sum()).reset_index(drop=True)

# %%
sum_df = pandas.DataFrame({'con': control_group, 'exp': experiment_group})

# %%
sum_des, sum_res = researchpy.ttest(sum_df['exp'],sum_df['con'])