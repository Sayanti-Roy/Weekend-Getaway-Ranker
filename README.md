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

📊 SAMPLE CONSOLE OUTPUTS

The following outputs demonstrate the recommender system ranking destinations based on distance, rating, and popularity.

```text
--- Weekend Getaway Recommender ---
Enter your source city (or type 'exit' to quit): Kolkata

Finding top weekend getaways from Kolkata...
Processing recommendations for: Kolkata (22.5726, 88.3639)...

City                     Type        Distance_km  Google review rating  Score
-------------------------------------------------------------------------------
Deoghar                  Temple          272.5                  4.7     0.76
Hooghly                  Temple           52.0                  4.6     0.74
Sundarbans National Park  Wildlife         68.7                  4.4     0.71
Bolpur                   Temple          139.0                  4.7     0.67
Digha                    Beach           137.5                  4.5     0.67


--- Weekend Getaway Recommender ---
Enter your source city (or type 'exit' to quit): Delhi

Finding top weekend getaways from Delhi...
Processing recommendations for: Delhi (28.6139, 77.2090)...

City           Type                     Distance_km  Google review rating  Score
----------------------------------------------------------------------------------
Greater Noida  Mall, Race Track               34.0                  4.4     0.92
Gurugram       Entertainment, Mall            24.1                  4.6     0.85
Agra           Mausoleum, Fort               178.1                  4.6     0.76
Vrindavan      Temple                        124.9                  4.8     0.74
Meerut         Temple                         69.5                  4.8     0.73


--- Weekend Getaway Recommender ---
Enter your source city (or type 'exit' to quit): Varanasi

Finding top weekend getaways from Varanasi...
Processing recommendations for: Varanasi (25.3356, 83.0076)...

City         Type                 Distance_km  Google review rating  Score
----------------------------------------------------------------------------
Patna        Zoo, Gurudwara           214.6                  4.5     0.73
Aurangabad  Cave                     153.2                  4.6     0.68
Allahabad   Confluence               118.5                  4.5     0.68
Deoghar     Temple                   384.0                  4.7     0.67
Lucknow     Monument, Mall            266.0                  4.5     0.66


Enter your source city (or type 'exit' to quit): exit
```




📂 Project Structure
Plaintext

📁 Project Structure (Plaintext)
```text
task-4-travel-ranker/
│
├── weekend_ranker.py
│   └── Main Python script containing the recommendation algorithm
│       for ranking weekend getaway destinations based on distance,
│       rating, and popularity.
│
├── Top Indian Places to Visit.csv
│   └── Source dataset containing Indian tourist destinations,
│       location details, and Google review ratings.
│
├── requirements.txt
│   └── List of Python dependencies required to run the project.
│
└── README.md
    └── Project documentation submitted as part of the
        Internship Technical Assessment 2025.
```
Submitted as part of the Internship Technical Assessment 2025.


### ⚠️ Don't forget the `requirements.txt`
If you haven't created the `requirements.txt` file for this folder yet, create it inside `task-4-travel-ranker` and add these two lines:

pandas

geopy



