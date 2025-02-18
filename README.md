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
# af: Afrikaans
# sq: Albanian
# am: Amharic
# ar: Arabic
# hy: Armenian
# az: Azerbaijani
# eu: basque
# be: Belarusian
# bn: Bengali
# bs: Bosnian
# bg: Bulgarian
# ca: Catalan
# ceb: Cebuano
# ny: Chichewa
# zh-cn: Chinese (simplified)
# zh-tw: Chinese (Traditional)
# co: Corsican
# hr: Croatian
# cs: Czech
# da: danish
# nl: dutch
# en: English
# eo: Esperanto
# et: Estonian
# tl: Filipino
# fi: Finnish
# fr: french
# fy: Frisian
# gl: Galician
# ka: Georgian
# de: german
# el: greek
# gu: Gujarati
# ht: Haitian Creole
# ha: Hausa
# haw: Hawaiian
# iw: hebrew
# he: hebrew
# hi: hindi
# hmn: hmong
# hu: hungarian
# is: icelandic
# ig: igbo
# id: indonesian
# ga: irish
# it: italian
# ja: japanese
# jw: javanese
# kn: kannada
# kk: kazakh
# km: khmer
# ko: korean
# ku: kurdish (kurmanji)
# ky: Kyrgyz
# lo: lao
# la: Latin
# lv: Latvian
# lt: Lithuanian
# lb: Luxembourgish
# mk: Macedonian
# mg: Malagasy
# ms: Malay
# ml: Malayalam
# mt: Maltese
# mi: Maori
# mr: Marathi
# mn: Mongolian
# my: Myanmar (Burmese)
# ne: Nepali
# no: Norwegian
# or: odia
# ps: Pashto
# fa: Persian
# pl: polish
# pt: Portuguese
# pa: Punjabi
# ro: Romanian
# ru: Russian
# sm: Samoan
# gd: Scots Gaelic
# sr: Serbian
# st: Sesotho
# sn: Shona
# sd: Sindhi
# si: Sinhala
# sk: Slovak
# sl: Slovenian
# so: Somali
# es: Spanish
# su: Sundanese
# sw: Swahili
# sv: Swedish
# tg: Tajik
# ta: Tamil
# te: Telugu
# th: Thai
# tr: Turkish
# uk: Ukrainian
# ur: urdu
# ug: Uyghur
# uz: Uzbek
# vi: Vietnamese
# cy: welsh
# xh: Xhosa
# yi: Yiddish
# yo: Yoruba
# zu: Zulu
