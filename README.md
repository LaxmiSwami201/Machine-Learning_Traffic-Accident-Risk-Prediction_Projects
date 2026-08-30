# Machine-Learning_Traffic-Accident-Risk-Prediction_Projects
# 🎬 Movie Rating Analysis Dashboard – Power BI Project

## 📌 Project Overview

The **Movie Rating Analysis Dashboard** is an interactive Business Intelligence project developed using **Microsoft Power BI**. The project analyzes movie information, user activity, and ratings to generate meaningful insights through interactive dashboards and visualizations.

The main objective of this project is to transform raw movie rating data into an interactive dashboard that helps users understand **movie popularity, average ratings, genres, user activity, and rating trends**.

## 🎯 Project Objectives

* Analyze movie ratings and popularity.
* Identify the highest-rated movies.
* Analyze movies based on different genres.
* Understand user rating activity.
* Calculate average movie ratings.
* Identify the most reviewed movies.
* Analyze movie releases by year.
* Create an interactive and user-friendly dashboard.

## 🛠️ Tools & Technologies

* **Microsoft Power BI**
* Power Query
* DAX
* Data Modeling
* Data Cleaning
* Data Transformation
* Relationships
* Interactive Visualizations
* Slicers and Filters

## 🗄️ Dataset

The project uses three main tables:

### 👤 Users

Contains information about users.

* User ID
* User Name
* City
* Phone Number

### 🎬 Movies

Contains information about movies.

* Movie ID
* Movie Title
* Genre
* Release Year

### ⭐ Ratings

Contains information about movie ratings.

* Rating ID
* User ID
* Movie ID
* Rating
* Rating Date

## 🔗 Data Model

The three tables were connected using relationships between their primary and foreign keys.

```text
Users                    Movies
  |                         |
  | User_ID                 | Movie_ID
  ↓                         ↓
              Ratings
```

The **Ratings** table acts as the central table connecting users and movies.

## 🔄 Project Workflow

### 1. Data Import

The movie, user, and rating datasets were imported into **Power BI Desktop**.

### 2. Data Cleaning & Transformation

**Power Query** was used to:

* Remove duplicate records.
* Handle missing values.
* Correct data types.
* Clean inconsistent data.
* Format columns.
* Prepare the data for analysis.

### 3. Data Modeling

Relationships were created between the **Users, Movies, and Ratings** tables to build an effective data model.

### 4. DAX Calculations

DAX measures were created to calculate important business metrics such as:

* Total Movies
* Total Users
* Total Ratings
* Average Rating
* Highest Rating
* Lowest Rating

Example:

```DAX
Total Ratings = COUNT(Ratings[rating])
```

```DAX
Average Rating = AVERAGE(Ratings[rating])
```

### 5. Dashboard Development

Power BI visualizations were used to present the analysis in an interactive format.

## 📊 Dashboard Features

The dashboard includes important KPI cards such as:

* 🎬 **Total Movies**
* 👤 **Total Users**
* ⭐ **Total Ratings**
* 📊 **Average Rating**
* 🏆 **Highest Rated Movie**
* 🔥 **Most Reviewed Movie**

### 📈 Visualizations

The dashboard contains visualizations such as:

* **Movies by Genre** – Shows the distribution of movies across genres.
* **Rating Distribution** – Shows how ratings are distributed.
* **Movies Released by Year** – Displays movie release trends over time.
* **Top 10 Movies by Average Rating** – Identifies highly rated movies.
* **Genre-wise Average Rating** – Compares average ratings across genres.
* **Most Reviewed Movies** – Identifies movies receiving the highest number of ratings.
* **User Activity by City** – Shows rating activity across different cities.

### 🎛️ Interactive Filters

Slicers and filters allow users to interact with the dashboard and analyze the data based on:

* Genre
* Movie
* Release Year
* City
* Rating
* Rating Date

## 💡 Key Insights

The dashboard helps identify:

* Which movies have the highest average ratings.
* Which genres are most popular.
* Which movies receive the most ratings.
* How movie releases have changed over the years.
* Rating distribution across movies.
* Which users or cities show higher rating activity.
* Which genres have better average ratings.

## 📈 Business Value

This project demonstrates how **Power BI can transform raw movie data into actionable insights**.

The dashboard can help movie platforms, production companies, and entertainment businesses understand **audience preferences, movie performance, genre popularity, and user engagement**.

These insights can support decisions related to **movie promotion, content strategy, and audience targeting**.

## 🚀 Skills Demonstrated

* Power BI
* Power Query
* DAX
* Data Cleaning
* Data Transformation
* Data Modeling
* Relationships
* KPI Creation
* Data Visualization
* Interactive Dashboards
* Business Intelligence
* Analytical Thinking

## 📂 Project Structure

```text
Movie-Rating-PowerBI/
│
├── Movie_Rating_Dashboard.pbix
├── Movie_Rating_Data.xlsx
├── README.md
└── screenshots/
    └── movie_rating_dashboard.png
```

## 🏁 Conclusion

The **Movie Rating Analysis Dashboard** successfully converts movie, user, and rating data into an interactive Power BI report.

The project demonstrates practical knowledge of **Power Query, DAX, data modeling, relationships, KPI development, and data visualization**. It provides meaningful insights into movie ratings, genres, user activity, and popularity, making it a strong **Data Analyst / Business Intelligence portfolio project**.

## 👩‍💻 Author

**Laxmi Swami**

*Data Analyst | Power BI | SQL | Excel | Python*
