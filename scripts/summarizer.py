from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

def summarize_text(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_entities(document=document)

    keywords = [entity.name for entity in response.entities if entity.salience > 0.01]
    return "キーワード: " + ", ".join(keywords[:10])