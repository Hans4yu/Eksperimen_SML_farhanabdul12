#!/usr/bin/env python3
"""
Validation script untuk memastikan semua file dan konfigurasi
siap untuk GitHub Actions workflow.
"""

import os
import sys
import yaml
import json
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if file exists and return status"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - FILE NOT FOUND!")
        return False

def check_python_script(filepath):
    """Check if Python script has valid syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            compile(f.read(), filepath, 'exec')
        print(f"✅ Python script syntax valid: {filepath}")
        return True
    except SyntaxError as e:
        print(f"❌ Python script syntax error in {filepath}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error checking {filepath}: {e}")
        return False

def check_yaml_syntax(filepath):
    """Check if YAML file has valid syntax"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✅ YAML syntax valid: {filepath}")
        return True
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error in {filepath}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error checking {filepath}: {e}")
        return False

def check_requirements_txt(filepath):
    """Check requirements.txt format"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        mlflow_found = False
        for line in lines:
            line = line.strip()
            if line.startswith('mlflow'):
                mlflow_found = True
                if '2.19.0' in line:
                    print(f"✅ MLflow 2.19.0 found in requirements.txt")
                else:
                    print(f"⚠️  MLflow version might not be 2.19.0")
                break
        
        if not mlflow_found:
            print(f"❌ MLflow not found in requirements.txt")
            return False
            
        print(f"✅ Requirements.txt format valid")
        return True
    except Exception as e:
        print(f"❌ Error checking requirements.txt: {e}")
        return False

def main():
    """Main validation function"""
    print("🔍 Validating GitHub Actions Setup for Eksperimen_SML_farhanabdul12")
    print("=" * 70)
    
    # Get current directory
    base_dir = Path.cwd()
    print(f"📁 Base directory: {base_dir}")
    print()
    
    # List of required files with their descriptions
    required_files = [
        ("loanapproval_raw.csv", "Dataset mentah"),
        ("requirements.txt", "Python dependencies"),
        ("environment.yml", "Conda environment"),
        ("README.md", "Dokumentasi utama"),
        (".github/workflows/preprocessing.yml", "GitHub Actions workflow"),
        ("preprocessing/automate_farhanabdul12.py", "Script preprocessing"),
    ]
    
    # Check required files
    print("📋 Checking Required Files:")
    all_files_exist = True
    for filepath, description in required_files:
        if not check_file_exists(filepath, description):
            all_files_exist = False
    
    print()
    
    # Check Python script syntax
    print("🐍 Checking Python Script:")
    python_valid = check_python_script("preprocessing/automate_farhanabdul12.py")
    print()
    
    # Check YAML syntax
    print("📄 Checking YAML Files:")
    yaml_files_valid = True
    if os.path.exists(".github/workflows/preprocessing.yml"):
        if not check_yaml_syntax(".github/workflows/preprocessing.yml"):
            yaml_files_valid = False
    
    if os.path.exists("environment.yml"):
        if not check_yaml_syntax("environment.yml"):
            yaml_files_valid = False
    print()
    
    # Check requirements.txt
    print("📦 Checking Requirements:")
    requirements_valid = check_requirements_txt("requirements.txt")
    print()
    
    # Check directory structure
    print("📂 Checking Directory Structure:")
    expected_dirs = [".github", ".github/workflows", "preprocessing"]
    dirs_valid = True
    for dir_path in expected_dirs:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            print(f"✅ Directory exists: {dir_path}")
        else:
            print(f"❌ Directory missing: {dir_path}")
            dirs_valid = False
    print()
    
    # Overall validation result
    print("🎯 Validation Summary:")
    print("=" * 30)
    
    checks = [
        ("Required Files", all_files_exist),
        ("Python Script", python_valid),
        ("YAML Files", yaml_files_valid),
        ("Requirements", requirements_valid),
        ("Directory Structure", dirs_valid),
    ]
    
    all_passed = True
    for check_name, passed in checks:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{check_name}: {status}")
        if not passed:
            all_passed = False
    
    print()
    
    if all_passed:
        print("🎉 ALL CHECKS PASSED!")
        print("✨ Repository siap untuk GitHub Actions!")
        print()
        print("Next Steps:")
        print("1. git add .")
        print("2. git commit -m 'Initial setup for automated preprocessing'")
        print("3. git push origin main")
        print("4. Check GitHub Actions tab untuk workflow execution")
        return 0
    else:
        print("🚨 SOME CHECKS FAILED!")
        print("❌ Harap perbaiki error di atas sebelum push ke GitHub")
        return 1

if __name__ == "__main__":
    sys.exit(main())
