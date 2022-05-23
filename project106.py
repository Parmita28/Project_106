# -*- coding: utf-8 -*-
"""Project106

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k7So6uHXJDYauFzh90Z2KilCztu3rUrT
"""

from google.colab import files
data_to_load = files.upload()

import plotly.express as px
import csv

with open("Student Marks vs Days Present.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
      fig.show()

import csv
import numpy as np

def getDataSource(data_path):
    marks_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation:",correlation[0,1])

data_path  = "Student Marks vs Days Present.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)

from google.colab import files
data_to_load = files.upload()

import plotly.express as px
import csv

with open("cups of coffee vs hours of sleep.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
      fig.show()

import csv
import numpy as np

def getDataSource(data_path):
    Coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x" : Coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation:",correlation[0,1])

data_path  = "cups of coffee vs hours of sleep.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)