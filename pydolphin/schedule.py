from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

class dolphin:
    def add_job(ping, seconds=600):
        scheduler.add_job(ping, "interval", seconds=seconds)
    async def swim():
        scheduler.start()
        print("swimming...")
