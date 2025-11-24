import httpx
import logging
import os
from openai import OpenAI
from dotenv import load_dotenv
import LoggingTransport

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("httpx")
logger.setLevel(logging.DEBUG)

#to check request payload
transport = LoggingTransport.LoggingTransport(httpx.HTTPTransport())

client = OpenAI(
    api_key=os.getenv("DATABRICKS_API_KEY"),
    base_url="https://apim-rfc-dbpim.azure-api.net/dynamic",
    default_headers= {
        "Ocp-Apim-Subscription-Key": os.getenv("APIM_SUBSCRIPTION_KEY")
    },
    http_client=httpx.Client(transport=transport)
)

#print("------------------------------------------------------------")
#print(client.default_headers)
#print("------------------------------------------------------------")

response = client.chat.completions.create(
    #model="databricks-claude-sonnet-4-5",
    model="databricks-gpt-oss-20b",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is a galaxy in 50 words?",
      }
    ],
    max_tokens=256
)

print("--------------------RESPONSE-------------------------")
print(response.choices[0].message.content)
