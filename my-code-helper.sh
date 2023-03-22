#!/bin/bash
# set path to the directory where this script is located
s_path=$(dirname "$0")
# wrapper for src/gpt.py
# set the prompt
s_prompt=$1
#run the python script
python3 $s_path/src/gpt.py "$s_prompt"