import sys, os
import numpy as np
root_dir = os.getcwd()
sub_dirs = [x[0] for x in os.walk(root_dir)]
sys.path.extend(sub_dirs)
from mpi_functions import MPI_Box


class Simulation:
  def __init__( self, L, N, n_g=1 ):
    self.Lbox = L
    self.n_total = N
    self.n_ghost = n_g
    self.dx = L / N
    
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
    self.dens     = np.zeros( n_full )
    self.momentum = np.zeros( n_full )
    self.energy   = np.zeros( n_full ) 
    self.send_buffer_l = np.zeros( n_fileds * self.n_ghost )
    self.send_buffer_r = np.zeros( n_fileds * self.n_ghost )
    self.recv_buffer_l = np.zeros( n_fileds * self.n_ghost )
    self.recv_buffer_r = np.zeros( n_fileds * self.n_ghost )
    self.n_fileds = n_fileds
    mpi.print( 'Allocated Memory')
    
  def Set_Boundaries( self ):
    id = self.id
    id_l = self.id_l
    id_r = self.id_r
    n_fileds = self.n_fileds
    
    # Set Left Buffer
    self.send_buffer_l[0*n_ghost:1*n_ghost] = dens[:n_ghost]
    self.send_buffer_l[1*n_ghost:2*n_ghost] = momentum[:n_ghost]
    self.send_buffer_l[2*n_ghost:3*n_ghost] = energy[:n_ghost] 
    
    # Set Right Buffer
    self.send_buffer_r[0*n_ghost:1*n_ghost] = dens[-n_ghost:]
    self.send_buffer_r[1*n_ghost:2*n_ghost] = momentum[-n_ghost:]
    self.send_buffer_r[2*n_ghost:3*n_ghost] = energy[-n_ghost:] 
    
    
    # if id % 2 == 0:
      
 
