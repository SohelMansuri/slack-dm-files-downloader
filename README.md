# slack-dm-files-downloader
This repo contains a script that downloads files which are sent as direct messages for Slack.

This project is basically a fork of [auino/slack-downloader](https://github.com/auino/slack-downloader), but used for a different purpose (downloading direct message files).

### Pre-Requirements

1. Slack API Token: [Slack API](https://api.slack.com/web)
2. (Optional) Download all public channels files: [auino/slack-downloader](https://github.com/auino/slack-downloader/blob/master/slack-downloader.py)
3. Download all public channel messages, private channel messages, and direct messages: [Chandler/slack_history.py](https://gist.github.com/Chandler/fb7a070f52883849de35)
4. Download this file and place in the same directory that contains "direct_messages" folder created by the above project (slack_history).

### Requirements

* `Python`: The app is written in Python.
* `python-requests`: web request library for Python

### Installation Instructions

1. Download the script from the project [slack-dm-files-downloader]()
2. After downloading, move this file and place it in the same directory that contains "direct_messages" folder created by the (slack_history) project.
3. Run the script with Slack API token:
```
    python slack-dm-files-downloader.py --token="SLACK-API-TOKEN-HERE"
```
4. Have fun!

### Contact Information ###

You can e-mail me at sohelm786(at)gmail.com
