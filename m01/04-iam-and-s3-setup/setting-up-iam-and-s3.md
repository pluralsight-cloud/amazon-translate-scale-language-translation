# Prerequisites

- Replace `ps-translations-fmc` with your own bucket name below
- Update the `translate-allow-s3-policy.json` file with the same bucket name
- Update `trust-policy.json` with your own AWS Account ID

**Remember** - Run the commands below in the same directory as the json files for this section. Or edit the commands to reference the correct location of the relevant JSON files.

# Preparing Your Translation Environment

First, create the S3 bucket for input files and translations. Remember to change the bucket name as needed:

```bash
aws s3api create-bucket --bucket ps-translations-fmc
```

Then create a role with a trust policy for the Amazon Translate Service:

```bash
aws iam create-role \
--role-name TranslateS3Role \
--assume-role-policy-document file://trust-policy.json
```

Then create a policy for that role to assume:

```bash
aws iam create-policy \
--policy-name s3AccessForTranslate \
--policy-document file://translate-allow-s3-policy.json
```

Copy the resulting ARN from the command above or get it again with this command:

```bash
aws iam list-policies \
--query 'Policies[?PolicyName==`s3AccessForTranslate`].Arn'
```

Then associate the policy and role using the role name and the policy ARN you just copied which should look something like this:

```bash
aws iam attach-role-policy \
--role-name TranslateS3Role \
--policy-arn arn:aws:iam::804540873837:policy/s3AccessForTranslate
```

Then you are set up to work with Amazon Translate and S3! Just make sure to keep a hold of the ARN of the role so you can use it in later examples.
