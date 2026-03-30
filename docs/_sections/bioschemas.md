## Bioschemas Sphinx extension

- [Pypi package](https://pypi.org/project/sphinx-bioschemas/)
- [Project page](https://github.com/biocorecrg/sphinx-bioschemas)
- [Documentation](https://biocorecrg.github.io/sphinx-bioschemas/)

### Motivation

- Simplify the process of including [Schema.org](https://schema.org/docs/schemas.html) or [Bioschemas profiles](https://bioschemas.org/profiles/)
- Allow embedding JSON+LD in a simpler way (YAML) 
- Enable Sphinx as a metadata-friendly framework as *Jekyll* or *Mkdocs*

## Embedding

### Global

Applies Bioschemas markup to every page automatically via `conf.py`:

```python
extensions = [
    "sphinx_bioschemas",
    "myst_parser",
]

# List of YAML or JSON files with schema markup
bioschemas = ["bioschemas.yaml"]
```

### Global

Example `bioschemas.yaml`:

```yaml
"@context": https://schema.org/
"@type": LearningResource
"@id": https://example.org/docs/
name: My Documentation
description: A Sphinx-based documentation site with Bioschemas metadata
license: MIT
```

### Page-specific

Added per page using the `{bioschemas}` directive — appends to global markup, does not replace it:

````markdown
```{bioschemas}
:format: yaml

"@context": https://schema.org/
"@type": LearningResource
"@id": https://example.org/docs/my-page
http://purl.org/dc/terms/conformsTo:
  - "@type": CreativeWork
    "@id": https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE
name: My Page
author:
  - "@type": Person
    name: Jane Doe
keywords: sphinx, bioschemas, FAIR
```
````

### Page-specific

Or by pointing to an external file:

````markdown
```{bioschemas} ./page-bioschemas.yaml
```
````
