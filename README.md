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

1. Download the script from the project [slack-dm-files-downloader](https://github.com/SohelMansuri/slack-dm-files-downloader/blob/master/slack_dm_files_downloader.py)
2. After downloading, move this file and place it in the same directory that contains "direct_messages" folder created by the (slack_history) project.
3. Run the script with Slack API token:
```
    python slack-dm-files-downloader.py --token="SLACK-API-TOKEN-HERE"
```
4. A new directory "direct_message_files" will be created, containing your direct message files that were downloaded, separated by each user (including yourself).
5. A file "files_not_downloaded.txt" will also be created, giving you direct links to files the script was not able to download.  For several reasons: A) If the file was shared from another direct message.  B) If a file was shared using an app like Google Drive.
6.  Have fun!

### Contact Information ###

You can e-mail me at sohelm786(at)gmail.com
