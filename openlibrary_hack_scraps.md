https://github.com/internetarchive/openlibrary/tree/master/docker

* docker build -t olbase:latest -f docker/Dockerfile.olbase . ; docker-compose build web ; docker-compose build solr

* docker-compose down ; INFOGAMI=local PYENV_VERSION=2.7.6 docker-compose up -d ; docker-compose logs -f web | more
* docker-compose down ; INFOGAMI=local PYENV_VERSION=3.8.5 docker-compose up -d ; docker-compose logs -f web | more
* open http://localhost:8080
* docker-compose down ; INFOGAMI=local PYENV_VERSION=3.8.5 docker-compose up -d ; docker exec -it openlibrary_web_1 /bin/bash
    * pytest -v --show-capture=all openlibrary/plugins/openlibrary/tests/test_home.py
    * apt-get install -y vim ; cd vendor/infogami ; git branch ; git diff master
    * git branch ; apt-get install -y vim ; vi infogami/utils/template.py

http://localhost:8080/admin/attach_debugger
* code openlibrary/templates/type/edition/view.html
* code openlibrary/plugins/upstream/models.py

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
  File "/openlibrary/openlibrary/plugins/worksearch/search.py", line 42, in work_search
    result = solr.select(query, start=offset, rows=limit, **kw)
  File "/openlibrary/openlibrary/utils/solr.py", line 98, in select
    data = urllib.request.urlopen(request, timeout=10).read()
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/urllib/request.py", line 522, in open
    req = meth(req)
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/urllib/request.py", line 1281, in do_request_
    raise TypeError(msg)
TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
Traceback (most recent call last):
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 290, in process
    return self.handle()
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 281, in handle
    return self._delegate(fn, self.fvars, args)
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
    return handle_class(cls)
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
    return tocall(*args)
  File "/openlibrary/infogami/utils/app.py", line 187, in <lambda>
    HEAD = GET = POST = PUT = DELET = lambda self: delegate()
  File "/openlibrary/infogami/utilsE/app.py", line 206, in delegate
    return getattr(cls(), method)(*args)
  File "/openlibrary/openlibrary/plugins/worksearch/publishers.py", line 24, in GET
    if page.work_count == 0:
AttributeError: 'NoneType' object has no attribute 'work_count'

Traceback (most recent call last):
  File "/openlibrary/infogami/utils/template.py", line 143, in saferender
    result = t(*a, **kw)
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/template.py", line 987, in __call__
    return BaseTemplate.__call__(self, *a, **kw)
  File "/home/openlibrary/.pyenv/versions/3.8.4/lib/python3.8/site-packages/web/template.py", line 898, in __call__
    return self.t(*a, **kw)
  File "/openlibrary/openlibrary/templates/work_search.html", line 43, in __template__
    $ start_facet_count = 5
  File "/openlibrary/openlibrary/plugins/worksearch/code.py", line 396, in do_search
    if not reply or reply.startswith('<html'):
TypeError: startswith first arg must be bytes or a tuple of bytes, not str


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

# 23 July 2020
# UI test cases:
### Problematic URLs
1. http://localhost:8080/search?q=twain&debug=true -- AttributeError: module 'config' has no attribute 'get'
2. http://localhost:8080/people/openlibrary7987/books/already-read/stats -- lang
3. http://localhost:8080/type/object?m=edit -- lang
4. ~http://localhost:8080/search/authors?q=Twain~
5. ~http://localhost:8080/account/loans~
6. ~http://localhost:8080/people/openlibrary7987/preferences?m=diff&b=3~
7. ~http://localhost:8080/people/openlibrary7987/preferences?_compare=Compare&b=3&a=2&m=diff~
### Screen elements:
* Home: http://localhost:8080/ -- OK
* Vision: http://localhost:8080/about/vision (404 - Page Not Found) -- OK
* Volunteer: http://localhost:8080/volunteer (404 - Page Not Found) -- OK
* Books: http://localhost:8080/search -- OK
    * "Twain": http://localhost:8080/search?q=twain&mode=everything -- ___Displays ok but AttributeError___
```
Traceback (most recent call last):
   File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 290, in process
     return self.handle()
   File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 281, in handle
     return self._delegate(fn, self.fvars, args)
   File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
     return handle_class(cls)
   File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
     return tocall(*args)
   File "/openlibrary/openlibrary/coverstore/code.py", line 251, in GET
     value = self.query(category, key, value)
   File "/openlibrary/openlibrary/coverstore/code.py", line 346, in query
     return _query(category, key, value)
   File "/openlibrary/openlibrary/coverstore/code.py", line 56, in _query
     return get_cover_id([olkey])
   File "/openlibrary/openlibrary/coverstore/code.py", line 38, in get_cover_id
     doc = ol_get(olkey)
   File "/openlibrary/openlibrary/coverstore/utils.py", line 66, in ol_get
     if oldb.is_supported():
   File "/openlibrary/openlibrary/coverstore/oldb.py", line 15, in is_supported
     return bool(config.get("ol_db_parameters"))
 AttributeError: module 'config' has no attribute 'get'
```
* Authors: http://localhost:8080/search/authors -- OK
    * "Twain": http://localhost:8080/search/authors?q=Twain (same as Books) -- OK
* http://localhost:8080/subjects (404 - Page Not Found) -- OK
* Advanced Search http://localhost:8080/advancedsearch -- OK
    * "Twain" http://localhost:8080/search?author=Twain (same as Books) -- ___Displays ok but AttributeError___
* Developers: http://localhost:8080/developers (404 - Page Not Found) -- OK
* API: http://localhost:8080/developers/api (404 - Page Not Found) -- OK
* Bulk Data Dumps: http://localhost:8080/developers/dumps (404 - Page Not Found) -- OK
* Add a Book: http://localhost:8080/books/add -- OK
    * DO IT
* Help Center: http://localhost:8080/help (404 - Page Not Found) -- OK
* Report A Problem: http://localhost:8080/contact?path=/help -- OK
    * Fill form and click `Send` --> Sent! -- OK
* Suggesting Edits: http://localhost:8080/help/faq/editing (404 - Page Not Found) -- OK
* User menu at upper right
    * Login / Logout: -- OK
    * My Loans: http://localhost:8080/account/loans -- OK
    * My Lists: http://localhost:8080/people/openlibrary7987/lists -- OK
    * My Profile: http://localhost:8080/people/openlibrary7987 -- OK
    * My Profile/Diff: http://localhost:8080/people/openlibrary7987/preferences?m=diff&b=3 -- OK
    * My Profile/Compare: http://localhost:8080/people/openlibrary7987/preferences?_compare=Compare&b=3&a=2&m=diff -- OK
    * Settings: http://localhost:8080/account -- OK


### Problems
* (continued)
    * My Profile/Stats: http://localhost:8080/people/openlibrary7987/books/already-read/stats&debug=true -- ___Internal Server Error___
```
 Traceback (most recent call last):
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 290, in process
    return self.handle()
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 281, in handle
    return self._delegate(fn, self.fvars, args)
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
    return handle_class(cls)
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
    return tocall(*args)
  File "/openlibrary/infogami/utils/app.py", line 187, in <lambda>
    HEAD = GET = POST = PUT = DELETE = lambda self: delegate()
  File "/openlibrary/infogami/utils/app.py", line 206, in delegate
    return getattr(cls(), method)(*args)
  File "/openlibrary/openlibrary/plugins/upstream/account.py", line 826, in GET
    lang=web.ctx.lang,
AttributeError: 'ThreadedDict' object has no attribute 'lang'
```
* (continued)
    * My Profile/Edit: http://localhost:8080/type/object?m=edit&debug=true -- ___Internal Server Error___
```
Traceback (most recent call last):
  File "/openlibrary/infogami/utils/i18n.py", line 109, in __call__
    return str(self) % tuple(web.safestr(x) for x in a)
  File "/openlibrary/infogami/utils/i18n.py", line 102, in __str__
    data = get(web.ctx.lang) or default_data
AttributeError: 'ThreadedDict' object has no attribute 'lang'
```
### After advanced search succeeds, we get:
* http://localhost:8080/search?q=twain&debug=true -->
```
Traceback (most recent call last):
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 290, in process
    return self.handle()
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 281, in handle
    return self._delegate(fn, self.fvars, args)
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
    return handle_class(cls)
  File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
    return tocall(*args)
  File "/openlibrary/openlibrary/coverstore/code.py", line 251, in GET
    value = self.query(category, key, value)
  File "/openlibrary/openlibrary/coverstore/code.py", line 346, in query
    return _query(category, key, value)
  File "/openlibrary/openlibrary/coverstore/code.py", line 56, in _query
    return get_cover_id([olkey])
  File "/openlibrary/openlibrary/coverstore/code.py", line 38, in get_cover_id
    doc = ol_get(olkey)
  File "/openlibrary/openlibrary/coverstore/utils.py", line 66, in ol_get
    if oldb.is_supported():
  File "/openlibrary/openlibrary/coverstore/oldb.py", line 15, in is_supported
    return bool(config.get("ol_db_parameters"))
AttributeError: module 'config' has no attribute 'get'
```
* Click `A Tramp Abroad`
    * http://localhost:8080/books/OL24197475M/The_complete_works_of_Mark_Twain.?debug=true
```
Traceback (most recent call last):
   File "/openlibrary/infogami/utils/template.py", line 145, in saferender
     result = t(*a, **kw)
   File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/template.py", line 987, in __call__
     return BaseTemplate.__call__(self, *a, **kw)
   File "/home/openlibrary/.pyenv/versions/3.8.5/lib/python3.8/site-packages/web/template.py", line 898, in __call__
     return self.t(*a, **kw)
   File "/openlibrary/openlibrary/templates/type/edition/view.html", line 315, in __template__
     </div>
 TypeError: '>' not supported between instances of 'Nothing' and 'int'
```

### URLs to test:
```python
#!/usr/bin/env python3

import requests

URLS = """\
http://localhost:8080
http://localhost:8080/#  # logout
http://localhost:8080/account/login
http://localhost:8080/account
http://localhost:8080/account/import
http://localhost:8080/account/loans
http://localhost:8080/account/notifications
http://localhost:8080/account/privacy
http://localhost:8080/advancedsearch
http://localhost:8080/authors
http://localhost:8080/authors/OL18319A
http://localhost:8080/books/add
http://localhost:8080/contact
http://localhost:8080/search
http://localhost:8080/search?q=place%3AItaly
http://localhost:8080/search?place=Italy
http://localhost:8080/search?subject=Adventure
http://localhost:8080/search?q=twain&debug=true -- AttributeError: module 'config' has no attribute 'get'
http://localhost:8080/search?q=twain
http://localhost:8080/search/authors
http://localhost:8080/search/authors?q=twain
http://localhost:8080/type/object
http://localhost:8080/people/openlibrary6320/books/already-read/stats
http://localhost:8080/people/openlibrary6320/books/currently-reading
http://localhost:8080/people/openlibrary6320/books/want-to-read
http://localhost:8080/people/openlibrary6320/lists
http://localhost:8080/people/openlibrary6320/preferences?m=diff&b=3
http://localhost:8080/people/openlibrary6320/preferences?_compare=Compare&b=3&a=2&m=diff
http://localhost:8080/works/OL53924W/The_complete_works_of_Mark_Twain
"""

"""
1. TypeError: '>' not supported between instances of 'Nothing' and 'int' (falling back to default template)
2. AttributeError: 'ThreadedDict' object has no attribute 'lang'
* /openlibrary/openlibrary/plugins/worksearch/code.py:489: FutureWarning: The behavior of this method will change in future versions. Use specific 'len(elem)' or 'elem is not None' test instead.
"""

BAD_URLS = """\
http://localhost:8080/books/OL42679M&debug=true  # 1.
http://localhost:8080/works/OL24197475M/The_complete_works_of_Mark_Twain.?debug=true  # 1.
http://localhost:8080/people/openlibrary6320/books/already-read/stats?debug=true  # 2.
http://localhost:8080/people/openlibrary6320/books/currently-reading/stats?debug=true  # 2.
http://localhost:8080/people/openlibrary6320/books/want-to-read/stats?debug=true  # 2.
http://localhost:8080/type/object?m=edit&debug=true  # 2.
"""

for url in URLS.splitlines():
    print(url)
    print(requests.get(url).text)
```

* http://localhost:8080/works/OL54120W.json
* http://localhost:8080/books/OL42679M.json
