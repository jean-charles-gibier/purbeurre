status : [![CircleCI](https://circleci.com/gh/jean-charles-gibier/PurBeurre.svg?style=shield)](https://app.circleci.com/pipelines/github/jean-charles-gibier/PurBeurre)

# PurBeurre
Projet 8 DaPy

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
(venv) D:\github\PurBeurre_switch\pur_beurre>coverage run --source='.' manage.py test core.tests.test_config core.tests.test_core  product.tests.test_filler product.tests.test_models product.tests.test_ux_product pur_beurre.tests.test_statics_pages user.tests.test_forms user.tests.test_ux_user
 ````

Puis :
 ````
venv) D:\path\to\PurBeurre\pur_beurre>coverage report 
````

(Score actuel: 70%)
