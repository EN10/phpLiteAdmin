# phpLiteAdmin

phpLiteAdmin on github codespaces based on [cs50](https://github.com/cs50/codespace/tree/main/opt/cs50/phpliteadmin)

## Install

```
git clone https://github.com/eniompw/phpLiteAdmin
mkdir -p /opt/cs50/phpliteadmin/
cd phpLiteAdmin
mv ./share/ /opt/cs50/phpliteadmin/
sudo apt update
sudo apt install phpliteadmin
pip install termcolor
```
## Run
```
touch test.db
python phpliteadmin.py test.db
```
