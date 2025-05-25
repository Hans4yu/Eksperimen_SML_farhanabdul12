# GitHub Repository Setup Guide

## Required Secrets & Variables untuk GitHub Actions

### Secrets yang Diperlukan ✅

**Kabar Baik:** Workflow ini **TIDAK memerlukan secrets tambahan**!

- `GITHUB_TOKEN` sudah **otomatis tersedia** di setiap repository GitHub
- Digunakan untuk operasi git (commit, push) dalam workflow

### Optional Variables (Opsional)

Anda bisa menambahkan **Repository Variables** untuk kustomisasi:

| Variable Name | Default Value | Description |
|---------------|---------------|-------------|
| `GIT_EMAIL` | `action@github.com` | Email untuk git commit |
| `GIT_NAME` | `GitHub Action Bot` | Nama untuk git commit |

## Cara Setup Repository Variables (Opsional)

### 1. Via GitHub Web Interface

1. **Buka repository** di GitHub
2. **Settings** → **Secrets and variables** → **Actions**
3. **Tab "Variables"**
4. **Klik "New repository variable"**
5. **Tambahkan variables:**
   ```
   Name: GIT_EMAIL
   Value: your-email@example.com
   
   Name: GIT_NAME  
   Value: Your Name
   ```

### 2. Atau Biarkan Default

Jika tidak menambahkan variables, workflow akan menggunakan:
- Email: `action@github.com`
- Name: `GitHub Action Bot`

## Permissions yang Diperlukan

### Repository Permissions ✅

Pastikan repository memiliki permissions berikut (biasanya sudah default):

- **Actions**: `Read and write` (untuk menjalankan workflow)
- **Contents**: `Write` (untuk commit files)
- **Metadata**: `Read` (untuk membaca info repository)

### Cara Cek/Set Permissions

1. **Repository Settings** → **Actions** → **General**
2. **Workflow permissions** → Pilih **"Read and write permissions"**
3. **✅ Allow GitHub Actions to create and approve pull requests** (opsional)

## File yang Dibutuhkan di Repository

```
Eksperimen_SML_farhanabdul12/
├── loanapproval_raw.csv              # ✅ Dataset mentah (WAJIB)
├── requirements.txt                   # ✅ Dependencies (WAJIB) 
├── environment.yml                    # ✅ Conda env (WAJIB)
├── README.md                         # ✅ Dokumentasi
├── .github/
│   └── workflows/
│       └── preprocessing.yml         # ✅ GitHub Actions (WAJIB)
└── preprocessing/
    └── automate_farhanabdul12.py     # ✅ Script preprocessing (WAJIB)
```

## Trigger Workflow

### Otomatis Triggers ⚡

- **Push ke main/master** (dengan perubahan pada file tertentu)
- **Pull Request** ke main/master
- **Schedule**: Setiap hari jam 02:00 UTC

### Manual Trigger 🖱️

1. **Repository** → **Actions** → **"Automated Data Preprocessing"**
2. **Klik "Run workflow"** → **Run workflow**

## Troubleshooting

### Error: "Permission denied"
- **Solusi**: Cek workflow permissions di Settings → Actions → General

### Error: "No such file or directory"
- **Solusi**: Pastikan file `loanapproval_raw.csv` ada di root repository

### Error: "Module not found"
- **Solusi**: Cek `requirements.txt` dan pastikan semua dependencies ada

### Workflow tidak trigger otomatis
- **Solusi**: Pastikan file yang diubah sesuai dengan `paths` filter di workflow

## Testing Workflow

### Quick Test
```bash
# Push perubahan kecil untuk trigger workflow
echo "# Test" >> README.md
git add README.md
git commit -m "Test workflow trigger"
git push
```

### Monitoring
- **Repository** → **Actions** untuk melihat status workflow
- **Artifacts** akan tersedia setelah workflow selesai

## Hasil Workflow

### Artifacts yang Dihasilkan 📦

1. **processed-dataset-{run_number}**: File CSV hasil preprocessing
2. **preprocessing-summary-{run_number}**: Summary report

### Auto-commit 🤖

- File hasil preprocessing akan otomatis di-commit ke repository (hanya di branch main/master)
- Commit message: `🤖 Auto-generated: Updated processed dataset on {date} [skip ci]`

---

**✨ Setup Lengkap!** Workflow siap digunakan tanpa konfigurasi secrets tambahan.
