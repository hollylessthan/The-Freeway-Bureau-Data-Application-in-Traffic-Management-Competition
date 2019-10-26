import scipy.stats as ss
from collections import Counter
import math 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

df = pd.read_csv('/Users/lofangyu/Documents/data_analytics/normal_data_sum.csv')

df1 = pd.read_csv('/Users/lofangyu/Documents/data_analytics/A1A2table1.csv')
#trafficcols = ['acc_data',	acc_time_hour	acc_time_min	highway_name	highway_km	highway_m	direction	acc_type	acc_cause	pre_door	"post_door"	sum(pre_1)	sum(pre_2)	sum(post_1)	sum(post_2)	Speed]
#catcols = ['Preferred Foot','Position','Body Type','Nationality','Weak Foot']
print(df.head())
print(df1.head())

df3= pd.merge(df,df1,on = ['日期', '時', '分', '公路', '公里', '公尺', '事故類型及型態', '主要肇事因素'],how='left')
#print(df3)
#print(df3[["acc_data" , "日期"]])

numcols = ['前車量1', '後車量1','速度','單位前車量1', '單位後車量1','時','公里','天候','光線', '道路類別','速限', '道路型態', '事故位置', '路面鋪裝','路面狀態','路面缺陷','障礙物','視距','號誌種類', '號誌動作','分向設施','分道設施-快車道間','主要肇事因素','分道設施-快慢車道間','分道設施-路面邊線']
catcols = ['車道位置']

df3= df3[numcols+catcols]
traindf = pd.concat([df3[numcols], pd.get_dummies(df3[catcols])],axis=1)
features = traindf.columns

traindf = traindf.dropna()
traindf = pd.DataFrame(traindf,columns=features)
print(traindf)




y = (traindf['主要肇事因素'] == 7) | (traindf['主要肇事因素'] ==16) | (traindf['主要肇事因素'] ==23) 
print(y)
X = traindf.copy()
del X['主要肇事因素']
feature_name = list(Ｘ.columns)
# no of maximum features we need to select
num_feats=12


#Pearson correlation
def cor_selector(X, y,num_feats):
    cor_list = []
    feature_name = X.columns.tolist()
    # calculate the correlation with y for each feature
    for i in X.columns.tolist():
        cor = np.corrcoef(X[i], y)[0, 1]
        cor_list.append(cor)
    # replace NaN with 0
    cor_list = [0 if np.isnan(i) else i for i in cor_list]
    # feature name
    cor_feature = X.iloc[:,np.argsort(np.abs(cor_list))[-num_feats:]].columns.tolist()
    # feature selection? 0 for not select, 1 for select
    cor_support = [True if i in cor_feature else False for i in feature_name]
    return cor_support, cor_feature
cor_support, cor_feature = cor_selector(X, y,num_feats)
print(str(len(cor_feature)), 'selected features')

print(cor_feature)

#chi-square
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import MinMaxScaler
X_norm = MinMaxScaler().fit_transform(X)
chi_selector = SelectKBest(chi2, k=num_feats)
chi_selector.fit(X_norm, y)
chi_support = chi_selector.get_support()
chi_feature = X.loc[:,chi_support].columns.tolist()
print(str(len(chi_feature)), 'selected features')
print(chi_feature)

#Recursive Feature Elimination
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
rfe_selector = RFE(estimator=LogisticRegression(), n_features_to_select=num_feats, step=10, verbose=5)
rfe_selector.fit(X_norm, y)

rfe_support = rfe_selector.get_support()
rfe_feature = X.loc[:,rfe_support].columns.tolist()
print(str(len(rfe_feature)), 'selected features')
print(rfe_feature)


#Lasso: SelectFromModel

from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression

embeded_lr_selector = SelectFromModel(LogisticRegression(penalty="l1"), max_features=num_feats)
embeded_lr_selector.fit(X_norm, y)

embeded_lr_support = embeded_lr_selector.get_support()
embeded_lr_feature = X.loc[:,embeded_lr_support].columns.tolist()
print(str(len(embeded_lr_feature)), 'selected features')

print(embeded_lr_feature)

#Tree-based: SelectFromModel

from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier

embeded_rf_selector = SelectFromModel(RandomForestClassifier(n_estimators=100), max_features=num_feats)
embeded_rf_selector.fit(X, y)

embeded_rf_support = embeded_rf_selector.get_support()
embeded_rf_feature = X.loc[:,embeded_rf_support].columns.tolist()
print(str(len(embeded_rf_feature)), 'selected features')

print(embeded_rf_feature)

from sklearn.feature_selection import SelectFromModel
from lightgbm import LGBMClassifier

lgbc=LGBMClassifier(n_estimators=500, learning_rate=0.05, num_leaves=32, colsample_bytree=0.2,
            reg_alpha=3, reg_lambda=1, min_split_gain=0.01, min_child_weight=40)

embeded_lgb_selector = SelectFromModel(lgbc, max_features=num_feats)
embeded_lgb_selector.fit(X, y)

embeded_lgb_support = embeded_lgb_selector.get_support()
embeded_lgb_feature = X.loc[:,embeded_lgb_support].columns.tolist()
print(str(len(embeded_lgb_feature)), 'selected features')

print(embeded_lgb_feature)


# put all selection together
feature_selection_df = pd.DataFrame({'Feature':feature_name, 'Pearson':cor_support, 'Chi-2':chi_support, 'RFE':rfe_support, 'Logistics':embeded_lr_support,
                                    'Random Forest':embeded_rf_support, 'LightGBM':embeded_lgb_support})
# count the selected times for each feature
feature_selection_df['Total'] = np.sum(feature_selection_df, axis=1)
# display the top 100
feature_selection_df = feature_selection_df.sort_values(['Total','Feature'] , ascending=False)
feature_selection_df.index = range(1, len(feature_selection_df)+1)
print(feature_selection_df.head(num_feats))