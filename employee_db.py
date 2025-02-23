# employee_db.py

# Function to read employee data from file and store it in a dictionary
def load_employee_data(filename):
    employee_dict = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                emp_id, name = line.strip().split(", ", 1)  # Split only on first comma
                employee_dict[int(emp_id)] = name  # Store in dictionary
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return employee_dict

# Function to display employees sorted by ID
def display_sorted_employees(employee_dict):
    print("\nEmployee List (Sorted by ID):")
    for emp_id in sorted(employee_dict.keys()):
        print(f"ID: {emp_id}, Name: {employee_dict[emp_id]}")

# Function to search for an employee by ID
def search_employee(employee_dict):
    try:
        emp_id = int(input("\nEnter Employee ID to search: "))
        if emp_id in employee_dict:
            print(f"Employee Found - ID: {emp_id}, Name: {employee_dict[emp_id]}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input! Please enter a valid Employee ID.")

# Main Execution
if __name__ == "__main__":
    emp_data_file = "emp_data.txt"
    employees = load_employee_data(emp_data_file)  # Load employees

    if employees:  # Only proceed if data was loaded
        display_sorted_employees(employees)  # Display employees
        search_employee(employees)  # Allow user to search for an employee
