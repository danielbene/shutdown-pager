import os
from bottle import request, route, run, static_file
from time import sleep
from multiprocessing import Process


@route('/')
def main():
    return server_static('index.html')


@route('/shutdown')
def shutdown():
    # that frickin args comma - https://stackoverflow.com/a/1559149
    Process(target=proc_task, args=(request.path,)).start()
    return server_static('shutdown.html')


@route('/reboot')
def reboot():
    Process(target=proc_task, args=(request.path,)).start()
    return server_static('reboot.html')


@route('/<filename>')
def server_static(filename):
    static = static_file(filename,
                         root=os.path.dirname(__file__) + '/static')
    static.add_header('Cache-Control', 'no-cache, no-store, must-revalidate')
    return static


def proc_task(mode):
    sleep(5)
    if (mode == '/shutdown'):
        print('shutdown')
        # os.system('/sbin/shutdown now')
    else:
        print('reboot')
        # os.system('/sbin/reboot now')


if __name__ == '__main__':
    localip = os.popen('hostname -I').read().split(' ')[0]
    run(host=localip, port='6969', debug=False)
