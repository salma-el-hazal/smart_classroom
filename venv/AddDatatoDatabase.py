from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb+srv://developerbadreddine:zt23FgyjykIYOW8J@cluster0.ns7t9lp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['smart_classroom_db']
collection = db['attendance_records']

data = [
    {
        "_id": "321654",
        "name": "Murtaza Hassan",
        "major": "Robotics",
        "starting_year": 2017,
        "total_attendance": 7,
        "standing": "G",
        "year": 4,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    {
        "_id": "852741",
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "B",
        "year": 1,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    {
        "_id": "963852",
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
]

# Insert data into the MongoDB collection
collection.insert_many(data)
