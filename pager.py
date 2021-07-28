import os
from time import sleep
from bottle import request, route, run, static_file
from multiprocessing import Process


@route('/')
def main():
    return server_static('index.html')


@route('/shutdown')
def shutdown():
    Process(target=proc_task(request.path)).start()
    return server_static('shutdown.html')


@route('/reboot')
def reboot():
    Process(target=proc_task(request.path)).start()
    return server_static('reboot.html')


@route('/<filename>')
def server_static(filename):
    return static_file(filename,
                       root=os.path.dirname(__file__) + '/static')


def proc_task(mode):
    sleep(5)
    if (mode == '/shutdown'):
        print('shutdown')
        os.system('shutdown now')
    else:
        print('reboot')
        os.system('reboot now')


localip = os.popen('hostname -I').read().split(' ')[0]
run(host=localip, port='6969', debug=False)
