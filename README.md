# Python Practice Projects

A list of projects done to address various problem statements using python.

### 1. Analysis of Covid Cases in Countries

Given a CSV file with data regarding the cases recorded in countries, calculates and returns one of the following depending on the command line input:
* Statistics - calculates for each month, the minimum, maximum, average and standard deviation of the recorded cases across that month.
* Correlation - calculates the correlation of each of the above results for any two countries.

Example CSV file is provided and the examples for possible interactions are as follows:
* python main.py 'Covid-data-for-project_1_sample.csv' "France" "statistics"
* python main.py 'Covid-data-for-project_1_sample.csv' ["france","italy"] "correlation"
