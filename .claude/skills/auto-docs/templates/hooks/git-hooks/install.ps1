# install.ps1 — Windows installer for git hooks.
# Run from repo root: .\.githooks\install.ps1

$RepoRoot = git rev-parse --show-toplevel
$HookSrc  = Join-Path $RepoRoot ".githooks"
$HookDst  = Join-Path $RepoRoot ".git\hooks"

if (-not (Test-Path $HookDst)) {
    Write-Host "❌ .git\hooks not found. Are you in a git repository?"
    exit 1
}

# Use the .ps1 variants on Windows — git on Windows runs them via Git Bash
# We copy the unix-style hook but it should call PowerShell internally.
# Simpler: copy a wrapper that invokes the .ps1 script.

$hooks = @{
    "post-commit" = "post-commit.ps1"
    "pre-push"    = "pre-push"
}

foreach ($hook in $hooks.Keys) {
    $src = Join-Path $HookSrc $hook
    $dst = Join-Path $HookDst $hook

    if (Test-Path $src) {
        Copy-Item $src $dst -Force
        Write-Host "✅ Installed: $hook"
    }

    # Also copy the .ps1 variant for PowerShell-based hook execution
    $psSrc = Join-Path $HookSrc $hooks[$hook]
    if (Test-Path $psSrc) {
        $psDst = Join-Path $HookDst $hooks[$hook]
        Copy-Item $psSrc $psDst -Force
    }
}

Write-Host ""
Write-Host "Git hooks installed. They fire on every commit and push."
Write-Host "To uninstall: Remove-Item .git\hooks\post-commit, .git\hooks\pre-push"
