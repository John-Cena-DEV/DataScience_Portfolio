# 📊 Hair Transplant Clinic Data Analysis  

## 🔎 Project Overview  
This project analyzes anonymized clinical data from a **hair transplant clinic** to demonstrate **data science skills** in **data cleaning, exploratory data analysis (EDA), descriptive statistics, correlation analysis, forecasting, and business insights generation**.  

The dataset contains information on patient demographics, surgery details, graft counts, follow-up progress (1–13 months), clinical outcomes, and media/testimonial data.  

The objective is to showcase **end-to-end data analysis workflow** using **Google Sheets (pivot tables, charts, formulas)** and communicate **actionable insights** that could support clinical decision-making and marketing strategies.  

---
## 🗂️ Key Data Insights 

- Monthly surgeries peaked at 290 in January, declined to a low of 247 in March, recovered steadily from April (273) to July (275), then dropped sharply to 204 in August.
- Haridwar branch reports 3 to 4 times more patients than Delhi in the 20-29 and 30-39 age groups.
- Both Haridwar and Delhi have minimal patient counts beyond age 39, indicating most surgeries are performed on patients under 40.
- The 40-49 age group, despite having fewer patients (90), has a slightly higher average graft count (~4,480) than younger cohorts.
- The single patient in the 60-69 age group shows a graft average spike (~5,000), suggesting an outlier effect due to small sample size. Haridwar has a significantly higher "No Consent" count (865) compared to Delhi (209), indicating possible differences in consent policies between branches.

---

## 🗂 Dataset Description
- **Demographics**: Age, Age Bin, Location, Branch, Language  
- **Surgery details**: Surgery Date, Grade, Grafts, Case Type  
- **Follow-ups**: 13 monthly check-ups (`Followup_M1 … Followup_M13`)  
- **Outcome**: Patient Result, Looks, Communication Skill  
- **Consent & Media**: Consent Form, Video Shoot, Testimonial Approval  
- **Derived Features**:  
  - `Followup_Count` (number of follow-ups attended)  
  - `Followup_Completed` (1 if ≥12 months attended, else 0)  
  - `Has_Any_Followup` (1 if at least one follow-up attended)  
  - `Month_Year`, `Year`, `Age_Bin_Clean` 

<img width="958" height="398" alt="Screenshot 2025-09-17 174840" src="https://github.com/user-attachments/assets/1c894f18-d809-4962-90fd-1291670023f2" />


 
---
## 🧹 Data Cleaning & Preprocessing  
- Removed duplicate records to ensure data integrity  
- Anonymized patient names into unique IDs (P001, P002, …) to maintain confidentiality  
- Standardized date formats (`YYYY-MM-DD`) for time-series analysis  
- Converted categorical outcomes (`Successful`, `Partial`, `Failed`) into numerical scale (1, 0.5, 0) for quantitative modeling  
- Handled missing values (`0` for numeric, `Unknown` for categorical)  

<img width="956" height="125" alt="image" src="https://github.com/user-attachments/assets/28003340-88ff-43a6-822e-043e051a6b26" />


📌 *Skills Demonstrated:* **data wrangling, preprocessing, anonymization, data integrity**  

---

## 📈 Exploratory Data Analysis (EDA)  

### 1️⃣ Patient Demographics Analysis    
- **Insight:** Most patients (45%) are in the 30–39 age group, indicating the core customer base.
- **Business Recommendation:** Target marketing campaigns to this segment.
<img width="1176" height="575" alt="image" src="https://github.com/user-attachments/assets/bbaccb25-78e9-41cb-96bd-b3de6b14dbc5" />


### 2️⃣ Case Type & Grafts  
- **Pivot Table:** Average grafts per Case Type  
- **Insight:** Average grafts increase steadily with patient age, from ~2800 in patients under 30 to ~4000 in patients over 40. Higher clinical grades also correspond to higher graft requirements.
- **Business Recommendation:** This helps in inventory planning for graft supplies and cost estimation per age group. 
<img width="1176" height="575" alt="image" src="https://github.com/user-attachments/assets/2e0a96bc-b9fa-4da6-922f-6841f2ccd623" />


### 3️⃣ Branch Distribution  
- **Pivot Table:** Age wise demographics across branches  
- **Insight:** Most patients (45%) are in the 30–39 age group, indicating the core customer base.
- **Business Recommendation:** Target marketing campaigns to this segment.
<img width="1118" height="615" alt="Branch vs Age" src="https://github.com/user-attachments/assets/f7f83bba-f2aa-4d0b-ad1f-9f356348a7cb" />


### 4️⃣ Patient Result Distribution  
- **Pivot Table:** AVERAGE of Grafts vs Patient Result
- **Insight:** Patients with >3500 grafts are 20% more likely to report ‘Good Result’ compared to those with fewer grafts.
- **Business Recommendation:** Proper pre-surgery counseling can set expectations based on graft count and grade.
<img width="884" height="371" alt="AVERAGE of Grafts vs Patient Result" src="https://github.com/user-attachments/assets/85adc919-7d20-4e08-b8c8-92ebf9f607cc" />


### 5️⃣ Follow-up Compliance Analysis  
- **Pivot Table:** % of patients attending each month (M1–M13)  
- **Insight:** Retention drops sharply after Month 3. While 45% attend the 1st follow-up, **None** Visted after 7 Months.  
- **Business Recommendation:**  
  - Introduce automated SMS/WhatsApp reminders after Month 3 to maintain engagement  
  - Offer small incentives (e.g., free check-up, consultation) for completing all 12 follow-ups

<img width="932" height="599" alt="image" src="https://github.com/user-attachments/assets/33f43918-ccf0-4550-b8f3-9070fe03167f" />

📌 *Skills Demonstrated:* **EDA, pivot tables, trend analysis, data visualization**  

---

## 📊 Advanced Analysis  

### 🔗 Correlation Analysis  
- **Grafts vs Patient Result:** Moderate positive correlation (more grafts → higher success rate)  
- **Age vs Recovery:** Slight negative correlation (younger patients recover faster)  
<img width="2112" height="969" alt="AVERAGE of Grafts vs Age Bin" src="https://github.com/user-attachments/assets/ec2a0b75-67e0-473b-8455-b5db509552e6" />


### 📈 Forecasting & Predictive Modeling  
- Applied **linear regression (LINEST)** to forecast surgery volume for upcoming months  
<img width="783" height="459" alt="Procedure and Forecast" src="https://github.com/user-attachments/assets/393b08f8-cd2a-4af5-ad9a-a1be66bcfb20" />


### ⚠️ Patient Risk Segmentation  
- Defined **risk factors**: Age > 45, Grade ≥ 4, Grafts > 3000  
- Created a **risk score metric** and segmented patients into “High Risk” vs “Normal”  
- Found ~15% of patients fall into high-risk category, requiring closer monitoring  

📌 *Skills Demonstrated:* **statistical analysis, regression, forecasting, risk modeling, feature engineering**  

---

## 🐍 Python Analysis

This project also includes a [`notebooks/`](notebooks/) folder with:
- `01_data_cleaning_and_eda.ipynb` → Data cleaning, preprocessing, and exploratory data analysis  
- `02_retention_analysis.ipynb` → Follow-up retention curves and branch-level compliance  


Below are some sample Python snippets and their outputs ⬇️

### 1️⃣ Data Cleaning & Feature Engineering
```python
# Convert TRUE/FALSE follow-up columns to 1/0
followup_cols = [c for c in df.columns if c.startswith("Followup_M")]
for col in followup_cols:
    df[col] = df[col].astype(str).str.upper().map({"TRUE": 1, "FALSE": 0})

# Create new features
df['Followup_Count'] = df[followup_cols].sum(axis=1)
df['Followup_Completed'] = (df['Followup_Count'] >= 12).astype(int)
```
<img width="1176" height="576" alt="image" src="https://github.com/user-attachments/assets/193858b5-30b7-4b23-bf16-ce155e0ffe0e" />

### 2️⃣ Data Cleaning & Feature Engineering
```python
def kpi_summary(df):
    kpis = {}
    kpis['total_patients'] = int(df['FUE ID '].nunique())
    kpis['surgeries_this_month'] = int(df[df['Month_Year'] == df['Month_Year'].max()].shape[0])
    kpis['avg_grafts'] = float(df['Grafts'].mean())
    kpis['good_result_rate'] = float((df['Patient Result'] == 'Good').mean())
    return kpis

# Convert to lists
labels = list(kpis.keys())
values = list(kpis.values())

plt.figure(figsize=(8,5))
plt.bar(labels, values, color="skyblue", edgecolor="black")

plt.title("Clinic KPI Summary", fontsize=16, weight="bold")
plt.ylabel("Value")
plt.xticks(rotation=20)

# Annotate values
for i, v in enumerate(values):
    plt.text(i, v + (0.02 * max(values)), str(round(v,2)), ha='center', fontsize=12)

plt.show()
```
<img width="1070" height="771" alt="image" src="https://github.com/user-attachments/assets/e156f093-7c96-415a-908b-ab80621a6fdb" />

---

## 🗄 SQL Analysis

This project also includes a dedicated [`SQL/`](SQL/) folder with:
- `core_queries.sql` → collection of KPI, retention, and branch performance queries
- `SQL_Outputs.pdf/` → screenshots / exported results of query outputs

Below are some sample queries and results ⬇️

# SQL Analysis Queries  

## 1️⃣ Surgeries per Month  
This query counts the number of surgeries performed each month:  
```
SELECT       
  DATE_FORMAT(STR_TO_DATE(`Surgery Date`, '%d-%m-%Y'), '%b-%Y') AS month_year, 
  COUNT(`FUE ID`) AS Number_of_Surgeries
FROM dataset
GROUP BY month_year
ORDER BY Number_of_Surgeries DESC;
```

<img width="185" height="185" alt="Screenshot 2025-09-19 140800" src="https://github.com/user-attachments/assets/a482c51d-c3bf-4e35-8247-794d6f470e0a" />

### 2️⃣ Average Grafts by Age Bin
```
SELECT 
    `Age Bin` as Age_Bins, 
     round(avg(`Grafts`),0) as Avg_Grafts from dataset
group by Age_Bins
order by Avg_Grafts desc;
```
<img width="118" height="132" alt="Screenshot 2025-09-19 141014" src="https://github.com/user-attachments/assets/cd12ffaa-e1d6-4bd3-846a-98a3add11f0d" />

📌 *Skills Demonstrated:* **data visualization, storytelling, business intelligence (BI)**  

---

## 🚀 Key Takeaways  
- Demonstrated **end-to-end data analysis workflow**: cleaning → EDA → advanced analysis → insights → visualization  
- Translated clinical and marketing data into **actionable business insights**  
- Applied **statistical techniques** (correlation, regression, segmentation) to real-world healthcare data  
- Built a **portfolio-ready project** to showcase **data-driven decision-making**  

---

## 🛠 Tools & Technologies
- **Python**: pandas, numpy, matplotlib, seaborn, scikit-learn  
- **SQL**: Aggregations, KPIs, retention queries  
- **Google Sheets / Excel**: Pivot tables, KPI summaries  
- **Visualization**: Line charts, bar charts, cohort retention plots  
- **Version Control**: GitHub for reproducibility 
---

## 📂 Project Structure  

HairTransplantAnalysis/
├── data/
│   └── cleaned_data.csv
├── notebooks/
│   ├── 01_data_cleaning_and_eda.ipynb
│   ├── 02_retention_analysis.ipynb
│   └── 03_modeling_patient_result.ipynb
├── sql/
│   └── core_queries.sql
├── Analysis/
│   ├── Charts_Output.pdf
│   ├── Python_Charts.pdf
│   └── Pivot_Tables
├── README.md
└── slides/
    └── executive_summary.pdf


---

## 📌 Future Improvements  
- Automate analysis with **Python (Pandas, Matplotlib, Seaborn)**  
- Build an interactive dashboard using **Power BI / Tableau / Google Data Studio**  
- Train a **predictive ML model** to classify patient outcomes based on pre-surgery features  




