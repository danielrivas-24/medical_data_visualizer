# Medical Data Visualizer

This project analyzes medical examination data and creates visualizations using **Pandas**, **Matplotlib**, and **Seaborn**.  
The dataset comes from medical examinations and contains body measurements, blood test results, lifestyle choices, and the presence or absence of cardiovascular disease.

---

## 📂 Project Structure
├── medical_data_visualizer.py   # Main script with data processing and plotting functions
├── main.py                      # Entry point to run and test the visualizations
├── test_module.py               # Unit tests
├── medical_examination.csv      # Dataset (loaded from GitHub raw link)
└── README.md                    # Documentation

---

## 📊 Dataset

The dataset used in this project is available in CSV format:  

👉 [medical_examination.csv](https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/main/medical_examination.csv)

### Columns Description

| Feature                | Type                | Values                                    |
|-------------------------|---------------------|-------------------------------------------|
| `age`                  | Objective           | int (in days)                             |
| `height`               | Objective           | int (cm)                                  |
| `weight`               | Objective           | float (kg)                                |
| `gender`               | Objective           | categorical (code)                        |
| `ap_hi`                | Examination         | int (systolic blood pressure)             |
| `ap_lo`                | Examination         | int (diastolic blood pressure)            |
| `cholesterol`          | Examination         | 1 = normal, 2 = above normal, 3 = high    |
| `gluc`                 | Examination         | 1 = normal, 2 = above normal, 3 = high    |
| `smoke`                | Subjective          | 0 = no, 1 = yes                           |
| `alco`                 | Subjective          | 0 = no, 1 = yes                           |
| `active`               | Subjective          | 0 = no, 1 = yes                           |
| `cardio`               | Target              | 0 = no disease, 1 = disease               |

---

## ⚙️ Installation

1. Clone this repository or download the files.
2. Install the required dependencies:

▶️ Usage

Run the main script:
python main.py

This will generate:
	•	Categorical plot: shows the distribution of lifestyle and examination features split by cardiovascular disease.
	•	Heatmap: shows correlations between medical features after data cleaning.

⸻

✅ Testing

Run the unit tests with:
python -m unittest test_module.py

📈 Visualizations

	•	Categorical Plot
Displays counts of good/bad outcomes for features like cholesterol, glucose, alcohol intake, activity, smoking, and overweight, split by cardiovascular disease.
	•	Heatmap
Shows correlations between cleaned medical data features.

⸻

📝 Notes
	•	Data cleaning steps remove outliers (e.g., implausible blood pressure values, extreme height/weight).
	•	The overweight column is derived from BMI:
[BMI = \frac{weight}{height^2}]
where BMI > 25 → overweight = 1, otherwise 0.

⸻

📌 Credits

Dataset: FreeCodeCamp - Medical Data Visualizer
Author: Daniel Rivas Tovar
