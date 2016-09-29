habla = input("Habla: ")

if habla.endswith("?"):
    print ("Ofi")
elif habla.isupper():
    print ("Chilea")
elif not habla:
    print ("Mmm...")
else:
    print ("Me da igual")
