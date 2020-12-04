# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:37:39 2020

@author: Hemant.Rathore
"""

import streamlit as st
import webbrowser
from d3graph import d3graph, vec2adjmat
import streamlit.components.v1 as components


source = ['node A','node F','node B','node B','node B','node A','node C','node Z']
target = ['node F','node B','node J','node F','node F','node M','node M','node A']
weight = [5.56, 0.5, 0.64, 0.23, 0.9,3.28,0.5,0.45]

# Import library


# Convert to adjacency matrix
adjmat = vec2adjmat(source, target, weight=weight)

node_size = [10,20,10,10,15,10,5]


if st.button('Draw the Network Plot'):
    out = d3graph(adjmat, node_color=adjmat.columns.values, node_size=node_size)
    webbrowser.open('index.html')
    out['G']
    HtmlFile = open('index.html')
    source_code = HtmlFile.read()
    components.iframe(source_code)
    components.html(HtmlFile)
    



 


