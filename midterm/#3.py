outfile = open("Coffee.txt", 'a')
brand = input("\nEnter favorite coffee brand: ")
outfile.write(f"\n{brand},99-8888,9.88")
outfile.close()
infile = open("Coffee.txt", 'r')
content = infile.read()
infile.close()
print(content)