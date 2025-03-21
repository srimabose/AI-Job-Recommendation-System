function getRecommendations() {
    let skills = document.getElementById("skills").value;
    
    fetch("http://127.0.0.1:5000/recommend", {  // Ensure correct backend URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "skills": skills })
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById("results");
        resultDiv.innerHTML = "<h2>Recommended Jobs:</h2>";
        
        if (data.jobs && data.jobs.length > 0) {
            data.jobs.forEach(job => {
                resultDiv.innerHTML += `<p>${job}</p>`;
            });
        } else {
            resultDiv.innerHTML += "<p>No job recommendations found.</p>";
        }
    })
    .catch(error => console.error("Error:", error));
}
