#!/bin/bash


while true
do
rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 Speech/data/ep/test.wav
python Speech/src/jp_speech.py Speech/data/ep
python Speech/src/convert_utf-8.py Speech/data/ep_text

python src/voice_strip_n.py Speech/data/ep_text/scripts.txt 
python text_summarization/generate_data.py --input_dir=text_summarization/voice_train --data_path=text_summarization/voice_binary_train/NE109

python text_summarization/seq2seq_attention.py --vocab_path=text_summarization/data/jp_vocab --data_path=text_summarization/voice_binary_train/NE109 --article_key=article --mode=decode --abstract_key=abstract --log_root=textsum/log_root --decode_dir=textsum/log_root/decode --beam_size=1
continue
done
