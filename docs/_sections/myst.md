# MyST

## Markdown

Why Markdown matters for documentation:

- Widely adopted: used by GitHub, GitLab, Jupyter, and most modern platforms
- Readable as plain text, even without rendering
- Low barrier to entry for contributors unfamiliar with reStructuredText
- Enables documentation to live closer to code in the same ecosystem

## Markdown Example

```markdown
# Title

A paragraph with **bold**, *italic*, and `inline code`.

- First item
- Second item

[Link](https://example.com)

![Image alt text](image.png)
```

## Markdown Dialects

Not all Markdown is equal — several dialects exist:

- **CommonMark**: standardised, minimal spec; the base most dialects build on
- **GitHub Flavored Markdown (GFM)**: adds tables, task lists, and strikethrough
- **Pandoc Markdown**: rich extension set targeting multi-format conversion
- **MyST (Markedly Structured Text)**: designed specifically for technical and scientific documentation with Sphinx

## MyST

MyST bridges Markdown and Sphinx's full power:

- Superset of CommonMark — any valid Markdown is valid MyST
- Supports all Sphinx **directives** and **roles** using Markdown-friendly syntax
- First-class support for cross-references, math, and code execution (via Jupyter)
- Allows teams to write Sphinx documentation without learning reStructuredText

