
from util import *
from ADI_SOLVER import *
import ipywidgets

def start():
    layout = ipywidgets.Layout(width= '100%',height='20px')
    bc1 = ipywidgets.IntSlider(min=0,max=1000,value = 681,step=1,description='Top BC' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    bc2 = ipywidgets.IntSlider(min=0,max=1000,value=205,step=1,description='Right BC' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    bc3 = ipywidgets.IntSlider(min=0,max=1000,value=239,step=1,description='Bottom BC' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    bc4 = ipywidgets.IntSlider(min=0,max=1000,step=1,value=611,description='Left BC' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    ic0 = ipywidgets.IntSlider(min=0,max=1000,step=1,value=71,description='IC' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    lam = ipywidgets.FloatSlider(min=0,max=0.5,value=239,step=0.001,description='lambda' ,layout=layout,continuous_update=False,readout_format='.5f',style = {'description_width': 'initial'})
    grid = ipywidgets.IntSlider(min=0,max=1000,step=1,value=50,description='grid size (NxN)' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    iters = ipywidgets.IntSlider(min=0,max=1000,step=1,value=10,description='iterations' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    time_step = ipywidgets.IntSlider(min=0,max=1000,step=1,value=10,description='plot time step' ,layout=layout,continuous_update=False,style = {'description_width': 'initial'})
    interact_calc=ipywidgets.interact.options(manual=True, manual_name="Solve!")

    @interact_calc(grid_size=grid,bc1=bc1,bc2=bc2,bc3=bc3,bc4=bc4,ic0=ic0,Lambda=lam,time_step=time_step)
    def adi_solver_interact(grid_size,bc1,bc2,bc3,bc4,ic0,Lambda,time_step):
        grid = generate_grid(n = grid_size , bc=(bc1,bc2,bc3,bc4) , ic=ic0)
        solution = solve(grid.copy(),Lambda=Lambda,iters=time_step,steps = True)
        show_heat_maps((solution[time_step],f'Numerical solution at time step ={time_step}'),figsize=(7,7))
