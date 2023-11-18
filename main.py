print('Welcome to Adult Census Income Prediction')
print('----------------------------------------------------------')
print('Importing Libraries...')
import pickle
import pandas as pd
import numpy as np
import json
import random
import warnings
warnings.filterwarnings('ignore')
print('Loading model...')
all_set=False
columns=[]
if 1>0:
    #loading the csv files
    i_data=pd.read_csv('data/i_data.csv')
    i_data['education-num']=i_data['education-num'].astype(str)
    final_data=pd.read_csv('data/final_data_all.csv')
    with open('data/encoded_values.json','rb') as file:
        encoded_values=json.load(file)
    columns=list(final_data.columns)
    obj_cols=i_data.select_dtypes(include='object').columns
    num_cols=i_data.select_dtypes(include='number').columns
    with open('data/hist_grad_bc.pkl','rb') as file_name:
        model=pickle.load(file_name)
    with open('data/ss_scale_values.pkl','rb') as file_name:
        ss_scale_model=pickle.load(file_name)
    print('Required files loaded successfully:)')
    all_set=True
else:
    print('Model not loaded.')
def work():
    i_inputs={}
    final_inputs=[]
    print('Please enter the input values in json format to predict the output')
    print('------------------------')
    i=1
    for col in columns:
        if col=='salary':
            continue
        if col in obj_cols:
            uni_values=list(encoded_values[col].keys())
            print('------------------------------------')
            while True:
                print('Column: ('+str(i)+'/'+str(len(columns)-1)+')'+'Enter the input for '+col+'(Must be one from the following list of values) or Press enter to select the random value:')
                print(uni_values)
                inp_val=input('Here: ')
                print('------------------------------------')
                if len(inp_val)==0:
                    inp_val=random.choice(uni_values)
                    print(inp_val)
                if inp_val in uni_values:
                    encoded_value=encoded_values[col][inp_val]
                    final_inputs.append(encoded_value)
                    break
                else:
                    print("Incorrect input")
            i=i+1
        if col in num_cols:
            print('------------------------------------')
            while True:
                print('Column: ('+str(i)+'/'+str(len(columns)-1)+')'+'Enter the input for '+col+'(Number) or Press enter to select the random value: ')
                inp_val=input('Here: ')
                print('------------------------------------')
                if len(inp_val)==0:
                    inp_val=random.randrange(0,max(i_data[col]))
                    print(inp_val)
                try:
                    inp_val=int(inp_val)
                    if col=='fnlwgt':                    
                        final_inputs.append(np.sqrt(inp_val))
                        break
                    else:
                        final_inputs.append(np.log(inp_val))
                        break
                except:
                    print('Please enter number, not text character(s)')
            i=i+1        
    output=model.predict(ss_scale_model.transform([final_inputs]))[0]
    print('------------------------------------')
    print('Predicted value: ',output)
    print('-------------------------------------------------------------------------------------')
if all_set==True:
    print('All set to work...')
    print('------------------------------------------------------------------')
    print('------------------------------------------------------------------')
    while True:
        p_or_not=input('Predict the values: [Y/n]?')
        if p_or_not.lower()=='y':
            work()
        if p_or_not.lower()=='n':
            print('Thanks for using...')
            break