First, run a basic translation with formality settings turned to formal in JSON:

```bash
aws translate translate-text \
  --text "How are you doing today?" \
  --source-language-code en \
  --target-language-code es \
  --settings '{"Formality":"FORMAL"}'
```

Now try this with informal: 

```bash
aws translate translate-text \
  --text "How are you doing today?" \
  --source-language-code en \
  --target-language-code es \
  --settings '{"Formality":"INFORMAL"}'
```

Here are some similar examples in German using the non-JSON version of settings:

```bash
aws translate translate-text \
  --text "How are you doing today?" \
  --source-language-code en \
  --target-language-code de \
  --settings Formality=FORMAL
```

```bash
aws translate translate-text \
  --text "How are you doing today?" \
  --source-language-code en \
  --target-language-code de \
  --settings Formality=INFORMAL
```

