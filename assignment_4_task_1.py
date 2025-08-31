try:
    a=open("sample.txt","r")
    b=a.read()
    print("Reading File content")
    c=b.split("\n")
    for i in c:
        print(i)
        a.close()
except:
    print("Error:The file","sample.txt","was not found.")
finally:
    print()
