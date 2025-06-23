import boto3

client = boto3.client("translate")


def translate_text(text, source_lang='en', target_lang='es'):
    response = client.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    return response['TranslatedText']


def lambda_handler(event, context):
    text = event['text']
    source_lang = event['source_lang']
    target_lang = event['target_lang']
    translated_text = translate_text(text, source_lang, target_lang)
    return {
        'statusCode': 200,
        'body': translated_text
    }

# Example event
# {
#    "text":"Hello, world!",
#    "source_lang":"en",
#    "target_lang":"es"
# }
