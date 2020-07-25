ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM thing WHERE key='/admin/block'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM thing WHERE key='/books'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM thing WHERE key='/'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT data FROM data WHERE thing_id=523 AND revision=1
ESC[36mweb_1        |ESC[0m 2020-07-25 13:10:42 [infobase.cache] [DEBUG] MemcachedDict.update: dict_keys(['/'])
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM thing WHERE key='/admin/block'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM thing WHERE key='/admin/block'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM thing WHERE key='/admin/block'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT store.* FROM store, store_index WHERE store.id = store_index.store_id AND type = 'account' AND name='internetarchive_itemname' AND value='@openlibrary' ORDER BY store.id desc LIMIT 100 OFFSET 0
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM store WHERE key='account-email/cclauss@me.com'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM store WHERE key='account-email/cclauss@me.com'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM store WHERE key='account-email/cclauss@me.com'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM store WHERE key='account-email/cclauss@me.com'
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT store.* FROM store, store_index WHERE store.id = store_index.store_id AND type = 'account' AND name='username' AND value='openlibrary' ORDER BY store.id desc LIMIT 1 OFFSET 0
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT store.* FROM store, store_index WHERE store.id = store_index.store_id AND type = 'account' AND name='username' AND value='openlibrary860' ORDER BY store.id desc LIMIT 1 OFFSET 0
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT store.* FROM store, store_index WHERE store.id = store_index.store_id AND type = 'account' AND name='lusername' AND value='openlibrary860' ORDER BY store.id desc LIMIT 1 OFFSET 0
ESC[36mweb_1        |ESC[0m 0.0 (1): SELECT * FROM store WHERE key='account/openlibrary860'
ESC[36mweb_1        |ESC[0m http://0.0.0.0:7000/
ESC[36mweb_1        |ESC[0m 2020-07-25 13:11:03 [infobase.account] [INFO] new account registration username=openlibrary860
ESC[36mweb_1        |ESC[0m 0.02 (1): 200 POST /openlibrary.org/account/register {'username': 'openlibrary860', 'displayname': 'openlibrary', 'email': 'cclauss@me.com', 'password': '!!!!!!!'}
