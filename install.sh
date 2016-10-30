#!/bin/bash

echo "Installing klingel.py..."
mkdir /opt/klingel
cp klingel.py /opt/klingel/klingel.py
chmod +x /opt/klingel/klingel.py

echo "Setting up systemd service..."
cp klingel.service //lib/systemd/system/klingel.service
systemctl daemon-reload

echo "Installed!"
