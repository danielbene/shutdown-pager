# shutdown-pager
Minimalistic solution for convenient shutdown/reboot initiation of a local linux server.

## how-to
Modify `project_path` to the cloned dir path and the `user` to your username in the `install.sh` file . After running it with sudo, it will take care of everything:
- installing python deps
- setting up sudoers for passwordless shutdown
- creating a linux service for handling and autorun

If nothing fails you will reach it on the `http://192.168.x.x:6969` adress on your local network (you need the substitute the ip with your own).

## Requirements
Nothing fancy. A linux machine with python3+ and pip installed.

## Have fun
Modify the gui/port/framework/etc as you like, it really is just a low-effort design.
