# Translate Text API: 

```bash
aws translate translate-text \
--region us-west-2 \
--source-language-code "ru" \
--target-language-code "en" \
--text "Иван Ильич был сотоварищ собравшихся господ, и все любили его."
```

A simple phrase in English to Spanish: 

```bash
aws translate translate-text \
--source-language-code "en" \
--target-language-code "es" \
--text "Hello my good friend. How are you doing today?"
```

