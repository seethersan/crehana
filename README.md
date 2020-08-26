Django 3 project

**Instructions:**
1. Create a virtualenv and activate

```
virtualenv env && source env/bin/activate
```

2. Clone the repository

```
git clone https://github.com/seethersan/crehana.git
cd productsapi
```

3. Install requirements

```
pip install -r requirements.txt
```

4. Migrate database
```
python manage.py migrate
```

5. The command to make categoria and inscripcion migration is:
```
python manage.py migrar_categoria_inscripcion
```