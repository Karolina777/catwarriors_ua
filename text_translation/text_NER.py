import spacy


def get_named_entities(text):
    # Check if the 'en_core_web_sm' model is installed, and if not, download and install it
    if not spacy.util.is_package('en_core_web_sm'):
        download('en_core_web_sm')

    # Load the spaCy English model
    nlp = spacy.load('en_core_web_sm')

    # Process the text with spaCy
    doc = nlp(text)

    # Extract named entities from the document
    named_entities = list()
    for entity in doc.ents:
        if entity.label_ not in ['TIME', 'CARDINAL']:
            if ',' or "'" not in entity.text:
                named_entities.append(entity.text)

    # Return the set of named entities
    return named_entities
