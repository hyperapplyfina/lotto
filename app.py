import streamlit as st
import numpy as np
import pandas as pd
from numpy.random import choice
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv('mark6.csv')
    df['draw_date'] = pd.to_datetime(df['draw_date'], dayfirst=True)
    df = df.sort_values(by=['draw_date'])
    return df

@st.cache_data
def get_hotness(df, tail_value):
    df_tail = df.tail(tail_value)
    ball_count = np.concatenate((df_tail.ball_1, df_tail.ball_2, df_tail.ball_3, df_tail.ball_4, df_tail.ball_5, df_tail.ball_6, df_tail.ball_7))
    counts = np.array([(ball_count == i).sum() for i in balls])
    proba = np.divide(counts + 1, np.sum(counts) + 2)
    hotness = np.divide(proba, (1+1)/(49+2))
    return hotness

@st.cache_data
def get_new_proba(hotness, multiplier):
    new_proba = np.divide(np.multiply(1/49, hotness ** multiplier), np.sum(np.multiply(1/49, hotness ** multiplier)))
    return new_proba

balls = np.arange(1, 50, 1, dtype=int)



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

color_code = {
    "red": "#ed4d4b",
    "green": "#68bf66",
    "blue": "#83bacb"
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
	position: relative;
    background-color:#fff;
	margin: 5px;
    border:5px solid;
	width: 40px;
    height:40px;
    line-height:28px;
    font-size: 20px;
    color: black;
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
df = load_data()

language = st.radio(
    "文A",
    ["中文", "English"],
    )

col1, col2 = st.columns(2)

with col1:
    
    if language == "English":
        temp = st.select_slider(
            'Hot/Cold numbers',
            options=['Super Cold', 'Cold', 'a little cold', 'room temperature', 'a little hot', 'Hot', 'Super Hot'],
            value = 'room temperature')
        
        temp_dict = {
            'Super Cold' : -4,
            'Cold': -2,
            'a little cold': -1,
            'room temperature' : 0,
            'a little hot' : 1,
            'Hot': 2,
            'Super Hot': 4
            }
        
        tail_value = st.slider("number of draws considered", min_value = 1, max_value = len(df), step = 1, value = 100)
        
    elif language == "中文":
        temp = st.select_slider(
            '熱門／冷門 數字',
            options=['大冷門', '冷門', '小冷門', '常溫', '小熱門', '熱門', '大熱門'],
            value = '常溫')
        
        temp_dict = {
            '大冷門' : -4,
            '冷門': -2,
            '小冷門': -1,
            '常溫' : 0,
            '小熱門' : 1,
            '熱門': 2,
            '大熱門': 4
            }
        
        tail_value = st.slider("參考期數", min_value = 1, max_value = len(df), step = 1, value = 100)
        
multiplier = temp_dict[temp]
hotness = get_hotness(df, tail_value)
new_proba = get_new_proba(hotness, multiplier)


p = st.write(f'<style>{css}</style>', unsafe_allow_html=True)

chart_data = pd.DataFrame({'probability':new_proba, 'ball_number':[i for i in balls.tolist()]})
color_discrete_sequence = [color_code[colors[i]] for i in chart_data.ball_number]
chart_data['category'] = [str(i) for i in chart_data.index]

fig = px.bar(chart_data, x = 'ball_number', y = 'probability', color = 'category', color_discrete_sequence = color_discrete_sequence, height=300)
fig.layout.update(showlegend=False)
fig.update_traces(
    hovertemplate='<b>%{x}</b><extra></extra>',

) 
with col2:
    st.plotly_chart(fig, config = {'displayModeBar': False}, use_container_width = True)

num_balls = st.slider("number of balls", min_value = 1, max_value = 48, step = 1, value = 6)

if language == "English":
    draw = st.button('Gimme a number!')
elif language == "中文":
    draw = st.button('畀個冧把我!')

    

if draw == True:

    randomNumberList = choice(balls, num_balls, p=new_proba, replace=False)
    sortedRandomNumberList = np.sort(randomNumberList)
    
    ball_display = '''
    <div class="balls">
    '''
    
    for i in range(num_balls):
        ball_display += f'''<div class="-{colors[sortedRandomNumberList[i]]}">{sortedRandomNumberList[i]}</div>'''
      
    ball_display += '''
    </div>
    '''
    



    st.markdown(ball_display, unsafe_allow_html=True)


    

    
