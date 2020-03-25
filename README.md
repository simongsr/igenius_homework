# igenius_homework
iGenius homework

Steps to run on Linux / Mac:
```bash
> cd igenius_homework
> virtualenv --python=python3.8 venv # create a virtual environment with python 3.8
> source venv/bin/activate
> pip install -r requirements.txt # install requirements
> python manage.py makemigrations
> python manage.py migrate # prepare DB schema
> python manage.py test # run tests
> python manage.py runserver # start development server
> curl --location --request GET 'http://localhost:8000/convert?amount=11.0&src_currency=EUR&dest_currency=USD&reference_date=2020-03-23' # run example request
```

How to build and run with docker:
```bash
> sudo docker-compose build web . # build image
> sudo docker-compose up # run app
```
