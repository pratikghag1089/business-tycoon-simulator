# Game configuration constants

# Financial constants
STARTING_CASH = 100000
MAX_LOAN = 500000
VICTORY_THRESHOLD = 10000000

# Time constants
GAME_DAYS_PER_SECOND = 1
FPS = 60

# Town definitions
TOWNS = [
    {"name": "Riverdale", "population": 50000},
    {"name": "Mountain View", "population": 35000},
    {"name": "Coastal Bay", "population": 75000},
    {"name": "Sunny Valley", "population": 42000},
    {"name": "Industrial Park", "population": 28000}
]

# Product categories
PRODUCT_CATEGORIES = [
    "Electronics",
    "Clothing",
    "Food",
    "Furniture",
    "Automotive"
]

# Raw material types
RAW_MATERIALS = [
    "Metal",
    "Plastic",
    "Wood",
    "Fabric",
    "Glass"
]

# Simulation parameters
DEMAND_BASE = 1000
PRICE_ELASTICITY = 0.5
BRAND_EFFECT = 0.3