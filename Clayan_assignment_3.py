# Student: Clayan Ariaga
# File: clayan_assignment_3.py
# Description: PERSONAL ACADEMIC & LIFE PORTFOLIO
# Requirements:
# - Uses strings, lists, tuples, sets, dictionaries
# - Demonstrates list indexing, tuple indexing, dictionary key access, set creation
# - Includes descriptive variable names and professional f-string formatting
# - Updated with realistic personal info for Git workflow Part 2

print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student: Clayan Ariaga | Email: cariaga@ncat.edu")
print("From: Raleigh, NC | Graduating: Spring 2025")
print("Major: Software Engineering")
print("")

# ================= ACADEMIC PROFILE =================
print("=== ACADEMIC PROFILE ===")
current_courses = ["COMP 163", "MATH 150", "ENG 102", "HIS 210"]  # list of current courses
completed_courses = ["COMP 160", "MATH 140", "ENG 101", "HIS 105"]  # list of completed courses
credit_hours = (3, 4, 3, 3)  # tuple of credit hours per course
professors = {  # dictionary mapping courses to instructors
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 102": "Dr. Martinez",
    "HIS 210": "Dr. Brown"
}
locations = {  # dictionary mapping courses to classrooms
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 102": "Crosby 121",
    "HIS 210": "Crosby 210"
}

print(f"Current Semester Courses:")
print(f"{current_courses[0]} - {credit_hours[0]} credits - {professors['COMP 163']} - {locations['COMP 163']}")
print(f"{current_courses[1]} - {credit_hours[1]} credits - {professors['MATH 150']} - {locations['MATH 150']}")
print(f"{current_courses[2]} - {credit_hours[2]} credits - {professors['ENG 102']} - {locations['ENG 102']}")
print(f"{current_courses[3]} - {credit_hours[3]} credits - {professors['HIS 210']} - {locations['HIS 210']}")
print("")

# Extra academic calculations
total_credits = sum(credit_hours)  # sum of credits
num_courses = len(current_courses)  # number of courses
weekly_study_hours = 25
semester_study_hours = weekly_study_hours * 16  # total study hours in a semester

print(f"Total Credits this Semester: {total_credits}")
print(f"Number of Courses: {num_courses}")
print(f"Total Study Hours for Semester: {semester_study_hours}")
print("")

# ================= PERSONAL DEVELOPMENT =================
print("=== PERSONAL DEVELOPMENT ===")
current_skills = {"Time Management", "Python Basics", "Photography", "Football", "Problem Solving"}  # set
learning_goals = {"Data Structures", "Web Design", "JavaScript", "Git", "Public Speaking"}  # set
career_interests = {"Software Development", "Game Development", "Web Development", "Data Science"}  # set

print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {learning_goals}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(learning_goals)}")
print("")

# ================= FINANCIAL OVERVIEW =================
print("=== FINANCIAL OVERVIEW ===")
monthly_budget = {
    "monthly_budget": 900,
    "food": 400,
    "entertainment": 200,
    "books": 150,
    "transportation": 100,
    "annual_projection": 10800
}

# daily food cost calculation
daily_food_budget = round(monthly_budget["food"] / 30, 2)

print(f"Monthly Budget: ${monthly_budget['monthly_budget']}")
print(f"Food: ${monthly_budget['food']} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget['entertainment']}")
print(f"Books: ${monthly_budget['books']}")
print(f"Transportation: ${monthly_budget['transportation']}")
print(f"Annual Projection: ${monthly_budget['annual_projection']}")
print("")

# ================= CONNECTIONS & CONTACTS =================
print("=== CONNECTIONS & CONTACTS ===")
print("Emergency Contact: Hannah Ariaga (Mom) - 919-555-1234")
print("Home Address: 789 Pine Street, Raleigh, NC 27606")
print("Social Media Presence: 500 followers across 2 platforms")
print("Key Contacts: 5 people in directory")
print("")

# ================= LIFE STATISTICS =================
print("=== LIFE STATISTICS ===")
print("Total Courses Completed: 8")
print("Current Academic Load: 37 weekly commitments")
print("Entertainment Backlog: 4 items")
print("Current Hobbies: 5 activities")
print("================================================================")