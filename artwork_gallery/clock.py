from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command

sched = BlockingScheduler()


@sched.scheduled_job("interval", minutes=3)
def timed_job():
    print("This job is run every three minutes.")
    call_command("fetch_missing_data")


sched.start()
