#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate
python -m pip install "kivy[base]" kivy_examples
python3 main.py