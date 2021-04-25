# periodic.py
# from apps.dashboard.task import send_notifiction
from celery import Celery

app = Celery('periodic', broker="pyamqp://guest@localhost//")
@app.task
def see_you():
    print("See you in ten seconds!")
    # send_notifiction()
    

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 10.0
    }
}