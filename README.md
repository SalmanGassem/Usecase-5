# Usecase-5

Streamlit link: https://usecase-5-salmang.streamlit.app/

## Data Cleaning steps:

## 1.  Reliability

The data comes from a reliable and trusted source, the government of Saudi Arabia.

Jadarat is a Unified National Employment Platform 

Partners:
- Digital Government Authority
- Human Resources Development Fund
- Human Resource and Social Development

All are governmental entities.

Sources:

- https://jadarat.sa/
- https://www.hrsd.gov.sa/en
- https://dga.gov.sa/en
- https://www.hrsd.gov.sa/en/ministry/about-ministry/minister-headed/entities-headed/hrdf

## 2.  Timeliness

The dates on the job postings are from 2022, and the Kaggle source that provided this dataset shown "Last Updated a Year Ago" which we can safely assume has been scraped and uploaded in 2023.

When checking for an up to date version from the original source "Jadarat", we are unable to download the data, however, we can view it. When checking job postings in the year 2022, we found out that no jobs are within that year, therefore we concluded that the data available in the current dataset at hand is of an old version.

Since we have no access to the most recent data, we will continue our analysis on the available 2022 data.

## 3.  Consistency
 
- After going over the data, it seems as though it has good consistency.

- Columns are filled with consistent values, no irregularities in terms of information they provide.

## 4.  Relevance

### Information we need:
1. region
2. gender
3. salary
4. experience
### Columns that are of relevance to our analysis are:

1. ['region']
2. ['city']
3. ['benefits']
4. ['exper']
5. ['gender']

Column that is not of relevance, but will be kept as a key to the uniqueness of our data to avoid false positives with duplication:

- job_post_id	

Other columns will be dropped due to them not serving our Problem Statements:
- 'job_title' 
- 'job_date'
- 'job_desc'
- 'job_tasks'
- 'comp_name'
- 'comp_no'
- 'comp_type'
- 'comp_size'
- 'eco_activity'
- 'qualif'
- 'contract'
- 'positions'
  
- * the 'benefits' column needs to be split into a 'Salary' and 'Benefits" column, and then dropping the "Benefits" column

## 5.  Uniqueness
    
-   Found 89 duplicated rows. Dropped them.
    
## 6.  Completeness

-   No null values are present after removing the irrelevant columns.

## 7.  Accuracy
Data types changed to a more logical approach:

- Salary column type changed to 'float'
- 'Years of Experience' column type changed to int after removing the strings

##### Columns renamed:

    'region': "Region",
    'city': "City", 
    'job_post_id': "Job ID", 
    'exper': "Years of Experience", 
    'gender': "Gender"

##### Outliers:

![image](https://github.com/user-attachments/assets/c32af89e-0152-4a37-ac6b-4c63e43f6aae)

Decided to cut off the outliers at the 'Salary' value of 18000, as our problem statements considers this as unattainable in most cases.

- Salman Gassem
