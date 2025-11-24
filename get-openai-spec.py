from databricks.sdk import WorkspaceClient
import json

w = WorkspaceClient()
endpoint = w.serving_endpoints.get(name="model-name") # model name like databricks-meta-llama-3-3-70b-instruct
print(f"Endpoint state: {endpoint.state.ready}")
print(f"Update state: {endpoint.state.config_update}")
