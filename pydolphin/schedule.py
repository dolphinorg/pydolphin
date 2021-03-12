from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

class dolphin:
    def add_job(ping, seconds=600):
        scheduler.add_job(ping, "interval", seconds=seconds)
    def swim():
        scheduler.start()
        print("swimming...")
