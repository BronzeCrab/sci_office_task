# sci_office_task

## Как запустить (на примере голой ubuntu 14.04):

ставим гит

-  `sudo apt-get install git`

пип

-  `wget https://bootstrap.pypa.io/get-pip.py`
-  `python get-pip.py`

клонируем этот репо

-  `git clone https://github.com/BronzeCrab/sci_office_task`

зависимости

-  `cd sci_office_task`
-  `pip install -r requirements.txt`

bootstapform

-  `wget https://pypi.python.org/packages/source/d/django-bootstrap-form/django-bootstrap-form-3.2.tar.gz`
-  `tar xzf django-bootstrap-form-3.2.tar.gz`
-  `cd django-bootstrap-form-3.2`
-  `sudo python setup.py install `

запускаем
- `python manage.py runserver`