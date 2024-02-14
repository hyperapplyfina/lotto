'''

import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

'''

import streamlit as st

#st.button('Click me!')

css='''
<html>
<head>
  <style>
    .circle {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background-color: teal;
      display: flex;
      justify-content: center;
      align-items: center;
      color: white;
      font-size: 24px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="circle">
    16
  </div>
  <div class="circle">
    16
  </div>
</body>
</html>
'''

st.markdown(css, unsafe_allow_html=True)    

#html = '''<span class="dot"></span>'''

#st.markdown(html, unsafe_allow_html=True)  

