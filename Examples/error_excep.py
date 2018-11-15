def file_open():
    print("Enter file name")
    try:
        file = open(input(),"r")
    except:
        print("File not found")
        file = file_open()
    return file

file = file_open()
print("Thank You")