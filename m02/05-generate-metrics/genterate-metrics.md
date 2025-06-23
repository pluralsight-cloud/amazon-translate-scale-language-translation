# Generate Metrics

To generate a few metrics for Amazon Translate to show within CloudWatch you can run the basic translation command a few times with different language pairs:

```bash
aws translate translate-text \
--region us-west-2 \
--source-language-code "en" \
--target-language-code "es" \
--text "Hello! How are you today my friend?"
```

```bash
aws translate translate-text \
--region us-west-2 \
--source-language-code "en" \
--target-language-code "de" \
--text "Hello! How are you today my friend?"
```

```bash
aws translate translate-text \
--region us-west-2 \
--source-language-code "en" \
--target-language-code "fr" \
--text "Hello! How are you today my friend?"
```

```bash
aws translate translate-text \
--region us-west-2 \
--source-language-code "ru" \
--target-language-code "en" \
--text "Иван Ильич был сотоварищ собравшихся господ, и все любили его. Он болел уже несколько недель; говорили, что болезнь его неизлечима."
```

Run each of these commands a few times.
