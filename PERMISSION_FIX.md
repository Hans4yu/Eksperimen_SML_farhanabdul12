# GitHub Actions Permission Fix

## Issue Resolved
Fixed the "Permission denied" error when GitHub Actions tries to push processed files back to the repository.

## Changes Made

### 1. Added Workflow Permissions
```yaml
permissions:
  contents: write  # Allows reading and writing repository content
  actions: read    # Allows reading workflow actions
  checks: write    # Allows writing check results
```

### 2. Updated Git Push Command
Changed from:
```bash
git push
```

To:
```bash
git push origin HEAD:${{ github.ref_name }}
```

This explicitly specifies the target branch and uses the GitHub Actions context.

### 3. Simplified Git Configuration
```bash
git config --local user.email "action@github.com"
git config --local user.name "GitHub Action"
```

## How It Works

1. **`contents: write`** - Gives the GitHub Actions bot permission to modify repository files
2. **`HEAD:${{ github.ref_name }}`** - Pushes to the correct branch (main/master) using GitHub's built-in variables
3. **`GITHUB_TOKEN`** - Uses the automatically provided token for authentication

## Result
The workflow can now successfully:
- ✅ Process data automatically
- ✅ Commit processed files back to repository  
- ✅ Push changes without permission errors
- ✅ Maintain proper git history with meaningful commit messages

## Security Note
These permissions are scoped to the workflow only and follow GitHub's principle of least privilege.
