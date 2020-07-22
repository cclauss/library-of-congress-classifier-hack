https://github.com/internetarchive/openlibrary/tree/master/docker

* docker build -t olbase:latest -f docker/Dockerfile.olbase . ; docker-compose build web ; docker-compose build solr

* docker-compose down ; PYENV_VERSION=2.7.6 docker-compose up -d ; docker-compose logs -f web | more
* docker-compose down ; PYENV_VERSION=3.8.5 docker-compose up -d ; docker-compose logs -f web | more
* docker-compose down ; PYENV_VERSION=3.8.5 docker-compose up -d ; docker exec -it openlibrary_web_1 /bin/bash
    * pytest -v --show-capture=all openlibrary/plugins/openlibrary/tests/test_home.py
    * apt-get install vim
    * cd vendor/infogami/infogami
    * git branch ; apt-get install -y vim ; vi vendor/infogami/infogami/utils/template.py


```
docker build -t olbase:latest -f docker/Dockerfile.olbase .
docker-compose build web
docker-compose build solr
PYENV_VERSION=2.7.6 docker-compose up -d
open http://$(docker-machine ip):8080

docker run -p 8000:80 -d nginx
docker container ls
docker stop amazing_mahavira
docker rm amazing_mahavira

docker-compose up -d

pytest -v --show-capture stdout openlibrary/catalog/marc/tests/test_parse.py | more  #3584
pytest -v --show-capture stdout openlibrary/catalog/marc/tests/test_get_subjects.py | more
pytest -v --show-capture stdout openlibrary/tests/catalog/test_get_ia.py | more
pytest -v --show-capture stdout openlibrary/plugins/openlibrary/tests/test_home.py | more
```
http://localhost:8080
http://192.168.99.100:8080

# 22 July 2020
```
Traceback (most recent call last):
ESC[36mweb_1        |ESC[0m   File "/openlibrary/openlibrary/plugins/worksearch/search.py", line 42, in work_search
ESC[36mweb_1        |ESC[0m     result = solr.select(query, start=offset, rows=limit, **kw)
ESC[36mweb_1        |ESC[0m   File "/openlibrary/openlibrary/utils/solr.py", line 98, in select
ESC[36mweb_1        |ESC[0m     data = urllib.request.urlopen(request, timeout=10).read()
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/urllib/request.py", line 222, in urlopen
ESC[36mweb_1        |ESC[0m     return opener.open(url, data, timeout)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/urllib/request.py", line 522, in open
ESC[36mweb_1        |ESC[0m     req = meth(req)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/urllib/request.py", line 1281, in do_request_
ESC[36mweb_1        |ESC[0m     raise TypeError(msg)
ESC[36mweb_1        |ESC[0m TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
ESC[36mweb_1        |ESC[0m Traceback (most recent call last):
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 290, in process
ESC[36mweb_1        |ESC[0m     return self.handle()
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 281, in handle
ESC[36mweb_1        |ESC[0m     return self._delegate(fn, self.fvars, args)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
ESC[36mweb_1        |ESC[0m     return handle_class(cls)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
ESC[36mweb_1        |ESC[0m     return tocall(*args)
ESC[36mweb_1        |ESC[0m   File "/openlibrary/infogami/utils/app.py", line 187, in <lambda>
ESC[36mweb_1        |ESC[0m     HEAD = GET = POST = PUT = DELET = lambda self: delegate()
ESC[36mweb_1        |ESC[0m   File "/openlibrary/infogami/utilsE/app.py", line 206, in delegate
ESC[36mweb_1        |ESC[0m     return getattr(cls(), method)(*args)
ESC[36mweb_1        |ESC[0m   File "/openlibrary/openlibrary/plugins/worksearch/publishers.py", line 24, in GET
ESC[36mweb_1        |ESC[0m     if page.work_count == 0:
ESC[36mweb_1        |ESC[0m AttributeError: 'NoneType' object has no attribute 'work_count'

Traceback (most recent call last):
ESC[36mweb_1        |ESC[0m   File "/openlibrary/infogami/utils/template.py", line 143, in saferender
ESC[36mweb_1        |ESC[0m     result = t(*a, **kw)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/template.py", line 987, in __call__
ESC[36mweb_1        |ESC[0m     return BaseTemplate.__call__(self, *a, **kw)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/template.py", line 898, in __call__
ESC[36mweb_1        |ESC[0m     return self.t(*a, **kw)
ESC[36mweb_1        |ESC[0m   File "/openlibrary/openlibrary/templates/work_search.html", line 43, in __template__
ESC[36mweb_1        |ESC[0m     $ start_facet_count = 5
ESC[36mweb_1        |ESC[0m   File "/openlibrary/openlibrary/plugins/worksearch/code.py", line 396, in do_search
ESC[36mweb_1        |ESC[0m     if not reply or reply.startswith('<html'):
ESC[36mweb_1        |ESC[0m TypeError: startswith first arg must be bytes or a tuple of bytes, not str


```
# Next up...
```
File "/openlibrary/infogami/infobase/server.py", line 98, in g
     result = d.json_data if isinstance(d, JSON) else json.dumps(d)
   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/__init__.py", line 231, in dumps
     return _default_encoder.encode(obj)
   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/encoder.py", line 199, in encode
     chunks = self.iterencode(o, _one_shot=True)
   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/encoder.py", line 257, in iterencode
     return _iterencode(o, 0)
   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/encoder.py", line 179, in default
     raise TypeError(f'Object of type {o.__class__.__name__} '
 TypeError: Object of type datetime is not JSON serializable
```
