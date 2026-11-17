# NYC Airbnb Room Type Predictor

A Machine Learning classification project that explores Airbnb listings in New York City and predicts the type of room offered based on listing-related features.

The project focuses on understanding the dataset through Exploratory Data Analysis (EDA), preprocessing the data, addressing class imbalance, and building classification models to predict room types.

## Project Overview

Airbnb offers different types of accommodation, such as entire homes or apartments, private rooms, and shared rooms. This project uses listing information to build a classification model that predicts the room type of an Airbnb listing.

### Objective

To develop and evaluate Machine Learning classification models that can predict the `room_type` of an Airbnb listing using relevant numerical and categorical features.

## Dataset

The dataset contains Airbnb listing information for New York City.

The target variable is:

- `room_type`

The project explores features including:

| Feature | Description |
|---|---|
| `price` | Nightly price of the listing |
| `minimum_nights` | Minimum number of nights required for booking |
| `number_of_reviews` | Total number of reviews received |
| `reviews_per_month` | Average number of reviews per month |
| `calculated_host_listings_count` | Number of listings managed by the host |
| `availability_365` | Number of days the listing is available during the year |
| `latitude` | Geographic latitude of the listing |
| `longitude` | Geographic longitude of the listing |
| `neighbourhood_group` | NYC borough in which the listing is located |
| `neighbourhood` | Neighbourhood of the listing |

## Target Classes

The target variable, `room_type`, contains three classes:

- **Entire home/apt**
- **Private room**
- **Shared room**

The dataset has an imbalanced class distribution, with shared rooms representing a considerably smaller proportion of the listings. Class imbalance is therefore an important consideration during model development and evaluation.

## Project Workflow

The project follows these major steps:

1. **Data Loading** – Importing the NYC Airbnb dataset.
2. **Data Exploration** – Understanding the dataset structure, feature types, missing values, and statistical summaries.
3. **Exploratory Data Analysis (EDA)** – Investigating distributions, room-type proportions, pricing patterns, and geographical patterns.
4. **Data Preprocessing** – Preparing numerical and categorical features for Machine Learning.
5. **Handling Class Imbalance** – Applying an appropriate resampling strategy to address the underrepresented class.
6. **Model Training** – Training multiple classification algorithms.
7. **Model Evaluation** – Comparing model performance using classification evaluation metrics.

## Machine Learning Models

The project explores the following classification algorithms:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

## Evaluation Metrics

Model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Macro F1-score is particularly relevant to this project because it gives equal importance to each room-type class, including the underrepresented shared-room category.

## Technologies and Libraries

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn

## Repository Structure

```text
NYC-Airbnb-Room-Type-Predictor/
│
├── notebooks/              # Jupyter notebooks for analysis and modelling
├── data/                   # Dataset files (if included)
├── README.md
└── requirements.txt        # Project dependencies (if included)
```

*The repository structure may evolve as the project progresses.*

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AlwinVJ/NYC-Airbnb-Room-Type-Predictor.git
```

### 2. Navigate to the Project Directory

```bash
cd NYC-Airbnb-Room-Type-Predictor
```

### 3. Create a Conda Environment

```bash
conda create -n nyc-airbnb python=3.12
```

### 4. Activate the Environment

```bash
conda activate nyc-airbnb
```

### 5. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
```

### 6. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the project notebook to explore the analysis and modelling workflow.

## Project Status

**Status: In Progress**

This project is currently under development. Further experimentation, model evaluation, and improvements may be added as the project progresses.

## Video Credit

The project is based on the learning material presented in the following video:

[Watch the Video on YouTube](https://www.youtube.com/watch?v=oOyCUmZC5NY)

Credit to the original video creator for the reference material.

## Author

**Alwin VJ**

- GitHub: [AlwinVJ](https://github.com/AlwinVJ)
- Project Repository: [NYC Airbnb Room Type Predictor](https://github.com/AlwinVJ/NYC-Airbnb-Room-Type-Predictor)
