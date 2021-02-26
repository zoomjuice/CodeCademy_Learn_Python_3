# Define create_spreadsheet()
# Setting a variable in the function definition creates a default value if no value is given

def create_spreadsheet(title, row_count=1000):
    print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows.")


# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Applications", 10)
