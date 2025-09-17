# 📊 Hair Transplant Clinic Data Analysis  

## 🔎 Project Overview  
This project analyzes anonymized clinical data from a **hair transplant clinic** to demonstrate **data science skills** in **data cleaning, exploratory data analysis (EDA), descriptive statistics, correlation analysis, forecasting, and business insights generation**.  

The dataset contains information on patient demographics, surgery details, graft counts, follow-up progress (1–13 months), clinical outcomes, and media/testimonial data.  

The objective is to showcase **end-to-end data analysis workflow** using **Google Sheets (pivot tables, charts, formulas)** and communicate **actionable insights** that could support clinical decision-making and marketing strategies.  

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

### 1️⃣ Patient Volume Analysis  
- **Pivot Table:** Surgeries by Month and Branch  
- **Insight:** Seasonal peaks in June–July, Branch A has the highest patient volume  

### 2️⃣ Case Type & Grafts  
- **Pivot Table:** Average grafts per Case Type  
- **Insight:** FUT cases typically involve higher graft counts than FUE  

### 3️⃣ Clinical Outcomes  
- **Pivot Table:** Success vs Non-success across branches  
- **Insight:** 85% overall success rate; Branch B shows slightly lower performance  

### 4️⃣ Patient Recovery Progress  
- **Pivot Table:** Average improvement across 1–13 months  
- **Insight:** Noticeable improvement after 3 months; recovery plateaus after 9 months  

### 5️⃣ Marketing & Media Insights  
- **Pivot Table:** Testimonial and video shoot approvals  
- **Insight:** 60% of patients consent to testimonials, providing valuable marketing opportunities  

📌 *Skills Demonstrated:* **EDA, pivot tables, trend analysis, data visualization**  

---

## 📊 Advanced Analysis  

### 🔗 Correlation Analysis  
- **Grafts vs Patient Result:** Moderate positive correlation (more grafts → higher success rate)  
- **Age vs Recovery:** Slight negative correlation (younger patients recover faster)  

### 📈 Forecasting & Predictive Modeling  
- Applied **linear regression (LINEST)** to forecast surgery volume for upcoming months  
- Prediction: ~120 surgeries expected next quarter  

### ⚠️ Patient Risk Segmentation  
- Defined **risk factors**: Age > 45, Grade ≥ 4, Grafts > 3000  
- Created a **risk score metric** and segmented patients into “High Risk” vs “Normal”  
- Found ~15% of patients fall into high-risk category, requiring closer monitoring  

📌 *Skills Demonstrated:* **statistical analysis, regression, forecasting, risk modeling, feature engineering**  

---

## 📊 Visualizations  
Included visual insights using **Google Sheets dashboards**:  
- Line chart → Monthly surgeries trend  
- Line chart → Patient recovery progress (1–13 months)  
- Bar chart → Branch-wise success rates  
- Pie chart → Testimonial approval distribution  
- Histogram → Age distribution  

📌 *Skills Demonstrated:* **data visualization, storytelling, business intelligence (BI)**  

---

## 🚀 Key Takeaways  
- Demonstrated **end-to-end data analysis workflow**: cleaning → EDA → advanced analysis → insights → visualization  
- Translated clinical and marketing data into **actionable business insights**  
- Applied **statistical techniques** (correlation, regression, segmentation) to real-world healthcare data  
- Built a **portfolio-ready project** to showcase **data-driven decision-making**  

---

## 🛠️ Tools & Techniques  
- **Google Sheets** → Pivot Tables, Charts, Dashboards  
- **Statistical Functions** → `CORREL`, `LINEST`, `COUNTIFS`, `AVERAGEIF`  
- **Data Analysis Concepts** → EDA, Time Series Trend Analysis, Regression, Segmentation, Forecasting  
- **Version Control** → GitHub for portfolio presentation  

---

## 📂 Project Structure  

HairTransplantAnalysis/
├── data/
│ └── cleaned_data.csv # anonymized dataset
├── analysis/
│ ├── pivot_tables.pdf # pivot tables summary
│ └── charts/ # screenshots of visualizations
├── README.md # project documentation



---

## 📌 Future Improvements  
- Automate analysis with **Python (Pandas, Matplotlib, Seaborn)**  
- Build an interactive dashboard using **Power BI / Tableau / Google Data Studio**  
- Train a **predictive ML model** to classify patient outcomes based on pre-surgery features  




