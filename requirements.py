import pandas as pd
import numpy as np

import csv
from tqdm import tqdm_notebook,tnrange,tqdm_pandas,tqdm
tqdm.pandas(tqdm())

import os
import cPickle as pickle

import datetime as dt


import jupyternotify
import ipywidgets as widgets
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import matplotlib.pyplot as plt
from IPython.display import HTML
from datetime import timedelta
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import clear_output
import math
from graphviz import render, Digraph