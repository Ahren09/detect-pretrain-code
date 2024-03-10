import logging
import os
import os.path as osp
import traceback

import openai

DEFAULT_OPENAI_ENDPOINT = "openaiazure"  # "openai" or "openaiazure"
logging.basicConfig(level=logging.INFO)

def openai_setup(mode: str = DEFAULT_OPENAI_ENDPOINT, idx_auth: int = 0, default_model="gpt-4"):
    """

    Refer to [this page](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/switching-endpoints)
    for more information.

    Refer to [this page](https://platform.openai.com/docs/models/gpt-3-5) for information about authentication.

    """

    assert mode in ["openaiazure", "openai"]

    try:
        if mode == "openai":
            os.environ["OPENAI_API_KEY"] = "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"

            client = openai.OpenAI(
                api_key=os.environ['OPENAI_API_KEY']
            )


        elif mode == "openaiazure":

            lines = open(osp.expanduser('~/azure_openai_key.txt')).readlines()
            segments = lines[idx_auth].strip().split(',')
            azure_openai_key, endpoint_id, region,  = segments[0].strip(' '), segments[1].strip(' '), segments[2].strip(
                ' ')

            # POST https://Cheesecake5.openai.azure.com/openai/deployments/gpt-35-turbo/completions?api-version=2023-12-01-preview
            os.environ['AZURE_DEPLOYMENT'] = deployment_id = default_model # gpt-4 or gpt-4-2

            logging.info(f"Using endpoint {endpoint_id} deployment {deployment_id}")
            azure_openai_endpoint = f'https://{endpoint_id}.openai.azure.com/'
            os.environ['OPENAI_API_VERSION'] = "2023-12-01-preview"
            os.environ['OPENAI_API_TYPE'] = "azure"
            os.environ['DEFAULT_MODEL'] = default_model

            os.environ["AZURE_OPENAI_KEY"] = azure_openai_key

            client = openai.AzureOpenAI(
                api_key=azure_openai_key,
                azure_endpoint=azure_openai_endpoint,
                azure_deployment=deployment_id,

            )


        else:
            raise NotImplementedError


    except:
        traceback.print_exc()
        client = None

    return client
