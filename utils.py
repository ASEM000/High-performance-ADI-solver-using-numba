
import matplotlib.pyplot as plt
import numpy as np
from numba import jit ,f8

@jit(nopython=True)
def generate_grid(n,bc,ic=0):
    #n=> Number of interior nodes

    A = np.ones((n+2,n+2),dtype=np.float32) * ic
    A[0,0]=A[-1,-1]=A[0,-1]=A[-1,0]=0
    A[0,1:-1]=bc[2]    # switch the top and bottom wall since we start the iterations from top
    A[1:-1,-1]=bc[1]
    A[-1,1:-1]=bc[0]
    A[1:-1,0]=bc[3]

    return A

def showHeatMap(grid,annotate=False,figures = None,title='',bar=False,figsize=(15,15)):
    grid =np.flip(grid,0)
    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(grid,cmap='viridis_r')
    
    plt.rcParams.update({'font.size': 15})
    
    if figures : grid = np.round(grid,figures)
    
    
    if annotate:
        N,M = int(grid.shape[0]),int(grid.shape[1])
        for i in range(N):
            for j in range(M):
                text = ax.text(j, i, 
                               grid[i,j],
                               ha="center", va="center", color="w")
    
    if bar :  ax.figure.colorbar(im, ax=ax)
    
    plt.title(title)
    plt.tight_layout()
    plt.xticks([]);
    plt.yticks([])
    plt.show() 
