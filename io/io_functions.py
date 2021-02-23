import numpy as np
import h5py as h5



def Save_Snapshot_HDF5( self ):
  
  
  id = self.mpi.id
  n_file = self.n_file
  output_dir = self.output_dir
  
  n_ghost = self.n_ghost
  density  = self.density [n_ghost:-n_ghost]
  momentum = self.momentum[n_ghost:-n_ghost]
  energy   = self.energy  [n_ghost:-n_ghost]
  
  file_name = f'{output_dir}/snaphot_{n_file:03}.h5.{id}'
  

  self.mpi.print( f'Saved File: {file_name[:-2]}') 
  self.n_file += 1
