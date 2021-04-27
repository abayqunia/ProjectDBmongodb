import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(" Program Demo Operasi CRUD Mongo Database ")
print("       Achmad Bayquni Alfarisi           ")
print("       (19/447309/SV/17003) ARM 1           ")
print("===========================================\n")
def main() :
    print("Menu operasi database")
    print("1. Create Collection ")
    print("2. Insert data")
    print("3. Select/search data")
    print("4. Update data")
    print("5. Delete data")
    menu=input("Silahkan pilih operasi ( 1 / 2 / 3 / 4 / 5 ) = ")
    print("Anda memilih : " + menu)

    if menu=='1' :
        print("Create Collection")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["jasa"]
        mylist = [
        { "_id": 1, "nama": "cuci motor", "harga": "10000"},
        { "_id": 2, "nama": "ganti oli", "harga": "25000"},
        ]
        x = mycol.insert_many(mylist)
        #print list of the _id values of the inserted documents:
        print(x1.inserted_ids)
    elif menu=='2' :
        print("Insert data")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["jasa"]
        mydict = { "_id":3, "nama": "pasang lampu", "harga": "15000" }
        x = mycol.insert_one(mydict)
    elif menu=='3' :
        print("Select/search data")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["jasa"]
        myquery = { "nama": "pasang lampu" }
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)
    elif menu=='4' :
        print("Update data")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["jasa"]
        myquery = { "nama": "pasang lampu" }
        newvalues = { "$set": { "nama": "bongkar" } }
        mycol.update_one(myquery, newvalues)
        #print "customers" after the update:
        for x in mycol.find():
            print(x)
    elif menu=='5' :
        print("Delete data")
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["jasa"]
        myquery = { "nama": "bongkar" }
        mycol.delete_one(myquery)
    else :
        print("Perintah Yang Dimasukkan Salah")

    lagi=input("\nApakah Anda Ingin Melanjutkan Program (Y/T) = ")
    if lagi.lower() == "y" :
        main ()
    else :
        print("Program selesai")
    
main()