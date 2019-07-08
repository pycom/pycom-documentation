# run locally

```
brew install hugo
hugo serve
```

# Workflow

- Make PR using Master branch
- PR get merged on master
- Then merge publish with master

```
git commit -m "section: commit message"
git push origin master
git checkout publish
git merge master
git push origin publish
```

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
