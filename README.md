# 🗺️ Weekend Getaway Ranker (Task 4)

## Overview
**Weekend Getaway Ranker** is a data engineering recommendation engine designed to suggest the best travel destinations based on a user's source city. It uses a **Weighted Scoring Algorithm** to rank locations by balancing travel distance, visitor ratings, and popularity.

This project fulfills the **Task 4** requirements of the internship assessment, utilizing **Python**, **Pandas**, and **GeoPy** for geospatial calculations.

## 🚀 Features
1.  **Smart Recommendation Engine:** Ranks destinations based on a composite score.
2.  **Geospatial Calculation:** Uses `geodesic` distance (in km) to filter locations within a "Weekend Trip" radius.
3.  **Weighted Algorithm:**
    * **Distance (40%):** Closer locations get higher scores (normalized).
    * **Rating (40%):** Higher-rated places are prioritized.
    * **Popularity (20%):** Places with more reviews get a slight boost.
4.  **Multi-City Support:** Works for any major Indian city (e.g., Delhi, Mumbai, Bangalore).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Geospatial Library:** GeoPy (for accurate distance calculation)

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.9+** installed.

### 2. Install Dependencies
Navigate to the project folder and install the required packages:

cd task-4-travel-ranker
pip install -r requirements.txt
3. Run the Recommendation Engine
Run the script to start the interactive ranker:


python weekend_ranker.py
🧪 Usage Example
When you run the script, you will be prompted to enter your current city.

Input:

Plaintext

Enter Source City: Delhi
Output:

Plaintext

✅ Top 5 Weekend Getaways from Delhi:

1. 🏆 Rishikesh
   - Rating: 4.8/5.0
   - Distance: 240 km
   - Score: 9.2/10

2. 🥈 Jaipur
   - Rating: 4.6/5.0
   - Distance: 280 km
   - Score: 8.9/10


📂 Project Structure
Plaintext

task-4-travel-ranker/
│
├── weekend_ranker.py          # Main algorithm script
├── Top Indian Places to Visit.csv # Dataset (Source Data)
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation
Submitted as part of the Internship Technical Assessment 2025.


### ⚠️ Don't forget the `requirements.txt`
If you haven't created the `requirements.txt` file for this folder yet, create it inside `task-4-travel-ranker` and add these two lines:

pandas
geopy