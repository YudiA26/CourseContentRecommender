from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def recommend(self, videos, course_name, competencies):
        if not videos:
            return []

        # Prepare the data for TF-IDF
        video_descriptions = [video['description'] for video in videos]
        descriptions = [course_name + " " + " ".join(competencies)] + video_descriptions
        
        # Fit and transform the descriptions
        tfidf_matrix = self.vectorizer.fit_transform(descriptions)
        
        # Compute the cosine similarity
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
        
        # Get the scores
        similarity_scores = cosine_sim[0]
        
        # Pair the scores with the videos
        scored_videos = [(score, video) for score, video in zip(similarity_scores, videos)]
        
        # Sort videos based on the score
        scored_videos.sort(key=lambda x: x[0], reverse=True)
        
        # Return the top N recommended videos
        recommended_videos = [video for _, video in scored_videos[:5]]  # Adjust the number as needed
        return recommended_videos
