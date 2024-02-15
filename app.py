import streamlit as st
import numpy as np
import pandas as pd
from numpy.random import choice

df = pd.read_csv('mark6.csv')
balls = np.concatenate((df.ball_1, df.ball_2, df.ball_3, df.ball_4, df.ball_5, df.ball_6, df.ball_7))

unique, counts = np.unique(balls, return_counts=True)
proba = np.multiply(counts, 1 / np.sum(counts))

colors = {
  1: "red",
  2: "red",
  3: "blue",
  4: "blue",
  5: "green",
  6: "green",
  7: "red",
  8: "red",
  9: "blue",
  10: "blue",
  11: "green",
  12: "red",
  13: "red",
  14: "blue",
  15: "blue",
  16: "green",
  17: "green",
  18: "red",
  19: "red",
  20: "blue",
  21: "green",
  22: "green",
  23: "red",
  24: "red",
  25: "blue",
  26: "blue",
  27: "green",
  28: "green",
  29: "red",
  30: "red",
  31: "blue",
  32: "green",
  33: "green",
  34: "red",
  35: "red",
  36: "blue",
  37: "blue",
  38: "green",
  39: "green",
  40: "red",
  41: "blue",
  42: "blue",
  43: "green",
  44: "green",
  45: "red",
  46: "red",
  47: "blue",
  48: "blue",
  49: "green"
}

css='''

.wrapper {
      overflow: hidden;
      /*make sure the wrapper has no dimension*/
      margin-bottom: 10px;
      margin-left: 25%;
      margin-right: 25%;
}

.balls div {
    animation: fadeIn 5s;
	position: relative;
    background-color:#fff;
	margin: 5px;
    border:5px solid;
	width: 50px;
    height:50px;
    line-height:40px;
    font-size: 20px;
    border-radius:50%;
	box-shadow: 0 5px 5px rgba(0,0,0,.2);
	text-align: center;
    -moz-border-radius:50%;
    -webkit-border-radius:50%;
}

.balls div.-red {
    float: left;
    border-color: #ed4d4b
}

.balls div.-green {
    float: left;
    border-color: #68bf66
}

.balls div.-blue {
    float: left;
    border-color: #83bacb
}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)




if st.button('draw'):
    randomNumberList = choice(unique, 6, p=proba, replace=False)
    sortedRandomNumberList = np.sort(randomNumberList)
    
    html = f'''
    <div class="balls">						
    	<div class="-{colors[sortedRandomNumberList[0]]}">{sortedRandomNumberList[0]}</div>
    	<div class="-{colors[sortedRandomNumberList[1]]}">{sortedRandomNumberList[1]}</div>
    	<div class="-{colors[sortedRandomNumberList[2]]}">{sortedRandomNumberList[2]}</div>
    	<div class="-{colors[sortedRandomNumberList[3]]}">{sortedRandomNumberList[3]}</div>
    	<div class="-{colors[sortedRandomNumberList[4]]}">{sortedRandomNumberList[4]}</div>
    	<div class="-{colors[sortedRandomNumberList[5]]}">{sortedRandomNumberList[5]}</div>
    </div>
    '''   

    st.markdown(html, unsafe_allow_html=True)  



