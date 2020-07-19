sudo apt update && sudo apt upgrade -y

sudo apt install python3 python3-dev
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
sudo apt install python3-venv python3-pip

poetry env use python3


