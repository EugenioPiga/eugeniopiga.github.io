# Deployment checklist (GitHub Pages)

Use this to publish the updated site so `https://eugeniopiga.github.io/` shows the new version.

## 0) First: run commands inside the repository folder

```bash
cd ~/eugeniopiga.github.io
pwd
git status
```

If `pwd` is your home folder (`/c/Users/...`) and `git status` lists personal files (Downloads, AppData, etc.), you are in the wrong directory.

## 1) Set remote (HTTPS recommended)

```bash
git remote set-url origin https://github.com/EugenioPiga/eugeniopiga.github.io.git
git remote -v
```

(If remote does not exist: `git remote add origin https://github.com/EugenioPiga/eugeniopiga.github.io.git`)

## 2) Push website changes

```bash
git checkout work
git push -u origin work
```

## 3) Merge to `main` and push

```bash
git checkout main
git pull --ff-only origin main
git merge --ff-only work
git push origin main
```

## 4) Verify GitHub Pages settings

In repository settings → **Pages**:
- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/ (root)` **or** `/docs`

This repository has a root `index.html` redirect to `docs/index.html`, so either folder configuration should reach the updated site.

## 5) Confirm live site

Open:
- `https://eugeniopiga.github.io/`
- `https://eugeniopiga.github.io/docs/index.html`

Hard-refresh (Cmd/Ctrl+Shift+R) if needed.

## Troubleshooting

- `src refspec ... does not match any`: you are in the wrong folder or branch has no commits.
- `Permission denied (publickey)`: use HTTPS remote above instead of SSH.
- `index.lock exists`: remove lock in that repo: `rm -f .git/index.lock`.
