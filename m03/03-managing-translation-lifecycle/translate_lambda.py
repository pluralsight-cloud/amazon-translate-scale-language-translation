import boto3
import urllib.parse

s3 = boto3.client('s3')
translate = boto3.client('translate')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        text = response['Body'].read().decode('utf-8')
        result = translate.translate_text(
            Text=text,
            SourceLanguageCode='es',
            TargetLanguageCode='en'
        )
        print("Original:", text)
        print("Translated:", result['TranslatedText'])
        return {
            'statusCode': 200,
            'body': result['TranslatedText']
        }
    except Exception as e:
        print(e)
        raise e
