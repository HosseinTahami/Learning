
# Backend for results
result_backend = 'rpc://'

# Time limitation for doing a task
task_time_limit = 20

#
task_soft_time_limit = 15

'''
CPU-bound: Task which use power of CPU for example convert
IO-bound: Task which use power of connection and network
---
if the Task was CPU-bound use all of your cores or all-1
'''
worker_concurrency = 5

# number of task which each worker gets
# by default it is 4
worker_prefetch_multiplier = 1

# Do not need the results and do not save them !!
task_ignore_result = True

# Celery will wait till the task is done and after that it will be checked
task_ack_late = True
