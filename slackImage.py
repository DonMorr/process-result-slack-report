#!/usr/bin/python

import ConfigParser, os
import subprocess
import argparse
import json
import requests
import resource
import time


# Get the name of the file to monitor
parser = argparse.ArgumentParser()
parser.add_argument('--i', dest='image', help='Path to the image url to share \'http://site.com/image.jpg\'')
args = parser.parse_args()

# Read the expected config file
config = ConfigParser.ConfigParser()
configFile=os.path.expanduser('~/.slackimagerc');
config.read(configFile)

channel = config.get('CONFIG', 'channel')
url     = config.get('CONFIG', 'url')
username=config.get('CONFIG', 'username')

# Run the command, making sure the command output is sent to the console
# http://www.cyberciti.biz/faq/python-run-external-command-and-get-output/

print('image: ' + args.image)


# Now send the result to slack
payload = {
	"text": "",
        "username": username,
        "channel": channel
}


response = "A response"

payload['text']=response
attachments = [{'image_url':args.image, "fallback":"fallback"}]

#attachments = [{"title":"Image sent","fields":[{"title":"Volume","value":"1","short":True},{"title":"Issue","value":"3","short":True}],"author_name":"Stanford S. Strickland","author_icon":"http://a.slack-edge.com/7f18https://a.slack-edge.com/bfaba/img/api/homepage_custom_integrations-2x.png","image_url":args.image}]

payload['attachments']=attachments

payload_json = json.dumps(payload)
print payload_json
req = requests.post(url, payload_json, headers={'content-type': 'application/json'})

print req.text
