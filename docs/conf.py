# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import django
 
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'digidiagno.settings' 
os.environ['SECRET_KEY'] = 'your_django_project_secret_key'
django.setup()
...
extensions = [
 'sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc'
]

project = 'Diagnotech-Servicereport-Software'
copyright = '2024, Dibas Pratap Basnet'
author = 'Dibas Pratap Basnet'
release = 'version 1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
