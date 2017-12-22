#
# slack-dm-files-downloader
# Author: Sohel Mansuri
# Email: sohelm786[at]gmail.com
# GitHub project URL: https://github.com/SohelMansuri/slack-dm-files-downloader
#

import json
import requests
import os
import time
import argparse

from glob import glob

#### Slack API URL ###
SLACK_API = "https://slack.com/api"
USERS_URL = SLACK_API + "/" + "users.info"

MAIN_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) + '/'
FILE_NOT_DOWNLOADED_PATH = MAIN_DIRECTORY + "files_not_downloaded.txt"
MESSAGES_DIRECTORY = MAIN_DIRECTORY + "direct_messages"
FILES_DIRECTORY = MAIN_DIRECTORY + "direct_message_files"

def createDirectoryIfItDoesntExist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def createLogOfFilesNotDownloaded(notDownloadedList):
    try:
        fileOutput = open(FILE_NOT_DOWNLOADED_PATH, "w")
        fileOutput.write("These are the files that weren't downloaded (whether it be it was shared from one direct message to another or it was shared using an app like Google Drive):")
        for element in notDownloadedList:
            fileOutput.write("\n" + str(element))
        fileOutput.close()
    except Exception, e:
        return False

def getLocalFileName(timestamp, userSpecificDIR, fileName, fileCreator):
    timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime(float(timestamp)))
    fileName, fileExtension  = os.path.splitext(fileName)

    return userSpecificDIR + '/' + str(timestamp) + '-' + fileName + '_by_' + fileCreator + fileExtension

def convertAPIResponseToJSON(apiResponse):
    try:
        res = apiResponse.json
        checkIfOk = res['ok']
        return res
    except:
        return apiResponse.json()

def getUserName(userID):
    postData = {'token': API_TOKEN, 'user': userID}
    apiResponse = requests.post(USERS_URL, data=postData)
    return convertAPIResponseToJSON(apiResponse)['user']['name']

def downloadThisFile(baseDIR, localFileName, fileURL):
    createDirectoryIfItDoesntExist(baseDIR)
    try:
        requestHeaders = {'Authorization': 'Bearer ' + API_TOKEN}
        singleRequest = requests.get(fileURL, headers=requestHeaders)

        with open(localFileName, 'wb') as f:
            for chunk in singleRequest.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        print "File downloaded to: " + localFileName
    except Exception, e:
        pass

#### MAIN CODE ####
createDirectoryIfItDoesntExist(FILES_DIRECTORY)
filesNotDownloadedList = []
dictionaryOfUsers = dict()

parser = argparse.ArgumentParser(description="Slack direct messages downloader.")
parser.add_argument("--token", help="Slack user's API token")
args = parser.parse_args()
API_TOKEN = args.token

if((API_TOKEN is None) or (len(API_TOKEN) == 0)):
    print("No token found.  Please enter a token!")
else:
    for jsonFileName in glob(MESSAGES_DIRECTORY + "/*.json"):
        jsonData = json.load(open(jsonFileName))
        for messages in jsonData["messages"]:
            try:
                if 'file' in messages:
                    file = messages['file']
                    fileName = str(file['name'])
                    if 'upload' in messages:
                        fileURL = file['url_private']
                        if(messages['upload'] == False):
                            filesNotDownloadedList.append(fileURL)
                        else:
                            timestamp = str(file['timestamp'])
                            user = file['user']
                            userName = getUserName(user)
                            fileCreator = dictionaryOfUsers.get(user, userName)
                            userSpecificDIR = FILES_DIRECTORY + '/' + userName
                            localFileName = getLocalFileName(timestamp, userSpecificDIR, fileName, fileCreator)

                            print "Download the following file: " + str(fileURL)
                            downloadThisFile(userSpecificDIR, localFileName, fileURL)
            except Exception, e:
                print str(e)
                pass

    createLogOfFilesNotDownloaded(filesNotDownloadedList)
    print("Downloads complete!")