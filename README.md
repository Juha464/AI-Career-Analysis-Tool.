# 🧭 AI Career Analysis Tool

A simple Python script that analyzes real AI/tech job salary data for Bangladesh and gives personalized study advice based on how many hours per day you study AI.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

---

## 📋 Overview

This tool reads a dataset of AI/tech job roles, seniority levels, and salaries in Bangladesh, calculates the average starting (Junior-level) salary, and then gives the user interactive career advice based on their daily AI study habits.

## 🎯 Features

- Loads and filters salary data with `pandas`
- Calculates the average salary for Junior-level roles
- Takes interactive user input (daily study hours)
- Returns simple, rule-based career advice based on that input

## 🗂️ Dataset

`salaries.csv` — AI/tech job salaries in Bangladesh (2026):

| Role | Level | Salary (BDT) |
|---|---|---|
| AI Engineer | Junior | 60,000 |
| AI Engineer | Senior | 150,000 |
| ML Engineer | Junior | 55,000 |
| SQA Engineer | Senior | 120,000 |
| SQA Engineer | Junior | 90,000 |

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Juha464/AI-Career-Analysis-Tool..git
cd AI-Career-Analysis-Tool.

# Install dependencies
pip install pandas

# Run the tool
python main.py
```

## 💡 Example Usage

```
--- AI CAREER INSIGHTS (BANGLADESH 2026) ---
Average starting salary for Juniors: ৳68333.33333333333
How many hours do you study AI per day? 6
You are on the fast track to a 68333.33333333333 BDT job!
```

If you study fewer than 5 hours a day:

```
How many hours do you study AI per day? 2
At this rate, it might take longer to reach the Junior level.
```

## 🛠️ Tech Stack

- Python
- pandas

## 📁 Project Structure

```
AI-Career-Analysis-Tool./
├── main.py                # loads data, computes avg salary, gives advice
├── salaries.csv            # AI/tech job salary dataset (Bangladesh)
└── README.md
```

## 📌 Future Improvements

- Format the printed salary to 2 decimal places (e.g. `৳68,333.33`) instead of a raw float
- Break down average salary by role (AI Engineer vs ML Engineer vs SQA Engineer), not just by level
- Replace the fixed 5-hour threshold with a more nuanced scoring system
- Add error handling for non-numeric input
- Expand the dataset with more roles, companies, and years of data
- Turn this into a small CLI tool or web app for easier interaction

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> 💡 **Tip:** Consider renaming this repo from `AI-Career-Analysis-Tool.` to `AI-Career-Analysis-Tool` (drop the trailing period) — it currently looks like a typo in the URL.
