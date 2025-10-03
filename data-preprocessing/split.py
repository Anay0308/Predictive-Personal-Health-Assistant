from sklearn.model_selection import train_test_split

def split_data(X, y, test_size: float = 0.2, val_size: float = 0.1, random_state: int = 42):
    """Split dataset into train/val/test sets."""
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=(test_size+val_size), random_state=random_state)
    relative_val_size = val_size / (test_size + val_size)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=relative_val_size, random_state=random_state)
    return X_train, X_val, X_test, y_train, y_val, y_test
