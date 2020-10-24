
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


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

def show_heat_maps(*grids,annotate=False,save=False,figsize=(30,10)):

    
#     if annotate:
#         N,M = int(grids1.shape[0]),int(grids1.shape[1])
#         for k in range(N):
#             for j in range(M):
#                 text1 = ax1.text(j, k, 
#                                np.round(grids1[k, j],1),
#                                ha="center", va="center", color="w",fontsize=12)
                
#                 text2 = ax2.text(j, k, 
#                                np.round(grids2[k, j],1),
#                                ha="center", va="center", color="w",fontsize=12)
     
# #                 text3 = ax3.text(j, k, 
# #                                np.round(diff[k, j],1),
# #                                ha="center", va="center", color="w")

    
    # Set up figure and image grid
    fig = plt.figure(figsize=figsize)

    grid = ImageGrid(fig, 111,          # as in plt.subplot(111)
                     nrows_ncols=(1,len(grids)),
                     axes_pad=0.25,
                     share_all=True,
                     cbar_location="left",
                     cbar_mode="single",
                     cbar_size="5%",
                     cbar_pad=0.25,
                     )

    # Add data to image grid
    for ax,g in zip(grid,grids):#,['Numerical solution','DefusionNet','Difference']):
        im = ax.imshow(g[0])
        ax.title.set_text(g[1])


        if annotate:
            N,M = int(g[0].shape[0]),int(g[0].shape[1])
            for k in range(N):
                for j in range(M):
                    text1 = ax.text(j, k, np.round(g[0][k, j],1),ha="center", va="center", color="w",fontsize=12)

    # Colorbar
    ax.cax.colorbar(im)
    ax.cax.toggle_label(True)

    #plt.tight_layout()    # Works, but may still require rect paramater to keep colorbar labels visible
    plt.show()
