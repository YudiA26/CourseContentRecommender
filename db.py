from pymongo import MongoClient

def get_db_connection():
    client = MongoClient('mongodb://your_mongo_db_uri')
    return client['your_database_name']

def fetch_videos(course_name, competencies):
    db = get_db_connection()
    collection = db['videos_collection']
    
    query = {
        'course_name': course_name,
        'competencies': {'$in': competencies}
    }
    
    videos = list(collection.find(query))
    return videos
