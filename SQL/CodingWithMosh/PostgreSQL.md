# PostgreSQL

```bash
sudo -u postgres psql postgres
```
```bash
sudo -u postgres psql 
```

```bash
postgres-# \l+


   Name    |  Owner   | Encoding |                 
-----------+----------+----------+
 postgres  | postgres | UTF8     |
 template0 | postgres | UTF8     | 
           |          |          |
 template1 | postgres | UTF8     |
           |          |          | 
(3 rows)

```

```sql
ALTER USER user_name WITH PASSWORD 'new_password';
```