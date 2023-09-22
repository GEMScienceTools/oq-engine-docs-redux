# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenQuake Engine'
copyright = '2023, GEM Foundation'
author = 'GEM Foundation'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_favicon = "_static/OQ-Logo-favicon.png"
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "logo": {
           "image_light": "_static/OQ-Logo-Standard-RGB-72DPI-01-transparent.png",
           "image_dark": "_static/OQ-Logo-Inverted-RGB-72DPI-01.jpg",
        },
    "icon_links": [
        {
            # Label for this link
            "name": "GEM",
            # URL where the link will redirect
            "url": "https://www.globalquakemodel.org/gem",  # requiredx"
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "_static/GEM-LOGO-Plain-RGB-72DPI-01.png",
            # The type of image to be used (see below for details)
            "type": "local",
        },
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/gem/oq-engine",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "Linkedin",
            # URL where the link will redirect
            "url": "https://it.linkedin.com/company/gem-foundation",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-linkedin",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "Twitter",
            # URL where the link will redirect
            "url": "https://twitter.com/GEMwrld",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "_static/square-x-twitter.png",
            # The type of image to be used (see below for details)
            "type": "local",
        },
        {
            # Label for this link
            "name": "Youtube",
            # URL where the link will redirect
            "url": "https://www.youtube.com/channel/UCfvGcHtZYk_kQ_mqz3AYQYQ",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-youtube",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            # Label for this link
            "name": "Facebook",
            # URL where the link will redirect
            "url": "https://www.facebook.com/GEMwrld/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-facebook",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ]
}
html_context = {
   "default_mode": "light"
}
extensions = [
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx.ext.autosectionlabel',
    'sphinxcontrib.images',
    'sphinxcontrib.youtube'
]
