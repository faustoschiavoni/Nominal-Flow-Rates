import time
from pyomo.core import *
from pyomo.environ import AbstractModel
from Model_Creation_2 import Model_Creation
from Model_Resolution_4 import Model_Resolution
from Results_5 import Risultati

start = time.time()
model = AbstractModel()

Optimization_Goal = "NPV" #o NPV, IRR, PBT

Model_Creation(model)
instance = Model_Resolution(model, Optimization_Goal)

Risultati(instance, Optimization_Goal)

end = time.time()
elapsed = end - start
print('\n\nModel run complete (overall time: ', round(elapsed, 0), 's,', round(elapsed/60, 1), ' m)\n')
