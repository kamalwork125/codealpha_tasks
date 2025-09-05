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


   git clone https://github.com/your-username/ecommerce-visualization.git
 
