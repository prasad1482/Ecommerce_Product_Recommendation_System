#!/bin/bash

# Define the directory structure
DIRS=("data/raw" "data/processed" "data/interim" "src" "notebooks")

# Create directories
echo "Creating project directory structure..."
for dir in "${DIRS[@]}"; do
    mkdir -p "$dir"
done
echo "Directory structure created."

# Create a Python virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv env
echo "Virtual environment 'env' created."

# Activate the virtual environment
echo "Activating the virtual environment..."
source env/bin/activate
echo "Virtual environment activated."

# Install required Python packages
echo "Installing required Python packages..."
pip install pandas numpy scikit-learn Faker
echo "Packages installed."

# Generate requirements.txt file
echo "Generating requirements.txt..."
pip freeze > requirements.txt
echo "requirements.txt generated."

# Create empty placeholder files
touch src/__init__.py
touch .gitignore
touch README.md
touch generate_data.py
mv generate_data.py src/

echo "Project setup complete! To start working, run 'source env/bin/activate'."