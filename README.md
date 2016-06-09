# process-result-slack-report

##### Sample Config to be put in ~/.slackreportrc
```
[CONFIG]
channel=#alertschannel
url=https://hooks.slack.com/services/Txxxxxxxxx/yyyyyyyy/zzzzzzzzzzzzz
username=SlackReporter
```

##### Sample Usage
Monitoring a process:
```
slackReport.py --c 'sudo ./b2 install'
```
Message posted in slack channel:
```
Command 'sudo ./b2 install' successful - time taken: 4935.06 seconds
```

##### Required Packages
Python 2 &  python-requests

##### Sample Output in Slack
![slack channel output](https://sites.google.com/site/donalmorrissey/images/process-result-slack.png)
