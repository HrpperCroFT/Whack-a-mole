#!/bin/bash

python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
python3 -m pip install "kivy[base]" kivy_examples
python3 main.py
