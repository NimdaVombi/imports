echo This script installs the necessary packages for main.py to function properly. 
rm -rf imports
git clone https://github.com/NimdaVombi/imports.git
pip install PySimpleGUI
echo Updated. Running main.py
python3 imports/main.py
