a=open("output.txt","w")
b=a.write(input("Enter text to write to the file: "))
print("Data successfully written to","output.txt.\n")
a.close()

a=open("output.txt","a")
b=a.write("\n")
b=a.write(input("Enter additional text to append: "))
print("Data successfully appended.\n")
a.close()

a=open("output.txt","r")
b=a.read()
print("Final content of","output.txt")
c=b.split("\n")
for i in c:
    print(i)
a.close()
