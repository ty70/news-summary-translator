from google.cloud import translate_v2 as translate

client = translate.Client()

def translate_to_english(text):
    result = client.translate(text, target_language='en', source_language='ja')
    return result['translatedText']