# my_market_service

### Create .env file

and set "SQLALCHEMY_DATABASE_URL"

### Run this service via terminal and venv:

```bash
python -m venv venv

source venv/bin/activate

pip3 install -r requerments.txt

uvicorn my_market_services.src.main:app --reload
```

### See the docs

You can use FastAPI's automatic interactive API documentation by navigating to:

http://localhost:8000/docs
