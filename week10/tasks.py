from celery import Celery

app = Celery(name='tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y
