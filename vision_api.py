import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd


def convert(file_name, file_type, txt_name):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"service_account.json"

    client = vision.ImageAnnotatorClient()
    content = file_name
    image = vision.types.Image(content=content)
    response = 0
    if file_type == "Typed":
        response = client.text_detection(image=image) #for text detection in normal images
    elif file_type == "Handwritten":
        response = client.document_text_detection(image=image) #for text detection in handwritten images
    else:
        print("something is wrong")
    texts = response.text_annotations

    df = pd.DataFrame(columns=['locale', 'description'])
    for text in texts:
        df = df.append(dict(locale=text.locale, description=text.description), ignore_index=True)
    extracted_text = df.description[0]
    save_file = open(str(txt_name)+".txt", 'w+')
    save_file.write(extracted_text)
    save_file.close()
    print("done")
    return extracted_text
