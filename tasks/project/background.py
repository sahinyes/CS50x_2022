from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from graph import grapher

# Background scheduler

def sensor():
    """ Function for test purposes. """
    grapher()
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=120)
sched.start()

app = Flask(__name__)


if __name__ == "__main__":
    app.run()


