# Prerequisites

- Replace `ps-translations-fmc` with your own bucket name 
- Update the `translate-allow-s3-policy.json` file with the bucket name
- Update `trust-policy.json` with your own AWS Account ID

# Translate Text API: 

```bash
aws translate translate-text \
--region us-west-2 \
--source-language-code "ru" \
--target-language-code "en" \
--text "Иван Ильич был сотоварищ собравшихся господ, и все любили его. Он болел уже несколько недель; говорили, что болезнь его неизлечима. Место оставалось за ним, но было соображение о том, что в случае его смерти Алексеев может быть назначен на его место, на место же Алексеева – или Винников, или Штабель. Так что, услыхав о смерти Ивана Ильича, первая мысль каждого из господ, собравшихся в кабинете, была и о том, какое значение может иметь эта смерть на перемещения или повышения самих членов или их знакомых."
```

# Translate Document API: 

First, create the S3 bucket for input files and translations. Remember to change the bucket name and region as needed. 

```bash
aws s3api create-bucket --bucket ps-translations-fmc --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
```

Then upload the document to S3:

```bash
aws s3 cp russian-text-ivan-illich.txt s3://ps-translations-fmc/russian-text-ivan-illich.txt
```

Then create a role for the Amazon Translate Service to access S3:

```bash



Then you can translate the document:

```bash

aws translate start-text-translation-job \
--job-name ivan-ru-to-en \
--input-data-config "S3Uri=s3://ps-translations-fmc-test/russian-text-ivan-illich.txt,InputFormat=TXT,ContentType=text/plain" \
--output-data-config "S3Uri=s3://ps-translations-fmc-test/english-ivan-illich,OutputFormat=TXT" \
--source-language-code "ru" \
--target-language-code "en" \
--data-access-role-arn


aws translate start-text-translation-job \
--job-name my-translation-job \

--data-access-role-arn "arn:aws:iam::123456789012:role/TranslateRole"
