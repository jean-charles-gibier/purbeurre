# Complément de documentation pour le projet 10
Brieffing [présent ici](https://openclassrooms.com/fr/paths/68/projects/160/assignment)

## La démarche
Le produit intialement hébergé sur la plateforme Heroku à été redéployée sur AWS (Amazon Web Services)
qui permet de compartiementer l'application, l'itégration des services satellites (Base de donnée, serveur, dns, sockage des statiques) sur le "cloud"

# installation du serveur
Outre le choix du l'image serveur EC2 et du service RDS (base pgsql), les étapes d'installation de l'instance (ie :le serveur virtuel mis en fonction) peuvent définies dans le paramétrage du service
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
pip install -r PurBeurre/requirements.txt
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
sudo systemctl enable cron
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
0 4 * * * cd Pure_beurre/pur_beurre && python ./manage.py purge 2>&1 >> /tmp/purge.log && python ./manage.py filler 2>&1 >> /tmp/filler.log

````


