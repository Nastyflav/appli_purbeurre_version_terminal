# Pur Beurre, what is it ?
----------------
Pur Beurre is an application using the open database provided by [Open Food Facts](https://world.openfoodfacts.org/).
By using Pur Beurre, you'll be able to find a substitute for a food product, with better nutritive grades and higher 
quality. The programm also leaves you with the possibility of saving all your query results in your database.

# What do Pur Beurre really does ?
----------------
By launching Pur Beurre the following steps will happen :
	- a local database with datas from [Open Food Facts](https://world.openfoodfacts.org/) will be installed
	- you'll be able to search in this database a certain amount of products and their substitutes
	- a saving function is built to allow you to save all your favorites substitutes in your database

# How to install and launch :
--------------
Clone with https : https://github.com/Nastyflav/pur_beurre_OC.git \
or clone with SSH : git@github.com:Nastyflav/pur_beurre_OC.git \
into a repo on your local machine \
Documentation about pull --> https://help.github.com/en/articles/cloning-a-repository 

Set your virtual environment under python3.7.x `pip install virtualenv`\
Create an new virtual environment `virtualenv -p python env`\
Activate it `source env/Scripts/activate.bat`\
Install requirements `pip install -r requirements.txt`\
Write `main_program.py` in your terminal 

## Dependancies :
--------------
Python 3.7.x \
download : https://www.python.org/downloads/ \
install : https://realpython.com/installing-python/ 

MySQL \
download : https://dev.mysql.com/downloads/mysql/#downloads \
install : https://www.mysqltutorial.org/install-mysql/
**Please be sure remembering your host name, your user name and your password, to allow access for the program to your MySQL**

Depending of your python's install, you might need PIP\
install pip : https://packaging.python.org/tutorials/installing-packages/

## Modules :
--------------
main_program.py\
db_init.sql creates the database in the user's system
Models/ contains all the different classes and the app functions\
Settings/ contains constants.py\

## Built with :
--------------
Visual Studio Code (IDE)\
Python 3.7.5\
UTF-8

## Author :
--------------
Flavien Murail : https://github.com/Nastyflav

