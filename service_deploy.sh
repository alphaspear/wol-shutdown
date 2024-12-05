#!/usr/bin/bash

sudo chmod +x wol_shutdown.py
sudo cp wol_listener.service /etc/systemd/system/wol_listener.service
sudo systemctl daemon-reload
sudo systemctl enable wol_listener.service
sudo systemctl start wol_listener.service
sudo systemctl restart wol_listener.service
sudo systemctl status wol_listener.service
