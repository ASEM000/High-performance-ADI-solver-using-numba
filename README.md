[![DOI](https://zenodo.org/badge/295934862.svg)](https://zenodo.org/badge/latestdoi/295934862)

# High performance ADI solver using numba
2D diffusion equation solver using ADI method and accelerated by numba

#### Comparison between the execution time between numpy and numba implementation




![Image](https://i.imgur.com/hlpckHG.png)

### How to use

** Example : Solve a grid of 10x10 (boundaries inclusive) with**
* boundary conditions of ( 100c Top,  50c right ,  0c bottom , 75c left  ) 
* initial condition of 0c
* Lambda = Kdt/(dx^2)=0.0835
* time steps = 1000

### 1.Generate grid

generate grid 10x10 

` grid = utils.generate_grid(n = 8 , bc=(100,50,0,75) , ic=0) ` <br>
` utils.showHeatMap(grid,annotate=True,figsize=(15,15)) `

![Image](https://i.imgur.com/xTO5MPd.png)

### 2.Solve 

` steps = True => means keep the intermediate solution steps `  <br>
` solution = ADI_SOLVER.solve(grid,Lambda=0.0835,iters=1000,steps = True) `

##### The solution output array is in form of (time_step,row,col ) , where time_step = 0 is the initial grid
**Show result**

` time_step = 50 ` <br>
` utils.showHeatMap(solution[time_step,:,:], annotate=True,figsize=(15,15)) `


![Image](https://i.imgur.com/JV3mJUf.png)
