user=`whoami`
SOAPBOX_HOME=/home/tdevoe/work/soapbox/

if [ "$user" == root ]; then
	echo "Logged in as root. Logging to /var/log/django.log"
	log=/var/log/django_messages
else
	echo "Not logged in as root. Logging to ~/log/django.log"
	log=~/log/django.log
fi


cd $SOAPBOX_HOME/soapbox/
python manage.py runserver 0.0.0.0:8000 > $log 2>&1
