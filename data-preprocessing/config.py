"""
Configuration file for data preprocessing pipeline.
Keeps all paths, constants, and default parameters centralized.
"""

# ========================
# File Paths
# ========================
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
RESULTS_PATH = "results/"

# Example dataset file
DEFAULT_DATASET = RAW_DATA_PATH + "dataset.csv"

# ========================
# Preprocessing Parameters
# ========================
MISSING_VALUE_STRATEGY = "mean"   # Options: mean, median, mode, zero
DUPLICATE_REMOVAL = True

# Scaling
SCALING_METHOD = "standard"       # Options: standard, minmax, none

# Train/Validation/Test Split
TEST_SIZE = 0.2
VAL_SIZE = 0.1
RANDOM_STATE = 42

# ========================
# Feature Engineering
# ========================
CATEGORICAL_ENCODING = "onehot"   # Options: onehot, label
POLYNOMIAL_FEATURES = False
POLY_DEGREE = 2

# ========================
# Logging
# ========================
LOG_LEVEL = "INFO"   # Options: DEBUG, INFO, WARNING, ERROR
