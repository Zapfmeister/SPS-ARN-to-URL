import sys

try:
    eventSourceARN = input("Please provide the SQS ARN:")
    StrSplit = eventSourceARN.split(":")
    service = StrSplit[2]
    region = StrSplit[3]
    accountId = StrSplit[4]
    queueName = StrSplit[5]
    queueUrl = "https://" + service + "." + region + ".amazonaws.com/" + accountId + '/' + queueName
    print("\n")
    print("======================================================================================")
    print("SQS URL: " + queueUrl)
    print("======================================================================================")
except:
    print("Invalid input")
    print("Syntax is supposed to be: arn:aws:sqs:us-east-2:123456789012:MyTopic")
