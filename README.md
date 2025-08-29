# E-commerce Product Recommendation System

## Overview
This project is a hands-on learning exercise to build a product recommendation system for a simulated e-commerce platform. It demonstrates key concepts in applied machine learning, from data engineering and preprocessing to model training and evaluation.

The system is built to mimic a real-world, production-level application, focusing on a **Collaborative Filtering** approach to suggest products to users based on their past purchase behavior.

## Motivation
The primary goal of this project is to learn and implement the entire machine learning project lifecycle in a structured way. By building the system from scratch, we cover essential steps including:
- **Data Simulation:** Creating realistic user and product data when real-world data is unavailable.
- **Data Preprocessing:** Cleaning, merging, and preparing data for a machine learning model.
- **Model Training:** Implementing and training a collaborative filtering model using a production-ready framework.
- **Project Structure:** Setting up a reproducible and scalable project environment using best practices (virtual environments, source control).

## Key Features
- **Data Generation Script:** A script to create a synthetic dataset of products, users, and user interactions.
- **Data Preprocessing:** Scripts to load, inspect, and prepare the raw data into a clean, model-ready format.
- **Collaborative Filtering Model:** A basic recommendation model built using the SVD algorithm from the `scikit-surprise` library.
- **Reproducible Setup:** A `setup.sh` script to automate the environment setup and dependency installation.

## Technical Stack
- **Python:** The core programming language.
- **Pandas & NumPy:** For data manipulation and numerical operations.
- **scikit-surprise:** A powerful library for building and evaluating recommender systems.
- **Faker:** For generating realistic-looking fake data.

## Getting Started
To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/prasad1482/Recomendation-system.git
    cd your-repo-name
    ```
2.  **Run the setup script:**
    ```sh
    ./setup.sh
    ```
    This script will create a virtual environment, install all dependencies, and set up the directory structure.

3.  **Generate the data:**
    Navigate to the `src/` directory and run the data generation script.
    ```sh
    python src/generate_data.py
    ```

4.  **Run the model:**
    Run the model training and evaluation script.
    ```sh
    # Assuming your model script is in src/train_model.py
    python src/train_model.py
    ```

## File Structure
