https://github.com/internetarchive/openlibrary/tree/master/docker

* docker-compose down ; PYENV_VERSION=3.8.3 docker-compose up -d ; docker-compose logs -f web
* docker-compose down ; PYENV_VERSION=3.8.3 docker-compose up -d ; docker exec -it openlibrary_web_1 /bin/bash
    * pytest -v --show-capture=all openlibrary/plugins/openlibrary/tests/test_home.py


```
docker build -t olbase:latest -f docker/Dockerfile.olbase .
docker-compose build web
docker-compose build solr
PYENV_VERSION=2.7.6 docker-compose up -d
open http://$(docker-machine ip):8080
```
