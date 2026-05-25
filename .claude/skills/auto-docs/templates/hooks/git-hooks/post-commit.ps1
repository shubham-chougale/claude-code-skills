# post-commit.ps1 — Windows PowerShell variant of post-commit hook.
# Installed by: .\.githooks\install.ps1

$ErrorActionPreference = 'SilentlyContinue'

$RepoRoot = git rev-parse --show-toplevel
Set-Location $RepoRoot

# Resolve python
$Python = $null
if (Get-Command python -ErrorAction SilentlyContinue) { $Python = 'python' }
elseif (Get-Command python3 -ErrorAction SilentlyContinue) { $Python = 'python3' }
else {
    Write-Host "Python not found. Doc hooks skipped."
    exit 0
}

# Skip if last commit only touched CHANGELOG
$LastFiles = git diff --name-only HEAD~1 HEAD
if ($LastFiles -eq "CHANGELOG.md") { exit 0 }

# 1. Append CHANGELOG
& $Python .claude/hooks/scripts/update_changelog.py

# 2. Amend CHANGELOG into the commit if it changed
git diff --quiet CHANGELOG.md
if ($LASTEXITCODE -ne 0) {
    git add CHANGELOG.md
    $env:GIT_HOOKS_DISABLE = "1"
    git commit --amend --no-edit --no-verify | Out-Null
    Remove-Item Env:GIT_HOOKS_DISABLE
}

# 3. Print doc impact report
& $Python .claude/hooks/scripts/detect_changes.py

exit 0
