# Complément de documentation pour le projet 10
Brieffing [présent ici](https://openclassrooms.com/fr/paths/68/projects/160/assignment)<br>
Le site installé [est accessible ici](http://15.237.65.43/)<br>


## La démarche
Le produit intialement hébergé sur la plateforme Heroku à été redéployée sur AWS (Amazon Web Services)
qui permet de compartimenter l'application, l'itégration des services satellites (Base de donnée, serveur, dns, sockage des statiques) sur le "cloud"

# Integration continue
Le projet est déployé en fonction du résultat des tests (initiés au projet 8) l'outil employé ici est circle CI<br>
Le dashboard de l'integration est [présent ici](https://app.circleci.com/pipelines/github/jean-charles-gibier/PurBeurre)<br>
La présent branche "production_aws" à été dupliquée pour expérimenter l'autre outil d'intégration continue nommé "Travis".<br>
Le dépot est [présent ici](https://github.com/jean-charles-gibier/mysandbox).

# Surveillance de l'activité
Le monitoring du site est hébergé à la fois par :<br>
[Le service Sentry](https://sentry.io/organizations/onmyown/issues/?project=5435011) pour l'analyse des log Django<br>
Et par [les outils de supervision AWS](https://eu-west-3.console.aws.amazon.com/cloudwatch/home?region=eu-west-3#)pour l'infrastructure.

# installation du serveur
Le service est hébergé dans [le cloud AWS](https://aws.amazon.com/fr/)<br>
Outre le choix du l'image serveur EC2 et du service RDS (base pgsql), les étapes d'installation de l'instance (ie :le serveur virtuel mis en fonction) peuvent être définies dans le paramétrage du service
ou installées via une connexion ssh de la façon suivante :

```
git clone https://github.com/jean-charles-gibier/PurBeurre.git
alias python='python3'
sudo apt update
sudo apt install -y nginx
sudo apt install -y python3-pip
sudo apt install -y python-dev
sudo apt install -y libpq-dev
sudo apt-get install supervisor
sudo pip3 install pipenv
pipenv install
pipenv shell
cd ~/PurBeurre/pur_beurre
pip install -r requirements.txt
mkdir /home/ubuntu/PurBeurre/pur_beurre/dumps/

cd /etc/nginx/
sudo touch sites-available/pur_beurre
sudo ln -s /etc/nginx/sites-available/pur_beurre /etc/nginx/sites-enabled
sudo bash
sudo cat << EOF > sites-available/pur_beurre
	server { 
			
		listen 80; server_name http://15.237.65.43/; 
		root /home/ubuntu/PurBeurre/;
			
		location / {
			proxy_set_header Host $http_host;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_redirect off;
			proxy_pass http://127.0.0.1:8000;
		}
			
	}
EOF
cd -
python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py filler
python manage.py collectstatic

# apres installation de raven et enregistrement Sentry
pip install --upgrade sentry-sdk
python manage.py raven test

sudo systemctl enable cron

export DEPLOY_ENVIRON=PRODUCTION
gunicorn --pythonpath pur_beurre pur_beurre.wsgi
```

Une fois mis en place le sysème de 'cron' pourra être programmé de la façon suivante pour une mise à jour automatisée de la base :
````
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command

# MAJ de la base OFF exécute la commande chaque jour à 4h00.
0 4 * * * cd PurBeurre/pur_beurre && pipenv run python ./manage.py purge 2>&1 >> /tmp/purge.log && pipenv run python ./manage.py filler 2>&1 >> /tmp/filler.log

````

Contenu du fichier de supervision '/etc/supervisor/conf.d/pur_beurre-gunicorn.conf'<br>
avec le paramètre DJANGO_SETTINGS_MODULE pointant sur la configuration de production.

```
[program:pur_beurre-gunicorn]
environment = DEPLOY_ENVIRON="PRODUCTION",DJANGO_SETTINGS_MODULE="pur_beurre.settings.production"
command = /home/ubuntu/.local/share/virtualenvs/ubuntu-7Wf190Ea/bin/gunicorn --pythonpath pur_beurre pur_beurre.wsgi
user = ubuntu
directory = /home/ubuntu/PurBeurre
autostart = true
autorestart = true
```
