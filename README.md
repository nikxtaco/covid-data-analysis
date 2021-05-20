# Python Practice Projects

A list of projects done to address various problem statements using python.

### 1. Analysis of Covid Cases in Countries

Given a CSV file with data regarding the cases recorded in countries, calculates and returns one of the following depending on the command line input:
* Statistics - calculates for each month, the minimum, maximum, average and standard deviation of the recorded cases across that month.
* Correlation - calculates the correlation of each of the above results for any two countries.

Example CSV file is provided and the examples for possible interactions are as follows:
* python main.py 'Covid-data-for-project_1_sample.csv' "France" "statistics"
* python main.py 'Covid-data-for-project_1_sample.csv' ["france","italy"] "correlation"

### 2. Analysis of Covid Cases in Continents

Given a CSV file with data regarding the cases recorded in countries within each continent, calculates and returns the following:
* A dictionary containing the country name as key and a list having the following data about  
that country as value.  
   * A list containing the total number of recorded positive cases of COVID-19 for each  
month of the year. 
   * A list containing the total number of recorded deaths due to COVID-19 for each month  
of the year. 
   * A list containing the total number of days for each month of year, when the recorded  
positive cases of COVID-19 for that month of the year were greater than the average  
recorded positive cases of that month of the year. 
   * A list containing the total number of days for each month of year, when the recorded  
deaths due to COVID-19 for that month of the year were greater than the average  
deaths due to COVID-19 for that month of the year. 
* A dictionary containing the continent name as key and a list having the data similar to above  
for each continent as value.

Example CSV file is provided and the examples for possible interactions are as follows:

* dict_country,dict_continent = main('Covid-data-for-project-2-sample.csv') 

The output returned are dictionaries which can be accessed in the following ways: 
   * dict_country['afghanistan'] 
   * dict_country['italy'] 
   * dict_continent.keys() 
   * dict_continent['oceania'] 
