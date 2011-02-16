# Pyredis-rest

A **simple** RESTful API server to use with Redis over HTTP.

## Dependencies

### [Flask](http://flask.pocoo.org/)

Install
<pre><code>sudo easy_install flask</code></pre>
Test
<pre><code>python -c "import flask"</code></pre>

### [redis-py](http://github.com/andymccurdy/redis-py)

Install
<pre><code>sudo easy_install redis</code></pre>
Test
<pre><code>python -c "import redis"</code></pre>

## How to run it

Yo only need to run the script
<pre><code>./pyredis-rest.py</code></pre>

Using your favourite web browser you can access to http://localhost:5000 and send standard Redis commands:

### Examples

A simple PING command:
<pre><code>http://localhost:5000/ping/</code></pre>

Using SET command:
<pre><code>http://localhost:5000/set/counter/100/</code></pre>

Using GET command:
<pre><code>http://localhost:5000/get/counter/</code></pre>
