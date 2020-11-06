status : [![CircleCI](https://circleci.com/gh/jean-charles-gibier/PurBeurre.svg?style=shield)](https://app.circleci.com/pipelines/github/jean-charles-gibier/PurBeurre)

# PurBeurre
Projet 8 DaPy

Note : ce dépôt conserve également [les documents du projet 10](https://github.com/jean-charles-gibier/PurBeurre/blob/production_aws/P10_README.md) qui completent le présent P8.<br>
Il comprend également les évolutions du projet 11 à savoir :<br>
Purbeurre V 1.2 change.log <br>
| # 	| Enhancements / bug-fixes	| Explanations 	|  
|-	|-	  | -	  |
| 1 | Adaptation du filler à l'orm django 	| L'ancien "filler" exploitait nativement le connecteur plsql (psychopg2). Cette remarque à d'ailleurs été soulevée dans la soutenance du projet 8. L'alimentation à donc été modifiée pour effectuer le travail avec l'ORM Django. Certains bugs ont également été incidemment corrigés (paramère des limites de chargement de produits ou de ctégories) |
| 2 	| redirection sur un nom de domaine propriétaire 	| Le projet 10 proposait en option, l'achat et la redirection du nom de domaine sur le service, cette redirection est opérationelle via le domaine '[lemulotfou.com]((https://www.lemulotfou.com)' |
| 3 	|  Ajout d'un gestionnaire de static	| Le projet 8 proposait le middleware whitenoise comme gestionaire de fichiers static. L'amélioration propose une sauvegarde des "statics" sur le cloud AWS (S3) pour rester dans la perspective des choix du projet 10 |
 | 4 	|  Complétion du profil utilisateur	| Le systeme popose maintenant la modification des données personnelles de l'utilsateur (nom, prenom, mot de passe) sauvegardées par le système |
 | 5 	|  Regression mystère| Résolution des "modifications" glisssées par le mentor dans le cadre de ce projet  |


 La société "Pur beurre" souhaite un site dont les exigences sont décrites dans 
 le document suivant : [Brief P8](https://openclassrooms.com/fr/paths/68/projects/159/assignment)


installation:
Git clone de ce projet + tests + migrations 

````
pip install -r requirements.txt
# pour purger la base
python ./manage.py purge
# pour alimenter la base 
python ./manage.py filler 4000
````

(Ici on importe 4000 produits de OpenFoodFacts + 4000 associations avec une dizaine de catégories) 

Admin local :<br>
    127.0.0.1:8000/user/admin/
<br/>    
Test coverage courant :
 ````
(venv) D:\path\to\PurBeurre\pur_beurre>coverage run --source='.'  manage.py test core.tests.test_config core.tests.test_core  product.tests.test_filler product.tests.test_models product.tests.test_ux_product pur_beurre.tests.test_statics_pages user.tests.test_forms user.tests.test_ux_user pur_beurre.tests.test_manager
 ````

Puis :
 ````
(venv) D:\path\to\PurBeurre\pur_beurre>coverage report 
````

````
(venv) D:\path\to\PurBeurre\pur_beurre
Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
__init__.py                                              0      0   100%
core\__init__.py                                         0      0   100%
core\constant.py                                         8      0   100%
core\dao\__init__.py                                     0      0   100%
core\dao\daocategory.py                                 14      0   100%
core\dao\daoproduct.py                                  13      0   100%
core\dao\writer.py                                      85      7    92%
core\dbconnector.py                                     20      2    90%
core\dbconnector_mysql.py                                0      0   100%
core\downloader\__init__.py                              0      0   100%
core\downloader\categorydownloader.py                   23      2    91%
core\downloader\customrequest.py                        16      6    62%
core\downloader\productdownloader.py                    30      3    90%
core\filler.py                                          67      8    88%
core\model\__init__.py                                   0      0   100%
core\model\category.py                                  31      6    81%
core\model\product.py                                   56     14    75%
core\tests\__init__.py                                   0      0   100%
core\tests\test_config.py                                8      0   100%
core\tests\test_core.py                                 15      0   100%
manage.py                                               12      2    83%
product\__init__.py                                      0      0   100%
product\admin.py                                         3      0   100%
product\apps.py                                          3      0   100%
product\management\__init__.py                           0      0   100%
product\management\commands\__init__.py                  0      0   100%
product\management\commands\filler.py                   12      0   100%
product\management\commands\purge.py                     8      0   100%
product\migrations\0001_initial.py                       5      0   100%
product\migrations\0002_auto_20200803_2138.py            4      0   100%
product\migrations\0003_product_nutrition_grade.py       4      0   100%
product\migrations\0004_auto_20200806_2336.py            4      0   100%
product\migrations\0005_auto_20200807_0022.py            4      0   100%
product\migrations\0006_auto_20200808_1518.py            4      0   100%
product\migrations\0007_product_image_front_url.py       4      0   100%
product\migrations\__init__.py                           0      0   100%
product\models.py                                       25      2    92%
product\templatetags\__init__.py                         0      0   100%
product\templatetags\getcolor.py                        10      1    90%
product\templatetags\urlparams.py                       11      6    45%
product\tests\__init__.py                                0      0   100%
product\tests\test_filler.py                            10      0   100%
product\tests\test_models.py                            42      0   100%
product\tests\test_ux_product.py                        41      0   100%
product\urls.py                                          3      0   100%
product\views.py                                        57     26    54%
pur_beurre\__init__.py                                   0      0   100%
pur_beurre\asgi.py                                       4      4     0%
pur_beurre\settings.py                                  41     11    73%
pur_beurre\tests\__init__.py                             0      0   100%
pur_beurre\tests\test_manager.py                        15      0   100%
pur_beurre\tests\test_statics_pages.py                  13      0   100%
pur_beurre\urls.py                                       7      2    71%
pur_beurre\wsgi.py                                       4      4     0%
substitute\__init__.py                                   0      0   100%
substitute\admin.py                                      0      0   100%
substitute\apps.py                                       3      0   100%
substitute\migrations\0001_initial.py                    6      0   100%
substitute\migrations\0002_auto_20200808_1518.py         6      0   100%
substitute\migrations\__init__.py                        0      0   100%
substitute\models.py                                    11      1    91%
substitute\urls.py                                       3      0   100%
substitute\views.py                                     38     21    45%
user\__init__.py                                         0      0   100%
user\admin.py                                            0      0   100%
user\apps.py                                             3      0   100%
user\emailbackend.py                                    22      2    91%
user\forms.py                                           34      1    97%
user\migrations\0001_initial.py                          5      0   100%
user\migrations\0002_delete_user.py                      4      0   100%
user\migrations\__init__.py                              0      0   100%
user\models.py                                           0      0   100%
user\tests\__init__.py                                   2      0   100%
user\tests\test_forms.py                                45      0   100%
user\tests\test_ux_user.py                             125     18    86%
user\tests\test_views.py                                 0      0   100%
user\urls.py                                             6      0   100%
user\views.py                                           46     19    59%
------------------------------------------------------------------------
TOTAL                                                 1095    168    85%
````

.
