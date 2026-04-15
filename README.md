# 🤖 Machine Learning — Complete Learning Repository

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)]()

> A structured, end-to-end learning path covering Python fundamentals, data science libraries, machine learning algorithms, model deployment, and real-world projects — all in Jupyter Notebooks.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Module Breakdown](#module-breakdown)
  - [1. Functions](#1-functions)
  - [2. File Handling](#2-file-handling)
  - [3. Object-Oriented Programming](#3-object-oriented-programming)
  - [4. Advanced Python](#4-advanced-python)
  - [5. NumPy & Pandas](#5-numpy--pandas)
  - [7. Logging in Python](#7-logging-in-python)
  - [8. Multithreading & Multiprocessing](#8-multithreading--multiprocessing)
  - [9. Memory Management](#9-memory-management)
  - [10. Flask](#10-flask)
  - [11. Feature Engineering](#11-feature-engineering)
  - [12. Streamlit](#12-streamlit)
  - [13. Exploratory Data Analysis (EDA)](#13-exploratory-data-analysis-eda)
  - [14. Linear Regression](#14-linear-regression)
  - [15. Ridge, Lasso & ElasticNet](#15-ridge-lasso--elasticnet)
  - [16. Logistic Regression](#16-logistic-regression)
  - [17. Caching](#17-caching)
  - [Crash Course – ML](#crash-course--ml)
  - [Data](#data)
  - [Practice](#practice)
  - [ML Projects](#ml-projects)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Learning Path](#learning-path)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository is a comprehensive, hands-on machine learning curriculum built entirely in Python and Jupyter Notebooks. It takes a learner from core Python programming fundamentals all the way through to building, evaluating, and deploying machine learning models.

The content is organized numerically by topic, representing a logical progression from language basics to advanced ML algorithms and production-level deployment tools like Flask and Streamlit.

---

## Repository Structure

```
Machine-Learning/
│
├── 1-Function/                   # Python functions & scope
├── 2-File Handling/              # Reading/writing files in Python
├── 3-oops/                       # Object-Oriented Programming
├── 4-AdvancePython/              # Decorators, generators, comprehensions
├── 5-Numpy&Pandas/               # NumPy arrays & Pandas DataFrames
├── 7-Loggin_Python/              # Python logging module
├── 8-Multi-(Threading&Process)/  # Concurrency & parallelism
├── 9-Memory Managment/           # Memory optimization techniques
├── 10-Flask/flask/               # Web API deployment with Flask
├── 11-FeatureEngg/               # Feature engineering techniques
├── 12-Streamlit/                 # Interactive ML web apps
├── 13-EDA/                       # Exploratory Data Analysis
├── 14-Linear regression/         # Simple & multiple linear regression
├── 15-Ridge+Lasso+ElasticNet_Algo/ # Regularization techniques
├── 16-Logistic Regression/       # Classification with logistic regression
├── 17-Cache/                     # Caching strategies in Python
├── Crash Course - ML/            # Quick ML overview & key concepts
├── Data/                         # Datasets used across modules
├── Practice/                     # Practice notebooks & exercises
├── ml-Projects/                  # End-to-end real-world ML projects
│
├── requirements.txt              # Python dependencies
├── LICENSE                       # MIT License
└── README.md                     # This file
```

---

## Module Breakdown

### 1. Functions

**Folder:** `1-Function/`

Covers Python functions in depth — the building blocks of reusable and modular code.

**Topics covered:**
- Defining and calling functions
- Default, keyword, and arbitrary arguments (`*args`, `**kwargs`)
- Lambda functions and anonymous expressions
- Nested functions and closures
- Recursion and recursive problem-solving
- Variable scope: local, global, and nonlocal

---

### 2. File Handling

**Folder:** `2-File Handling/`

Focuses on reading from and writing to files using Python's built-in I/O capabilities.

**Topics covered:**
- Opening, reading, and writing text files
- Working with CSV and JSON files
- Context managers (`with` statement)
- File modes: read, write, append, binary
- Exception handling during file operations
- Working with the `os` and `pathlib` modules

---

### 3. Object-Oriented Programming

**Folder:** `3-oops/`

A thorough introduction to OOP principles in Python.

**Topics covered:**
- Classes and objects
- `__init__` and instance methods
- Class variables vs. instance variables
- Inheritance and method overriding
- Encapsulation and access modifiers
- Polymorphism and duck typing
- Dunder (magic) methods: `__str__`, `__repr__`, `__len__`, etc.
- Abstract classes and interfaces

---

### 4. Advanced Python

**Folder:** `4-AdvancePython/`

Covers Python features commonly used in data science and production code.

**Topics covered:**
- Decorators and function wrappers
- Generators and the `yield` keyword
- Iterators and the iterator protocol
- List, dict, and set comprehensions
- Context managers (custom `__enter__` / `__exit__`)
- Functional programming: `map`, `filter`, `reduce`
- Type hints and annotations
- Exception chaining and custom exceptions

---

### 5. NumPy & Pandas

**Folder:** `5-Numpy&Pandas/`

The core data science toolkit used in virtually every ML pipeline.

**NumPy topics:**
- Arrays: creation, indexing, slicing
- Broadcasting and vectorized operations
- Mathematical and statistical functions
- Reshaping, stacking, and splitting arrays
- Random number generation

**Pandas topics:**
- Series and DataFrame creation
- Reading from CSV, Excel, JSON
- Data selection: `.loc`, `.iloc`, boolean indexing
- Handling missing data (`NaN`)
- GroupBy, aggregation, and pivot tables
- Merging, joining, and concatenating DataFrames
- Time-series indexing and resampling

---

### 7. Logging in Python

**Folder:** `7-Loggin_Python/`

Proper logging is essential for debugging and monitoring ML pipelines.

**Topics covered:**
- Python `logging` module overview
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Configuring handlers: StreamHandler, FileHandler
- Log formatters and structured logs
- Rotating file handlers for long-running processes
- Best practices for logging in ML applications

---

### 8. Multithreading & Multiprocessing

**Folder:** `8-Multi-(Threading&Process)/`

Understanding concurrency is key for processing large datasets efficiently.

**Topics covered:**
- Differences between threading and multiprocessing
- Python's Global Interpreter Lock (GIL)
- `threading` module: Thread creation, locks, synchronization
- `multiprocessing` module: Process pools, shared memory
- `concurrent.futures`: ThreadPoolExecutor, ProcessPoolExecutor
- Use cases in ML: parallel data loading, hyperparameter search

---

### 9. Memory Management

**Folder:** `9-Memory Managment/`

Optimizing memory usage is critical when dealing with large datasets.

**Topics covered:**
- Python's memory model and garbage collection
- Reference counting and cyclic garbage collection
- Memory-efficient data structures
- Using generators to reduce memory footprint
- `__slots__` for class memory optimization
- Profiling memory usage with `tracemalloc` and `memory_profiler`
- Chunked data loading with Pandas

---

### 10. Flask

**Folder:** `10-Flask/flask/`

Deploy trained machine learning models as REST APIs using Flask.

**Topics covered:**
- Flask application structure and routing
- Building RESTful endpoints (`GET`, `POST`)
- Serializing and deserializing JSON requests/responses
- Loading and serving a pickled ML model
- Input validation and error handling
- Running a local development server
- Overview of deployment to cloud platforms

---

### 11. Feature Engineering

**Folder:** `11-FeatureEngg/`

Feature engineering is one of the most impactful steps in improving model performance.

**Topics covered:**
- Handling missing values: imputation strategies
- Encoding categorical variables: Label Encoding, One-Hot Encoding, Target Encoding
- Feature scaling: StandardScaler, MinMaxScaler, RobustScaler
- Creating polynomial and interaction features
- Binning and discretization
- Date/time feature extraction
- Feature selection: correlation, variance threshold, recursive elimination (RFE)
- Handling skewed distributions with log/Box-Cox transforms

---

### 12. Streamlit

**Folder:** `12-Streamlit/`

Build interactive, browser-based UIs for ML models without any front-end expertise.

**Topics covered:**
- Streamlit app structure and lifecycle
- Widgets: sliders, dropdowns, text inputs, file uploaders
- Displaying DataFrames, charts, and plots
- Real-time model inference in the browser
- Caching with `@st.cache_data` for performance
- Deploying Streamlit apps to Streamlit Community Cloud

---

### 13. Exploratory Data Analysis (EDA)

**Folder:** `13-EDA/`

EDA is the critical step of understanding your data before modeling.

**Topics covered:**
- Descriptive statistics: mean, median, std, skewness, kurtosis
- Univariate analysis: histograms, box plots, KDE plots
- Bivariate analysis: scatter plots, correlation matrices, heatmaps
- Detecting and handling outliers (IQR method, Z-score)
- Distribution analysis and normality tests
- Visualizations using `Matplotlib`, `Seaborn`, and `Plotly`
- Identifying data quality issues: duplicates, wrong types, erroneous values
- Generating automated EDA reports with `ydata-profiling`

---

### 14. Linear Regression

**Folder:** `14-Linear regression/`

The foundation of supervised learning and predictive modeling.

**Topics covered:**
- Simple linear regression: theory and derivation
- Multiple linear regression with multiple features
- Assumptions of linear regression (linearity, homoscedasticity, etc.)
- Cost function: Mean Squared Error (MSE)
- Gradient descent: batch, stochastic, mini-batch
- Normal equation (closed-form solution)
- Evaluating models: R², Adjusted R², MAE, MSE, RMSE
- Visualizing regression lines and residuals
- Implementing with `scikit-learn`'s `LinearRegression`

---

### 15. Ridge, Lasso & ElasticNet

**Folder:** `15-Ridge+Lasso+ElasticNet_Algo/`

Regularization prevents overfitting by penalizing model complexity.

**Topics covered:**
- Overfitting vs. underfitting: the bias-variance trade-off
- Ridge Regression (L2 regularization): theory and math
- Lasso Regression (L1 regularization): feature selection via sparsity
- ElasticNet: combining L1 and L2 penalties
- Hyperparameter tuning: cross-validated alpha selection (`RidgeCV`, `LassoCV`)
- Comparing regularized vs. unregularized models
- Coefficient paths and shrinkage visualization
- When to use Ridge vs. Lasso vs. ElasticNet

---

### 16. Logistic Regression

**Folder:** `16-Logistic Regression/`

The go-to algorithm for binary and multi-class classification.

**Topics covered:**
- From linear to logistic: the sigmoid function
- Maximum Likelihood Estimation (MLE) and log-loss
- Binary classification and decision boundaries
- Multi-class classification: One-vs-Rest (OvR), Softmax
- Regularization in logistic regression (C parameter)
- Evaluation metrics: accuracy, precision, recall, F1-score
- Confusion matrix and ROC-AUC curve
- Handling class imbalance: `class_weight='balanced'`, SMOTE
- Implementation with `scikit-learn`

---

### 17. Caching

**Folder:** `17-Cache/`

Caching speeds up repetitive computations — critical in data pipelines and web applications.

**Topics covered:**
- Python `functools.lru_cache` and `functools.cache`
- Memoization patterns
- Caching database queries
- Redis-based caching for production ML systems
- Streamlit caching: `@st.cache_data`, `@st.cache_resource`
- Cache invalidation strategies

---

### Crash Course – ML

**Folder:** `Crash Course - ML/`

A fast-paced overview of the machine learning landscape — perfect as a reference or refresher.

**Topics covered:**
- What is Machine Learning? Types: Supervised, Unsupervised, Reinforcement
- The ML workflow: problem → data → features → model → evaluation → deployment
- Key algorithms at a glance: KNN, Decision Trees, SVM, Naive Bayes, Clustering
- Model selection and cross-validation
- Hyperparameter tuning: GridSearchCV, RandomizedSearchCV
- Pipelines with `sklearn.pipeline.Pipeline`
- Saving and loading models with `pickle` and `joblib`

---

### Data

**Folder:** `Data/`

A collection of datasets used throughout the various modules and projects.

Contains a mix of well-known benchmark datasets (e.g., housing prices, classification datasets) and domain-specific CSVs used in the ML projects. All datasets are in readily loadable formats (`.csv`, `.xlsx`, `.json`).

---

### Practice

**Folder:** `Practice/`

Supplementary practice notebooks for reinforcing concepts covered in the main modules.

Includes exercises, mini-challenges, and concept reviews designed to test and solidify understanding through hands-on application.

---

### ML Projects

**Folder:** `ml-Projects/`

End-to-end machine learning projects that integrate multiple concepts from across the curriculum into real-world applications.

Each project follows the full ML pipeline:

```
Data Collection → EDA → Feature Engineering → Model Training → Evaluation → Deployment
```

Projects are built with real datasets and demonstrate how to take a model from a notebook to a deployable application using Flask or Streamlit.

---

## Tech Stack

| Category | Libraries / Tools |
|---|---|
| **Language** | Python 3.8+ |
| **Notebooks** | Jupyter Notebook |
| **Data Manipulation** | NumPy, Pandas |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn |
| **Web Deployment** | Flask, Streamlit |
| **Utilities** | pickle, joblib, logging, functools |
| **Concurrency** | threading, multiprocessing, concurrent.futures |

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- `pip` (Python package manager)
- `git`

Verify your Python installation:

```bash
python --version
pip --version
```

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/dksh-sood/Machine-Learning.git
cd Machine-Learning
```

**2. (Recommended) Create a virtual environment**

```bash
# Using venv
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Or using conda
conda create -n ml-env python=3.10
conda activate ml-env
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Launch Jupyter Notebook**

```bash
jupyter notebook
```

This opens the Jupyter interface in your browser. Navigate to any module folder and open a `.ipynb` file to get started.

---

## Usage

### Running a specific module

Navigate to any numbered folder and open the notebook:

```bash
cd "14-Linear regression"
jupyter notebook
```

### Running a Flask app

```bash
cd 10-Flask/flask
python app.py
```

The API will be available at `http://127.0.0.1:5000`.

### Running a Streamlit app

```bash
cd 12-Streamlit
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## Learning Path

If you're new to machine learning, follow the modules in this recommended order:

```
Python Fundamentals (1 → 2 → 3 → 4)
         ↓
Data Science Libraries (5)
         ↓
Python for Production (7 → 8 → 9 → 17)
         ↓
Data Understanding (13 - EDA)
         ↓
Feature Engineering (11)
         ↓
ML Algorithms (14 → 15 → 16)
         ↓
Crash Course Review
         ↓
Deployment (10 - Flask → 12 - Streamlit)
         ↓
End-to-End Projects (ml-Projects)
```

> **Tip:** Even if you're comfortable with Python, a quick pass through modules 3–5 is recommended to ensure you're familiar with the OOP and data library patterns used throughout the ML modules.

---

## Contributing

Contributions, corrections, and new notebooks are welcome!

1. Fork this repository
2. Create a new branch: `git checkout -b feature/new-topic`
3. Add your notebook or make your changes
4. Commit your changes: `git commit -m "Add: new topic notebook"`
5. Push to your fork: `git push origin feature/new-topic`
6. Open a Pull Request

Please ensure notebooks are clean (cleared output cells before committing) and well-commented.

---

## License

This project is licensed under the [MIT License](LICENSE) — you are free to use, modify, and distribute this code with attribution.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/dksh-sood">dksh-sood</a></sub>
</div>
