
import boto3

client = boto3.client('comprehend')

response = client.start_pii_entities_detection_job(
    InputDataConfig={
        'S3Uri': 's3://content-moderation-jt-london/detect_sample.txt',
        'InputFormat': 'ONE_DOC_PER_FILE'
    },
    OutputDataConfig={
        'S3Uri': 's3://content-moderation-jt-london',
        #'KmsKeyId': 'arn:aws:kms:eu-west-2:858545927766:alias/content-moderation-s3-pii-redaction'
    },
    Mode='ONLY_REDACTION',
    RedactionConfig={
        'PiiEntityTypes': [
            'ALL'
        ],
        'MaskMode': 'MASK',
        'MaskCharacter': '*'
    },
    DataAccessRoleArn='arn:aws:iam::858545927766:role/content-moderation-for-s3',
    JobName='content-moderation-redaction-2',
    LanguageCode='en',
    #ClientRequestToken='string'
)