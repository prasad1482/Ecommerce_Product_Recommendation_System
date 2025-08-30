import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker to generate fake data
fake = Faker()

# --- 1. Generate Products Data ---
print("Generating products data...")
num_products = 5000
product_ids = range(1, num_products + 1)

product_categories = [
    "Electronics", "Apparel", "Books", "Home & Kitchen", 
    "Beauty", "Sports", "Toys & Games", "Tools"
]

products_df = pd.DataFrame({
    'product_id': product_ids,
    'product_name': [fake.word().capitalize() + " " + fake.word().capitalize() for _ in range(num_products)],
    'product_category': [random.choice(product_categories) for _ in range(num_products)],
    'product_description': [fake.text(max_nb_chars=200) for _ in range(num_products)],
    'price': [round(random.uniform(5.0, 500.0), 2) for _ in range(num_products)]
})
products_df.to_csv('products.csv', index=False)
print("products.csv created successfully.")

# --- 2. Generate Users Data ---
print("\nGenerating users data...")
num_users = 1000
user_ids = range(1, num_users + 1)
signup_dates = [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_users)]

users_df = pd.DataFrame({
    'user_id': user_ids,
    'signup_date': signup_dates
})
users_df.to_csv('users.csv', index=False)
print("users.csv created successfully.")

# --- 3. Generate User Interactions Data ---
# --- 3. Generate User Interactions Data ---
print("\nGenerating interactions data...")
num_interactions = 100000

# We will now create ratings based on different event types
event_types = ['view', 'add_to_cart', 'purchase']
event_weights = [0.7, 0.2, 0.1] # Same as before, but now we'll map them to ratings
ratings = {
    'view': 1,
    'add_to_cart': 3,
    'purchase': 5
}

# Create lists to hold the data for the DataFrame
interaction_data = {
    'user_id': [],
    'product_id': [],
    'rating': [], # Changed from 'event_type' to 'rating'
    'timestamp': []
}

# The number of unique events for a user follows a power-law distribution
active_user_weights = np.random.lognormal(0, 1, num_users)
active_user_weights /= active_user_weights.sum()
user_choices = random.choices(users_df['user_id'], weights=active_user_weights, k=num_interactions)

# The number of interactions for a product also follows a power-law distribution
popular_product_weights = np.random.lognormal(0, 1, num_products)
popular_product_weights /= popular_product_weights.sum()
product_choices = random.choices(products_df['product_id'], weights=popular_product_weights, k=num_interactions)

# Generate events and map them to our new ratings
generated_events = random.choices(event_types, weights=event_weights, k=num_interactions)
interaction_data['rating'] = [ratings[event] for event in generated_events]

interaction_data['user_id'] = user_choices
interaction_data['product_id'] = product_choices
interaction_data['timestamp'] = [fake.date_time_between(start_date='-2y', end_date='now') for _ in range(num_interactions)]

interactions_df = pd.DataFrame(interaction_data)
interactions_df.to_csv('interactions.csv', index=False)
print("interactions.csv created with weighted ratings.")