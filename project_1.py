import pandas as pd

# 1. Load the real data
df = pd.read_csv('salaries.csv')

# 2. Filter data (This is a pro skill!)
junior_jobs = df[df['Level'] == 'Junior']

# 3. Calculate Average Salary for Juniors
avg_junior_salary = junior_jobs['Salary_BDT'].mean()

print("--- AI CAREER INSIGHTS (BANGLADESH 2026) ---")
print("Average starting salary for Juniors: ৳" + str(avg_junior_salary))

# 4. Your Logic: The "Career Advice" Function
def career_advice(hours):
    if hours >= 5:
        return "You are on the fast track to a " + str(avg_junior_salary) + " BDT job!"
    else:
        return "At this rate, it might take longer to reach the Junior level."

study_time = float(input("How many hours do you study AI per day? "))
print(career_advice(study_time))