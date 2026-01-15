import csv

def create_csv():
    with open("users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "email"])   # header
        writer.writerow(["Piyush Mondal", "piyush@gmail.com"])
        writer.writerow(["Neha Verma", "neha@gmail.com"])
        writer.writerow(["Rohit Das", "rohit@gmail.com"])

    print("CSV file created successfully")


create_csv()
