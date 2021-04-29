import random, datetime, os, pickle, shutil

def New_Document():
  LUD = 1 # LAST UNIQUE DIGIT
  unique = []
  date = datetime.date.today()
  unique.append(date)
  unique_id = str(unique[0])
  unique_id = unique_id.replace('-', '')
  unique_id = unique_id + str(LUD)

  
  folder = r'E:\\Programming related\\DATASAVER\\DATA'
  filenames = list(os.listdir(folder))
  print(filenames)
  

  file = len(filenames)

  for i in range(file):
    
    if unique_id == filenames[i]:
        LUD += file 
        unique_id = unique_id + str(LUD)
        break
    else:
        continue
     

  print(f"Your  unique id is: {unique_id}")
  data = open('E:\\Programming related\\DATASAVER\\DATA\\' + unique_id, 'w')
  name =input("Name: ")
  age = input("Age: ")
  dis = input("Disease: ")
  ward = input("Ward no: ")

  with data as d:
    d.write(f"Name: {name}\n")
    d.write(f"Age: {age}\n")
    d.write(f"Disease: {dis}\n")
    d.write(f"Ward: {ward}\n")




  
print("Please choose a NUMBER:")
print("1: New Document")
print("2: Existing Document")
while True:
    try:
        ask = int(input("Please enter a NUMBER: "))
        if ask == 1:
          break
        elif ask == 2:
            break
        else:
            print("Please enter '1' OR '2'")
            continue
    except:
        print("Please enter '1' OR '2' NOT a WORD")

if ask == 1:
    New_Document()
else:
    pass
