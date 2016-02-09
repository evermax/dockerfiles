# ADL LRS Docker

First things first, this is merely a work of containerizing the project, the real work and help on that goes to [ADL team](https://github.com/adlnet/ADL_LRS). A special thanks to [Lou Wolford](https://github.com/ljwolford) for his help to make this possible.

## Docker compose

This is a docker-compose project.

Before everything, you will need to run the following:

```
docker create -v /var/lib/postgresql/data/pgdata --name psql_data busybox
```

This will create a data volume container, so that your database content won't be deleted each time.

Clone the repo, go inside this folder, change different env variables in `psql.env`, `rabbitmq.env` and `lrs.env`. This will make it more secure, though it is currently in http. You might want to change the nginx configuration and add some SSL in that, if it is for more that just test purpose.

Then you do a `docker-compose up` and the magic should happend.


## What next?

Well, nginx should perhaps be separated from the LRS itself so that it is way easier to tweak.
So this will be the next step before the project is really proper. This is quite a good explaination on the [official repo](https://hub.docker.com/_/nginx/) on how to have it play well with docker compose.

The main issue that I see with having it in a different container is that it seem harder to cache static files. (But you should use the api more that anything else anyway.)
