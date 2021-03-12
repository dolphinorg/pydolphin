from apscheduler.schedulers.background import BackgroundScheduler
from typing import Optional
from .utils import ping


scheduler = BackgroundScheduler()

class dolphin:
    def add_job():
        scheduler.add_job(ping, "interval", seconds=1200)
  
    def swim():
        scheduler.start()
        print("swimming...")