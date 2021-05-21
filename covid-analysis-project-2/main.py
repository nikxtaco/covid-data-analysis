# COMMON FUNCTIONS

def filelist(csvfile): # converts tabular data from file to a list of lists divided into rows
    datalist=[]
    infile=open(csvfile,'r')
    
    for line in infile:      
        line=line.split(',') 
        line=line[:-1]                  
        datalist.append(line)
        
    infile.close()
    return datalist


def columnchecker(datalist): # to find the index of the required columns 
    country=0
    continent=0
    date=0
    new_cases=0
    new_deaths=0    
    
    line = datalist[0]
    try:
        country=line.index('location')
        continent=line.index('continent')
        date=line.index('date')
        new_cases=line.index('new_cases')
        new_deaths=line.index('new_deaths')
    
        return country,continent, date,new_cases,new_deaths
    
    except (ValueError):
        print('The headings do not exist.')
        return None
    

# FUNCTIONS REQUIRED FOR GENERATING THE COUNTRY DICTIONARY

def countrylist(datalist,location): # returns the four lists for each country
    country_index,continent_index,date_index,newcase_index,newdeath_index = columnchecker(datalist)
    
    totalcase_permonth_list=[0]*12  
    totaldeath_permonth_list=[0]*12 
    averagecase_permonth_list=[0]*12 
    averagedeath_permonth_list=[0]*12 
    casedays_list=[0]*12 
    deathdays_list=[0]*12
    casedays_moreavg=[0]*12 
    deathdays_moreavg=[0]*12 
    final_list=[]
    
    for line in datalist:              
    
        if line[country_index]==location:
            date = line[date_index].split('/')
            
            if len(date)==3:            
                month_index=int(date[1])-1
                casedays_list[month_index]+=1 
                deathdays_list[month_index] +=1 
                
                if line[newcase_index].isnumeric() and int(line[newcase_index])>0:
                    totalcase_permonth_list[month_index] += int(line[newcase_index]) 
                    
                if line[newdeath_index].isnumeric() and int(line[newdeath_index])>0:
                    totaldeath_permonth_list[month_index] += int(line[newdeath_index]) 
                 
    for i in range(12): 
    
        if casedays_list[i] != 0:
            averagecase_permonth_list[i]= totalcase_permonth_list[i]//casedays_list[i]
        elif casedays_list[i] ==0:
            averagecase_permonth_list[i]= totalcase_permonth_list[i]
            
        if deathdays_list[i]!=0:
            averagedeath_permonth_list[i]=totaldeath_permonth_list[i]//deathdays_list[i]
        elif deathdays_list[i]==0:
            averagedeath_permonth_list[i]=totaldeath_permonth_list[i]
        
    for line in datalist:          
    
        if line[country_index]==location:
            date= line[date_index].split('/')
            
            if len(date)==3:            
                month_index= int(date[1])-1
                
                if line[newcase_index].isnumeric() and averagecase_permonth_list[month_index] < int(line[newcase_index]):
                    casedays_moreavg[month_index] +=1
                        
                if line[newdeath_index].isnumeric() and averagedeath_permonth_list[month_index] < int(line[newdeath_index]):
                    deathdays_moreavg[month_index] +=1        
    
    final_list.append(totalcase_permonth_list)
    final_list.append(totaldeath_permonth_list)
    final_list.append(casedays_moreavg)
    final_list.append(deathdays_moreavg)
    
    return final_list


def keyfinder_country(datalist): # returns a list of all countries
     countrylist=[]
     country_index,continent_index,date_index,newcase_index,newdeath_index=columnchecker(datalist)
     
     for line in datalist:         
         if line[country_index] not in countrylist:
             countrylist.append(line[country_index])
     
     countrylist=countrylist[1:]       
     return countrylist


def countrydictionary(datalist): # gets the list of countries and each countries value lists separately, and joins them together to return the final country dictionary
    dict_country={}
    listofcountries=keyfinder_country(datalist)
    
    for country in listofcountries:
      final_list=countrylist(datalist,country)
      dict_country[country]=final_list
        
    return dict_country


# FUNCTIONS REQUIRED FOR GENERATING THE CONTINENT DICTIONARY

def keyfinder_continent(datalist): # returns a list of all continents
     continentlist=[]
     country_index,continent_index,date_index,newcase_index,newdeath_index=columnchecker(datalist)
     
     for line in datalist:         
         if line[continent_index] not in continentlist:
             continentlist.append(line[continent_index])
     
     continentlist=continentlist[1:]       
     return continentlist


def continentdictionary(datalist): # gets the list of continents and each continents value lists separately, and joins them together to return the final continent dictionary
    dict_continent={}
    listofcontinents=keyfinder_continent(datalist)
    
    for continent in listofcontinents:
        final_list=listcontinent(datalist,continent)
        dict_continent[continent]=final_list
        
    return dict_continent
        

def contries_in_continent(datalist, location): # returns the list of countries with the continent which is passed as an argument
  country_index,continent_index,date_index,newcase_index,newdeath_index=columnchecker(datalist)
  countrylist = []
  for line in datalist:              
        if line[continent_index]==location and line[country_index] not in countrylist:
             countrylist.append(line[country_index])

  return countrylist


def gen_list(input_list): # generates a list of lists capable of storing the sums of new cases or new deaths for each day of the year
    output = []
    for i in range(12):
        entry = []
        for j in range(input_list[i]):
            entry += [0]
        output.append(entry)
    return output


def morethan_continent(datalist,continent,avg1,avg2): # returns the number of days greater than the respective averages for each month which are passed as arguments
  country_index,continent_index,date_index,newcase_index,newdeath_index=columnchecker(datalist)
  morethanavg_case = [0] * 12
  morethanavg_death = [0] * 12

  days_list = [31,29,31,30,31,30,31,31,30,31,30,31]
  newcase_sumlist = gen_list(days_list)
  newdeath_sumlist = gen_list(days_list)

  for line in datalist:

    if(line[continent_index] == continent):     

      date= line[date_index].split('/')
      if len(date)==3:            
          month_index= int(date[1])-1
          day_index= int(date[0])-1

          if line[newcase_index].isnumeric() and int(line[newcase_index])>0:
            newcase_sumlist[month_index][day_index] += int(line[newcase_index])

          if line[newdeath_index].isnumeric() and int(line[newdeath_index])>0:
            newdeath_sumlist[month_index][day_index] += int(line[newdeath_index])

  for line in datalist: 
    
    if(line[continent_index] == continent):          
    
      date= line[date_index].split('/')
      if len(date)==3:            
          month_index= int(date[1])-1
          day_index= int(date[0])-1

          if avg1[month_index] < int(newcase_sumlist[month_index][day_index]):
              morethanavg_case[month_index] +=1
              newcase_sumlist[month_index][day_index] = -1
                  
          if avg2[month_index] < int(newdeath_sumlist[month_index][day_index]):
              morethanavg_death[month_index] +=1
              newdeath_sumlist[month_index][day_index] = -1

  return morethanavg_case, morethanavg_death   


def listcontinent(datalist, continent): # returns the four required lists for each continent
  countrylist = contries_in_continent(datalist, continent)
  sum1 = [0] * 12
  sum2 = [0] * 12
  avg1 = [0] * 12
  avg2 = [0] * 12
  days_list = [31,29,31,30,31,30,31,31,30,31,30,31]
  final_list = []

  final_dict_country = countrydictionary(datalist)

  for country in countrylist:
    list_of_lists = final_dict_country[country]
    zipped_lists1 = zip(list_of_lists[0], sum1)
    sum1 = [x + y for (x, y) in zipped_lists1]
    zipped_lists2 = zip(list_of_lists[1], sum2)
    sum2 = [x + y for (x, y) in zipped_lists2]

  for i in range(12):
    if days_list[i] !=0:
      avg1[i] = round (sum1[i] / days_list[i],4) 
    else:
      avg1[i] = 0

    if days_list[i] !=0:
      avg2[i] = round (sum2[i] / days_list[i],4) 
    else:
      avg2[i] = 0

  morethan1, morethan2 = morethan_continent(datalist, continent, avg1, avg2)

  final_list.append(sum1)
  final_list.append(sum2)
  final_list.append(morethan1)
  final_list.append(morethan2)

  return final_list

# MAIN FUNCTION

def main(csvfile):
  try: 
        datalist = filelist(csvfile)
        if columnchecker(datalist) == None:
          return None, None
        else:
          dict_country = countrydictionary(datalist)  
          dict_continent = continentdictionary(datalist)
          return dict_country, dict_continent
    
  # Error Handing
  except (IOError):
        print ("File not found.")
        return None, None
    
  except (TypeError):
        print ("CSV file invalid.")
        return None, None
    
dict_country,dict_continent=main('csvfile.csv')
print(dict_continent.keys())
