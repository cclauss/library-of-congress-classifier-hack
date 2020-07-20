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

docker run -p 8000:80 -d nginx
docker container ls
docker stop amazing_mahavira
docker rm amazing_mahavira

docker-compose up -d
http://localhost:8080



File "/openlibrary/openlibrary/solr/solrwriter.py", line 3, in <module>
ESC[36mweb_1        |ESC[0m     import httplib
   

File "/openlibrary/openlibrary/plugins/worksearch/subjects.py", line 222, in get_subject
ESC[36mweb_1        |ESC[0m     from search import work_search
ESC[36mweb_1        |ESC[0m ModuleNotFoundError: No module named 'search'

  File "/openlibrary/openlibrary/plugins/upstream/code.py", line 70, in static_url
ESC[36mweb_1        |ESC[0m     digest = hashlib.md5(open(fullpath).read()).hexdigest()
ESC[36mweb_1        |ESC[0m TypeError: Unicode-objects must be encoded before hashing

  File "/openlibrary/openlibrary/plugins/upstream/utils.py", line 716, in get_donation_include
ESC[36mweb_1        |ESC[0m     html += opener.open(url_banner_source + param, timeout=3).read()
ESC[36mweb_1        |ESC[0m TypeError: can only concatenate str (not "bytes") to str

 File "/openlibrary/openlibrary/core/middleware.py", line 44, in __call__
ESC[36mweb_1        |ESC[0m     return [compress("".join(data), 9)]
ESC[36mweb_1        |ESC[0m TypeError: sequence item 0: expected str instance, bytes found

File "/openlibrary/openlibrary/core/middleware.py", line 27, in compress
ESC[36mweb_1        |ESC[0m     gz = gzip.GzipFile(None, 'wb', level, fileobj=f)
ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/gzip.py", line 232, in _write_gzip_header
ESC[36mweb_1        |ESC[0m     self.fileobj.write(b'\037\213')             # magic header
ESC[36mweb_1        |ESC[0m TypeError: string argument expected, got 'bytes'

File "/openlibrary/infogami/infobase/server.py", line 98, in g
ESC[36mweb_1        |ESC[0m     result = d.json_data if isinstance(d, JSON) else json.dumps(d)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/__init__.py", line 231, in dumps
ESC[36mweb_1        |ESC[0m     return _default_encoder.encode(obj)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/encoder.py", line 199, in encode
ESC[36mweb_1        |ESC[0m     chunks = self.iterencode(o, _one_shot=True)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/encoder.py", line 257, in iterencode
ESC[36mweb_1        |ESC[0m     return _iterencode(o, 0)
ESC[36mweb_1        |ESC[0m   File "/home/openlibrary/.pyenv/versions/3.8.3/lib/python3.8/json/encoder.py", line 179, in default
ESC[36mweb_1        |ESC[0m     raise TypeError(f'Object of type {o.__class__.__name__} '
ESC[36mweb_1        |ESC[0m TypeError: Object of type datetime is not JSON serializable
ERROR: Aborting.
cclauss@christians-macbook-pro-1 openlibrary % code openlibrary/core/middleware.py
