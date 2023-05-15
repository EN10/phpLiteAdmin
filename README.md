# phpLiteAdmin

phpLiteAdmin on github codespaces based on [cs50](https://github.com/cs50/codespace/tree/main/opt/cs50/phpliteadmin)

## Install

```
git clone https://github.com/eniompw/phpLiteAdmin
cd phpLiteAdmin
mkdir -p /opt/cs50/phpliteadmin/
mv ./share/ /opt/cs50/phpliteadmin/
chmod +x phpliteadmin.py
mv phpliteadmin.py /usr/local/bin
rm ../phpLiteAdmin/ -fr
sudo apt update
sudo apt install phpliteadmin
pip install termcolor
```
## Run
```
touch test.db
phpliteadmin.py test.db
```
