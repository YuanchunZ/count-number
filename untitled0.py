#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:14:53 2022

@author: zhaoyuanchun
"""

import streamlit as st
import pandas as pd
import numpy as np
#from TextBlob import TextBlob
#i = 0
#def count():
    #global i
#    i=i+1
#    st.write(i)
    #return i
#st.title("COUNT")
#result=st.button("increment")
#st.success(count(0))
#if st.button("analyze"):
#     #st.success(count())
#     global i
#     i = i + 1
#     st.write(i)
     #st.write(result)
    
st.title('Counter Example')

# Streamlit runs from top to bottom on every iteraction so
# we check if `count` has already been initialized in st.session_state.

# If no, then initialize count to 0
# If count is already initialized, don't do anything
if 'count' not in st.session_state:
    st.session_state.count = 0

# Create a button which will increment the counter
increment = st.button('Increment')
if increment:
    st.session_state.count += 1

# A button to decrement the counter
#decrement = st.button('Decrement')
#if decrement:
#    st.session_state.count -= 1

st.write('Count = ', st.session_state.count)
st.write("squared compute")
x=st.slider('x')
st.write(x,'squared is', x * x)
def main():
    

    st.subheader("Natural Language processing:")
    if st.checkbox("Token and lemma"):
       st.subheader("Natural Language processing:")
       message = st.text_area("enter","type here")
       if st.button("analyze"):
           st.success(message.title())
        
#read_and_cache_csv = st.cache(pd.read_csv)
#BUCKET = "https://streamlit-self-driving.s3-us-weat-2.amazonaws.com/"
#data = read_and_cache_csv(BUCKET + "labels.csv.gz" ,  nrows=1000)
#desired_lable = st.selectbox('filter to:', ['car','truck'])
#st.write(data[data.label==desired_label])
if __name__ == '__main__':
      main()    