import os
imports = ('task')
task_ignore_result = False
broker_host = 'ec2-52-3-18-175.compute-1.amazonaws.com'
broker_port = 7169 
CELERY_BROKER_BACKEND  = 'redis://:p73d6f7f3c5f65c8df7025adbf268983e39e3253132438aca8ecb0b41d7f8d171@ec2-52-3-18-175.compute-1.amazonaws.com:7169'
result_backend  = 'redis://:p73d6f7f3c5f65c8df7025adbf268983e39e3253132438aca8ecb0b41d7f8d171@ec2-52-3-18-175.compute-1.amazonaws.com:7169'
