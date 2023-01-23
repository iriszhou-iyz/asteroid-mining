asteroid-mining
a cost-benefit framework to determine asteroid mining targets using machine learning principles

# instructions
download the following link to your drive.
replace 'asteroids.csv' with the drive link in asteroid-mining-pca.py

# procedure
the program used nasa's jpl small-body database query, selecting near-earth objects and asteroids. the program conducted standard deviation and data cleaning on the raw data by dropping null values. pca was then completed, producing a two-dimensional graph. the program split the most correlated variable into quartiles indicated by color. the program was tested with the first 20 data points of the database, then the first 500 data points, then all 28,461 data points.

# conclusions
the following characteristics of asteroids were evaluated to determine the net benefits arising from mining a specific asteroid: distance from Earth, diameter, albedo, orbital eccentricity, semi-major axis, and period. the program was mostly successful in establishing a cost-benefit framework for analyzing the extent to which asteroids are net beneficial for mining processes: it found that middle- to far-range near-earth asteroids contained an abundance of precious minerals that could be mined.
