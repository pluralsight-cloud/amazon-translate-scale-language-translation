import boto3
import random
import time
from botocore.exceptions import ClientError


def get_requests():
    valid_languages = [("en", "es"), ("en", "fr"), ("en", "de"), ("en", "it")]
    invalid_languages = [("xx", "yy"), ("zz", "aa"), ("qq", "ww"), ("rr", "tt")]
    requests = [random.choice(valid_languages) for _ in range(70)]
    requests += [random.choice(invalid_languages) for _ in range(10)]
    random.shuffle(requests)
    return requests


def perform_translation(requests):
    translate = boto3.client("translate")
    for source_lang, target_lang in requests:
        try:
            response = translate.translate_text(
                Text="Hello, how are you?",
                SourceLanguageCode=source_lang,
                TargetLanguageCode=target_lang
            )
            print(f"Translation from {source_lang} to {target_lang}: {response['TranslatedText']}")
        except ClientError as e:
            print(f"Error translating from {source_lang} to {target_lang}: {e}")
        time.sleep(0.1)


def generate_data():
    requests = get_requests()
    perform_translation(requests)


generate_data()
