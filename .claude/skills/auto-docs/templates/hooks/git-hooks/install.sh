#!/usr/bin/env bash
# install.sh — One-time installer that copies hooks into .git/hooks/
# Run from repo root: bash .githooks/install.sh

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOK_SRC="$REPO_ROOT/.githooks"
HOOK_DST="$REPO_ROOT/.git/hooks"

if [ ! -d "$HOOK_DST" ]; then
    echo "❌ .git/hooks not found. Are you in a git repository?"
    exit 1
fi

# Copy and make executable
for hook in post-commit pre-push; do
    if [ -f "$HOOK_SRC/$hook" ]; then
        cp "$HOOK_SRC/$hook" "$HOOK_DST/$hook"
        chmod +x "$HOOK_DST/$hook"
        echo "✅ Installed: $hook"
    fi
done

echo ""
echo "Git hooks installed. They will fire on every commit and push."
echo "To uninstall: rm .git/hooks/post-commit .git/hooks/pre-push"
