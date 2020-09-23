[![DOI](https://zenodo.org/badge/295934862.svg)](https://zenodo.org/badge/latestdoi/295934862)

# High performance ADI solver using numba
2D diffusion equation solver using ADI method and accelerated by numba

![Image](https://i.imgur.com/u3chQ9p.png)

### How to use

**Solve a grid of 10x10 (boundaries inclusive) with**

* boundary conditions of ( 100c Top,  50c right ,  0c botton , 75c left  ) 

* initial condition of 0c

* Lambda = Kdt/(dx^2)=0.0835

 * time step = 1000

#### Generate grid

generate grid 10x10 

` grid = utils.generate_grid(n = 8 , bc=(100,50,0,75) , ic=0) 
utils.showHeatMap(grid,annotate=True,figsize=(15,15)) `

![Image](https://i.imgur.com/xTO5MPd.png)

**Solve** 
`solution = ADI_SOLVER.solve(grid,Lambda=0.0835,iters=1000,steps = True)`

**Show result**

`
time_step = 50
utils.showHeatMap(solution[time_step,:,:], annotate=True,figsize=(15,15))
`

![Image](https://i.imgur.com/JV3mJUf.png)
