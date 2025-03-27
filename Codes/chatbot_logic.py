import pandas as pd

# Load the dataset
career_data = pd.read_csv("career_data.csv")

def chatbot_response(user_query):
    """Searches for a career in the dataset and returns insights."""
    user_query = user_query.lower()
    
    # Search for a matching career in the dataset
    for index, row in career_data.iterrows():
        if row["Profession"].lower() in user_query:
            response = f"### {row['Profession']}\n\n"
            response += f"**Description:** {row['Description']}\n\n"
            response += f"**Skills Required:** {row['Skills']}\n\n"
            response += f"**Certifications:** {row['Certifications']}\n\n"
            response += f"**Salary Range:** {row['Salary']}\n\n"
            response += "**Free Courses:**\n"
            
            courses = row["Free Courses"].split(";")  # Assume courses are separated by semicolons
            for course in courses:
                response += f"- {course.strip()}\n"

            response += f"\n**Job Roles:** {row['Job Roles']}\n\n"
            response += "**Next Steps:**\n"
            
            steps = row["Next Steps"].split(";")  # Assume steps are separated by semicolons
            for step in steps:
                response += f"- {step.strip()}\n"

            return response
    
    return "❌ Sorry, I only provide career-related insights. Try asking about a profession!"
