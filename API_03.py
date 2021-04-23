# Speech to Text
# First we import SpeechToTextV1 from ibm_watson.
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import wget

# The service endpoint is based on the location of the service instance, 
# we store the information in the variable URL. To find out which URL to 
# use, view the service credentials and paste the url here.
url_s2t = "https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/82ed2ec2-291a-4dc5-879f-5dc7b28b02b9"
iam_apikey_s2t = "hJ2mOKcEYTtJPiYjEut2cqztt7sawwCZ9sSRnPHs1_nq"

# You create a Speech To Text Adapter object the parameters are the 
# endpoint and API key
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

# Lets download the audio file that we will use to convert into text.
# wget -O PolynomialRegressionandPipelines.mp3 https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/PolynomialRegressionandPipelines.mp3

filename='PolynomialRegressionandPipelines.mp3'

# We create the file object wav with the wav file using open ; we set the 
# mode to "rb" , this is similar to read mode, but it ensures the file is 
# in binary mode.We use the method recognize to return the recognized text. 
# The parameter audio is the file object wav, the parameter content_type is 
# the format of the audio file.
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')

# The attribute result contains a dictionary that includes the translation:
print(response.result)

from pandas import json_normalize

json_normalize(response.result['results'],"alternatives")
print(response)

# We can obtain the recognized text and assign it to the variable 
# recognized_text:
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
print(type(recognized_text))

# Language Translator
# First we import LanguageTranslatorV3 from ibm_watson.
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# The service endpoint is based on the location of the service instance, 
# we store the information in the variable URL. To find out which URL 
# to use, view the service credentials.
url_lt='https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/b60e14cb-8afc-441c-93e8-6c240a03dddd'
# You require an API key, and you can obtain the key on the Dashboard.
apikey_lt='qeFFmCRIzVD0fbPWdNgTAapdtwZLm1WCAiLp6_Stq71x'

# API requests require a version parameter that takes a date in the format 
# version=YYYY-MM-DD. This lab describes the current version of Language 
# Translator, 2018-05-01
version_lt='2018-05-01'

# we create a Language Translator object language_translator:
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

# We can get a Lists the languages that the service can identify. The 
# method Returns the language code. For example English (en) to Spanis 
# (es) and name of each language.
from pandas import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

# We can use the method translate this will translate the text. The 
# parameter text is the text. Model_id is the type of model we would like 
# to use use we use list the language . In this case, we set it to 'en-es' 
# or English to Spanish. We get a Detailed Response object 
# translation_response
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
print(translation_response)

# The result is a dictionary.
translation=translation_response.get_result()
print(translation)

# We can obtain the actual translation as a string as follows:
spanish_translation =translation['translations'][0]['translation']
print(spanish_translation) 

# We can translate back to English
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

# We can obtain the actual translation as a string as follows:
translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)

# Quiz
# Translate to French.
French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

print(French_translation['translations'][0]['translation'])