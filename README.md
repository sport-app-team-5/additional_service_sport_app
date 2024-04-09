# Aditional Services SportApp

This is an additional services management platform

## Documentation
This is automatically generated and can be accessed via `http://0.0.0.0:8001/docs`

## Deployment in local environment
### Requirements for running with docker
1. Docker
2. Docker compose

### Requirements for running with python
1. python 3.9
2. fastapi==0.100.0
3. uvicorn[standard]
4. python-dotenv 
5. pydantic==2.1.1 
6. python-multipart 
7. sqlalchemy 
8. alembic 
9. psycopg2-binary 
10. pyjwt==2.8.0 
11. pytest 
12. httpx

### Run docker
1. Modify the file name `.env.example`, should stay with the name `.env`
2. Modify the file name `alembic.ini.example`, should stay with the name `alembic.ini`
3. Modify the `.env` y `alembic.ini` file with the credentials of the environment to run
4. Create docker image and container with command `docker compose -f docker-compose-stage.yml up`
5. The project is accessible in the port http://127.0.0.1:8001

### Run python
1. Modify the file name `.env.example`, should stay with the name `.env`
2. Modify the file name `alembic.ini.example`, should stay with the name `alembic.ini`
3. Modify the `.env` y `alembic.ini` file with the credentials of the environment to run
4. Create docker image and container with command `uvicorn --host 0.0.0.0 --port 8008 app.main:app`
5. The project is accessible in the port http://127.0.0.1:8001


## Migrations and seeders
### Migrations
1. Run migrations with the command `alembic upgrade head`, this command will fill the database

### Seeders
1. In http://127.0.0.1:8001/docs execute route seeders `/api/v1/aditional_service/third_parties/seeders/run`
