# Batch Translation Jobs

To prepare a translation job, start by uploading a source file or files to the S3 bucket you created earlier (remember to replace my bucket name with your own):

```bash
aws s3 cp english-text-alice-wonderland.txt s3://ps-translations-fmc/input/english-text-alice-wonderland.txt
```

Then, you'll need the ARN of the role that Amazon Translate will use to access S3. We created this in the earlier demo. We named it `TranslateS3Role`, if you kept the name the same you can get the ARN value with this command or by looking for it in the AWS Console:

```bash
aws iam list-roles \
--query  'Roles[?RoleName==`TranslateS3Role`].Arn'
```

It should look something like this `arn:aws:iam::804540873837:role/TranslateS3Role`.

Now you can translate the document:

```bash
aws translate start-text-translation-job \
--job-name "translate-alice-wonderland"
--input-data-config "S3Uri=s3://ps-translations-fmc/input/,ContentType=text/plain" \
--output-data-config "S3Uri=s3://ps-translations-fmc/translation-outputs/english-ivan-illich/" \
--source-language-code "en" \
--target-language-codes es fr de \
--data-access-role-arn "arn:aws:iam::804540873837:role/TranslateS3Role"
```

Then you can check on the progress of your job:

```bash
aws translate list-text-translation-jobs
```

You can also review the output of the job in the S3 Bucket:

```bash
aws s3 ls s3://ps-translations-fmc/translation-outputs/english-ivan-illich
```