#!/bin/bash


while true
do
rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 Speech/data/ep/test.wav
python Speech/src/jp_speech.py Speech/data/ep
python Speech/src/convert_utf-8.py Speech/data/ep_text

#Extract Information
python RB/main_model2.py Speech/data/ep_text/scripts.txt

#Update view

continue
done
