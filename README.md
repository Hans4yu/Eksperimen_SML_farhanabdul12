# Eksperimen SML - Farhan Abdul

Proyek Machine Learning untuk sistem prediksi persetujuan pinjaman dengan preprocessing otomatis dan deployment menggunakan GitHub Actions.

## Setup Environment

### 1. Menggunakan Conda (Recommended)

#### Buat Environment Baru
```bash
# Buat environment dengan Python 3.12.7
conda create -n sml_farhanabdul12 python=3.12.7 -y

# Aktifkan environment
conda activate sml_farhanabdul12

# Install MLflow versi spesifik
pip install mlflow==2.19.0

# Install dependencies lainnya
pip install -r requirements.txt
```

#### Atau Menggunakan Environment.yml
```bash
# Buat environment dari file yml
conda env create -f environment.yml

# Aktifkan environment
conda activate sml_farhanabdul12
```

### 2. Verifikasi Instalasi

```bash
# Cek versi Python
python --version  # Harus menampilkan Python 3.12.7

# Cek library penting
pip list | findstr "mlflow pandas numpy scikit-learn"
```

Expected output:
```
mlflow                             2.19.0
mlflow-skinny                      2.19.0
numpy                              2.2.6
pandas                             2.2.3
scikit-learn                       1.6.1
```

## Struktur Project

```
Eksperimen_SML_farhanabdul12/
├── loanapproval_raw.csv              # Dataset mentah
├── requirements.txt                   # Dependencies Python
├── environment.yml                    # Conda environment file
├── README.md                         # Dokumentasi ini
├── .github/
│   └── workflows/
│       └── preprocessing.yml         # GitHub Actions workflow
└── preprocessing/
    ├── automate_farhanabdul12.py     # Script preprocessing otomatis
    ├── Eksperimen_farhanabdul12.ipynb # Notebook eksperimen
    └── loanapproval_preprocessing.csv # Dataset hasil preprocessing
```

## Penggunaan Script Preprocessing

### Basic Usage
```bash
cd preprocessing
python automate_farhanabdul12.py
```

### Custom Input/Output
```bash
python automate_farhanabdul12.py --input ../data/custom_data.csv --output output/processed_data.csv
```

### Help
```bash
python automate_farhanabdul12.py --help
```

## Tahapan Preprocessing

Script `automate_farhanabdul12.py` melakukan tahapan berikut secara otomatis:

1. **Loading Data** - Memuat dataset dari file CSV
2. **Data Exploration** - Eksplorasi awal dataset (shape, info, missing values, duplicates)
3. **Remove Identifier** - Menghapus kolom identifier yang tidak diperlukan (loan_id)
4. **Feature Type Identification** - Mengidentifikasi fitur numerik dan kategorikal
5. **Standardization** - Standardisasi fitur numerik menggunakan StandardScaler
6. **Outlier Removal** - Penghapusan outlier menggunakan metode IQR
7. **Categorical Encoding** - Encoding fitur kategorikal menggunakan LabelEncoder
8. **Save Processed Data** - Menyimpan dataset yang sudah diproses

## Dependencies

### Core Libraries
- **Python**: 3.12.7
- **MLflow**: 2.19.0 (untuk experiment tracking)
- **Pandas**: 2.2.3 (data manipulation)
- **NumPy**: 2.2.6 (numerical operations)
- **Scikit-learn**: 1.6.1 (machine learning)
- **Matplotlib**: 3.10.3 (plotting)

### Additional Libraries
- **Seaborn**: Data visualization
- **Joblib**: Model serialization
- **Flask**: Web framework untuk deployment
- **Jupyter**: Notebook environment
- **XGBoost, LightGBM**: Advanced ML algorithms
- **Optuna**: Hyperparameter optimization

## GitHub Actions Workflow

File `.github/workflows/preprocessing.yml` akan otomatis menjalankan preprocessing setiap kali ada trigger tertentu (push, pull request, atau schedule).

Workflow ini akan:
1. Setup Python 3.12.7
2. Install dependencies
3. Menjalankan preprocessing script
4. Upload hasil sebagai artifact
5. Commit hasil kembali ke repository

## Kontribusi

1. Fork repository ini
2. Buat branch untuk fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## Lisensi

Distributed under the MIT License. See `LICENSE` for more information.

## Kontak

Farhan Abdul - [@farhanabdul12](https://github.com/farhanabdul12)

Project Link: [https://github.com/farhanabdul12/Eksperimen_SML_farhanabdul12](https://github.com/farhanabdul12/Eksperimen_SML_farhanabdul12)
