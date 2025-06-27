import boto3

# Create a Translate client
translate = boto3.client('translate')

text = "How are you doing today?"

# Formal Spanish translation
response_formal_es = translate.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='es',
    Settings={
        'Formality': 'FORMAL'
    }
)
print("Spanish (Formal):", response_formal_es['TranslatedText'])

# Informal Spanish translation
response_informal_es = translate.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='es',
    Settings={
        'Formality': 'INFORMAL'
    }
)
print("Spanish (Informal):", response_informal_es['TranslatedText'])

# Formal German translation
response_formal_de = translate.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='de',
    Settings={
        'Formality': 'FORMAL'
    }
)
print("German (Formal):", response_formal_de['TranslatedText'])

# Informal German translation
response_informal_de = translate.translate_text(
    Text=text,
    SourceLanguageCode='en',
    TargetLanguageCode='de',
    Settings={
        'Formality': 'INFORMAL'
    }
)
print("German (Informal):", response_informal_de['TranslatedText'])
