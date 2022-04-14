#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 16:14:53 2022

@author: zhaoyuanchun
"""

import streamlit as st
import pandas as pd
import numpy as np

    
st.title('Counter Example')


if 'count' not in st.session_state:
    st.session_state.count = 0

# Create a button which will increment the counter
increment = st.button('Increment')
if increment:
    st.session_state.count += 1



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

if __name__ == '__main__':
      main()    