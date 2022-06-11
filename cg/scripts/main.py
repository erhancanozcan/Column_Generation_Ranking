#srcg main.py

import sys
folder_location="/Users/can/Documents/GitHub/Ranking-CG"
data_location=folder_location+"/cg/data"
sys.path.append(folder_location)
#please type the location where github_column_generation folder exists.


#dataset name
d_name="xor"

#folder_location=folder_location+"/github_column_generation"
#data_location=folder_location+"/data"
#script_location=folder_location+"/scripts"


from cg.scripts.read_available_datasets import selected_data_set
#from cg.scripts.algs.smooth_ranking_cg import base_srcg

#import os
#import datetime
#import math
#import pandas as pd
#from scipy.spatial import distance_matrix
#import numpy as np
#from gurobipy import *
#from sklearn.metrics import accuracy_score
#from sklearn.metrics import roc_auc_score
#from sklearn.tree import DecisionTreeClassifier
#os.chdir(script_location)

#from sklearn import tree
#import matplotlib.pyplot as plt
#from scipy import signal
#import scipy
#from scipy import stats
#from scipy.stats import iqr
#import itertools
import random
#import cvxpy as cp
#from cvxpy.atoms.pnorm import pnorm



#%%
df,df_test,test_class,test_data,train_class,train_data=selected_data_set(datasetname=d_name,location=data_location)
random.seed(3)
data=train_data.append(test_data)           
class_data=train_class.append(test_class)
#%%

from cg.scripts.algs.init_alg import init_alg

"""
Parameters:
   
    Alg_type         : Options
                                base
                                dec_lr
                                exp_smooth
                                dec_lr_exp_smooth
                                l1_rank
                               
                               
                               
    stp_perc          : controls the column generation iterations. Required for all algorithms
   
    stp_cond         : the rule stopping cg iterations.
                      Options
                              real_tr_obj : considers only the sum xi_{p,n} values. 
                              
                              tr_obj      : considers the surrogate objective we are minimizing. 
                                                   the sum xi_{p,n} + deviation penalizer.
                               
                              tr_roc      : considers calculated tr roc values. We expect this
                                            to be similar to real_tr_obj. Also, I believe that
                                            it is easier to explain the first two options.
                                            
       
   
   
    lr                : controls the magnitude of gradient steps. 
                        In base, it remains constant.
                        In decaying_lr: it increases after each iteration.
   
               
   
    alpha             : Controls the exponential smoothing of past weights. 
                        Required in exo_smooth and dec_lr_exp_smooth
"""





alg_type="l1_rank"
stp_perc=0.01
stp_cond="tr_obj"
lr=1.0
alpha=0.1


method1=init_alg(alg_type,train_data,train_class,test_data,test_class,df,df_test,
                          distance="euclidian",stopping_condition=stp_cond,
                          stopping_percentage=stp_perc,lr=lr, alpha=alpha,
                          selected_col_index=0,scale=True)

method1.run()

#All the statistics that we want to check.
#print(method1.test_roc_list)
#print(method1.train_roc_list)

#print(method1.test_accuracy_list)
#print(method1.train_accuracy_list)

#print(method1.objective_values)
#print(method1.real_training_objective)

#%%






