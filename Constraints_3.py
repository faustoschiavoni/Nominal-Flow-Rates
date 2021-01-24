# Objective Functions
from pyomo.core import value

#Vincoli

def V_Portata_A(model, i, n):
    return model.Portata_A[i, n] == model.Binary_A[n] * model.Binary_Turbines_A[i, n] * model.Portata_Nom[1]


def V_Portata_B(model, i, n):
    return model.Portata_B[i, n] == model.Binary_B[n] * model.Binary_Turbines_B[i, n] * model.Portata_Nom[2]


def V_Qavailable(model, i):
    somma_portate = sum(model.Portata_A[i, n] + model.Portata_B[i, n] for n in model.nmax)
    return somma_portate <= model.Duration_Curve[i]


def V_Hnet_A(model, i, n):
    return model.Hnet_A[i, n] == model.Hgross[i] - model.Coeff * (model.Portata_A[i, n] ** 2)


def V_Hnet_B(model, i, n):
    return model.Hnet_B[i, n] == model.Hgross[i] - model.Coeff * (model.Portata_B[i, n] ** 2)



def V_Potenza_A(model, i):
    return model.Potenza_giorn_A[i] == (10 ** 3) * 9.81 * sum(
        model.Portata_A[i, n] * model.Hnet_A[i, n] * model.Etas[1] for n in model.nmax)


def V_Potenza_B(model, i):
    return model.Potenza_giorn_B[i] == (10 ** 3) * 9.81 * sum(
        model.Portata_B[i, n] * model.Hnet_B[i, n] * model.Etas[2] for n in model.nmax)



def V_EnergiaAnnua(model):
    return model.EnergiaAnnua == sum(model.Potenza_giorn_A[i] + model.Potenza_giorn_B[i] for i in
                                     model.giorni) * 24 * 1e-6 * model.Eta_aux  # aggiungere Potenza_parziale


def V_Costo_Turbine_Variabile(model):
    return model.Costo_Turbine_Variabile == sum(
        model.Binary_A[n] * model.Cost_turb[1] + model.Binary_B[n] * model.Cost_turb[2] for n in model.nmax)


def Separo_INV_COST(model):
    return model.INV_COST == model.Inv_Cost + model.Costo_Turbine_Variabile


def Separo_NPV(model):
    Revenues = model.EnergiaAnnua * model.Revenues_Specific
    Costs_perTasse = model.INV_COST * (model.Perc_OeM + (1 / model.Ammortization))
    Costs_perCF = model.INV_COST * model.Perc_OeM
    Taxes_1_20 = (Revenues - Costs_perTasse) * model.Taxes
    Taxes_21_30 = (Revenues - Costs_perCF) * model.Taxes
    CF_1_20 = Revenues - Costs_perCF - Taxes_1_20
    CF_21_30 = Revenues - Costs_perCF - Taxes_21_30

    Attual_amm = sum(1 / ((1 + model.Discount_Rate) ** i) for i in range(1, model.Ammortization + 1))
    Attual_senza = sum(1 / ((1 + model.Discount_Rate) ** i) for i in range(model.Ammortization + 1, model.Lifetime + 1))

    return model.cf == Attual_amm * CF_1_20 + Attual_senza * CF_21_30


def Net_Present_Value(model):  # objective!!
    # INV_COST = model.Inv_Cost + model.Costo_Turbine_Variabile
    return - model.INV_COST + model.cf
