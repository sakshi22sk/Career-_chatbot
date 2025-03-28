function askQuestion() {
    let userInput = document.getElementById("user-input").value;
    let responseElement = document.getElementById("response");

    if (userInput.toLowerCase().includes("data analyst")) {
        responseElement.innerHTML = "To become a Data Analyst, learn SQL, Python, Excel, and statistics.";
    } else if (userInput.toLowerCase().includes("ai engineer")) {
        responseElement.innerHTML = "AI Engineers need strong Python, ML, and AI model-building skills.";
    } else {
        responseElement.innerHTML = "I'm still learning! Try asking about Data Analyst or AI Engineer.";
    }
}
