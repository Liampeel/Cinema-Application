#!/bin/sh

cd Flask
rm -r flask
virtualenv flask
cd flask
source bin/activate
cd ../app
echo $'Installing libraries from requirements.txt (this may take a minute!)'
pip install -q -r requirements.txt
module add anaconda3
cd ..
mv flask/lib64/python2.7/site-packages/selenium* flask/lib64/python3.6/site-packages/
cp ../lib/geckodriver flask/lib64/python3.6/site-packages/selenium
python3 run.py
