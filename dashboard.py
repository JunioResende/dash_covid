import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import json
import pandas as pd
import geopandas as gpd

df_states = pd.read_csv('data/df_states.csv')
df_brasil = pd.read_csv('data/df_brasil.csv')
gdf_brasil = gpd.read_file('shapefile/brasil.shp')
gdf_brasil_geojson = json.load(open('shapefile/brasil.geojson', 'r'))

