import numpy as np




def Set_Initial_Conditions_Test( self ):
  
  id = self.mpi.id
  n_local = self.n_local
  n_ghost = self.n_ghost
  
  for i in range(n_local):
    self.density[i+n_ghost]  = id
    self.momentum[i+n_ghost] = 2*id
    self.energy[i+n_ghost] = 3*id
  
  