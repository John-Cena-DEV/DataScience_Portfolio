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
- A duplicate "No" consent entry (9) for Haridwar points to potential data entry inconsistencies in consent records.

---

## 🗂️ Dataset Description  
Key features of the dataset include:  
- **Month** – surgery timeline  
- **QHT ID** – anonymized patient identifier  
- **Demographics:** Age, Language, Location, Branch  
- **Procedure Details:** Case Type, Grade, Grafts, Surgery Date, Latest Visit Date  
- **Outcomes:** Patient Result, Progress at 1–13 Months  
- **Media & Marketing:** Consent, Video Shoot, Testimonial Type, Editors  

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
- **Pivot Table:** Surgeries by Month and Branch  
- **Insight:** Surgeries show a seasonal spike in June (holiday period), and outcomes have improved in the last 6 months with fewer ‘Average’ ratings.
- **Business Recommendation:** Allocate more staff in December–January to handle demand. Track ongoing quality improvements.
<img width="880" height="395" alt="Delhi and Haridwar" src="https://github.com/user-attachments/assets/70d7c967-50b8-403c-9eff-173809ebcb63" />

### 2️⃣ Case Type & Grafts  
- **Pivot Table:** Average grafts per Case Type  
- **Insight:** Average grafts increase steadily with patient age, from ~2800 in patients under 30 to ~4000 in patients over 40. Higher clinical grades also correspond to higher graft requirements.
- **Business Recommendation:** This helps in inventory planning for graft supplies and cost estimation per age group. 
<img width="2104" height="603" alt="AVERAGE of Grafts vs Case Type" src="https://github.com/user-attachments/assets/d8a83606-2575-49e2-8967-ac41a7aa13b2" />

### 3️⃣ Branch Distribution  
- **Pivot Table:** AGe wise demographics across branches  
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

<img width="881" height="480" alt="Visit Percentage vs Month" src="https://github.com/user-attachments/assets/4d8794d0-1d69-4b24-9f73-d339c6798324" />

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

## 📊 Visualizations  
Included visual insights using **Google Sheets dashboards**:  
- Line chart → Monthly surgeries trend  
<img width="880" height="395" alt="Delhi and Haridwar" src="https://github.com/user-attachments/assets/0ec6f2df-37de-46a6-8ba4-6cd85fc8cd55" />

- Line chart → Patient recovery progress (1–13 months)  
- Bar chart → Branch-wise success rates
<img width="880" height="588" alt="Patient Result Branch Wise" src="https://github.com/user-attachments/assets/3d619489-c143-4f3a-94b0-22d1cd5458e1" />
  
- Pie chart → Age distribution
<img width="893" height="619" alt="Age vs Patient Count" src="https://github.com/user-attachments/assets/2c71e8f6-e473-48de-bb69-c78da5023bff" />


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




