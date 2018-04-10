# setup identify (for slicing data and grading)
NAME = "Kieran Murphy"
ID = 666

# load libraries 

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
sns.set_context("paper")

from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))

def identify():
    printmd ("Name: **%s**\n\nData slide generated using ID: **%s**" %(NAME,ID))

