import sys

def statistics(csvfile, country):
  min_list = [0] * 12
  max_list = [0] * 12
  avg_list = [0] * 12 # initially for sums, later avg
  count_for_avg_list = [0] * 12
  std_dev_list = [0] * 12 # initially for squares, later square root

  with open(csvfile, 'r') as f:
    for line in f:
        col = line.split(",")
        if col[2] == country:
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if min_list[month_index] == 0:
            min_list[month_index]=int(col[4])
          if int(col[4])<min_list[month_index] and int(col[4])!=0:
            min_list[month_index] = int(col[4])

          if max_list[month_index] == 0:
            max_list[month_index]=int(col[4])
          if int(col[4])>max_list[month_index]:
            max_list[month_index] = int(col[4])

          if avg_list[month_index] == 0:
            avg_list[month_index]=int(col[4])
          else:
            avg_list[month_index]+=int(col[4])
          count_for_avg_list[month_index]+=1

    i=0
    for avg in avg_list:
      if avg != 0:
        avg_list[i]/=count_for_avg_list[i]
        avg_list[i] = round(avg_list[i], 4)
      i+=1

  with open(csvfile, 'r') as f:
    for line in f:
      col = line.split(",")
      if col[2] == country:
        date = col[3].split('/')
        month_index = int(date[1]) - 1

        std_dev_list[month_index] += (int(col[4]) - avg_list[month_index])**2

    i=0
    for std in std_dev_list:
      if std != 0 and count_for_avg_list[i]!=0:
        std_dev_list[i] /= count_for_avg_list[i]
        std_dev_list[i] = std_dev_list[i]**0.5
        std_dev_list[i] = round(std_dev_list[i], 4)
      i+=1

    print(min_list)
    print(max_list)
    print(avg_list)
    print(std_dev_list)

def baselistmin(csvfile, first_country, second_country):
  min_list1 = [0] * 12
  min_list2 = [0] * 12
  
  with open(csvfile, 'r') as f:
    for line in f:
        col = line.split(",")
        current_country = col[2].lower()
        if current_country == first_country:          
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if min_list1[month_index] == 0:
            min_list1[month_index]=int(col[4])
          if int(col[4])<min_list1[month_index] and int(col[4])!=0:
            min_list1[month_index] = int(col[4])
        
        if current_country == second_country:          
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if min_list2[month_index] == 0:
            min_list2[month_index]=int(col[4])
          if int(col[4])<min_list2[month_index] and int(col[4])!=0:
            min_list2[month_index] = int(col[4])

  return min_list1, min_list2

def baselistmax(csvfile, first_country, second_country):
  max_list1 = [0] * 12
  max_list2 = [0] * 12
  
  with open(csvfile, 'r') as f:
    for line in f:
        col = line.split(",")
        current_country = col[2].lower()
        if current_country == first_country:          
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if max_list1[month_index] == 0:
            max_list1[month_index]=int(col[4])
          if int(col[4])>max_list1[month_index]:
            max_list1[month_index] = int(col[4])
        
        if current_country == second_country:          
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if max_list2[month_index] == 0:
            max_list2[month_index]=int(col[4])
          if int(col[4])>max_list2[month_index]:
            max_list2[month_index] = int(col[4])

  return max_list1, max_list2

def baselistavgstd(csvfile, first_country, second_country):
  avg_list1 = [0] * 12 # initially for sums, later avg
  count_for_avg_list1 = [0] * 12
  avg_list2 = [0] * 12 # initially for sums, later avg
  count_for_avg_list2 = [0] * 12
  std_dev_list1 = [0] * 12 # initially for squares, later square root
  std_dev_list2 = [0] * 12 # initially for squares, later square root
  
  with open(csvfile, 'r') as f:
    for line in f:
        col = line.split(",")
        current_country = col[2].lower()
        if current_country == first_country:          
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if avg_list1[month_index] == 0:
            avg_list1[month_index]=int(col[4])
          else:
            avg_list1[month_index]+=int(col[4])
          count_for_avg_list1[month_index]+=1
        
        if current_country == second_country:          
          date = col[3].split('/')
          month_index = int(date[1]) - 1

          if avg_list2[month_index] == 0:
            avg_list2[month_index]=int(col[4])
          else:
            avg_list2[month_index]+=int(col[4])
          count_for_avg_list2[month_index]+=1

    i=0
    for avg in avg_list1:
      if avg != 0:
        avg_list1[i]/=count_for_avg_list1[i]
        avg_list1[i] = round(avg_list1[i], 4)
      i+=1

    i=0
    for avg in avg_list2:
      if avg != 0:
        avg_list2[i]/=count_for_avg_list2[i]
        avg_list2[i] = round(avg_list2[i], 4)
      i+=1

  with open(csvfile, 'r') as f:
    for line in f:
      col = line.split(",")
      current_country = col[2].lower()
      if current_country == first_country:
        date = col[3].split('/')
        month_index = int(date[1]) - 1

        std_dev_list1[month_index] += (int(col[4]) - avg_list1[month_index])**2

    i=0
    for std in std_dev_list1:
      if std != 0 and count_for_avg_list1[i]!=0:
        std_dev_list1[i] /= count_for_avg_list1[i]
        std_dev_list1[i] = std_dev_list1[i]**0.5
        std_dev_list1[i] = round(std_dev_list1[i], 4)
      i+=1

  with open(csvfile, 'r') as f:
    for line in f:
      col = line.split(",")
      current_country = col[2].lower()
      if current_country == second_country:
        date = col[3].split('/')
        month_index = int(date[1]) - 1

        std_dev_list2[month_index] += (int(col[4]) - avg_list2[month_index])**2

    i=0
    for std in std_dev_list2:
      if std != 0 and count_for_avg_list2[i]!=0:
        std_dev_list2[i] /= count_for_avg_list2[i]
        std_dev_list2[i] = std_dev_list2[i]**0.5
        std_dev_list2[i] = round(std_dev_list2[i], 4)
      i+=1

  return avg_list1, avg_list2, std_dev_list1, std_dev_list2

def cor_calculation(csvfile, first_country, second_country, base_list1, base_list2):
  avg_x = 0
  avg_y = 0
  count_for_avg1 = 0
  count_for_avg2 = 0
  numerator = 0
  sqrt_term1 = 0
  sqrt_term2 = 0
  denominator = 0
  correlation_answer = 0

  i=0
  for x in base_list1:
    if base_list1[i]!=0 or 1==1:
      avg_x += base_list1[i]
      count_for_avg1+=1
    i+=1
  avg_x = avg_x / count_for_avg1

  i=0
  for x in base_list2:
    if base_list2[i]!=0 or 1==1:
      avg_y += base_list2[i]
      count_for_avg2+=1
    i+=1
  avg_y = avg_y / count_for_avg2

  cor_term1 = [0] * 12
  cor_term2 = [0] * 12

  with open(csvfile, 'r') as f:
    for line in f:
      col = line.split(",")
      current_country = col[2].lower()
      if current_country == first_country:
        date = col[3].split('/')
        month_index = int(date[1]) - 1
        cor_term1[month_index] = base_list1[month_index] - avg_x
      elif current_country == second_country:
        date = col[3].split('/')
        month_index = int(date[1]) - 1
        cor_term2[month_index] = base_list2[month_index] - avg_y

    cor_term1[1] = base_list1[1] - avg_x
    cor_term2[1] = base_list2[1] - avg_y

    i=0
    for x in cor_term1:
      if cor_term1[i] == 0:
        numerator += cor_term2[i]
      elif cor_term2[i] == 0:
        numerator += cor_term1[i]
      else:
        numerator += cor_term1[i]*cor_term2[i] 
      sqrt_term1 += (cor_term1[i])**2
      sqrt_term2 += (cor_term2[i])**2
      i+=1
    
    sqrt_term1 = sqrt_term1**0.5
    sqrt_term2 = sqrt_term2**0.5
    denominator = (sqrt_term1 * sqrt_term2)
    if denominator!=0:
      correlation_answer = numerator/denominator
    correlation_answer = round(correlation_answer, 4)

    print(correlation_answer)

def correlation(csvfile, country):
  country = country[1:-1]
  country = country.split(',')
  first_country = country[0].lower()
  second_country = country[1].lower()

  print("Min:")
  base_list1, base_list2 = baselistmin(csvfile, first_country, second_country)
  cor_calculation(csvfile, first_country, second_country, base_list1, base_list2)

  print("\nMax:")
  base_list1, base_list2 = baselistmax(csvfile, first_country, second_country)
  cor_calculation(csvfile, first_country, second_country, base_list1, base_list2)
  
  print("\nAvg:")
  base_list1, base_list2, std_list1, std_list2 = baselistavgstd(csvfile, first_country, second_country)
  cor_calculation(csvfile, first_country, second_country, base_list1, base_list2)
  print("\nStd:")
  cor_calculation(csvfile, first_country, second_country, std_list1, std_list2)

def main(csvfile, country, type):
  if type == 'statistics':
    print("\nSTATISTICS\n")
    statistics(csvfile, country)
  
  elif type == 'correlation':
    print("\nCORRELATION\n")
    correlation(csvfile, country)

  return 1,2,3,4

mn1, mx1, avg1, std1 = main(sys.argv[1], sys.argv[2], sys.argv[3])