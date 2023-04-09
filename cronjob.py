import sched
from apscheduler.schedulers.background import BackgroundScheduler


def test():
  print('Test')


scheduler = BackgroundScheduler()

scheduler.add_job(test, 'interval', seconds=10)

scheduler.start()

while True:
  pass
