from table import data, fields, add_record, amend_record, delete_record, print_table, display_full_details

def menu():
    print("\n------------- Main Menu -------------")
    print("1. Add Record")
    print("2. Amend Record")
    print("3. Delete Record")
    print("4. Display Full Details")

while True:
    print_table(fields, data)
    menu()
    try:
        selected = int(input("Choose a menu option (1-4):   "))

        if selected == 1:
            add_record(fields,data)

        elif selected == 2:
            amend_record(fields,data)
        elif selected == 3:
            delete_record(fields,data)
        elif selected == 4:
            display_full_details(fields, data)
        elif selected == 5:
            print("Exiting... ")
            break
        #Range check
        else:
            print("Error. Please enter a valid menu option (1-5).")
    except ValueError:
        print("Error. Please enter a valid menu option (1-5).")
        