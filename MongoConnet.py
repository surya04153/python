
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://surya04153:MongoLearning123@mongocluster.7zkgi.mongodb.net/?retryWrites=true&w=majority&appName=MongoCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # Select a database
    db = client['sample_mflix']

    # Select a collection
    collection = db['movies']

    # Fetch all documents from the collection
    documents = collection.find({"title":"The Great Train Robbery"})

    # Loop through and print each document
    for document in documents:
        print(document)

    # Close the connection
    client.close()
except Exception as e:
    print(e)