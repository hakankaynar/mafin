import boto3
from botocore.exceptions import ClientError
import logging


class Emailer:
    AWS_REGION = "us-east-1"
    CHARSET = "UTF-8"
    KID = ""
    KEY = ""

    def __init__(self):
        self.logger = logging.getLogger("Emailer")

    def send(self, to_email, txt):
        try:
            client = boto3.client('ses', region_name=self.AWS_REGION, aws_access_key_id=self.KID,
                                  aws_secret_access_key=self.KEY)
            self.logger.info("Sending email to " + to_email)
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        to_email,
                    ],
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': txt,
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': 'Subject',
                    },
                },
                Source='Mafin <mafin@gizemkaynar.com>',
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            self.logger.info(e.response['Error']['Message'])
        else:
            self.logger.info("Email sent! Message ID:"),
            self.logger.info(response['MessageId'])
