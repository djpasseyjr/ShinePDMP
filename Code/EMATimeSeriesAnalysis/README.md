# Time Series Analysis of the EMA Data

This directory contains work analyzing the EMA data. The goal here is to find features of the data that we can replicate with generative models. The work here divides into three categories

1. **Fourier Analysis:** Identifying ocillatory patterns in the drinking and mood time-series. For example we found evidence of a repeating seven day pattern in student drinking behavior.
2. **Stationarity:** This measures whether a time series has an increasing or decreasing trend over time. We found that about two-thirds of participants drank the same amount throughout the entire study, and one-third show an increasing or decreasing trend. The results for mood were similar. 
3. **Cross correlation:** This technique attempts to find the correlation between two time series across time. For example, using this technique we were able to show that individuals mood yesterday is correlated with the drinking they report today. (This is likely because the drinks they *report* today are the drinks they *had yesterday*)

### Directory Contents

* `CrossCorrelation(Num-Drank).ipynb`: This contains the first pass at analyzing the data. This looks at mood data and a drinking time series created from the *number* of drinks taken each day.
* `CrossCorrelation(If-Drank).ipynb`: We found that the drinking timeseries data was less noisy if we used a time series of zeros and ones where ones signify that the individual drank that day. This notebook contains the **best visualizations** and looks at a variety of ideas.
* `CrossCorrelation(If-Drank-Gtr-4).ipynb` Thanks to [Keith Wiley's work](FourierTransformStuff(KeithWiley).pdf) with the fourier transform, we found that eliminating the people who drank less than four times cleaned up our histograms. This notebook investigates the subset of individuals (about half) who drank more than four days of the study. The separation in these plots is probably the cleanest of any notebook.
* `MoodFunctionAnalysis.ipynb` Is the primary time series analysis of individual mood, there are some nice visuals here, but the analytical plots here are mostly out of date and are better visualized in `CrossCorrelation(If-Drank).ipynb`
* `DrinkingStats.ipynb` is also a preliminary exploratory notebook. It has some nice visuals as well, but the analysis is not as good as the work in `CrossCorelation(If-Drank).ipynb`


### Caveats

I made a choice to separate the full EMA time series into *two timeseries*. The first corresponds to the *morning prompt*, which contains answers to the EMA questions taken each morning. The time series here will have 28 entries for each daily morning prompt in the 28 day period. The second time series is the *evening prompt* series which also has 28 entries for each evening prompt. 

I did this in order to have equally spaced time intervals for the fourier transform, and because participants reported far less drinking in the evening prompt respone and this tended to skew the analysis. 


For this reason, most plots in `CrossCorrelation(Num-Drank).ipynb` are repeated twice (in salmon and then in blue) for the morning and eveing time series respectively. Ususally there is far less signal in the evening time series (because less drinking occurs in the day) and so it could be argued that including this data will increase the noise in the dataset. However, if conventional wisdom holds, day drinking is a strong indicator of other important psycological covariates and so the evening prompt data may contain useful information about individuals.

It is an open question if these timeseries are better investigated as a single 56 day time series or not. 