# Piecewise Deterministic Markov Process Models

This directory contains Jupyter Notebooks and scripts for simulating campus drinking with a PDMP. This contains Python and Julia implementations of the model. Due to the iterative nature of writing models, models from different notebooks may not be exactly the same, though they should be similar. Be careful when comparing code across locations.

### Directory Contents

* The [JuliaVersion](/JuliaVersion) directory contains implementation of the PDMP in Julia. This code makes use of the [Agents.jl](https://juliadynamics.github.io/Agents.jl/v4.0/) package which has a great framework for automating the simulation, data collection and plotting of multi-agent models.
    1. `SocialAgents.ipynb` is a Jupyter notebook containing the code used to generate the majority of figures and simulations presented in Thrust4 lab meetings. (Peter is familiar with this work)
    2. `Expectation.ipynb` is a Jupyter notebook containing the code used to generate figures for [DrinkingModel.pdf](../../DrinkingModel.pdf)
    3. `binge_nb.jl` is a [Pluto notebook](https://github.com/fonsp/Pluto.jl)/Julia script for running the model and adjusting variables interactively. It is still a work in progress but a nice proof of concept. To run the interactive notebook start a Julia REPL session and (after installing `Pluto.jl` with `] add Pluto` or some other way) enter `using Pluto; Pluto.run()` in the REPL and this will open the Pluto web application in the browser (just like Jupyter does). Type in the path to `binge_nb.jl` and after the notebook opens, wait a while while all the packages install and the code runs.
    
 * The [PythonVersion](PythonVersion) directory contains a Python implementation of the model. It was coded from scratch and doesn't rely on a agent based framework so it may be easier to understand.
    1. `CravingMoodandEncounters.ipynb` was the first attempt to run the simulations. The framework created in this notebook was copied into `drinking_model.py` and `event_stochastic_ode.py` so that it could be imported into other notebooks without copy-pasting.  
    2. `CoupledDrinkingCode.ipynb` imports `drinking_model.py` and `event_stochastic_ode.py` and attempts to simulate two individuals whose drinking impacts eachother. It was here that I realized the difficulty in generalizing the python simulation code to larger groups and different models and decided to switch to the `Agents.jl` framework.
    3. `ModelParameterAnalysis.ipynb` is a first attempt at sensitivity analysis, that is, understanding the responses of the model to different parameter combinations. The results here show that the preliminary model is rather inflexible, and changes in hyper parameters don't do a lot to affect long term simulated drinking. However, these simulations were all done using a sinusuidal mood function and the regularity of this function could have contributed to neutralizing the effect of parameter changes.