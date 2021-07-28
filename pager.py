import os
import sched
import time
from bottle import request, route, run, static_file


@route('/')
def main():
    return server_static('index.html')


@route('/shutdown')
def shutdown():
    # Process(target=proc_task(request.path)).start()
    # Thread(target=proc_task(request.path)).start()
    return server_static('shutdown.html')


@route('/reboot')
def reboot():
    # Process(target=proc_task(request.path)).start()
    # new Thread still blocking the main execution
    # t = Thread(target=proc_task('/reboot'))
    # t.daemon = False
    # t.start()

    s.enter(5, 1, proc_task('/reboot'))
    s.run()
    print('started')
    return server_static('reboot.html')


@route('/<filename>')
def server_static(filename):
    static = static_file(filename,
                         root=os.path.dirname(__file__) + '/static')
    static.add_header('Cache-Control', 'no-cache, no-store, must-revalidate')
    return static


def proc_task(mode):
    time.sleep(5)
    if (mode == '/shutdown'):
        print('shutdown')
        # os.system('/sbin/shutdown now')
    else:
        print('reboot')
        # os.system('/sbin/reboot now')


if __name__ == '__main__':
    localip = os.popen('hostname -I').read().split(' ')[0]
    s = sched.scheduler(time.time, time.sleep)
    run(host=localip, port='6969', debug=False)
