## CI/CD Deployment

Sphinx docs can be built and published automatically on every push:

- Both **GitHub Pages** and **GitLab Pages** are supported
- Triggered on changes to `docs/**` on `main`/`master`
- Builds versioned docs for each git tag + a `latest` snapshot
- Requires a `docs/requirements.txt` listing Sphinx dependencies

- Example repo: <https://github.com/biocorecrg/introduction-containers-course/>

### GitHub Pages

- Example: [pages.yml](https://github.com/biocorecrg/introduction-containers-course/blob/main/.github/workflows/pages.yml)

```yaml
name: Deploy Sphinx documentation to Pages

on:
  push:
    branches: [main]
    paths: ['docs/**']

permissions:
  pages: write
  id-token: write

jobs:
  pages:
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r docs/requirements.txt && cd docs && make html
      - uses: actions/upload-pages-artifact@v4
        with:
          path: site
      - uses: actions/deploy-pages@v4
```

### GitLab Pages

- Example: [.gitlab-ci.yml](https://github.com/biocorecrg/introduction-containers-course/blob/main/.gitlab-ci.yml) 

```yaml
image: python:3.12

stages: [build, deploy]

sphinx:
  stage: build
  script:
    - pip install -r docs/requirements.txt
    - cd docs && make html && cd ..
    - cp -r docs/_build/html site/latest
  artifacts:
    paths: [site]
  only: [main]

pages:
  stage: deploy
  dependencies: [sphinx]
  script:
    - mv site public
  artifacts:
    paths: [public]
  only: [main]
```

### Test in local

`conf.py` and `Makefile` needed

````
pyenv virtualenv 3.12.11 mysphinxenv

cd docs # Go to docs directory

pip install -r requirements.txt

make html

# Go to _build directory and check result...

````

