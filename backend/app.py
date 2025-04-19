from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Sample job dataset
jobs_data = pd.DataFrame({
    "job_id": [1, 2, 3, 4, 5],
    "title": ["Data Scientist", "Software Engineer", "AI Engineer", "Business Analyst", "Cybersecurity Analyst"],
    "skills": [
        "python, machine learning, data analysis",
        "java, javascript, react, backend",
        "deep learning, pytorch, tensorflow",
        "sql, excel, data visualization",
        "network security, penetration testing"
    ]
})

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
job_vectors = vectorizer.fit_transform(jobs_data["skills"])

@app.route('/recommend', methods=['POST'])
def recommend_jobs():
    try:
        # Get user input
        user_input = request.json.get("skills", "")
        if not user_input:
            return jsonify({"error": "Skills input is required"}), 400
        
        # Transform user input
        user_vector = vectorizer.transform([user_input])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(user_vector, job_vectors).flatten()
        
        # Get top 3 job recommendations
        top_indices = similarities.argsort()[-3:][::-1]
        recommendations = jobs_data.iloc[top_indices][["job_id", "title"]].to_dict(orient="records")
        
        return jsonify({"recommendations": recommendations})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
