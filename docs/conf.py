# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Abruan'
copyright = '2023 - 2024 Anubhav Gupta. All rights reserved'
author = 'Anubhav Gupta'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['source/_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'source/css/custom.css',
]
html_logo = 'source/_images/abruan-logo.png'
html_theme_options = {
    # 'logo': {
    #     'text': 'AbRuAn Logo',
    # },
    'logo_only': False,
    'display_version': True,
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'style_nav_header_background': 'goldenrod',
}