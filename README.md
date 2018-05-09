# Data Mining Assignment 2


## Run the project
To run this anaconda needs to be installed 

```
source activate py3
jupyter-notebook
```

## The Notebooks
The setup notebook should be run first to download all the data, after that the EDA, ARM, Regression and Classification notebooks are independent of one another.

Make sure when running through the setup notebook you wait for the instacart data to download.

Setup Notebook : https://nbviewer.jupyter.org/github/1carew1/instacart_investigation/blob/master/Assignment_2_-Setup.ipynb
EDA Notebook : https://nbviewer.jupyter.org/github/1carew1/instacart_investigation/blob/master/Assignment2_EDA.ipynb
ARM Notebook : https://nbviewer.jupyter.org/github/1carew1/instacart_investigation/blob/master/Assignment_2_ARM.ipynb
Regression Notebook : https://nbviewer.jupyter.org/github/1carew1/instacart_investigation/blob/master/Assignment_2_Regression.ipynb
Classification Notebook : https://nbviewer.jupyter.org/github/1carew1/instacart_investigation/blob/master/Assignment_2_Classification.ipynb

## Install Python3 and Jupyter
```
# Download Miniconda - python3 version
https://conda.io/miniconda.html - For Mac : https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
# Run the setup script
bash Miniconda3-latest-MacOSX-x86_64.sh
# Follow setup script and fill in info as necessary
# Create new termina and Create python3 environment
conda create -n py3
source activate py3
conda install jupyter
conda install seaborn
conda install -c conda-forge jupyter_contrib_nbextensions
pip install mlxtend  
# Start the notebook
jupyter-notebook
```
