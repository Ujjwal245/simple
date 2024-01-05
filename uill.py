from googletrans import Translator, LANGUAGES

def translate_with_googletrans(phrase, target_language="en"):
    translator = Translator()

    try:
        translation = translator.translate(phrase, dest=target_language)
        detected_language = LANGUAGES.get(translation.src, 'Unknown')
        target_language_name = LANGUAGES.get(target_language, 'Unknown')

        print(f"Detected language: {detected_language}")
        print(f"Target language: {target_language_name} ({target_language})")

        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return phrase

# Define a set of allowed target languages
allowed_languages = {"es": "Spanish", "zh-CN": "Mandarin", "fr": "French", "ja": "Japanese"}

# Take user input for phrase and validate target language
user_phrase = input("Enter a phrase: ")
user_language = input(f"Enter the target language code ({', '.join(allowed_languages.keys())}): ")

if user_language not in allowed_languages:
    print("Translation for the specified language is not allowed.")
else:
    translated_phrase = translate_with_googletrans(user_phrase, user_language)
    print("Translated phrase:", translated_phrase)
