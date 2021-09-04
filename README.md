# EMA time-series analysis and comparison with a simple piecewise deterministic Markov process model

**DJ Passey, David Lydon-Staley, Peter Mucha, and Zach Boyd**


*This material is based upon work supported by, or in part by, the U.S. Army Research Office under grant number W911NF-18-1-0244.*

This repository contains code and latex supporting work done to model campus drinking with a piecewise deterministic Markov process. Individuals are modeled with the following equations:
![Plot of 10 Simulated Drinking Days](https://github.com/djpasseyjr/ShinePDMP/raw/main/Latex/DrinkingModel/individual_w_equation.png)
This produces a probabalistic sequence of drinks. The mood function `m(t)` and drinking opportunities `e` are supplied apriori. (Here `m(t)` is sinusoidal and `e ~ Exponential(1)`) We couple this model with other individuals by providing a social network and the additional rule that each time your neighbors drink, you receive an opportunity to drink. This is visualized below:
![Raster Plot of drinking](https://github.com/djpasseyjr/ShinePDMP/raw/main/Latex/DrinkingModel/coupled_drinking_raster.png)
Here, a point at `(x, y)` represents a drink taken at time `x` by individual with id number `y`. For example, all points that fall on the line `y=6` were taken by individual 6. Point colors are the result of a clustering algorithm applied to the social network. We see that individuals are more likely to drink with other individuals in their own cluster. This can be seen by observing the differing behavior of the orange and green clusters at time=35.

### Contents
#### Directories
1. The `Code` directory contains Python and Julia Code analyzing the EMA data and simulating student drinking. See `Code/README.md` for information about running the code.
2. The `Latex` directory contains latex and images for the some of the project's writeups

#### Write Ups
1. `PDMPModelAnalyticExpectation.pdf` contains a complete description of the model of a single social drinker as well as analytic results about a simpler model.
2. `CoupledDrinkingModel.pdf` displays results of coupling and simulating multiple social drinkers at once.
3. `EMATimeseriesAnalysis.pdf` Contains fourier analysis, stationarity and cross correlation of the EMA data.
