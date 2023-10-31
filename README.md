# Booking

A full booking solution to manage and grow your business.
Packed with all the tools you need to boost sales, manage your calendar and
retain clients so you can focus on what you do best.

## Setup

This project need a database and two web server, one for the python API and the
second one for the nginx web server that displays the frontend.

Firstly you need to create a `.env` file with all the settings you prefer.
An easy way to do it is to just copy the demo file:

```bash
cp .env_demo .env
```

All these containers are provisioned using docker. To start the dev environment
run:

```bash
docker compose up -d
```

In the first run, execute the migrations below to set up the database.

### Migrations

The project database is set up using
[Dbmate migrations](https://github.com/amacneil/dbmate), to execute the
migrations run:

```bash
dbmate up
# OR
docker run --rm -it --network=host -v "$(pwd)/migrations:/db" ghcr.io/amacneil/dbmate up
```

Any changes to the database should be provisioned using migrations. To
better understand now to create a new migration please follow the 
[Dbmate docs](https://github.com/amacneil/dbmate/blob/main/README.md)

### MySQL

Since you now have the database server running as a container, you can access it
using your preferred method. The server is running on:

```markdown
HOST: localhost
PORT: 3306
USER: root
PASS: jux4mgm@ktn5mnk4YAT
```

### API

The python API is running on port `5000` so you can access it at:
`http://localhost:5000/`.

A health check endpoint is provided so that you can check if everything is
running smoothly: http://localhost:5000/healthcheck

### Frontend

The app frontend will run on port `8181`so you can access it at:
`http://localhost:8181/`.

## Dev environment

After the initial setup, you just need to `docker compose up -d` to start the
containers, and `docker compose down` to stop it.

You can always use `docker ps` to check if the containers are running.

`docker compose logs -f` allow you to keep a look in the logs.

## Contribute

If you want to contribute please check the [issues page](issues). There you will
find all the things we want to be done. Add your code to a branch/fork and
create a Pull Request.

If you think something should be done differently or have a new feature proposal
Do not create a Pull Request regarding code that is not linked to an issue.
