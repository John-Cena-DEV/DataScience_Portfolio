
-- 1. Surgeries per month

SELECT DATE_FORMAT(STR_TO_DATE(`Surgery Date`, '%d-%m-%Y'), '%b-%Y') AS month_year, count(`FUE ID`) as Number_of_Surgeries
FROM dataset
group by month_year
order by Number_of_Surgeries desc;
