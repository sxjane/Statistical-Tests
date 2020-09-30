#%%
import pandas as pd
import researchpy
import share
import os
# %% 
#get data from files
post_df = pd.read_csv(share.POST_QUESTIONNAIRE,sep=';')

#collect data of control group
control_group_original = post_df[post_df['QUESTNNR'] == 'group1']
control_group = control_group_original.dropna(axis=1, how='all')
control_group = control_group.drop(['CASE','QUESTNNR','STARTED'], axis=1).reset_index(drop=True)
control_group.columns = share.CONTROL_COLUMN_NAME
share.export_to_csv(control_group, 'control_group.csv')

#collect data of experiment group
experiment_group_original = post_df[post_df['QUESTNNR'] == 'qnr2']
experiment_group = experiment_group_original.dropna(axis=1,how='all')
experiment_group = experiment_group.drop(['CASE', 'QUESTNNR','STARTED'], axis=1).reset_index(drop=True)
experiment_group.columns = share.EXPERIMENT_COLUMN_NAME
share.export_to_csv(experiment_group, 'experiment_group.csv')

#statistical analysis of scripts data by using t-test
script1_des, script1_res = researchpy.ttest(control_group['script1'].astype('int32'),experiment_group['script1'].astype('int32'),group1_name='control_script1',group2_name='exp_script1',equal_variances=False)
script2_des, script2_res = researchpy.ttest(control_group['script2'].astype('int32'),experiment_group['script2'].astype('int32'),group1_name='control_script2',group2_name='exp_script2',equal_variances=False)
script3_des, script3_res = researchpy.ttest(control_group['script3'].astype('int32'),experiment_group['script3'].astype('int32'),group1_name='control_script3',group2_name='exp_script3',equal_variances=False)
control_script = control_group.loc[:,['script1','script2','script3']].astype('int32').mean(axis=1)
experiment_script = experiment_group.loc[:,['script1','script2','script3']].astype('int32').mean(axis=1)
script_des, script_res = researchpy.ttest(control_script,experiment_script, group1_name ='control', group2_name='exp',equal_variances=False)

#%% export analysis results
share.export_to_csv(script1_des, 'script1_des.csv')
share.export_to_csv(script1_res, 'script1_res.csv')
share.export_to_csv(script2_des, 'script2_des.csv')
share.export_to_csv(script2_res, 'script2_des.csv')
share.export_to_csv(script3_des, 'script3_des.csv')
share.export_to_csv(script3_res, 'script3_res.csv')
share.export_to_csv(script_des, 'script_des.csv')
share.export_to_csv(script_res,'script_res.csv')


# %%
