import json

try:
    dictionary ={}
    with open("C:/Users/User/Desktop/html/python/Text1.txt","r") as f:
        for line in f.read().splitlines():
            a,b=line.split(" ")
            try:
                if type(int(b)) == int: 
                    dictionary[a]=int(b)
            except ValueError:
                if b== 'True' or b == 'False' :
                    dictionary[a]=bool(b)
                else:
                    dictionary[a]=b

    print (dictionary)
    writer=open("C:/Users/User/Desktop/html/python/data.json","a")
    print("Started writting\n")
    json.dump(dictionary,writer,indent=4,sort_keys=True)
    print("Continue writting\n")
    writer.close()
    print("Stoped writting")
except IOError as e:
    print("File Not Found : ",e)