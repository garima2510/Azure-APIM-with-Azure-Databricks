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
    base_url="https://adb-4137061686115761.1.azuredatabricks.net/serving-endpoints"
)

response = client.chat.completions.create(
    model="databricks-meta-llama-3-3-70b-instruct",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is the top use-case for Azure APIM",
      }
    ],
    max_tokens=256
)

print(response.choices[0].message.content)
