# Install polaris #
pip install django-polaris

# Run commands #
python app/manage.py collectstatic --no-input

python app/manage.py migrate

python app/manage.py shell

python app/manage.py runserver

python app/manage.py poll_pending_deposits --loop

# References: #
*Urban, J. (2021) https://github.com/stellar/django-polaris*

*Urban, J. & Reilly, K. (2021) https://django-polaris.readthedocs.io/en/stable/tutorials/index.html*

*Foundation, S, (2014) https://laboratory.stellar.org/*

*Quisel, T. & Urban, J. (2021) https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0001.md*

