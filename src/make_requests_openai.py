import requests
import json


def make_requests_davinci(model_name: str, **kwargs):
    # Set the deployment ID, model name, API version, and API key


    deployment_id = "cheesecake1"
    api_version = "2023-12-01-preview"
    api_key = "457506b3a6b04678b9d7812bcbc125dd"

    # URL for the POST request
    url = (f"https://{deployment_id}.openai.azure.com/openai/deployments/{model_name}/completions?api-version={api_version}")

    # Sample request body
    request_body = kwargs
    # request_body['engine'] = model_name

    # Convert the request body to JSON format
    json_body = json.dumps(request_body)

    # Set headers for the request
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key  # Replace YOUR_API_KEY with your actual API key
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json_body)

    # Print the response
    return response.json()

if __name__ == "__main__":
    model_name = "davinci-002"
    response = make_requests_davinci(model_name=model_name, prompt="Once upon a time,", max_tokens=0, temperature=1.,
                                     logprobs=5,
                                     echo=True)
    print(response)


