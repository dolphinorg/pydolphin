from .utils import *
from .utils import ping
from .schedule import dolphin

dolphin.add_job(ping)
