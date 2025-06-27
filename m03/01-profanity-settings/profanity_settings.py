import boto3

# Create the AWS Translate client
translate = boto3.client('translate')

# Short input with profanity
short_text = "Que mierda."

response_short = translate.translate_text(
    Text=short_text,
    SourceLanguageCode="es",
    TargetLanguageCode="en",
    Settings={
        'Profanity': 'MASK'
    }
)
print("Short text (profanity masked):", response_short['TranslatedText'])

# Longer input with context and profanity
long_text = (
    "Me desperté lentamente, ayer fue mi cumple. Que puta buena fiesta. "
    "Me quedé unos minutos allí, respirando profundo, disfrutando del momento perfecto. "
    "Pero una repentina presión en el estómago me recordó que la belleza del día no podía postergar lo inevitable. "
    "Con un suspiro resignado, me levanté y fui directo al baño. La vida, después de todo, también tiene su lado muy humano. Mierda."
)

response_long = translate.translate_text(
    Text=long_text,
    SourceLanguageCode="es",
    TargetLanguageCode="en",
    Settings={
        'Profanity': 'MASK'
    }
)
print("\nLong text (profanity masked):", response_long['TranslatedText'])
