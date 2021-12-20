#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


def overview_generator(data):

    overview = data.groupby(["medical_center", "project_id"]).count().reset_index()
    overview = overview[["medical_center", "project_id"]]

    overview = pd.merge(pd.DataFrame(data.project_id.value_counts()),
             overview.groupby("project_id").count(),
             left_index= True, right_index=True)
    
    overview = pd.merge(overview,
             data.groupby("project_id")["medical_center"].unique(),
             left_index= True, right_index=True)

    overview.columns = ["Number of WSIs", "Number of Contributing Medical Centers", "Medical Centers"]

    return overview

def overview_generator_mc(data):

    overview = data.groupby(["medical_center", "project_id"]).count().reset_index()
    overview = overview[["medical_center", "project_id"]]

    overview = pd.merge(pd.DataFrame(data.medical_center.value_counts()),
             overview.groupby("medical_center").count(),
             left_index= True, right_index=True)
    
    overview = pd.merge(overview,
             data.groupby("medical_center")["project_id"].unique(),
             left_index= True, right_index=True)

    overview.columns = ["Number of WSIs", "Number of Cancer Types", "Cancer Types"]

    return overview

def return_top(data, threshold, on = "medical_center"):
    
    top_mc = data[on].value_counts(normalize = True) > threshold
    top_mc = data[on].value_counts(normalize = True)[top_mc]
    
    top_mc = data[data[on].isin(top_mc.index)]
    
    return top_mc

def return_bottom(data, threshold, on = "medical_center"):
    
    bottom_mc = data[on].value_counts(normalize = True) <= threshold
    bottom_mc = data[on].value_counts(normalize = True)[bottom_mc]
    
    bottom_mc = data[data[on].isin(bottom_mc.index)]
    
    return bottom_mc

