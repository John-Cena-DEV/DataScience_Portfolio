**SQL QUERIES**
-- 1. Surgeries per month

SELECT DATE_FORMAT(STR_TO_DATE(`Surgery Date`, '%d-%m-%Y'), '%b-%Y') AS month_year, count(`FUE ID`) as Number_of_Surgeries
FROM dataset
group by month_year
order by Number_of_Surgeries desc;

-- 2. Average grafts by age bin

SELECT `Age Bin` as Age_Bins, round(avg(`Grafts`),0) as Avg_Grafts from dataset
group by Age_Bins
order by Avg_Grafts desc;

-- 3. Branch KPI summary

Select branch, COUNT(*) AS total_ops, ROUND(AVG(Grafts),0) AS avg_grafts,  
round(avg(case WHEN `Patient Result`='Good' or `Patient Result`='Excellent'  THEN 1 ELSE 0 END),3) AS good_result_rate from dataset
group by branch;

-- 4. Consent Number by branch
Select branch, ifnull(Consent, "Not Taken") as Consent, count(*) as patient_no from dataset
group by branch, Consent
order by branch desc, patient_no desc;
