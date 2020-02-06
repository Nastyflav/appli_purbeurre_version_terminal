# Pur Beurre, what is it ?
----------------
Pur Beurre is an application using the open database provided by [Open Food Facts](https://world.openfoodfacts.org/).
By using Pur Beurre, you'll be able to find a substitute for a food product, with better nutritive grades and higher 
quality. The program also gives you the possibility of saving all your search results in your database.

# What does Pur Beurre really do ?
----------------
By launching Pur Beurre the following steps will happen :
	- a local database with datas from [Open Food Facts](https://world.openfoodfacts.org/) will be installed \
	- you'll be able to search in this database a certain amount of products and their substitutes \
	- a saving function is built to allow you to save all your favorites substitutes in your database \

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
Open the Settings/constants.py file and replace the MySQL connexion parameters by your own user name, password and host name \
Write `main_program.py` in your terminal 

## Dependancies :

Python 3.7.x \
download : https://www.python.org/downloads/ \
install : https://realpython.com/installing-python/ 

MySQL \
download : https://dev.mysql.com/downloads/mysql/#downloads \
install : https://www.mysqltutorial.org/install-mysql/ \
**Please be sure remembering your host name, your user name and your password, to allow access for the program to your MySQL**

Depending of your python's install, you might need PIP\
install pip : https://packaging.python.org/tutorials/installing-packages/

## Modules :

main_program.py\
db_init.sql creates the database in the user's system \
Models/ contains all the different classes and the app functions\
Settings/ contains constants.py\

## Built with :

Visual Studio Code (IDE)\
Python 3.7.5\
UTF-8

## Author :

Flavien Murail : https://github.com/Nastyflav


# How does Pur Beurre works ?
----------------

This application is working only when it's being used by the user's terminal. You just need to use your keyboard to interact with the app. Pur Beurre is for now only available in french.

## 1. Select a research

At first, the user has to choose between two type of research :
```
Que souhaitez-vous faire ?
Pour consulter les catégories d'aliments disponibles -> Tapez 1
Pour consulter vos aliments favoris -> Tapez 2
```

## 2. Select a category

Then you can choose a category among all that the program provides :
```
=======CATEGORIES=========
Choisissez un type d'aliment en tapant son numéro :

Pâtes à tartiner -> Tapez 1
Thés -> Tapez 2
Fromages blancs -> Tapez 3
Jus de fruits -> Tapez 4
Confitures -> Tapez 5
(etc)
```

# 3. Select a product

Once the category is selected, the application returns a bunch of products associated. The user just has to choose which one he wants to consult :
```
=======ALIMENTS=======
Choisissez un produit à substituer en tapant son numéro :
```

# 4. Select a substitute

Based on the same system than during the product selection. The user can choose among a list of higher quality products and print its caracteristics :
```
=======BETTER, HEALTHIER, TASTIER=======
```

# 5. Save a substitute

The program then asks the user if he wants to save his result into his favorites :
```
Souhaitez vous placer ce produit dans vos favoris ?
Oui -> Tapez 1
Non -> Tapez 2
```
If the user answers `1`, the program will record the new favorite in the local database. In any case, the user is than back to the application homepage : 

# 6. Consult the favorites records

At the beginning of the application, if the user chose to consult his records, all of his favorites products are displayed. \
Every substitute is associated with the original product it replaces :
```
=======HALL OF FAME=======
```

# 7. Application ending

