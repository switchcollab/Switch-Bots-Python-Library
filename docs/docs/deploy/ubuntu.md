---
sidebar_position: 1
---

# Deploy on Ubuntu/Debian

After you have created your bot, you should deply it on a server (you can also run it locally, but that would require you to have your pc always on).

To deploy your bot on Ubuntu/Debian, please make sure you have installed the following dependencies:

- `python` 3.8 or higher (you can check your Python version by running `python3 --version`)
- `pip` (you can check your `pip` version by running `pip3 --version`)

*Not required, but recommended:*
- `venv` (you can check your `venv` version by running `python3 -m venv --version`)
- `git` (you can check your `git` version by running `git --version`)


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

