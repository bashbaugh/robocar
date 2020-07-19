# Raspberry pi installation script
# Not all of these packages are used but I found it easier to just install them all

sudo apt update && sudo apt upgrade -y

sudo apt install build-essential cmake pkg-config

sudo apt install python3-dev
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
sudo apt install python3-venv python3-pip

cd robocar
poetry env use python3
poetry install

sudo apt install python3-opencv

sudo apt autoremove

cd ..