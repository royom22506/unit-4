import csv
def count_rows(csv_filename):
    try:
        with open(your_file.csv,'r', newline=)as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
        print(f"total number of rows: {row_count}")
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print(f"an error occured: {e}")


    
    if __name__=="__main__":
        count_rows(csv_filename)