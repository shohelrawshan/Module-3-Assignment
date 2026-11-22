print("Hi! Welcome to Employee Salary Management System!")


# ==================================================
# Function 1: Add Employee
# ==================================================

def add_employee(name, emp_id, salary):
    """Save employee information into the text file."""

    file = open("employees.txt", "a")

    file.write(f"{name} | {emp_id} | {salary}\n")

    file.close()

    return "Employee Added Successfully!"


# ==================================================
# Function 2: View Employees
# ==================================================

def view_employees():
    """Read and display all employee records."""

    try:
        file = open("employees.txt", "r")

        data = file.read()

        file.close()

        if data == "":
            print("No employee records found.")
        else:
            print("\n----- Employee Records -----")
            print(data)

    except FileNotFoundError:
        print("No employee records found.")


# ==================================================
# Main Program
# ==================================================

def main():
    """Run the Employee Salary Management System."""

    while True:

        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")

        choice = input("\nChoose Option: ")

        if choice == "1":

            name = input("Enter Name: ")
            emp_id = input("Enter ID: ")
            salary = input("Enter Salary: ")

            result = add_employee(name, emp_id, salary)

            print(result)

        elif choice == "2":

            view_employees()

        elif choice == "3":

            print("Done! Thanks for using this application!")
            break

        else:

            print("Invalid option! Please choose 1, 2 or 3.")


# Start Program

if __name__ == "__main__":
    main()
