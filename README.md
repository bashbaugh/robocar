# robocar
My voice-controlled model self-driving car-robot

Inspired by Donkey Car.

`io-board` contains files and source code for the Atmega328 on the IO control board.

`robocar` contains the Robocar software, written in Python

`app` contains the Vue app that the car serves

`trainer` contains the program for training bahavioural cloning and reinforcement learning models for the car.

`scripts` contains useful scripts for installing software, etc.

### App

Node.js and Yarn must be installed to develop the app. Install all dependencies by typing `yarn install` in the app folder.

After building the app with `yarn build`, the dist folder must be moved to `robocar/app_dist` so that the python program can serve it, e.g. `rm robocar/app_dist -r && mv app/dist robocar/app_dist`

### Scripts

`pi-install.sh` installs the required software and dependencies on the Raspberry Pi.

`host-install.sh` installs the required software and dependencies on an apt-based host system.

`dev-install.sh` installed the required software and dependencies for building the app