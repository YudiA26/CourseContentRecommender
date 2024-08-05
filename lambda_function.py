import json
from db import fetch_videos
from recommender import Recommender

def lambda_handler(event, context):
    try:
        course_name = event['course_name']
        competencies = event['competencies']
        
        # Fetch videos from MongoDB
        videos = fetch_videos(course_name, competencies)
        
        # Create an instance of the recommender and get recommendations
        recommender = Recommender()
        recommended_videos = recommender.recommend(videos, course_name, competencies)
        
        return {
            'statusCode': 200,
            'body': json.dumps(recommended_videos)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
