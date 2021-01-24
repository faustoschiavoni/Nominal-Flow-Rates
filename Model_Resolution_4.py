from pyomo.opt import SolverFactory
from pyomo.core import *
from pyomo.environ import * #Objective, minimize, maximize, Constraint
from Constraints_3 import *



def Model_Resolution(model, Optimization_Goal, datapath="Inputs/Data.dat"):

    if Optimization_Goal == 'NPV':
            model.ObjectiveFunction = Objective(rule=Net_Present_Value, sense=maximize)

    model.V_Portata_A = Constraint(model.giorni, model.nmax, rule=V_Portata_A)
    model.V_Portata_B = Constraint(model.giorni, model.nmax, rule=V_Portata_B)
    model.V_Qavailable = Constraint(model.giorni, rule=V_Qavailable)
    model.V_Hnet_A = Constraint(model.giorni, model.nmax, rule=V_Hnet_A)
    model.V_Hnet_B = Constraint(model.giorni, model.nmax, rule=V_Hnet_B)
    model.V_Potenza_A = Constraint(model.giorni, rule=V_Potenza_A)
    model.V_Potenza_B = Constraint(model.giorni, rule=V_Potenza_B)
    model.V_EnergiaAnnua = Constraint(rule=V_EnergiaAnnua)
    model.V_Costo_Turbine_Variabile = Constraint(rule=V_Costo_Turbine_Variabile)

    model.Separo_NPV = Constraint(rule=Separo_NPV) 
    model.Separo_INV_COST = Constraint(rule=Separo_INV_COST) 


    #Carico i valori veri da recuperare dal Data.dat
    instance = model.create_instance(datapath)
    print('\nInstance created')
    opt = SolverFactory('gurobi')

   
    opt.set_options('Method=2 NonConvex=2 Crossover=0 BarConvTol=1e-3 OptimalityTol=1e-3 FeasibilityTol=1e-3 IterationLimit=1e13')

    print('Calling solver...')
    results = opt.solve(instance, tee=True, keepfiles=True)
    print('Instance solved')

    instance.solutions.load_from(results)
    return instance


