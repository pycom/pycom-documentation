# run locally

```
brew install hugo
hugo serve
```

# Workflow

## Make documentation update
- Checkout your branch from `master` and commit and push your changes
- Make a PR against `master` branch (implicitly set as `master` branch is our default branch) 
- Assign a reviewer and let your PR to be merged

## Deploy changes
- Make PR from `master` against `publish` branch
- Assign a reviewer and let your PR to be merged
- docs were updated

# Quickrefs

- master -> publish -> https://publish.d1rmdw1xyxqk1e.amplifyapp.com/ -> https://docs.pycom.io
- development -> development-publish -> https://development-publish.d2aq2bahs3kibc.amplifyapp.com/ -> https://development.pycom.io

# some infos:

- assets are in ./static directory, a directory aliased at /
- css in /themes/doc-theme/static/doc-theme.css
- SUMMARY.md is in config.toml


# help

- gohugo.io


# detect broken links

```
wget -o 404.txt -r  --spider http://localhost:1313
```
