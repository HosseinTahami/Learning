#Celery 
---

- **Run celery:** ` celery -A (app_name) worker`

- **Run celery with more information:** ` celery -A (app_name) worker -l info `

- `task.delay(arg1, arg2, ...)`

- `task.apply_async(args=[arg1, arg2, ...])`

- `task.apply_async(args=[arg1, arg2, ...], countdown=number of seconds)`

- `task.apply_async(args=[arg1, arg2, ...], expires=number of seconds)`

- **Monitoring & Management:**` celery --broker=amqp://guest:guest@localhost:5672// flower `

- **Status:** `celery status`

- **Purge:** `celery purge`

- **Worker Status:** `celery inspect status`