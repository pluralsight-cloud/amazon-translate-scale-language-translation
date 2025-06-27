Profanity Settings require you to add the `--settings` flag with the Profanity condition. For shorter translations like the following:

```bash
aws translate translate-text \
--source-language-code "es" \
--target-language-code "en" \
--text "Que mierda." \
--settings Profanity="MASK"
```

It will simply output the a brief, but potentially confusing translation that masks profanity with this string: "?$#@$."

For longer passages it will still mask profanity but the context may be more clear:

```bash
aws translate translate-text \
--source-language-code "es" \
--target-language-code "en" \
--text "Me desperté lentamente, ayer fue mi cumple. Que puta buena fiesta. Me quedé unos minutos allí, respirando profundo, disfrutando del momento perfecto. Pero una repentina presión en el estómago me recordó que la belleza del día no podía postergar lo inevitable. Con un suspiro resignado, me levanté y fui directo al baño. La vida, después de todo, también tiene su lado muy humano. Mierda." \
--settings Profanity="MASK"
```