from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import gridfs

# Connect
client = MongoClient("mongodb://localhost:27017")
db = client["studentdb"]
collection = db["students"]

# Setup GridFs
# fs = gridfs.GridFS(db)

def get_all_students():
    return list(collection.find())

def get_student_by_id(student_id):
    return collection.find_one({"_id": ObjectId(student_id)})

def add_student(data):
    data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Received data:", data)
    return collection.insert_one(data)

def delete_student(student_id):
    return collection.delete_one({"_id": ObjectId(student_id)})

def update_student(student_id, data):
    print("data", data)
    return collection.update_one({"_id": ObjectId(student_id)}, {"$set": data})

# def update_student(student_id, data, new_image_file =None):
#     student = get_student_by_id(student_id)
#     if new_image_file:
#         if student and student.get("image_id"):
#             try:
#                 fs.delete(ObjectId(student["image_id"]))
#             except:
#                 pass
#         #Upload new image
#         new_image_id = fs.put(new_image_file, filename=new_image_file.filename, content_type= new_image_file.content_type)
#         data["image_id"] = str(new_image_id)
#     return collection.update_one({"_id": ObjectId(student_id)}, {"$set": data})