# Flask Shutdown
## Purpose

This script has one central purpose: shut down all Flask Apps on their respective ports. 

## Motivation

For CS340 Spring 2023, our final project consisted of a microservice system that required launching 13 separate flask apps. Without a script, shutting down these apps would take either: Navigating to 13 different terminals and manually shutting down the apps *or* using signal kills from the CLI. With this script, the process is simplified to just one line.

## How to Use it
1. Set all of the ports to correspond to the ports that your hosting your flask apps on.
2. From a terminal in a directory that contains the ``shutdown.py`` file, enter ``python shutdown.py`` if you're on Windows or ``python3 shutdown.py`` if you're on MacOS. 
