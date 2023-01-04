import pandas as pd
import requests
import time
import os
import pprint



# arts = ['wood burn art', 'sculpture', 'Stained Glass Artwork', 'graffiti art designs', 'digital art', 'coffee art']
facials = ['chevron mustache young men', 'toothbrush mustache styles', 'pencil mustache styles' , 'handlebar mustache styles', 'horseshoe mustache styles']



for facial in facials:
    api_key = "Azure API Key"
    endpoint = "https://api.bing.microsoft.com"

    url = f"{endpoint}/v7.0/images/search/"
    #url = f"{endpoint}/bing/v7.0/search"

    headers= {"Ocp-Apim-Subscription-Key": api_key}

    params = {
        "q" : facial,
        #"license" : "public",

        "imageType": "photo"
        #"safeSearch" : "Strict"
    }


    new_offset = 0
    contentUrls =[]

    while new_offset <= 100:

        params["offset"] = new_offset

        response = requests.get(url, headers=headers, params=params)

        response.raise_for_status()

        result = response.json()

        time.sleep(1)

        new_offset = result["nextOffset"]
        for item in result["value"]:
            content_url = item["contentUrl"]

            contentUrls.append(content_url)


    dir_path = f"C:/Users/farha/KAGGLE_DS_PROJECTS/Iconic Shades Classifier/train_data/{facial}"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    for i, url in enumerate(contentUrls):

        path = os.path.join(dir_path,str(i)+'.jpg')

        try:
            with open(path, "wb") as f:
                image_data = requests.get(url)

                f.write(image_data.content)
        except OSError:
            pass


