from pyomo.environ import Param, RangeSet, NonNegativeReals, NonNegativeIntegers, Var, Set, PositiveIntegers, Reals, Binary
from pyomo.core import *
from Initialize_1 import Initialize_Duration_Curve, Initialize_Hgross#, Initialize_MaxN


def Model_Creation(model):
    #Param. per Sets
    model.Giorni = Param(within=NonNegativeReals)
    model.Numero_TipiTurbine = Param(within=NonNegativeReals)
    model.Nmax = Param(within=NonNegativeIntegers)
    #Sets
    model.giorni = RangeSet(model.Giorni)
    model.t = RangeSet(model.Numero_TipiTurbine)
    model.nmax = RangeSet(model.Nmax)

    #Parametri singoli
    model.DMV = Param(within=NonNegativeReals)
    model.Eta_aux = Param(within=NonNegativeReals)
    model.Revenues_Specific = Param(within=NonNegativeReals)
    model.Perc_OeM = Param(within=NonNegativeReals)
    model.Inv_Cost = Param(within=NonNegativeReals)
    model.Ammortization = Param(within=NonNegativeReals)
    model.Taxes = Param(within=NonNegativeReals)
    model.Discount_Rate = Param(within=NonNegativeReals)
    model.Lifetime = Param(within=NonNegativeIntegers)
    model.Coeff = Param(within=NonNegativeReals)

    #Param. multi-ingresso indicizzati sul numero di turbine diversi
    model.Portata_Nom = Param(model.t, within=NonNegativeReals)
    model.Portata_Min = Param(model.t, within=NonNegativeReals)
    model.Portata_Max = Param(model.t, within=NonNegativeReals)
    model.Etas = Param(model.t, within=NonNegativeReals)
    model.Cost_turb = Param(model.t, within=NonNegativeReals)

    #Param. inizializzati da excel (da dare come input)
    model.Duration_Curve = Param(model.giorni, within=NonNegativeReals, initialize=Initialize_Duration_Curve)  # già tolto il DMV
    model.Hgross = Param(model.giorni, within=NonNegativeReals, initialize=Initialize_Hgross)

    # Var. modello
    #Var. Binarie
    #Binary_Turbines ti dice se il giorno i la turbina n sta venendo usata (accesa/spenta quel giorno quella turbina)
    model.Binary_Turbines_A = Var(model.giorni, model.nmax, within=Binary)
    model.Binary_Turbines_B = Var(model.giorni, model.nmax, within=Binary)
    #Binary ti dice se la turbina in generale è stata usata (funziona o non funziona-->la pago o non la pago per NPV)
    model.Binary_A = Var(model.nmax, within=Binary)
    model.Binary_B = Var(model.nmax, within=Binary)

    #Var di prova per esperimenti
    model.Portata_A = Var(model.giorni, model.nmax)
    model.Portata_B = Var(model.giorni, model.nmax)
    model.Hnet_A = Var(model.giorni, model.nmax)
    model.Hnet_B = Var(model.giorni, model.nmax)
    model.Potenza_giorn_A = Var(model.giorni)
    model.Potenza_giorn_B = Var(model.giorni)
    model.EnergiaAnnua = Var()
    model.Costo_Turbine_Variabile = Var()

    #Var. per visualizzare NPV e dati in uscita
    model.cf = Var()
    model.INV_COST = Var()
 
