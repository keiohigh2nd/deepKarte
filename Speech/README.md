#Recording  
rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 test.wav  
#Speech Recgnition  
python Speech/src/jp_speech.py data/ep 
#sum up texts to script  
python Speech/src/convert-utf_8.py data/ep  
#Separate dialogue and put them each content(symptom, family, medicaiton etc..) -> into Json  
python Speech/src/separate_dialogue.py Speech/data/ep7/scripts.txt  
#From Json, make html  
python Speech_UI/app.py Speech/karte/karte_ep7.json  

