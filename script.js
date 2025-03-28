const careerKeywords = ["job", "career", "salary", "skills", "internship", "promotion",
    "certification", "resume", "hiring", "recruitment", "freelance"];

function isCareerRelated(question) {
return careerKeywords.some(keyword => question.toLowerCase().includes(keyword));
}

async function getCareerAdvice(question) {
if (!isCareerRelated(question)) {
return "❌ Sorry, I can only provide career-related insights.";
}

let response = await fetch(`https://api.example.com/career?query=${question}`);
let data = await response.json();
return data.answer || "No relevant career data found.";
}

document.getElementById("askBtn").addEventListener("click", async function() {
let question = document.getElementById("userInput").value;
let responseText = await getCareerAdvice(question);
document.getElementById("chatbotResponse").innerText = responseText;
});
