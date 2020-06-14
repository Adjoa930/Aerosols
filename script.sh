#using cdo to calculate trends, seasons and residuals
#!/bin/bash
#removing trends
#cdo -b 32  detrend West_Africa_aqua2.nc seas_resid.nc

#removing seasonality to get only residuals
#cdo -b 32 ymonsub seas_resid.nc -ymonmean seas_resid.nc residual.nc

#subtracting the residuals from the detrended to get seasonal components
#cdo -b 32 sub seas_resid.nc residual.nc seasonal.nc

#calculating trends by subtracting seasons and residuals from the main data
#cdo -b 32 sub West_Africa_aqua2.nc -add residual.nc seasonal.nc trend_estimate.nc


#calculating the trend at all grid points

#cdo trend West_Africa_aqua2.nc trend_slope.nc trend_intercept.nc


#merging all slopes and intercepts together
cdo mergetime trend_slope.nc trend_intercept.nc trends.nc


#calculating regression on the dataset

cdo regres West_Africa_aqua2.nc linreg.nc
