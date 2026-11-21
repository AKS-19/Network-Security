from pymongo import MongoClient
uri = "mongodb+srv://akshitsahoo1911_db_user:Admin123@cluster0.ie4xdgw.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)