import os
import pickle

class product():
    item_code = 0
    item_name = ""
    item_price = 0.0
    category = ("input","output","storage","process")

def add(new_record):
    file = open("Product.dat","rb")
    temp_file = open("Temp_file.dat","ab")
    temp_record = product()
    file.read()
    eof = file.tell()
    file.seek(0)
    found = False
    while file.tell() != eof:
        temp_record = pickle.load(file)
        if temp_record.item_code > new_record.item_code:
            pickle.dump(new_record,temp_file)
            found = True
        pickle.dump(temp_record,temp_file)
    if found == False:
        pickle.dump(new_record, temp_file)

    file.close()
    temp_file.close()
    os.remove("Product.dat")
    os.rename("Temp_file.dat","Product.dat")
