import pandas as pd
import re


def Initialize_Duration_Curve(model, g): #g = [i for i in range(0, 365)]

  
    xls = pd.ExcelFile('Inputs/Excel.xls')
    df1 = pd.read_excel(xls, 'Duration_Curve')

    Data_file = "Inputs/Data.dat"
    Data_import = open(Data_file).readlines()
    for i in range(len(Data_import)):
        if "param: DMV" in Data_import[i]:
            DMV = float((re.findall('\d+\.\d+', Data_import[i])[0]))
        if "param: Giorni" in Data_import[i]:
            giorni = int((re.findall('\d+', Data_import[i])[0]))
    serie_portate = []
    for i in range(0, giorni):
        serie_portate += [df1.loc[i][1]-DMV] #così ho direttamente la Q_available

    return serie_portate[g-1]


def Initialize_Hgross(model, g): #g = [i for i in range(0, 365)]

   
    xls = pd.ExcelFile('Inputs/Excel.xls')
    Data_file = "Inputs/Data.dat"
    Data_import = open(Data_file).readlines()
    for i in range(len(Data_import)):
        if "param: Giorni" in Data_import[i]:
            giorni = int((re.findall('\d+', Data_import[i])[0]))
    df1 = pd.read_excel(xls, 'Hgross')

    serie_Hgross = []
    for i in range(0, giorni):
        serie_Hgross += [df1.loc[i][1]]

    return serie_Hgross[g-1]
