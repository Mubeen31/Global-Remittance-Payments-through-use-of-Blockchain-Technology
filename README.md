# Install polaris #
pip install django-polaris

# Run commands #
python app/manage.py collectstatic --no-input

python app/manage.py migrate

python app/manage.py shell

python app/manage.py runserver

python app/manage.py poll_pending_deposits --loop

# Links #
https://github.com/stellar/django-polaris

https://django-polaris.readthedocs.io/en/stable/tutorials/index.html

https://laboratory.stellar.org/

https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0001.md

https://www.youtube.com/watch?v=Mrgdvk1oRoA&t=2317s