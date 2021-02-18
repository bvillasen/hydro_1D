from mpi4py import MPI


class MPI_Box:
  def __init__( self ):
    comm = MPI.COMM_WORLD
    id = comm.Get_rank()
    n_procs = comm.Get_size()
    self.id = id
    self.n_procs = n_procs
    self.comm = comm
    
    # Set periodic MPI neighbors 
    self.id_l = id - 1 if id > 0 else n_procs - 1
    self.id_r = id + 1 if id < n_procs-1 else 0
    # print( f' id:{id}  l:{self.id_l}   r:{self.id_r}')
    self.print( f'Initialized MPI: Running on {self.n_procs} MPI tasks' )
    
  def print( self, text ):
    if self.id == 0: print( text )

