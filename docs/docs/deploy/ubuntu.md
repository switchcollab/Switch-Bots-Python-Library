---
sidebar_position: 1
---

# Deploy on Ubuntu/Debian

After you have created your bot, you should deply it on a server (you can also run it locally, but that would require you to have your pc always on).

To deploy your bot on Ubuntu/Debian, please make sure you have installed the following dependencies:

- `python` 3.10 or higher (you can check your Python version by running `python3 --version`)
- `pip` (you can check your `pip` version by running `pip3 --version`)

*Not required, but recommended:*
- `venv` (you can check your `venv` version by running `python3 -m venv --version`)
- `git` (you can check your `git` version by running `git --version`)


## Install Python 3.10 (if not available in the default repositories)
Python 3.10 is not available in the default Ubuntu repositories. You can install it by following the steps below:

1. Add the deadsnakes PPA:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

2. Update the package list:

```bash
sudo apt update
```

3. Install Python 3.10:

```bash

sudo apt install python3.10
```

4. Install `pip` for Python 3.10:

```bash
sudo apt install python3.10-distutils
curl https://bootstrap.pypa.io/get-pip.py | sudo python3.10
```


## Install dependencies

To install the dependencies, run the following commands:

*If you have a requirements.txt file:*
```bash
pip3 install -r requirements.txt
```

*If you don't have a requirements.txt file:*
```bash
pip3 install swibots
```
Install other dependencies if you need them.

## Run the bot

To run the bot, run the following command:

```bash
python3 <your bot file>.py
```

## Run the bot on startup

To run the bot on startup, you can use `systemd` or `supervisor`.

### Using systemd

To run the bot on startup using `systemd`, you can follow the steps below:

1. Create a service file for your bot. You can use the following template:

```ini
[Unit]
Description=<your bot name>
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=<your user>
ExecStart=python3 /path/to/bot.py

[Install]
WantedBy=multi-user.target

```

2. Save the file as `/etc/systemd/system/<your bot name>.service`.

3. Reload the systemd daemon:

```bash
systemctl daemon-reload
```

# Using supervisor

To run the bot on startup using `supervisor`, you can follow the steps below:

1. Install `supervisor`:

```bash
sudo apt install supervisor
```

2. Create a configuration file for your bot. You can use the following template:

```ini
[program:<your bot name>]
command=/home/user/your-user/venv/bin/python /path/to/bot.py
directory=/path/to/bot/directory
autostart=true
autorestart=true
startsecs=10
stderr_logfile=/var/log/<your bot name>.err.log
stdout_logfile=/var/log/<your bot name>.out.log
```

3. Save the file as `/etc/supervisor/conf.d/<your bot name>.conf`.

4. Reload the supervisor configuration:

```bash
sudo supervisorctl reread
sudo supervisorctl update
```

