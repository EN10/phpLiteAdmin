# download code files
git clone https://github.com/eniompw/phpLiteAdmin
cd phpLiteAdmin
# move linked php and css files
sudo mkdir -p /opt/cs50/phpliteadmin/
sudo mv ./share/ /opt/cs50/phpliteadmin/
# make phpliteadmin executable
chmod +x phpliteadmin.py
# add to path, allows running by name only
sudo mv phpliteadmin.py /usr/local/bin
# remove unneeded code
rm ../phpLiteAdmin -fr
cd ..
# install requirements
pip install termcolor
sudo apt update
sudo apt install phpliteadmin -y
sudo apt install python-is-python3 -y
