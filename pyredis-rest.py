#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis
r = redis.Redis()

from flask import Flask
app = Flask(__name__)

@app.route('/<command>/')
@app.route('/<command>/<path:arguments>')
def exec_command(command, arguments=None):
    try:
        redis_method = getattr(r, command)
        if arguments is None:
            return str(redis_method())
        else:            
            return str(redis_method(*arguments.strip('/').split('/')))
    except AttributeError:
        return '{0} is not a valid pyredis command.'.format(command)

if __name__ == '__main__':
    app.run()
