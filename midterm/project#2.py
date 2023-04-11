def read_coffee():
    infile=open("coffee.txt",'r')
    content=infile.read()
    infile.close()
    print(content)
read_coffee()