Problems with `/vendors`?
* `git submodule deinit -f . && git submodule update --init`

---

How to work on someone else’s pull request :
* git remote add theOtherGuy https://github.com/theOtherGuy/openlibrary
* git fetch theOtherGuy
* git checkout --track -b test_readlinks theOtherGuy/master

---

Monthly Dumps: [Cron-Jobs#monthly-data-dumps](https://github.com/internetarchive/openlibrary/wiki/Cron-Jobs#monthly-data-dumps)

Logger on macOS: log stream --info --debug --predicate "process == 'logger’”

Logger on Ubuntu: tail -f /var/log/syslog

tmux - https://gist.github.com/michaellihs/b6d46fa460fa5e429ea7ee5ff8794b96

Control-b d -- to put in background
tmux attach -t 0


```sh
# Required for users of zsh
# http://localhost:8080/status

export HOSTNAME=${HOSTNAME:-$HOST}

export COMPOSE_FILE="docker-compose.yml:docker-compose.override.yml"

docker-compose down && PYENV_VERSION=3.9.1 docker-compose up -d && docker-compose logs -f --tail=10

# docker exec -it openlibrary_web_1 /bin/bash

---

# ol-dev01 is http://staging.openlibrary.org/status
export COMPOSE_FILE="docker-compose.yml:docker-compose.staging.yml"
 
export HOSTNAME=${HOSTNAME:-$HOST}
docker-compose down && \
    docker-compose up -d memcached && \
    PYENV_VERSION=3.8.6 docker-compose \
        -f docker-compose.yml \
        -f docker-compose.staging.yml \
        up -d web && \
    docker-compose logs -f --tail=10 web
```

# Copy docker error log to the local machine
* [ ] ol-web1% `docker-compose exec web /bin/bash`
* [ ] openlibrary@ol-web1:`/var/log/openlibrary/ol-errors/2021-02-17$ grep "https://openlibrary.org/works/OL413150W" *`
* [ ] openlibrary@ol-web1:`vim 205420910740.html` # Make sure the file is of interest
* [ ]  openlibrary@ol-web1:`exit`
* [ ] ol-web1% `docker cp openlibrary_web_1:/var/log/openlibrary/ol-errors/2021-02-17/205420910740.html .`
* [ ] ol-web1% `cat 205420910740.html | mail -s "205420910740.html" cclauss@archive.org`

Docker and Kubernetes:
* https://k3d.io/
* https://microk8s.io/
* https://kubernetes.io/docs/tutorials/
* https://www.docker.com/blog/tag/python-env-series/
* https://docs.docker.com/develop/develop-images/multistage-build/
* https://www.ibm.com/uk-en/cloud/container-service/kubernetes-tutorials

* [ ] https://github.com/internetarchive/openlibrary/blob/master/openlibrary/tests/core/test_lending.py
needs tests for `compose_ia_url()`

| Important | URLs | for | Developers |
|:---:|:---:|:---:|:---:|
| [Deployment guide](https://github.com/internetarchive/openlibrary/wiki/Deployment-Guide) | [Assigned issues](https://github.com/internetarchive/openlibrary/issues/assigned/cclauss) | [Assigned pull requests](https://github.com/internetarchive/openlibrary/pulls/assigned/cclauss) | [Active sprint](https://github.com/internetarchive/openlibrary/milestone/35) | 
| | 8 -> 6 | 12 -> 8 | 21 -> 18 |
| localhost | dev0 is Python 2.7.6 | dev1 is Python 3 | prod is Python 2.7.6 |
| [http://localhost:8080](http://localhost:8080?debug=true) | [http://dev.openlibrary.org](http://dev.openlibrary.org?debug=true) | [http://staging.openlibrary.org](http://staging.openlibrary.org?debug=true) | [http://openlibrary.org](http://openlibrary.org?debug=true) |

https://sentry.archive.org/sentry/ol-web/

https://github.com/internetarchive/openlibrary/tree/master/docker
* __CAUTION:__ docker system prune -y

---
https://github.com/internetarchive/openlibrary/pull/3938

https://github.com/internetarchive/openlibrary/wiki/Deployment-Guide#rolling-back

```
ssh ol-covers1
/opt/openlibrary
. venv/bin/activate
sudo su openlibrary
ln -sf deploys/openlibrary/68474f6 openlibrary
sudo supervisorctl  status
rm openlibrary
ln -sf deploys/openlibrary/68474f6 openlibrary
ls -al
rm openlibrary
ln -sf deploys/openlibrary/4ed1ca3 openlibrary
ls -al
python2 -m pip --version
```
---

# Jumpservers
*  ssh-add ~/.ssh/id_rsa_archive_org ; ssh -A -i ~/.ssh/id_rsa_archive_org sshgw-sf.us.archive.org
    * ssh -A ol-dev0  # cd /opt/openlibrary/openlibrary && sudo vim _dev-merged.txt && head _dev-merged.txt
    * ssh -A ol-dev1  # cd /opt/openlibrary && sudo vim _dev-merged.txt
    * ssh -A ol-web1  # Python 3 on Docker -- Copy sudo ol-web3:/opt/.petabox/seed to clipboard && sudo touch ol-web1's seed && vi ol-web1's seed && paste && :w! && sudo systemctl start nginx && sudo systemctl status nginx
    * ssh -A ol-web3  # Production on Python 2.7.6 [blue node](https://github.com/internetarchive/openlibrary/wiki/Deployment-Guide#strategy)
    * ssh -A ol-web4  # Production on Python 2.7.6 green node
* sudo ./scripts/make-integration-branch.sh _dev-merged.txt dev-merged

### Only on dev0 (zsh: use &! to run a job in backround and disown)
```
sudo kill -9 `pgrep -f openlibrary-server`;sudo /olsystem/bin/upstart-service openlibrary-dev-server :7071 &!
### Please only run this on ol-dev0
It's a special way of restarting the dev server
`sudo ./scripts/make-integration-branch.sh _dev-merged.txt dev-merged; this will blow away any tracked but unstaged changes on ol-dev0`
The process is to open _dev_merged.txt and to add the remote branch to the right section/location
We'll then run the script command above which pull the latest master and replay all the patches on the various branches, giving you a super-branch of everything we want to test
```
### On dev1
https://github.com/internetarchive/openlibrary/blob/master/CONTRIBUTING.md#maintainers

https://sentry.archive.org/sentry/ol-web/issues/4139/?environment=staging says Py2.7.6
```
ssh -A ol-dev0
cd /opt/openlibrary/openlibrary && sudo vim _dev-merged.txt && head _dev-merged.txt

```
---
# dev0 is dev.openlibrary.org on Python 2.7.6
* [https://dev.openlibrary.org/status](https://dev.openlibrary.org/status)
# dev1 is staging.openlibrary.org on Python 3
* [http://staging.openlibrary.org/status](http://staging.openlibrary.org/status)

* https://github.com/internetarchive/openlibrary/wiki/Deployment-Guide#stagingopenlibraryorg

* cd /opt/openlibrary
* git status
* git diff
* docker-compose ; PYENV_VERSION=3.8.6 docker-compose -f docker-compose.yml up -d
* docker-compose logs --tail=10 -f web
* tail -f /var/log/ansible-pull.log
* service docker restart
* PYENV_VERSION=3.8.6 docker-compose up -d
---

https://github.com/internetarchive/openlibrary/tree/master/docker

* docker build -t olbase:latest -f docker/Dockerfile.olbase . ; docker-compose build web ; docker-compose build solr

* docker-compose down ; PYENV_VERSION=2.7.6 docker-compose up -d ; docker-compose logs -f --tail=10 web
* docker-compose down ; PYENV_VERSION=3.8.6 docker-compose up -d ; docker-compose logs -f --tail=10 web
* docker-compose down ; PYENV_VERSION=3.8.6 docker-compose -f docker-compose.yml up -d ; docker-compose logs -f --tail=10 web
* open http://localhost:8080
* docker exec -it openlibrary_web_1 /bin/bash
    * pytest -v --show-capture=all openlibrary/plugins/openlibrary/tests/test_home.py
    * git branch ; apt-get install -y vim ; vi infogami/utils/template.py

http://localhost:8080/admin/attach_debugger
* code openlibrary/templates/type/edition/view.html
* code openlibrary/plugins/upstream/models.py
* http://localhost:8081/b/olid/OL2058361M-L.jpg
* http://localhost:8081/b/olid/OL26835764M-L.jpg

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

# Bookserver
* docker system prune  # <-- !!! CAUTION !!!
* docker container stop bookserver
* docker container rm bookserver
* ./install.sh ; docker logs bookserver

docker container stop bookserver ; \\
    docker container rm bookserver ; \\
    docker run --name bookserver -d -p 8080:443 bookserver & ; \\
    docker logs -f --tail=10 bookserver

open http://localhost:8080 \
     http://localhost:8080/inlibrary \
     http://localhost:8080/downloads.xml \
     http://localhost:8080/new \
     http://localhost:8080/alpha.xml \
     http://localhost:8080/alpha/c/1 \
     http://localhost:8080/group/openaudiobooks \
     http://localhost:8080/group/recentreturns \
     http://localhost:8080/group/staffpicks \
     http://localhost:8080/group/detective

---

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
   File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 290, in process
     return self.handle()
   File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 281, in handle
     return self._delegate(fn, self.fvars, args)
   File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
     return handle_class(cls)
   File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
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
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 290, in process
    return self.handle()
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 281, in handle
    return self._delegate(fn, self.fvars, args)
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
    return handle_class(cls)
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
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
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 290, in process
    return self.handle()
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 281, in handle
    return self._delegate(fn, self.fvars, args)
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 531, in _delegate
    return handle_class(cls)
  File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/application.py", line 509, in handle_class
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
   File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/template.py", line 987, in __call__
     return BaseTemplate.__call__(self, *a, **kw)
   File "/home/openlibrary/.pyenv/versions/3.8.6/lib/python3.8/site-packages/web/template.py", line 898, in __call__
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

```
class Work(models.Work):
    """
    >>> from openlibrary.mocks.mock_infobase import MockSite
    >>> web.ctx.site = MockSite()
    >>> work = models.Work(web.ctx.site, '/works/OL42679M', web.Storage())
    >>> callable(work.get_sorted_editions)  # Issue #3633
    True
    >>> work.get_sorted_editions()
    []
    >>> print(work.get_sorted_editions)
    <bound method Work.get_sorted_editions of <Work: '/works/OL42679M'>>
    """
```

# SENTRY
https://git.archive.org/www/sentry/-/blob/master/NEWER-CHART.md
export KUBECONFIG=~/.kube/sentry
kubectl version
kubectl get -A all
kubectl logs -ngitlab-managed-apps pods/sentry-web-6dc7c6d8cf-6mhbg

---
# PURL
* https://git.archive.org/www/purl
* https://webarchive.jira.com/wiki/spaces/WWM/pages/169639946/PURL.org
* https://nomad.ux.archive.org/ui/jobs/www-purl
* https://nomad.ux.archive.org/ui/settings/tokens
* https://nomad.ux.archive.org/ui/jobs/www-purl/allocations
* https://ux-log0.us.archive.org:15601/app/home#/
* https://ux-log0.us.archive.org:15601/app/dashboards#/view/febd85f0-f706-11eb-978d-075f6fe91b95?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))

```
docker build -t purl .
docker run -dp 5001:5000 --name purl purl
sleep 3
open http://purl.archive.org:5001/
docker logs --follow purl
---
# Local does NOT work: Need memcached running, etc.
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
### supervisord.conf`
```[program:gunicorn]
command=gunicorn -w 32 -b 0.0.0.0:5000 app
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
```
---
