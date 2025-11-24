# Azure Databricks APIM Integration

This project demonstrates how to integrate Azure Databricks serving endpoints with Azure API Management (APIM) using the OpenAI Python SDK.

## Overview

The repository contains Python scripts that showcase:
- Querying Databricks serving endpoints directly
- Accessing Databricks models through Azure APIM
- Using OpenAI SDK for chat completions with Databricks models

## Resources

- [Query Chat Models - Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/machine-learning/model-serving/query-chat-models)
- [Databricks - Serve Multiple Models to Serving Endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-multiple-models-to-serving-endpoint)

## Prerequisites

- Python 3.8 or higher
- Azure Databricks workspace with serving endpoints
- Azure API Management instance
- Valid API keys for both services

## Installation

1. Clone the repository:
```bash
git clone git remote add origin https://github.com/garima2510/Azure-APIM-with-Azure-Databricks.git
cd azure-databricks-apim
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Fill in your actual credentials in the `.env` file

```bash
cp .env.example .env
```

## Configuration

Edit the `.env` file with your credentials:

```env
DATABRICKS_API_KEY=your_databricks_api_key_here
APIM_BASE_URL=https://your-apim-instance.azure-api.net/test
APIM_SUBSCRIPTION_KEY=your_apim_subscription_key_here
MODEL_NAME=databricks-meta-llama-3-3-70b-instruct
```

## Project Files

### `get-openai-spec.py`
Retrieves the serving endpoint specification from Databricks workspace.

### `openai_client_query.py`
Queries Databricks serving endpoints directly using the OpenAI SDK.

### `openai_apim.py`
Queries Databricks models through Azure APIM using the OpenAI SDK with custom headers.

## Usage

### Query Databricks Endpoint Directly
```bash
python openai_client_query.py
```

### Query Through Azure APIM
```bash
python openai_apim.py
```

### Get Endpoint Specification
```bash
python get-openai-spec.py
```

## Features

- **Environment-based Configuration**: Secure credential management using `.env` files
- **OpenAI SDK Compatibility**: Uses the standard OpenAI Python SDK for familiar API
- **Azure APIM Integration**: Routes requests through APIM for additional governance and monitoring
- **Debug Logging**: Includes HTTP request/response logging for troubleshooting

## Security Notes

- Never commit the `.env` file to version control
- Use the `.env.example` file as a template
- Rotate API keys regularly
- Use Azure Key Vault for production deployments

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue in the GitHub repository.
