#!/bin/bash

# Download and install MkDocs
pip install mkdocs

# Download and install plugins
pip install mkdocs-material
pip install pymdown-extensions
pip install mkdocs-encryptcontent-plugin   # 您需要的插件

# Run MkDocs build
mkdocs build
