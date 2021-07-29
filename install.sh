#! /bin/bash

project_path="/path/to/shutdown-pager/"

# root user's UID is always 0
if [ "$EUID" -ne 0 ]
    then echo "ERROR: Needs to run with sudo."
    exit
fi

### --- python ---
pip install -qq -r "${project_path}requirements.txt"
### --------------

### --- sudoers ---
sudoers_path="/etc/sudoers.d/shutdown_pager"
rm "$sudoers_path" 2> /dev/null
touch "$sudoers_path"
chmod 0440 "$sudoers_path"

cat << EOF >> "$sudoers_path"
%sudo ALL=(ALL) NOPASSWD: /sbin/poweroff, /sbin/reboot, /sbin/shutdown
EOF
### ---------------

### --- service ---
service_name="shutdown_pager.service"
service_path="/lib/systemd/system/${service_name}"
rm "$service_path" 2> /dev/null
touch "$service_path"

cat << EOF >> "$service_path"
[Unit]
Description=Shutdown Pager
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 "${project_path}pager.py"

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable "$service_name"
systemctl start "$service_name"
### ---------------

echo "INFO: Installation finished."
