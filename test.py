import pandas as pd
import numpy as np
import os

def load_data(path):
    if not os.path.exists(path):
        print(f"Không tìm thấy file: {path}")
        return None
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns from {path}")
    return df

def clean_data(df):
    if df is None:
        print("Không có DataFrame để làm sạch.")
        return None
    df = df.drop_duplicates()
    df = df.fillna(0)
    print("🧹 Đã làm sạch dữ liệu (xóa trùng, thay NaN bằng 0).")
    return df

if __name__ == "__main__":
    
    data_dir = "/Users/kytruong/Data/Project/IUH Hackathon/Project IUH Datasets"

    train_path = os.path.join(data_dir, "train.csv")
    test_path = os.path.join(data_dir, "test.csv")
    features_path = os.path.join(data_dir, "features.csv")
    stores_path = os.path.join(data_dir, "stores.csv")

    # Load dữ liệu
    train_df = load_data(train_path)
    test_df = load_data(test_path)
    features_df = load_data(features_path)
    stores_df = load_data(stores_path)

    # Làm sạch cơ bản
    train_df = clean_data(train_df)
    print("\nXem 5 dòng đầu tiên của train:")
    print(train_df.head())
