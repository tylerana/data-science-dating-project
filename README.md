# Data Science Dating Project

## Overview
This project leverages the **OKCupid Profiles Dataset** (sourced from Kaggle) to explore, analyze, and clean data for building a content-filtering system. The primary goal is to recommend potential matches based on user preferences and attributes. The dataset contains various user attributes, including demographics, interests, and lifestyle choices.

## Project Goals
- Clean and preprocess the data to ensure consistency and reliability.
- Engineer features to improve the quality of recommendations.
- Develop a content-filtering system for personalized recommendations.

## Dataset
The dataset contains **59,946 rows and 31 columns**, with features such as:
- **Demographics**: Age, location, ethnicity.
- **Preferences**: Orientation, body type, interests.
- **Lifestyle Choices**: Drinking, smoking, and dietary habits.
- **Essays**: User-written essays that provide additional insights.

## Tools and Libraries
The following tools and libraries are used in this project:
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **IDE**: Jupyter Notebook
- **Data Source**: [Kaggle OKCupid Dataset](https://www.kaggle.com)

## Key Features
### 1. **Data Cleaning**
- Addressed outliers and unrealistic values in numeric columns (e.g., age, income).
- Standardized categorical columns such as body type, education, and location.
- Handled missing values appropriately using placeholders like "Unknown" or inferred values.

### 2. **Feature Engineering**
- Converted `last_online` column into meaningful metrics like days since last activity.
- Grouped and standardized columns such as income, offspring, and drinks to enhance consistency.
- Derived insights from user essays by cleaning and tokenizing text data.

### 3. **Content Filtering System**
- Created personalized recommendations using content-based filtering techniques.
- Leveraged user attributes to calculate similarity and generate recommendations.

## Results and Insights
- The cleaned dataset offers reliable insights for building recommendation systems.
- Effective feature engineering enables better user segmentation and filtering.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/tylerana/data-science-dating-project.git
