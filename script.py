from sj4000 import camera as Camera



camera = Camera()



def start_movie():
    print("Trying start movie")
    stat, mode= camera.get_mode()
    if not stat:
        print('Failed get_mode!', mode)
        return
    if mode != camera.MODE_MOVIE and mode != camera.MODE_TMOVIE:
        print('Setting MOVIE mode')
        stat, info= camera.set_mode('MOVIE')
        if not stat:
            print('Failed set_mode!', info)
            return
        print('OK')
    stat, info= camera.start_stop_movie(camera.START)
    if stat:
        print('OK')
    else:
        print('Failed start_stop_movie!', mode)
        return
    print('Started MOVIE recording')
    

def stop_movie():
    stat, mode= camera.get_mode()
    if not stat:
        print('STOP failed at get_mode!', mode)
    if mode == camera.MODE_TPHOTO:
        print('Stopping TIMED PHOTO')
        stat, fname= camera.snap(None)
        if not stat:
            print('Failed snap!', fname)
            return
        print('Last image captured:', fname)
    else:
        print('Stopping MOVIE recording')
        stat, info= camera.start_stop_movie(camera.STOP)
        if stat:
            print('OK')
        else:
            print('Failed start_stop_movie!', info)
            return
    print('Stopped MOVIE recording')
    return


start_movie()

import time

t = 0
while t<5:
    time.sleep(1)
    t += 1
    print('t=', t)

stop_movie()

# TODO: if not connected weird error


# Done
# - reformatted prints for python3

