#!/bin/bash

grep -r \=\ param_find\(\" ./src > rawVarData
python ParameterMapGenerator.py
