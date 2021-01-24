import pandas as pd

def Risultati(instance, Optimization_Goal):
    
    na = instance.Binary_Turbines_A.get_values()
    nb = instance.Binary_Turbines_B.get_values()
    #Energia_annua = instance.Energia_Annua.get_values()
    print('\n', 'Numero Turbine A:', na, '\n', 'Numero Turbine B:', nb)

    x = instance.INV_COST.value
    y = instance.cf.value
    #z = instance.cf_2.value
    binaria1 = instance.Binary_A.get_values()
    binaria2 = instance.Binary_B.get_values()
    print('\n\n Valore NPV max:', -x+y, '\n Quante ne compro del tipo A:', binaria1, '\n Quante ne compro B:', binaria2)

    EE = instance.EnergiaAnnua.value#[MWh]
    print('\n Yeary Energy:', EE)
