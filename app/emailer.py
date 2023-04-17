import boto3
from botocore.exceptions import ClientError
import logging
import datetime


class Emailer:
    AWS_REGION = "us-east-1"
    CHARSET = "UTF-8"

    def __init__(self):
        self.logger = logging.getLogger("Emailer")

    def send(self, to_email, txt):
        try:
            current_datetime = datetime.datetime.now()
            str_date = current_datetime.strftime("%d-%m-%Y")

            client = boto3.client('ses', region_name=self.AWS_REGION)
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
                        'Data': "Signals - " + str_date,
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
