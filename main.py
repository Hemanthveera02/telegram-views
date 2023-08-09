from time import sleep as swait
from utilitys import auto_loader, input_loader
from threading import Thread, active_count
from auto_proxy import Proxy
from telegram import Api

THREADS = 800
logo = '''
                ~ Telegram Auto Views V2 ~
     ~ https://github.com/Hemanthveera02/Hemanthveera02 ~
              ~ telegram channel:@tricks077 ~
               ~username:@HemanthVeera077~
'''

print(logo)
channel, post = input_loader()
http, socks4, socks5 = auto_loader()

auto = Proxy(http_sources=http, socks4_sources=socks4, socks5_sources=socks5)
api = Api(channel, post=post)

Thread(target=api.views).start()
Thread(target=api.tui, args=(logo, THREADS)).start()


def start():
    threads = []
    auto.init()
    for proxy_type, proxy in auto.proxies:
        while active_count() > THREADS: swait(0.03)
        thread = Thread(target=api.send_view, args=(proxy, proxy_type))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
        start()

start()
