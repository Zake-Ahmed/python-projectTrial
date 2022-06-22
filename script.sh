#! /bin/bash
git config --global user.name "Zake-Ahmed"
git config --global user.email "zake3012@gmail.com"

sudo apt update

sudo apt install python3 python3-venv python3-pip

python3 -m venv venv

activate () {
    . venv/bin/activate 
}

activate

pip3 install -r requirements.txt

python3 create.py 

python3 app.py 
