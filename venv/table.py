from rich.console import Console
from rich.table import Table
import datetime

# Hard coded data
data = [
    [100, "VACCINES", "NHS", datetime.date(2020,8,13), datetime.date(2022,10,7), 437, "UK", 3],
    [101, "FASTFOOD APP", "PFC", datetime.date(2023,12,1), datetime.date(2024,12,1), 931, "USA", 1],
    [102, "HYDROGEN X", "NESTLE", datetime.date(2019,3,30), datetime.date(2023,10,18), 125, "NEW ZEALAND", 3],
    [103, "PEN PROGRAMME", "BIC", datetime.date(2024,4,6), datetime.date(2024,6,6), 740, "SWEDEN", 0],
    [104, "REUSABLE PAPER", "UNILEVER", datetime.date(2018,1,1), datetime.date(2024,1,1), 864, "SAUDI ARABIA", 3],
    [105, "APP RESEARCH", "LEXUS", datetime.date(2024,2,11), datetime.date(2024,10,30), 535, "JAPAN", 1],
    [106, "REWARDS APP", "COSTA", datetime.date(2023,8,1), datetime.date(2024,12,7), 437, "SPAIN", 1],
    [107, "FASTER LOGIN", "EVENTBRITE", datetime.date(2023,7,7), datetime.date(2024,7,7), 252, "UAE", 2],
    [108, "REDEVELOPMENT", "COUNCIL", datetime.date(2024,12,8), datetime.date(2025,12,8), 437, "UK", 0],
    [109, "TRANSPORT APP", "TFL", datetime.date(2022,2,27), datetime.date(2024,10,7), 105, "UK", 2],
]
fields = ["PROJECT ID", "PROJECT NAME", "CLIENT", "START DATE", "END DATE", "CONSULTANT ID", "COUNTRY", "STATUS"]


from rich.console import Console
from rich.table import Table
import datetime

#Using Rich to format table
def print_table(fields, data):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    for field in fields:
        table.add_column(field)

    for row in data:
        table.add_row(*map(str, row))

    console.print(table)
    

#Function to add record, data validation to check valid datatype is inputted by user.
def add_record(fields, data):
    new_record = []

#Project ID is the Primary Key and therefore cannot be duplicated.
    while len(new_record)<=1:
        try:
            new_projectid = int(input("\nWhat is the Project ID of the record you would like to add:   "))
            duplicate = any(new_projectid == row[0] for row in data)

            if duplicate:
                print("\nProject ID already taken")
            else:
                new_record.append(new_projectid)
                break  # Breaks the loop if the project ID is not taken.

        except ValueError:
            print("\nError: Project ID must be a number")   

#Project name can be int or str.
    while len(new_record)<2:
        new_projectname= input("\nWhat is the Project name of the record you would like to add:   ")
        new_record.append(new_projectname)

#Client can be int or str.
    while len(new_record)<3:
        new_client= input("\nWho is the Client of the record you would like to add:   ")
        new_record.append(new_client)

#Checking start date is in datetime format.
    while len(new_record)<4:    
        try:
            new_startdate= input("\nWhat is the Start Date of the record you would like to add:   ")
            new_record.append(new_startdate)
            datetime.datetime.strptime(new_record[3],"%Y-%m-%d").date()
        except ValueError:
            print("\nError: Start Date should be in the format YYYY-MM-DD.")
            new_record.pop(-1)

            
#Checking enddate is in datetime format and is after start date.
    while len(new_record)<5:
        try:
            new_enddate= input("\nWhat is the End Date of the record you would like to add:   ")
            if new_enddate<new_startdate: 
                print(f"\nEnd date cannot be before {new_startdate}")
            else:
                new_record.append(new_enddate)
                datetime.datetime.strptime(new_record[4],"%Y-%m-%d").date()
        except ValueError:
            print("\nError: End Date should be in the format YYYY-MM-DD.")
            new_record.pop(-1)

#Checking consultant ID is a number.
    while len(new_record)<6:    
        try:
            new_consultantid= int(input("\nWhat is the Consultant ID of the record you would like to add:   "))
            new_record.append(new_consultantid)
        except ValueError:
            print("\nError: Consultant ID must be a number")
             

# Checking country is a string.
    while len(new_record)<7:    
        new_country = input("\nWhat is the Country of the record you would like to add:   ")
        try:
            int(new_country)
            print ("\nError: Country must be a string")
        except ValueError:
            new_record.append(new_country)
 
#Checking project status is an integer between 0-3.
    while len(new_record)<8:    
        try:
            new_projectstatus= int(input("\nWhat is the Project Status of the record you would like to add (/3):   "))
            if 0<=new_projectstatus<4:
                new_record.append(new_projectstatus)
            else:
                print ("\nError: Project Status must be a number 0-3")
        except ValueError:
            print ("\nError: Project Status must be a number 0-3")
    
    data.append(new_record)
    print("The new record has been added succesfully.")
    return(fields,data)
         




#Deletes record from the table  
def delete_record(fields,data):
#Checking Project ID is an integer
    record_deleted = False
    while record_deleted == False:
        try:
            project_id_to_delete = int(input("\nEnter the Project ID of the record you would like to delete:   "))
        except ValueError:
            print("\nError: Project ID must be an integer")  
        else:
            #finding project id within data
            record_index = -1
            for i, record in enumerate(data):
                if record[0] == project_id_to_delete:
                    record_index = i
                    break
            if record_index == -1:
                print("\nRecord not found.")
            else:
                del data[record_index]
                print(f"\nRecord with Project ID {project_id_to_delete} deleted successfully.")
                record_deleted = True
        return(fields,data)
        



#Amends record in the table  
def amend_record(fields, data):
    valid_id = False
    #Making sure Project ID is an integer
    while valid_id == False:
        try:
            id_to_amend = int(input("\nEnter the Project ID of the project you want to amend: "))
            valid_id = True
        except ValueError:
            print("\nError: Project ID must be a number")
        else:
            #Making sure Project ID exists
            record_index = -1
            for i, record in enumerate(data):
                if record[0] == id_to_amend:
                    record_index = i
                    break

            if record_index == -1:
                print("\nRecord not found.")
                valid_id = False
    
    
    #Finding which field is to be amended for the specified record
    valid_field = False
    while valid_field == False:
        field_to_amend = input("\nWhich field would you like to amend? ").upper()
        if field_to_amend not in fields:
            print(f"\nField {field_to_amend} does not exist")
        else:
            valid_field = True

    
    #Project ID must be an int
    if field_to_amend == "PROJECT ID":
        while True:
            try:
                new_projectid = int(input(f"\nEnter the new data for {field_to_amend}: "))
            except ValueError:
                print("\nError: Project ID must be a number")  
            else:
                duplicate = any(new_projectid == row[0] for row in data)
                if duplicate:
                    print("\nError: Project ID already taken")
                else:
                    data[record_index][fields.index(field_to_amend)] = new_projectid
                    break

    #Start date must be in datetime format and before end date.
    elif field_to_amend == "START DATE":
        while True:
            try:
                new_startdate = input(f"\nEnter the new record for {field_to_amend} (YYYY-MM-DD): ")
                start_date = datetime.datetime.strptime(new_startdate, "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(str(data[record_index][fields.index("END DATE")]), "%Y-%m-%d").date()
                if start_date <= end_date:
                    data[record_index][fields.index(field_to_amend)] = start_date
                    break
                else:
                    print(f"\nStart date cannot be after {data[record_index][fields.index('END DATE')]}")
            except ValueError:
                print("\nError: Start Date should be in the format YYYY-MM-DD.")
        
    #End date must be in datetime format and after start date.
    elif field_to_amend == "END DATE":
        while True:
            try:
                new_enddate = input(f"\nEnter the new record for {field_to_amend} (YYYY-MM-DD): ")
                end_date = datetime.datetime.strptime(new_enddate, "%Y-%m-%d").date()
                start_date = datetime.datetime.strptime(str(data[record_index][fields.index("START DATE")]), "%Y-%m-%d").date()
                if end_date < start_date:
                    print(f"\nEnd date cannot be before {data[record_index][fields.index('START DATE')]}")
                else:
                    data[record_index][fields.index(field_to_amend)] = end_date
                    break
            except ValueError:
                print("\nError: End Date should be in the format YYYY-MM-DD.") 
            

    #Project name and client can be int or str.
    elif field_to_amend in ["PROJECT NAME", "CLIENT"]:
        new_PNC = input(f"\nEnter the new record for {field_to_amend}: ").upper()
        data[record_index][fields.index(field_to_amend)] = new_PNC

    #Country must be a string.
    elif field_to_amend == "COUNTRY":
        while True:
            new_country = input("\nEnter the new record for country: ").upper()
            try:
                int(new_country)
                print ("\nError: Country must be a string")
                
            except ValueError:
                new_country = data[record_index][fields.index(field_to_amend)]
                break
            
    #Consultant ID must be an integer.                  
    elif field_to_amend == "CONSULTANT ID":
        while True:
            try:
                new_consultant_id = int(input("\nEnter the new record for Consultant ID: "))
                data[record_index][fields.index(field_to_amend)] = new_consultant_id
                break
            except TypeError:
                print("\nError: Consultant ID must be a number")


    #Project status must be an integer between 0-3.           
    elif field_to_amend == "STATUS":
        while True:
            try:
                new_projectstatus = int(input("\nEnter the new record for Status: "))
                if 0<=new_projectstatus<4:
                    data[record_index][fields.index(field_to_amend)] = new_projectstatus
                    break
                else:
                    print ("\nError: Project Status must be a number 0-3")
            except ValueError:
                    print ("\nError: Project Status must be a number 0-3")
    print("\nRecord amended successfully...")
    return (fields, data)
            
        


#Displays full details for a record from the table based on status 
def display_full_details(fields, data):
    while True:
        try:
            project_id = int(input("\nEnter the Project ID for the record you would like to display details for: "))
            found = False
            for record in data:
                if record[0] == project_id:
                    found = True
                    if record[7] == 0:
                        print("\nThis project has not commenced yet.")
                    elif record[7] == 1:
                        print("\nThis project has commenced. Timeframe and cost have been agreed upon and the team has been assembled.")
                    elif record[7] == 2:
                        print("\nThis project is close to completion and is about to be finalised.")
                    elif record[7] == 3:
                        print("\nThis project is complete.")
            if not found:
                print("\nProject was not found.")
        except ValueError:
            print("\nError: Project ID must be an integer")
            #Notifies user that the entered Project ID does not exist    
                
        choice = input("\nEnter 'Exit' to leave the program or any other key to continue:  ")
        if choice.upper() == "EXIT":
            break
                    
