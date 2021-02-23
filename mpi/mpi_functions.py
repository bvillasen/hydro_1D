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




def Set_MPI_Boundaries( self ):
  id = self.mpi.id
  id_l = self.mpi.id_l
  id_r = self.mpi.id_r
  comm = self.mpi.comm
  n_ghost  = self.n_ghost
  n_fileds = self.n_fileds

  # Set Left Buffer
  self.send_buffer_l[0*n_ghost:1*n_ghost] = self.density [n_ghost:2*n_ghost]
  self.send_buffer_l[1*n_ghost:2*n_ghost] = self.momentum[n_ghost:2*n_ghost]
  self.send_buffer_l[2*n_ghost:3*n_ghost] = self.energy  [n_ghost:2*n_ghost] 

  # Set Right Buffer
  self.send_buffer_r[0*n_ghost:1*n_ghost] = self.density [-2*n_ghost:-n_ghost]
  self.send_buffer_r[1*n_ghost:2*n_ghost] = self.momentum[-2*n_ghost:-n_ghost]
  self.send_buffer_r[2*n_ghost:3*n_ghost] = self.energy  [-2*n_ghost:-n_ghost] 

  print( 'Transfering Boundaries' )
  # Even processes
  if id % 2 == 0:
    comm.Send(self.send_buffer_r, dest=id_r, tag=1)
    comm.Send(self.send_buffer_l, dest=id_l, tag=0)
    comm.Recv(self.recv_buffer_l, source=id_l, tag=1)
    comm.Recv(self.recv_buffer_r, source=id_r, tag=0)
    
  # Odd processes
  if id % 2 == 1:
    comm.Recv(self.recv_buffer_l, source=id_l, tag=1)
    comm.Recv(self.recv_buffer_r, source=id_r, tag=0)
    comm.Send(self.send_buffer_r, dest=id_r, tag=1)
    comm.Send(self.send_buffer_l, dest=id_l, tag=0)
    
  # Unload the transfer buffers
  self.density[:n_ghost]  = self.recv_buffer_l[0*n_ghost:1*n_ghost] 
  self.momentum[:n_ghost] = self.recv_buffer_l[1*n_ghost:2*n_ghost]  
  self.energy[:n_ghost]   = self.recv_buffer_l[2*n_ghost:3*n_ghost]  

  self.density[-n_ghost:]  = self.recv_buffer_r[0*n_ghost:1*n_ghost] 
  self.momentum[-n_ghost:] = self.recv_buffer_r[1*n_ghost:2*n_ghost]  
  self.energy[-n_ghost:]   = self.recv_buffer_r[2*n_ghost:3*n_ghost] 
    
