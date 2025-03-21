from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

@app.route('/recommend', methods=['POST'])
def recommend_jobs():
    data = request.get_json()
    skills = data.get("skills", "")

    # Dummy job recommendation based on skills
    job_recommendations = {
        "python": ["Python Developer", "Data Scientist"],
        "machine learning": ["ML Engineer", "AI Researcher"],
    }

    recommended_jobs = []
    for skill in skills.split(","):
        skill = skill.strip().lower()
        if skill in job_recommendations:
            recommended_jobs.extend(job_recommendations[skill])

    return jsonify({"jobs": list(set(recommended_jobs))})

if __name__ == '__main__':
    app.run(debug=True)
