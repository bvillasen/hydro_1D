import sys, os
root_dir = os.getcwd()
sub_dirs = [x[0] for x in os.walk(root_dir)]
sys.path.extend(sub_dirs)
from simulation import Simulation




L_box = 10.0
N_cells = 16

output_dir = '/raid/bruno/data/hydro_1D/test'

Sim = Simulation( L_box, N_cells, output_dir )


Sim.Set_Initial_Conditions()

Sim.Set_Boundaries()

Sim.Write_Snapshot()

# print( f'{Sim.mpi.id}  {Sim.density}')
# print( f'{Sim.mpi.id}  {Sim.momentum}')
# print( f'{Sim.mpi.id}  {Sim.energy}')


Sim.mpi.print( 'Finished Succesfully ')