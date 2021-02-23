import sys, os
import numpy as np
root_dir = os.getcwd()
sub_dirs = [x[0] for x in os.walk(root_dir)]
sys.path.extend(sub_dirs)
from  initial_conditions import Set_Initial_Conditions_Test
from mpi_functions import MPI_Box, Set_MPI_Boundaries
from io_functions import Save_Snapshot_HDF5

class Simulation:
  def __init__( self, L, N, out_dir, n_g=1 ):
    self.Lbox = L
    self.n_total = N
    self.n_ghost = n_g
    self.dx = L / N
    self.output_dir = out_dir
    
    # Number of file to save
    self.n_file = 0
    
    # Initializa MPI
    mpi = MPI_Box()
    n_procs = mpi.n_procs
    self.n_local = N // n_procs
    mpi.print( f'N cells: {self.n_total}  N local: {self.n_local}' )
    self.mpi = mpi
    
    # Allocate arrays
    n_fileds = 3
    n_full = self.n_local + 2 * self.n_ghost
    self.x = np.linspace( mpi.id * self.n_local, (mpi.id + 1) * self.n_local - 1, self.n_local ) * self.dx + 0.5 * self.dx
    self.density  = np.zeros( n_full )
    self.momentum = np.zeros( n_full )
    self.energy   = np.zeros( n_full ) 
    self.send_buffer_l = np.zeros( n_fileds * self.n_ghost )
    self.send_buffer_r = np.zeros( n_fileds * self.n_ghost )
    self.recv_buffer_l = np.zeros( n_fileds * self.n_ghost )
    self.recv_buffer_r = np.zeros( n_fileds * self.n_ghost )
    self.n_fileds = n_fileds
    mpi.print( 'Allocated Memory')
  
  # Save HDF5 files
  Write_Snapshot = Save_Snapshot_HDF5
  
  # Set the Boundary Transfer Method to MPI bpundaries
  Set_Boundaries = Set_MPI_Boundaries
  
  # Set Test Initial Conditions
  Set_Initial_Conditions = Set_Initial_Conditions_Test
  
 
