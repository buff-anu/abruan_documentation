# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add the path to your Python module
sys.path.insert(0, os.path.abspath('../../examples/scenarios'))
sys.path.insert(0, os.path.abspath('../../src'))
sys.path.insert(0, os.path.abspath('../../src/architecture'))
sys.path.insert(0, os.path.abspath('../../src/architecture/messaging'))
sys.path.insert(0, os.path.abspath('../../src/simulation/environment'))
sys.path.insert(0, os.path.abspath('../../src/simulation/mechanics'))
sys.path.insert(0, os.path.abspath('../../src/simulation/mechanics/dynamics/_GeneralModuleFiles'))
sys.path.insert(0, os.path.abspath('../../src/simulation/mechanics/dynamics/optics'))
sys.path.insert(0, os.path.abspath('../../src/simulation/mechanics/dynamics/spacecraft'))
sys.path.insert(0, os.path.abspath('../../src/simulation/numerical_methods/integrators'))
sys.path.insert(0, os.path.abspath('../../src/utilities'))

# ... other configurations ...

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AbRuAn'
copyright = '2023 - 2025 Anubhav Gupta. All rights reserved'
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
html_logo = '_static/abruan-logo.svg'
html_favicon = "_static/abruan-favicon.svg"
html_theme_options = {
    # 'logo': {
    #     'text': 'AbRuAn Logo',
    # },
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': True
    # 'style_nav_header_background': 'goldenrod',
}

def setup(app):
    app.add_js_file('js/newtab.js')