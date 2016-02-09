#!/bin/bash
cd /workspace/ADL_LRS
source ../env/bin/activate
fab setup_lrs
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$LRS_ADMIN_NAME', '$LRS_ADMIN_MAIL', '$LRS_ADMIN_PASS')" | python manage.py shell
service nginx restart
/workspace/env/bin/uwsgi --master --emperor /etc/uwsgi/vassals
