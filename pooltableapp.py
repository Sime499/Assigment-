from datetime import datetime
datetime=datetime.now()
current_time=datetime



tables=[]

class Table:
    def __init__(self, number):
       self.number = number
       self.occupied = False
       self.start_time = None
       self.end_time = None
       self.time_played = None
       self.current_time = None

    def checkout(self):
      self.occupied=True
      self.start_time=datetime.now()
      print(f"You checkout Table {self.number} {self.occupied} {self.start_time.strftime('%m/%d/%Y %H:%M%:%S')}")


    def checkin(self):
        self.occupied=False
        self.start_time=None
        self.end_time=None
        self.time_played=self.end_time-self.start_time
        print(f"Table Closed  Table {self.number} {self.occupied} {self.start_time.strftime('%m/%d/%Y %H:%M%:%S')}")

class ActivityLog():
    def __init__(self, date):
        self.date = date
        self.entry_list = []

    def create_entry(self, table, start, end, total_time):
        start_start = formatter.date_format(start)
        end_time = formatter.date_format(end)
        played_time = formatter.timer_format(end, start)
        cost = formatter.cost_calc(end, start)
        entry = {"Table Number": table, "Start Time": start_time,
            "End Time": end_time, "Total Time Played": f_total_time, "Cost": cost
        }
        self.entry_list.append(entry)
        return self.entry_list

    def cost_calc(self, end, start):
        delta_time =self.end_time - self.start_time
        delta_min = delta_time.now()
        cost = f"${(hours * 30.00) + (minutes * 0.50)}"
        return cost

        
      
def display_tables():
    
    for table in tables:


        print(f"\n Table--{table.number} current_time--{current_time.strftime('%m/%d/%Y %H:%M%:%S')}  status--{table.occupied} ")
        
        
        
        



    
for i in range (1,13):
  table=Table(i)
  tables.append(table)
  
  
print(f" \n----UNIVERSITY OF TEXAS POOL TABLE MANAGMANT--------\n")
print("TO CHECKOUT Table: Enter 1: ")
print("TO CHECKIN Table: Enter  2: ")
print("TO VIEW ALL Table: enter 3: ")
print("To QUIT the app:enter 'q': ")
print("******************************************************")

while True:

    choice=input("please select your choice from the menu:")
    print("*******************PoolTable List**************")

    try:
        if choice== "1":


            display_tables()
            table_number=int(input("Enter table Number to check-out:"))
            table=tables[table_number-1]
            table.time_start=None
            table.checkout()

        elif choice=="2":
            display_tables()
            table_number=int(input("Enter Checkin Number:"))
            table=tables[table_number-1]
            table_end_time=None
            cost = formatter.cost_calc(end, start)
            entry = {"Table Number": table, "Start Time": start_time,
            "End Time": end_time, "Total Time Played": f_total_time, "Cost": cost }
            print("entry")
        
            print(f"Table {table.number} has been closed out at: {self.end_time.strftime('%m/%d/%Y %H:%M%:%S')}")



        elif choice=="3":
            for table in tables:
                print(f"Table No1--{table.number}-- current_time--{current_time.strftime('%m/%d/%Y %H:%M%:%S')}--status--{table.occupied}")

        elif choice=="q":
            break

        else: 

             print("Thank you for using our shop!!")

    except IndexError:
        print("please select with in 1 and 12 range")

      
   