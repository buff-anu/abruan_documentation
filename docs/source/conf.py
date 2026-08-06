# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Configuration file for the Sphinx documentation builder.

import os
import sys

PROJECT_ROOT = os.path.abspath("../..")
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")
ABRUAN_ROOT = os.path.join(SRC_ROOT, "abruan")
SCENARIOS_ROOT = os.path.join(PROJECT_ROOT, "scripts", "scenarios")

# Proper package import support:
# import abruan.utilities.aero_optics
sys.path.insert(0, SRC_ROOT)

# Existing scenario imports.
sys.path.insert(0, SCENARIOS_ROOT)

# Compatibility for short autodoc names such as:
# .. automodule:: aero_optics
# .. automodule:: sys_model
for directory, subdirectories, files in os.walk(ABRUAN_ROOT):
    if any(filename.endswith(".py") for filename in files):
        sys.path.insert(0, directory)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AbRuAn'
copyright = '2023 - 2026 Anubhav Gupta. All rights reserved'
author = 'Anubhav Gupta'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    # 'sphinxcontrib.bibtex',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]
html_logo = '_images/abruan-logo.png'
html_theme_options = {
    # 'logo': {
    #     'text': 'AbRuAn Logo',
    # },
    'logo_only': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
    # 'style_nav_header_background': 'goldenrod',
}

def setup(app):
    app.add_js_file('js/newtab.js')