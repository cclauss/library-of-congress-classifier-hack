https://github.com/internetarchive/openlibrary/tree/master/docker

* docker-compose down ; PYENV_VERSION=2.7.6 docker-compose up -d ; docker-compose logs -f web | more
* docker-compose down ; PYENV_VERSION=3.8.3 docker-compose up -d ; docker-compose logs -f web | more
* docker-compose down ; PYENV_VERSION=3.8.3 docker-compose up -d ; docker exec -it openlibrary_web_1 /bin/bash
    * pytest -v --show-capture=all openlibrary/plugins/openlibrary/tests/test_home.py


```
docker build -t olbase:latest -f docker/Dockerfile.olbase .
docker-compose build web
docker-compose build solr
PYENV_VERSION=2.7.6 docker-compose up -d
open http://$(docker-machine ip):8080
```

docker run -p 8000:80 -d nginx
docker container ls
docker stop amazing_mahavira
docker rm amazing_mahavira

docker-compose up -d
http://localhost:8080



```
File "/openlibrary/openlibrary/solr/solrwriter.py", line 3, in <module>
     import httplib

File "/openlibrary/openlibrary/plugins/worksearch/subjects.py", line 222, in get_subject
     from search import work_search
 ModuleNotFoundError: No module named 'search'

File "/openlibrary/openlibrary/plugins/upstream/code.py", line 70, in static_url
     digest = hashlib.md5(open(fullpath).read()).hexdigest()
 TypeError: Unicode-objects must be encoded before hashing

File "/openlibrary/openlibrary/plugins/upstream/utils.py", line 716, in get_donation_include
     html += opener.open(url_banner_source + param, timeout=3).read()
 TypeError: can only concatenate str (not "bytes") to str

File "/openlibrary/openlibrary/core/middleware.py", line 44, in __call__
     return [compress("".join(data), 9)]
 TypeError: sequence item 0: expected str instance, bytes found

File "/openlibrary/openlibrary/core/middleware.py", line 27, in compress
     gz = gzip.GzipFile(None, 'wb', level, fileobj=f)
   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/gzip.py", line 232, in _write_gzip_header
     self.fileobj.write(b'\037\213')             # magic header
 TypeError: string argument expected, got 'bytes'
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
