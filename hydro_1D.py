import sys, os
root_dir = os.getcwd()
sub_dirs = [x[0] for x in os.walk(root_dir)]
sys.path.extend(sub_dirs)
from simulation_parameters import Simulation




L_box = 10.0
N_cells = 64

Sim = Simulation( L_box, N_cells )




Sim.mpi.print( 'Finished Succesfully ')