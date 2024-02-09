import csv

csv_file = open('/content/find_the_link.csv',encoding='UTF-8')
data = csv.reader(csv_file)
link = ""
data_lines = list(data)
for i in range(len(data_lines)):
  for j in range(len(data_lines[0])):
    if i == j:
      link+=data_lines[i][j]
  
print(link)