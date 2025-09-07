# 📊 E-commerce Data Visualization Project

This project is part of my **CodeAlpha Data Analyst Internship** (Task 3: Data Visualization).  
The goal of this project is to analyze an e-commerce dataset, clean the data, and create meaningful visualizations to answer important business questions.

---

## 📂 Dataset Overview
The dataset `ecommerce.csv` contains the following columns:

- **Product Name** → Name of the product  
- **Category** → Product category (e.g., Electronics, Clothing)  
- **Quantity Ordered** → Number of units ordered  
- **Price Each** → Price per unit  
- **Delivery Time (Days)** → Time taken for delivery  
- **Customer Rating** → Customer rating out of 5  
- **City** → Location of the order  

---

## 🛠️ Libraries Used
- **pandas** → Data cleaning & manipulation  
- **numpy** → Numerical calculations  
- **matplotlib** → Visualizations (basic plots)  
- **seaborn** → Advanced visualizations (heatmap, barplots)  
- **tabulate** → To display dataset in table format  

---

## 🔧 Data Cleaning
- Filled missing values using:
  - Median for `Price Each`  
  - Mean for `Delivery Time` & `Customer Rating`  
  - `"Unknown Product"` for missing product names  
- Created a new column **Sales** = `Quantity Ordered × Price Each`

---

## 📈 Business Questions Answered
1. **Which Product Category Generated the Most Revenue?**  
   → Bar chart of category vs sales  

2. **What is the Average Delivery Time in Each City?**  
   → Bar chart of city vs average delivery time  

3. **Top 5 Products by Average Customer Rating**  
   → Bar chart of product vs rating  

4. **Correlation Between Quantity Ordered and Customer Rating**  
   → Heatmap correlation chart  

5. **Which City Generated the Highest Total Sales?**  
   → Bar chart of city vs sales  

---

## 📊 Visualizations
Here are some sample charts generated in this project:

- **Total Sales by Category**  
- **Average Delivery Time per City**  
- **Top 5 Products by Rating**  
- **Correlation Heatmap**  
- **Total Sales by City**
- 

   Screenshots

<img width="725" height="544" alt="Screenshot 2025-09-05 175538" src="https://github.com/user-attachments/assets/9a740abb-7523-4ca7-84a9-b944a067a0fd" />
<img width="703" height="541" alt="Screenshot 2025-09-05 175712" src="https://github.com/user-attachments/assets/eb2823c4-8a8d-4c87-bbfd-abb0d9e0e41d" />
<img width="620" height="300" alt="Screenshot 2025-09-05 175736" src="https://github.com/user-attachments/assets/394f9a15-167c-48ba-a4e9-4cc63aa30d63" />
<img width="631" height="504" alt="Screenshot 2025-09-05 175800" src="https://github.com/user-attachments/assets/edc1594e-47e2-4c00-b1c5-b93a58e8f829" />





---

## 🚀 Insights
- Electronics category generated the highest revenue.  
- Some cities faced higher delivery times compared to others.  
- Certain products consistently received high customer ratings.  
- Correlation shows weak/strong relationship between ordered quantity and ratings.  
- City-wise analysis revealed top-performing markets.  

# 🚢 Titanic Survival EDA Project  

This project is an **Exploratory Data Analysis (EDA)** on the famous Titanic dataset.  
The goal is to explore the dataset, clean the data, visualize patterns, and extract meaningful insights about passenger survival.  
## 📂 Dataset  
The dataset contains information about passengers aboard the Titanic, such as:  
- PassengerId  
- Survived (0 = No, 1 = Yes)  
- Pclass (Passenger class)  
- Name  
- Sex  
- Age  
- SibSp (Number of siblings/spouses aboard)  
- Parch (Number of parents/children aboard)  
- Ticket  
- Fare  
- Cabin  
- Embarked (Port of Embarkation: C, Q, S)  
## 🔧 Tools & Libraries Used  
- Python 🐍  
- Pandas  
- Matplotlib  
- Seaborn  
## 📊 EDA Process  
1. **Data Understanding**  
   - `head()`, `info()`, `describe()`, `columns`  
   - Checked missing values  
2. **Data Cleaning**  
   - Identified missing values in Age, Cabin, and Embarked  
   - Dropped or imputed values (Age median, Embarked mode, Cabin ignored)  
3. **Univariate Analysis**  
   - Survival count  
   - Passenger Class distribution  
   - Age distribution  
4. **Bivariate/Multivariate Analysis**  
   - Survival by Gender  
   - Survival by Passenger Class  
   - Survival by Embarked location  
   - Correlation Heatmap (Fare, Age, Pclass)  
5. **Visualizations**  
   - Countplots  
   - Histograms  
   - Boxplots  
   - Heatmap  
## 🔍 Key Insights  

- **Gender**: Females had a much higher survival rate than males.  
- **Class**: Passengers in 1st class were more likely to survive compared to 2nd and 3rd class.  
- **Age**: Children had higher survival chances compared to middle-aged adults.  
- **Embarkation**: Passengers who embarked from Cherbourg (C) had better survival rates.  
## 📈 Visualizations  
Here are some of the visualizations created:  
- Survival Count  
- Survival by Gender  
- Age Distribution  
- Survival by Class  
- Correlation Heatmap
  <img width="686" height="848" alt="image" src="https://github.com/user-attachments/assets/23e6f0ca-4bde-40b7-8e50-497cdbe2bb60" />

## 📌 Conclusion  

This EDA project gave me hands-on experience with:  
✔️ Data Cleaning  
✔️ Exploratory Data Analysis  
✔️ Data Visualization  

The Titanic dataset is a classic beginner-friendly dataset that provides deep insights into survival factors during the tragedy.  

---

## 🚀 Next Steps  

- Apply Machine Learning models (Logistic Regression, Random Forest) to predict survival.  
- Perform feature engineering to improve prediction accuracy.  

---
Sentiment Analysis of [Amazon reviews] 📝
Project Overview

This project performs Sentiment Analysis on textual data to determine whether the sentiment expressed is Positive, Negative, or Neutral. The main goal is to explore the dataset, preprocess text, and visualize insights about sentiments in the data.
Objectives:

Clean and preprocess textual data.
Analyze sentiment distribution.
Visualize trends and patterns in the dataset.
Build insights for business or social media analytics.
<img width="896" height="701" alt="image" src="https://github.com/user-attachments/assets/2fdd8174-3f4b-48d5-a89b-8d6f9a55dbff" />
<img width="1471" height="784" alt="Screenshot 2025-09-07 121238" src="https://github.com/user-attachments/assets/f3139a9e-69e3-42cb-8137-7616f647e8c5" />
<img width="1465" height="770" alt="Screenshot 2025-09-07 121249" src="https://github.com/user-attachments/assets/5fc83da5-490c-4553-bb26-9482163cd8a0" />
<img width="683" height="198" alt="Screenshot 2025-09-07 121258" src="https://github.com/user-attachments/assets/a9738387-be08-4a98-8e24-b4d5f254334e" />






