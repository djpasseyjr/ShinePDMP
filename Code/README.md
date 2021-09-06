# Project Code and Computational Notebooks

This directory contains the code and computational notebooks used to studying campus drinking and explain the data with a generative model.

### Contents
1. The `EMATimeSeriesAnalysis` directory contains notebooks analyzing the EMA data from a time series perspective with the attempt to identify important features in the data that can be explained with a model.

2. The `ODEModels` directory contains code to simulate college drinking in social networks with a piecewise deterministic markov process. 

### Getting Started

To run the Python code contained in these notebooks you will need to [install jupyter](https://jupyter.org/install) and several python packages: `pandas, scipy, matplotlib, numpy, statsmodels`.

To run the Julia code you need to [install Julia](https://julialang.org/downloads/) and add several packages by starting a Julia REPL session and entering 

```
using Pkg
Pkg.add("IJulia")
] add Agents, DataFrames, Distributions, GraphPlot, LightGraphs, Plots, Clustering, Colors
```
 You will also need to [add a Julia Kernel to Jupyter](https://medium.com/@djpasseyjr/it-only-takes-10-minutes-to-add-a-julia-kernel-to-jupyter-739490456a2b).
