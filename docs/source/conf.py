# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "modelz-py"
copyright = "2023, TensorChord"
author = "TensorChord"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_click",
]

templates_path = ["_templates"]
exclude_patterns = []
master_doc = "index"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ["_static"]
html_theme_options = {
    "github_url": "https://github.com/tensorchord/modelz-py",
    "discord_url": "https://discord.gg/KqswhpVgdU",
    "twitter_url": "https://twitter.com/tensorchord",
}
html_context = {
    "source_type": "github",
    "source_user": "tensorchord",
    "source_repo": "modelz-py",
}
