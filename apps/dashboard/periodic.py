# periodic.py
# from apps.dashboard.task import send_notifiction
from celery import Celery

app = Celery('periodic', broker="pyamqp://guest@localhost//")
@app.task
def see_you():
    print("I am  deepak!")
    # send_notifiction()
    

app.conf.beat_schedule = {
    "run-in-5-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 5.0
    }
}