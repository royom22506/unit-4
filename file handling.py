def write_file(filename, content):
    with open(filename,'w') as file:
        file.write(content)
        print("data written to file successfully.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("file content:")
            print(content)

    except FileNotFoundError:
        print("file not found")

def append_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
        print("data appended to a file successfully")

def main():
    filename = "example_file.txt"

    write_file(filename, "hello, this is the first line.\n")
    read_file(filename)
    append_file(filename, "this is an appended line.\n")
    read_file(filename)

    if __name__=="__main__":
        main()
