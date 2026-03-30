## MyST

- [MyST parser](https://myst-parser.readthedocs.io/en/latest/)
- [MyST](https://mystmd.org/)

### Markdown

Why Markdown matters for documentation:

- Widely adopted: used by GitHub, GitLab, Jupyter, and most modern platforms
- Readable as plain text, even without rendering
- Low barrier to entry for contributors unfamiliar with reStructuredText
- Enables documentation to live closer to code in the same ecosystem

### Markdown Example

```markdown
# Title

A paragraph with **bold**, *italic*, and `inline code`.

- First item
- Second item

[Link](https://example.com)

![Image alt text](image.png)
```

### Markdown Dialects

Not all Markdown is equal — several dialects exist:

- **CommonMark**: standardised, minimal spec; the base most dialects build on
- **GitHub Flavored Markdown (GFM)**: adds tables, task lists, and strikethrough
- **Pandoc Markdown**: rich extension set targeting multi-format conversion
- **MyST (Markedly Structured Text)**: designed specifically for technical and scientific documentation with Sphinx

### MyST

MyST bridges Markdown and Sphinx's full power:

- Superset of CommonMark — any valid Markdown is valid MyST
- Supports all Sphinx **directives** and **roles** using Markdown-friendly syntax
- First-class support for cross-references, math, and code execution (via Jupyter)
- Allows teams to write Sphinx documentation without learning reStructuredText

### MyST Origins

- Created by the [Executable Books Project](https://executablebooks.org/) in 2020
- Born from the need to write Sphinx documentation in Markdown for Jupyter Book
- Maintained as part of the broader scientific and technical publishing ecosystem
- `myst-parser` is the Sphinx extension that enables MyST in any Sphinx project

### Migrating from reStructuredText

`rst-to-myst` is a tool that automates conversion of `.rst` files to MyST Markdown:

```bash
# Install
pip install rst-to-myst

# Convert a single file
rst2myst convert docs/index.rst

# Convert all rst files in a directory
rst2myst convert docs/**/*.rst
```

Output is valid MyST — directives, roles, and cross-references are all preserved.


