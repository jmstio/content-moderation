#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def moderate_image(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
    HumanLoopConfig={ \
            'HumanLoopName': 'image-review-4', \
            'FlowDefinitionArn': "arn:aws:sagemaker:eu-west-2:858545927766:flow-definition/content-moderation", \
            'DataAttributes': {'ContentClassifiers': ['FreeOfPersonallyIdentifiableInformation','FreeOfAdultContent']}
         }
    )

    print('Detected labels for ' + photo)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return len(response['ModerationLabels'])



def main():
    bucket='content-moderation-jt-london'
    photo='riot.jpg'
    label_count=moderate_image(photo, bucket)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
 
