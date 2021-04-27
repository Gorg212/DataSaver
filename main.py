import random, datetime

def New_Document():
  unique = []
  today = datetime.date.today()
  unique.append(today)
  unique_id = str(unique[0])
  unique_id = unique_id.replace('-', '')
  unique_id = unique_id + "1"
  print(f"Your  unique id is: {unique_id}")

# import 
#  # print the date object, not the container ;-)

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
        print("Please '1' OR '2' NOT a WORD")

if ask == 1:
    New_Document()
else:
    pass
