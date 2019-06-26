<<<<<<< HEAD
# At this moment deprecated in favor of <a target="_blank" href="https://github.com/pycom/pydocs">pydocs</a>.

This project is based on Gitbook, new docs are based on Github pages.

# Introduction
=======
# run locally
>>>>>>> publish

```
brew install hugo
hugo serve
```

# Workflow

<<<<<<< HEAD
* [Products](products.md)
* [Getting Started](getting-started/introduction.md)
* [Pymakr](pymakr-plugin/installation/)
* [Tutorials](tutorials-and-examples/introduction.md)
* [API Documentation](firmware-and-api-reference/introduction.md)
* [Product Info](product-info-datasheets/introduction.md)
* [Pybytes](pybytes/introduction.md)
=======
- Make PR using Master branch
- PR get merged on master
- Then merge publish with master
>>>>>>> publish

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

A webhook has been installed on the publish branch to:
- https://publish.d1rmdw1xyxqk1e.amplifyapp.com/
