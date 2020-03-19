from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=2)
def timed_job():
    print('This job is run every two minutes.')
    x = requests.get('http://127.0.0.1:8000/stocks/addStockData')
    print(x)

sched.start()