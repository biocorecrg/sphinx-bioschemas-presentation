## Challenges & Future Work

### Validation at Build Time (or CI/CD)

- Validate YAML/JSON against Schema.org and Bioschemas profiles during `make html`
- Warn or fail when required fields are missing for a given profile
- Check that `@id` URIs resolve — dead metadata link detection

### Richer Metadata Types

Beyond `LearningResource` / `TrainingMaterial`.

**Important**: integrate data and software in the same documentation repository

- `Dataset` — for data-heavy documentation sites
- `SoftwareSourceCode` — for software/tool documentation
- `ComputationalWorkflow` — for Nextflow, Snakemake, CWL pipeline docs

### Automatic Metadata

Reduce manual effort by deriving values from the repo:

- `dateModified` from the last git commit timestamp
- `version` from git tags

