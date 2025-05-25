# 🔐 GITHUB_TOKEN: Panduan Lengkap

## ❌ TIDAK PERLU DITAMBAHKAN MANUAL!

### **Penjelasan GITHUB_TOKEN:**

**`GITHUB_TOKEN`** adalah **secret yang otomatis tersedia** di setiap repository GitHub tanpa perlu setup manual.

## 🔍 Detail Teknis:

### **1. Otomatis Tersedia**
```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # ✅ Sudah tersedia otomatis
```

### **2. Permissions Default**
- **Read**: Repository contents, metadata
- **Write**: Repository contents (untuk commit/push)
- **Actions**: Read and write (untuk workflow operations)

### **3. Scope Otomatis**
- Hanya berlaku untuk repository tempat workflow berjalan
- Expired otomatis setelah workflow selesai
- Tidak bisa digunakan untuk repository lain

## 🚨 Yang TIDAK Perlu Dilakukan:

❌ **Jangan** buat Personal Access Token  
❌ **Jangan** tambahkan ke repository secrets  
❌ **Jangan** hardcode token di code  

## ✅ Yang Perlu Dipastikan:

### **1. Repository Permissions**
**Settings** → **Actions** → **General** → **Workflow permissions**:
```
✅ Read and write permissions
✅ Allow GitHub Actions to create and approve pull requests (optional)
```

### **2. File Permissions di Workflow**
```yaml
permissions:
  contents: write    # Untuk git push
  actions: read      # Untuk read workflow
```

## 🔧 Troubleshooting Common Issues:

### **Error: "Permission denied"**
**Solusi:**
1. Check workflow permissions di Settings
2. Pastikan `GITHUB_TOKEN` ada di env variables

### **Error: "Authentication failed"**
**Solusi:**
1. Pastikan repository bukan private dengan restrictions
2. Check branch protection rules

### **Error: "Token not found"**
**Penyebab:** Kemungkinan typo di YAML syntax

## 📋 Verification Checklist:

```bash
# 1. ✅ Repository permissions sudah benar
# 2. ✅ Workflow YAML syntax valid  
# 3. ✅ GITHUB_TOKEN sudah di env variables
# 4. ✅ Branch protection tidak menghalangi bot commits
```

## 🎯 Konfirmasi untuk Project Anda:

### **File: `.github/workflows/preprocessing.yml`**
```yaml
- name: Commit processed files (if on main branch)
  if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/master'
  run: |
    git config --local user.email "${{ vars.GIT_EMAIL || 'action@github.com' }}"
    git config --local user.name "${{ vars.GIT_NAME || 'GitHub Action Bot' }}"
    git add preprocessing/loanapproval_preprocessing_*.csv
    if git diff --staged --quiet; then
      echo "No changes to commit"
    else
      git commit -m "🤖 Auto-generated: Updated processed dataset"
      git push
    fi
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # ✅ OTOMATIS TERSEDIA
```

## 🚀 Kesimpulan:

**✨ GITHUB_TOKEN sudah siap digunakan tanpa setup tambahan!**

**Secrets yang perlu ditambahkan manual: 0 (nol)**
**Variables opsional: GIT_EMAIL dan GIT_NAME**

Repository Anda **100% siap** untuk GitHub Actions! 🎉
