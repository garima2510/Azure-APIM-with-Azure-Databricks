import httpx
import logging
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("httpx")
logger.setLevel(logging.DEBUG)

client = OpenAI(
    api_key=os.getenv("DATABRICKS_API_KEY"),
    base_url="https://apim-rfc-dbpim.azure-api.net/test",
    default_headers= {
        "Ocp-Apim-Subscription-Key": os.getenv("APIM_SUBSCRIPTION_KEY")
    }
)

print("------------------------------------------------------------")
print(client.default_headers)
print("------------------------------------------------------------")

response = client.chat.completions.create(
    model=os.getenv("MODEL_NAME", "databricks-meta-llama-3-3-70b-instruct"),
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
