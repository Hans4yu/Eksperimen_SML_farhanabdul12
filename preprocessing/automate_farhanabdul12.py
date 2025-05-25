# filepath: d:\All Data\Projek Portfolio\Submission Sistem Membangun Machine Learning - Proyek Akhir\Eksperimen_SML_farhanabdul12\preprocessing\automate_farhanabdul12.py

import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
import argparse

warnings.filterwarnings('ignore')

class LoanApprovalPreprocessor:
    """
    Kelas untuk melakukan preprocessing otomatis pada dataset loan approval
    berdasarkan eksperimen yang telah dilakukan sebelumnya
    """
    
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.numerical_features = []
        self.categorical_features = []
    
    def load_data(self, file_path):
        """
        Memuat dataset dari file CSV
        
        Args:
            file_path (str): Path ke file dataset
            
        Returns:
            pd.DataFrame: Dataset yang dimuat
        """
        try:
            data = pd.read_csv(file_path)
            print(f"Dataset berhasil dimuat. Shape: {data.shape}")
            return data
        except Exception as e:
            print(f"Error saat memuat dataset: {e}")
            return None
    
    def initial_exploration(self, data):
        """
        Melakukan eksplorasi awal pada dataset
        
        Args:
            data (pd.DataFrame): Dataset input
        """
        print("\n=== EKSPLORASI DATASET ===")
        print(f"Shape dataset: {data.shape}")
        print(f"\nInfo dataset:")
        print(data.info())
        print(f"\nMissing values:")
        print(data.isnull().sum())
        print(f"\nData duplikat: {data.duplicated().sum()}")
        print(f"\nLima baris pertama:")
        print(data.head())
    
    def remove_identifier_columns(self, data):
        """
        Menghapus kolom identifier yang tidak diperlukan untuk modeling
        
        Args:
            data (pd.DataFrame): Dataset input
            
        Returns:
            pd.DataFrame: Dataset setelah penghapusan kolom identifier
        """
        if 'loan_id' in data.columns:
            data = data.drop('loan_id', axis=1)
            print("Kolom 'loan_id' berhasil dihapus")
        return data
    
    def identify_feature_types(self, data):
        """
        Mengidentifikasi tipe fitur (numerical dan categorical)
        
        Args:
            data (pd.DataFrame): Dataset input
        """
        self.numerical_features = data.select_dtypes(include=np.number).columns.tolist()
        self.categorical_features = data.select_dtypes(include='object').columns.tolist()
        
        print(f"\nFitur numerik: {self.numerical_features}")
        print(f"Fitur kategorikal: {self.categorical_features}")
    
    def standardize_numerical_features(self, data):
        """
        Melakukan standardisasi pada fitur numerik
        
        Args:
            data (pd.DataFrame): Dataset input
            
        Returns:
            pd.DataFrame: Dataset dengan fitur numerik yang sudah distandardisasi
        """
        if self.numerical_features:
            data[self.numerical_features] = self.scaler.fit_transform(data[self.numerical_features])
            print("Standardisasi fitur numerik berhasil dilakukan")
        return data
    
    def handle_outliers_iqr(self, data, column):
        """
        Menangani outlier menggunakan metode IQR
        
        Args:
            data (pd.DataFrame): Dataset input
            column (str): Nama kolom untuk penanganan outlier
            
        Returns:
            pd.DataFrame: Dataset setelah penghapusan outlier
        """
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)].copy()
    
    def remove_outliers(self, data):
        """
        Menghapus outlier dari semua fitur numerik
        
        Args:
            data (pd.DataFrame): Dataset input
            
        Returns:
            pd.DataFrame: Dataset setelah penghapusan outlier
        """
        original_shape = data.shape
        data_cleaned = data.copy()
        
        for col in self.numerical_features:
            data_cleaned = self.handle_outliers_iqr(data_cleaned, col)
        
        print(f"Shape asli: {original_shape}")
        print(f"Shape setelah penghapusan outlier: {data_cleaned.shape}")
        print(f"Data yang dihapus: {original_shape[0] - data_cleaned.shape[0]} baris")
        
        return data_cleaned
    
    def encode_categorical_features(self, data):
        """
        Melakukan encoding pada fitur kategorikal menggunakan LabelEncoder
        
        Args:
            data (pd.DataFrame): Dataset input
            
        Returns:
            pd.DataFrame: Dataset dengan fitur kategorikal yang sudah di-encode
        """
        for col in self.categorical_features:
            self.label_encoders[col] = LabelEncoder()
            data[col] = self.label_encoders[col].fit_transform(data[col])
            print(f"Label encoding untuk kolom '{col}' berhasil dilakukan")
        
        return data
    
    def preprocess_data(self, input_file_path, output_file_path=None):
        """
        Fungsi utama untuk melakukan preprocessing lengkap
        
        Args:
            input_file_path (str): Path ke file dataset mentah
            output_file_path (str): Path untuk menyimpan dataset yang sudah diproses
            
        Returns:
            pd.DataFrame: Dataset yang sudah diproses dan siap untuk training
        """
        print("=== MEMULAI PREPROCESSING OTOMATIS ===")
        
        # 1. Memuat dataset
        data = self.load_data(input_file_path)
        if data is None:
            return None
        
        # 2. Eksplorasi awal
        self.initial_exploration(data)
        
        # 3. Menghapus kolom identifier
        data = self.remove_identifier_columns(data)
        
        # 4. Mengidentifikasi tipe fitur
        self.identify_feature_types(data)
        
        # 5. Standardisasi fitur numerik
        data = self.standardize_numerical_features(data)
        
        # 6. Penghapusan outlier
        data = self.remove_outliers(data)
        
        # 7. Encoding fitur kategorikal
        data = self.encode_categorical_features(data)
        
        # 8. Menyimpan dataset yang sudah diproses
        if output_file_path:
            data.to_csv(output_file_path, index=False)
            print(f"\nDataset yang sudah diproses disimpan ke: {output_file_path}")
        
        print("\n=== PREPROCESSING SELESAI ===")
        print(f"Dataset siap untuk training dengan shape: {data.shape}")
        
        return data

def main():
    """
    Fungsi main untuk menjalankan preprocessing dari command line
    """
    parser = argparse.ArgumentParser(description='Automated Loan Approval Data Preprocessing')
    parser.add_argument('--input', '-i', 
                       default='../loanapproval_raw.csv',
                       help='Path to input CSV file')
    parser.add_argument('--output', '-o', 
                       default='loanapproval_preprocessing.csv',
                       help='Path to output CSV file')
    
    args = parser.parse_args()
    
    # Inisialisasi preprocessor
    preprocessor = LoanApprovalPreprocessor()
    
    # Jalankan preprocessing
    processed_data = preprocessor.preprocess_data(args.input, args.output)
    
    if processed_data is not None:
        print(f"\nPreprocessing berhasil! Dataset siap untuk training ML.")
        print(f"File output: {args.output}")
    else:
        print("Preprocessing gagal!")

if __name__ == "__main__":
    main()