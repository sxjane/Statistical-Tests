#%%
import os
import pandas as pd
PY_PATH = '/Users/sg1/Develop/PY'
DATA_PATH = os.path.join(PY_PATH, 'data')
THESIS_PATH = os.path.join(DATA_PATH, 'thesis')
CHAT_MSG_CONTROL = os.path.join(THESIS_PATH, 'chat_msg_control.csv')
CHAT_MSG_EXP = os.path.join(THESIS_PATH, 'chat_msg_experiment.csv')
POST_QUESTIONNAIRE = os.path.join(THESIS_PATH, 'post-questionnaire.csv')
CONTROL_COLUMN_NAME = ['username','gender','age','script1','script2','script3','dis_quality1','dis_quality2', 'dis_quality3','learning_gain1','perception1','perception3','motivation1','motivation2','motivation3','emotion1','emotion3','emotion4']
EXPERIMENT_COLUMN_NAME = ['username','gender','age','script1','script2','script3','dis_quality1','dis_quality2', 'dis_quality3','learning_gain1','perception1','perception2','perception3','motivation1','motivation2','motivation3','emotion1','emotion2','emotion3','emotion4','opinion1','opinion2','opinion3']
CONTROL_GROUP = os.path.join(THESIS_PATH, 'control_group.csv')
EXPERIMENT_GROUP = os.path.join(THESIS_PATH, 'experiment_group.csv')
#%%
def export_to_csv(df, filename):
    file_path = os.path.join(THESIS_PATH, filename)
    if os.path.isfile(file_path):
        print('error: the file {} exists already', file_path)
        return
    try:
        df.to_csv(os.path.join(THESIS_PATH, filename), index=False)
    except:
        print('Unexpected error: data cannot be exported to the file: {}', file_path)

def count_frequencies(row):
    count={1:0, 2:0, 3:0, 4:0, 5:0}
    for i in row:
        count[i] = count[i]+1
    return pd.Series(count)

def create_data_plt(data_dict):
    new_dict = {}
    keys = data_dict['index']
    values = data_dict['data']
    pos = 0
    for i in keys:
        new_dict[i] = values[pos]
        pos += 1
    return new_dict


# %%
