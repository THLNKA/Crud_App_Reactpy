from pymongo import MongoClient
uri = "mongodb+srv://dbAdmin:admin123@cluster0.fxc6wqc.mongodb.net/"
client = MongoClient(uri)


# Replace <database-name> with the name of your database
db = client["ReactPyApp"]
# Replace <collection-name> with the name of your collection
collection = db["ReactPyApp"]

try:
 client.admin.command("ping")
 print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
 print(e)


document = {"name": "John", "age": 30}
# Insert the document into the collection
insert_result = collection.insert_one(document)
# Print the ID of the inserted document
print("Inserted Document ID:", insert_result.inserted_id)

def login(
 login_data: dict,
):
 username = login_data["name"]
 password = login_data["password"]
 # Create a document to insert into the collection
 document = {"name": username, "password": password}
 # logger.info('sample log message')
 print(document)
 # Insert the document into the collection
 post_id = collection.insert_one(document).inserted_id
 print(post_id)
 return {"message": "Login successful"}