import boto3
from datetime import datetime, timezone, timedelta
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ['BUCKET_NAME']  

    # Define o fuso horário de Brasília (UTC-3)
    BR_TIMEZONE = timezone(timedelta(hours=-3))

    # Pega a data/hora atual já ajustada para o fuso horário de Brasília
    now = datetime.now(tz=BR_TIMEZONE).strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"registro_{now}.txt"
    content = f"Arquivo gerado em {now}"

    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=content.encode('utf-8')
    )

    return {
        'statusCode': 200,
        'body': f'Arquivo {filename} criado no bucket {bucket_name}'
    }