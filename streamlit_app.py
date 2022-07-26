import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


CORGI_IMAGE = Image.open('corgi.jpeg')
CORGI_IMAGE_2 = Image.open('corgi2.jpg')
CORGI_IMAGE_3 = Image.open('corgi3.jpg')

st.set_page_config(page_title='Corgis', initial_sidebar_state='collapsed')

st.sidebar.header('Sidebar ⚡')
st.sidebar.image(CORGI_IMAGE, caption="Say hi to Kevin! 🐶")
st.sidebar.slider("Random Slider", min_value=0, max_value=20, value=0, step=1)
st.sidebar.number_input("Lucky Number", min_value=0, max_value=100, value=7, step=1)
st.sidebar.color_picker("Pick a Color", value="#464AB3")
st.sidebar.subheader('Surprise! More corgis 🐶')
st.sidebar.image(CORGI_IMAGE_2, caption="Another One")
st.sidebar.image(CORGI_IMAGE_3, caption="Another Other One")


# Build a bunch of data to display
df1 = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=[0, 1, 2], columns=['AA', 'BB', 'CC'])
df4 = (df1 * 111).rename(columns={'AA': 'DD', 'BB': 'EE', 'CC': 'FF'}).copy()
df2 = df1.join(df4) * 1000
df3 = df4.join(df1) * 11111

c1, c2, c3 = st.columns((3, 4, 5))

c1.subheader('Data A')
c1.table(df1)
c2.subheader('Data B')
c2.table(df2)
c3.subheader('Data C')
c3.table(df3)

# Interactive Scatter Plot Example

interactive_scatter_spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Drag the sliders to highlight points.",
  "title": f"Interactive Scatter Chart",
  "data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"},
  "transform": [{"calculate": "year(datum.Year)", "as": "Year"}],
  "layer": [{
    "params": [{
      "name": "CylYr",
      "value": [{"Cylinders": 4, "Year": 1977}],
      "select": {"type": "point", "fields": ["Cylinders", "Year"]},
      "bind": {
        "Cylinders": {"input": "range", "min": 3, "max": 8, "step": 1},
        "Year": {"input": "range", "min": 1969, "max": 1981, "step": 1}
      }
    }],
    "mark": "circle",
    "encoding": {
      "x": {"field": "Horsepower", "type": "quantitative"},
      "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
      "color": {
        "condition": {"param": "CylYr", "field": "Origin", "type": "nominal"},
        "value": "grey"
      }
    }
  }, {
    "transform": [{"filter": {"param": "CylYr"}}],
    "mark": "circle",
    "encoding": {
      "x": {"field": "Horsepower", "type": "quantitative"},
      "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
      "color": {"field": "Origin", "type": "nominal"},
      "size": {"value": 100}
    }
  }]
}

st.vega_lite_chart(interactive_scatter_spec, None, use_container_width=True)