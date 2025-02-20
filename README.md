# Language-Translator
A Python module that can be used to translate a variety of languages
There are a few things that need to be done before you can use this module:
-Create the fcntl python file and place it in the directory (refer to the fcntl.txt file)
-Install the following PIP packages:
googletrans, translate, langdetect, asyncio, speech_recognition, pyttsx3, re

IMPORTANT!!
There is currently an issue where if you say a phrase that contains more than one iteration of "to" the translator will make an error because it hears that as you are trying to translate to a non-existent language
Example: You say " Translate welcome TO my house to Spanish", instead of translating to Spanish, it will try to translate it to "my house to Spanish.

This module will not only translate languages but also give you the option to view the supported languages
So far these are the supported languages (106): (along with the language code)
Code  | Language
af: afrikaans
sq: albanian
am: amharic
ar: arabic
hy: armenian
az: azerbaijani
eu: basque
be: belarusian
bn: bengali
bs: bosnian
bg: bulgarian
ca: catalan
ceb: cebuano
ny: chichewa
zh-cn: chinese (simplified)
zh-tw: chinese (traditional)
co: corsican
hr: croatian
cs: czech
da: danish
nl: dutch
en: english
eo: esperanto
et: estonian
tl: filipino
fi: finnish
fr: french
fy: frisian
gl: galician
ka: georgian
de: german
el: greek
gu: gujarati
ht: haitian creole
ha: hausa
haw: hawaiian
iw: hebrew
he: hebrew
hi: hindi
hmn: hmong
hu: hungarian
is: icelandic
ig: igbo
id: indonesian
ga: irish
it: italian
ja: japanese
jw: javanese
kn: kannada
kk: kazakh
km: khmer
ko: korean
ku: kurdish (kurmanji)
ky: kyrgyz
lo: lao
la: latin
lv: latvian
lt: lithuanian
lb: luxembourgish
mk: macedonian
mg: malagasy
ms: malay
ml: malayalam
mt: maltese
mi: maori
mr: marathi
mn: mongolian
my: myanmar (burmese)
ne: nepali
no: norwegian
or: odia
ps: pashto
fa: persian
pl: polish
pt: portuguese
pa: punjabi
ro: romanian
ru: russian
sm: samoan
gd: scots gaelic
sr: serbian
st: sesotho
sn: shona
sd: sindhi
si: sinhala
sk: slovak
sl: slovenian
so: somali
es: spanish
su: sundanese
sw: swahili
sv: swedish
tg: tajik
ta: tamil
te: telugu
th: thai
tr: turkish
uk: ukrainian
ur: urdu
ug: uyghur
uz: uzbek
vi: vietnamese
cy: welsh
xh: xhosa
yi: yiddish
yo: yoruba
zu: zulu
