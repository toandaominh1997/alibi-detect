# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# Hide RemovedInSphinx40Warning. Can remove once upgraded to sphinx>=4.0
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "alibi-detect"
copyright = "2019, Seldon Technologies Ltd"
author = "Seldon Technologies Ltd"

# The short X.Y version
# import alibi_detect
exec(open("../../alibi_detect/version.py").read())

version = __version__
# The full version, including alpha/beta/rc tags
release = __version__

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.apidoc",  # automatically generate API docs, see https://github.com/rtfd/readthedocs.org/issues/1139
    "sphinxcontrib.bibtex",
    "nbsphinx",
    "myst_parser",
    "sphinx_design",
]

# -- nbsphinx settings -------------------------------------------------------
nbsphinx_execute = "auto"

# Create symlinks for example notebooks
import glob
nb_files = [os.path.basename(f) for f in glob.glob(os.path.join('examples','*.ipynb')) 
        if not os.path.basename(f).startswith('temp_')]
for nb_file in nb_files:
    target = os.path.join('../../examples', nb_file)
    if os.path.exists(target):
        os.remove(target)
    os.symlink(os.path.join('../doc/source/examples', nb_file), target)

# -- Bibliography ------------------------------------------------------------
bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrtalpha'

# apidoc settings
apidoc_module_dir = "../../alibi_detect"
apidoc_output_dir = "api"
apidoc_excluded_paths = ["**/*test*"]
apidoc_module_first = True
apidoc_separate_modules = True
apidoc_extra_args = ["-d 6"]

# mock imports
# numpy, pandas and matplotlib are not included as these are installed on 
# ReadTheDocs PYTHON_VERSION_39 docker image (https://hub.docker.com/r/readthedocs/build/dockerfile/)
autodoc_mock_imports = [
    "sklearn",
    "skimage",
    "requests",
    "cv2",
    "bs4",
    "keras",
    "seaborn",
    "PIL",
    "tensorflow",
    "spacy",
    "tensorflow_probability",
    "scipy",
    "fbprophet",
    "torch",
    "transformers",
    "tqdm",
    "dill",
    "numba",
    "pydantic",
    "toml",
    "catalogue",
    "pykeops"
]

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]
# source_suffix = '.rst'

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = '_static/Alibi_Detect_Logo_white.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"logo_only": True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# override default theme width
html_css_files = ['theme_overrides.css', 'custom_docs.css'] # override wide tables in RTD theme

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "alibi-detectdoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    #
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    #
    # Additional stuff for the LaTeX preamble.
    # - Replace unicode characters with utf8. 
    #   (U+2588 and U+258E are used in tqdm progress bars)
    # - Use enumitem for lists to prevent "too deeply nested" latex error
    'preamble': r''' 
        \DeclareUnicodeCharacter{2588}{=}
        \DeclareUnicodeCharacter{258E}{|} 
        \DeclareUnicodeCharacter{274C}{$\times$} 
        \DeclareUnicodeCharacter{2705}{$\checkmark$} 

        \usepackage{enumitem}
        \setlistdepth{99}
        ''',
    #
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "alibi-detect.tex", "alibi-detect Documentation", "Seldon Technologies Ltd", "manual")]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "alibi-detect", "alibi-detect Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "alibi-detect", "alibi-detect Documentation", author, "alibi-detect", "One line description of project.", "Miscellaneous")
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
        'python': ('https://docs.python.org/', None),
        'sklearn': ('https://scikit-learn.org/stable/', None),
        }

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- nbsphinx prolog ---------------------------------------------------------
# from https://github.com/vidartf/nbsphinx-link/blob/master/docs/source/conf.py for custom tags
import subprocess

try:
    git_rev = subprocess.check_output(["git", "describe", "--exact-match", "HEAD"], universal_newlines=True)
except subprocess.CalledProcessError:
    try:
        git_rev = subprocess.check_output(["git", "rev-parse", "HEAD"], universal_newlines=True)
    except subprocess.CalledProcessError:
        git_rev = ""
if git_rev:
    git_rev = git_rev.splitlines()[0] + "/"

nbsphinx_prolog = (
    r"""
{% set docname = env.doc2path(env.docname, base=False) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html
    
    .. nbinfo::
        This page was generated from `{{ docname }}`__.
    
    __ https://github.com/SeldonIO/alibi-detect/blob/
        """
    + git_rev
    + "doc/source/"
    + r"{{ docname }}"
)

# -- Override order of preference for image formats --------------------------
# Need to set gif above png so that it is chosen over png if present
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]

# -- myst-parser configuration -----------------------------------------------
# See https://myst-parser.readthedocs.io/en/stable/syntax/optional.html for 
# details of available extensions.
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
    "smartquotes",
    "tasklist",
    "html_image",
]

# Create heading anchors for h1 to h3 (useful for local toc's)
myst_heading_anchors = 3

# Below code fixes a problem with sphinx>=3.2.0 processing functions with
# torch.jit.script decorator. Probably occuring because torch is being mocked
# (see https://github.com/sphinx-doc/sphinx/issues/6709).
def call_mock(self, *args, **kw):
    from types import FunctionType, MethodType
    if args and type(args[0]) in [type, FunctionType, MethodType]:
        # Appears to be a decorator, pass through unchanged
        return args[0]
    return self

from sphinx.ext.autodoc.mock import _MockObject
_MockObject.__call__ = call_mock

