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

A webhook has been installed on the publish branch to
https://publish.d20i0wkqbblkur.amplifyapp.com/
