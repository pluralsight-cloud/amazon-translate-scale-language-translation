Remember to change the demo account id of `804540873837` and the bucket name of `ps-translation-lifecycle-fmc` to your own account ID and bucket name in all the commands and inside `notification.json`. 

First, create the bucket:

```bash
aws s3api create-bucket --bucket ps-translation-lifecycle-fmc
```

Then, create a role with a trust policy that allows Lambda to assume it:

```bash
aws iam create-role \
--role-name lambda-s3-translate-role \
--assume-role-policy-document file://trust-policy.json
```

Then, allow the role to use several managed AWS policies:

```bash
aws iam attach-role-policy --role-name lambda-s3-translate-role --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
aws iam attach-role-policy --role-name lambda-s3-translate-role --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsFullAccess
aws iam attach-role-policy --role-name lambda-s3-translate-role --policy-arn arn:aws:iam::aws:policy/AmazonTranslateFullAccess
```

Then create your Lambda Function package:

```bash
zip function.zip translate_lambda.py
```

And upload it:

```
aws lambda create-function \
  --function-name TranslateSpanishToEnglish \
  --zip-file fileb://function.zip \
  --handler translate_lambda.lambda_handler \
  --runtime python3.12 \
  --role arn:aws:iam::804540873837:role/lambda-s3-translate-role
```

Then allow S3 to trigger it:

```bash
aws lambda add-permission \
--function-name TranslateSpanishToEnglish \
--principal s3.amazonaws.com \
--statement-id s3invoke \
--action "lambda:InvokeFunction" \
--source-arn arn:aws:s3:::ps-translation-lifecycle-fmc
```

Then, have the S3 bucket set up a trigger for your Lambda:

```bash
aws s3api put-bucket-notification-configuration \
--bucket ps-translation-lifecycle-fmc \
--notification-configuration file://notification.json
```

# Testing Our App!

Now that we have all the configuration we can test it out! Start by uploading a file to the S3 bucket:

```bash
aws s3 cp sample_text.txt s3://ps-translation-lifecycle-fmc/sample_text.txt
```

Then let's see our Lambda translate it live:

```bash
aws logs describe-log-groups \
--query "logGroups[?contains(logGroupName,'/aws/lambda/TranslateSpanishToEnglish')].logGroupName" \
--output text
```

```bash
aws logs tail /aws/lambda/TranslateSpanishToEnglish --follow
```
