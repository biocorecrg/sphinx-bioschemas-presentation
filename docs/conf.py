# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

import yaml
from myst_parser import __version__
from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset
from sphinx_revealjs.utils import get_revealjs_path

project = "Sphinx and embedding Bioschemas"
copyright = "2026, Centre for Genomic Regulation (CRG)"
author = "Toni Hermoso Pulido"

html_title = "Introduction to Sphinx - embedding schemas.org/Bioschemas metadata"

version = "2026.04.01"
release = version

# -- Matomo configuration ---------------------------------------------------

matomo_url = "//stats.biocore.crg.eu/"
matomo_site_id = "24"

html_context = {
    "matomo_url": matomo_url,
    "matomo_site_id": matomo_site_id,
}

bioschemas = ["schemaorg.yaml"]


# -- Options for Reveal.js output ---------------------------------------------
revealjs_html_theme = "revealjs-simple"
revealjs_static_path = ["_static"]
revealjs_style_theme = "custom.css"
revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "hash": True,
    "center": True,
    "transition": "slide",
}
revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs/plugin/math/math.js",
    },
    {
        "name": "RevealCustomControls",
        "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/plugin.js",
    },
]

# - sphinx_revealjs.ext.sass
revealjs_sass_src_dir = "_sass"
revealjs_sass_out_dir = "_static"
revealjs_sass_targets = {}
revealjs_sass_include_paths = [
    get_revealjs_path() / "css" / "theme",
]
revealjs_sass_auto_targets = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_bioschemas",
    "myst_parser",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.footnotes",
    "sphinx_revealjs.ext.sass",
]

source_suffix = [".rst", ".md"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
# html_css_files = ["custom.css"]


myst_enable_extensions = [
    "colon_fence",
    "html_admonition",
    "html_image",
    "linkify",
    "substitution",
]
myst_enable_checkboxes = True
myst_substitutions = {"data_version": "latest"}


def copy_assets(app, exception):
    if app.builder.name != "html" or exception:
        return
    for asset_dir in ["images", "data"]:
        src = os.path.abspath(asset_dir)
        dst = os.path.join(app.outdir, asset_dir)
        if os.path.exists(src):
            copy_asset(src, dst)


def setup(app: Sphinx):
    """Add functions to the Sphinx setup."""
    # from myst_parser._docs import (
    #     MystAdmonitionDirective,
    # )
    #
    # app.add_directive("myst-admonitions", MystAdmonitionDirective)
    app.connect("build-finished", copy_assets)
