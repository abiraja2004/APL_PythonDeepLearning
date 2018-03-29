import numpy as np

import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import tensorflow as tf

import pandas as pd

import xlrd

DATA_FILE = 'data/USA_Housing.xls'

# Step 1: read in data from the .xls file

book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")

sheet = book.sheet_by_index(0)

data = np.asarray([[sheet.row_values(i)[2], sheet.row_values(i)[5]] for i in range(1, sheet.nrows)])

n_samples = sheet.nrows - 1

print(data)



