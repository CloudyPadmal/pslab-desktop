#!/bin/bash

# Define colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
ORANGE='\033[0;33m'
NOCOLOR='\033[0m'

echo -e "${GREEN}Welcome to PSLab Desktop app installer${NOCOLOR}"
echo -e "${YELLOW}Installing ...${NOCOLOR}"
apt-get update >/dev/null
# Install Python
echo -e "${ORANGE}Downloading Python 3.7.3${NOCOLOR}"
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
echo -e "${ORANGE}Extracting Python source file${NOCOLOR}"
tar -xvf Python-3.7.3.tgz >/dev/null
echo -e "${ORANGE}Removing source file${NOCOLOR}"
rm -rf Python-3.7.3.tgz >/dev/null
echo -e "${ORANGE}Installing GCC Compilers${NOCOLOR}"
apt-get install gcc -y
apt-get install zlib1g-dev -y
apt-get install libffi-dev -y
echo -e "${ORANGE}Move into Python folder${NOCOLOR}"
pushd Python-3.7.3
echo -e "${ORANGE}Execute installer scripts for Python 3.7.3${NOCOLOR}"
./configure >/dev/null
make >/dev/null
make install >/dev/null
# Install pip
apt-get install python3-pip -y >/dev/null
apt-get install python-dev build-essential -y >/dev/null
python3 -m pip install --upgrade pip >/dev/null
echo -e "${YELLOW}Setting up and upgrading pip is complete!${NOCOLOR}"
# Install PyQt5
python3 -m pip install pyqt5 >/dev/null
echo -e "${YELLOW}Setting up PyQt5 is complete!${NOCOLOR}"
# Install Numpy
python3 -m pip install numpy >/dev/null
python3 -m pip install numpy --upgrade >/dev/null
echo -e "${YELLOW}Setting up Numpy is complete!${NOCOLOR}"
# Install Serial libraries
python3 -m pip install pyserial >/dev/null
python3 -m pip install pyserial --upgrade >/dev/null
echo -e "${YELLOW}Setting up PySerial is complete!${NOCOLOR}"
# Install Dev Tools
apt-get install pyqt5-dev-tools -y >/dev/null
echo -e "${YELLOW}Setting up dev tools is complete!${NOCOLOR}"
# Install PyQt Graph
python3 -m pip install pyqtgraph >/dev/null
echo -e "${YELLOW}Setting up PyQt Graph is complete!${NOCOLOR}"
# Install SIP packages
python3 -m pip install PyQt5-sip >/dev/null
echo -e "${YELLOW}Setting up PyQt-SIP is complete!${NOCOLOR}"
# Install Webengine for HTML rendering
python3 -m pip install PyQtWebEngine >/dev/null
echo -e "${YELLOW}Setting up PyQtWebEngine is complete!${NOCOLOR}"
# Install PyOpenGl
python3 -m pip install PyOpenGL >/dev/null
echo -e "${YELLOW}Setting up PyOpenGL is complete!${NOCOLOR}"
# Install QtOpenGl
apt-get install python-qt5-gl -y >/dev/null
echo -e "${YELLOW}Setting up QtOpenGl is complete!${NOCOLOR}"
# Install iPython Console
python3 -m pip install qtconsole >/dev/null
echo -e "${YELLOW}Setting up qtconsole is complete!${NOCOLOR}"
# Clone Desktop apps and Python repos
apt-get install git -y >/dev/null
echo -e "${YELLOW}Setting up git is complete!${NOCOLOR}"
cd /opt/
git clone -b development https://github.com/fossasia/pslab-desktop.git
git clone -b development https://github.com/fossasia/pslab-python.git

# cd into Python repo and install
echo -e "${YELLOW}Cloning repositories is now complete! Let's start installation!${NOCOLOR}"
echo -e "${YELLOW}Installing Python Communication Library ...${NOCOLOR}"
cd /opt/pslab-python
make clean
make
make install
echo -e "${YELLOW}Python Communication Library installed!${NOCOLOR}"

# cd into Desktop apps repo and install
echo -e "${YELLOW}Installing desktop application ...${NOCOLOR}"
cd /opt/pslab-desktop
make clean
make
make install
echo -e "${YELLOW}Python Desktop application installed!${NOCOLOR}"
