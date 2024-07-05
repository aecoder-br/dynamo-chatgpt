# Dynamo ChatGPT
Custom Node developed to facilitate the use of the ChatGPT API for [chat completion](https://platform.openai.com/docs/api-reference/chat) within Dynamo

## Development
### Prerequisites
- [OpenAI Account Setup](https://platform.openai.com/docs/quickstart/account-setup)
- [OpenAI API Key](https://platform.openai.com/api-keys)
- Add credits to your **Organization** account in the [Billing section](https://platform.openai.com/settings/organization/billing/overview)
- Install the [DynamoChatGPT](./script/DynamoChatGPT.dyf) package in your Dynamo


### Setup & Run
- Search for `DynamoChatGPT` in the Dynamo package search and install the package as shown in the image below

![](/assets/01-install-package.png)

- Download and open the [sample script](/script/sample_dynamo_chatgpt.dyn) from this repository 

![](/assets/03-dynamo-script-sample.png)

- Setup the inputs:
	- **prompt** *(required)*: The prompt (message) you want to send to ChatGPT
	
	- **api_key** *(required)*: Your [OpenAI API Key](#prerequisites)
	
	- **organization_id** *(optional)*: Your [Organization ID](https://platform.openai.com/settings/organization/general)

	- **project_id** *(optional)*: [Your Project ID](https://platform.openai.com/settings/organization/general), under `Project > General`

	- **model** *(required)*: ID of the model to use. [Learn more here!](https://platform.openai.com/docs/models)
		> If you have [ChatGPT Plus](https://openai.com/index/chatgpt-plus/), we recommend using the `gpt-4o` model or newer, otherwise, use `gpt-3.5-turbo` or the latest free version

	- **temperature** *(optional)*: OpenAI description:
		> What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both.

	- **max_tokens** *(optional)*: OpenAI description:
		>The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length.
		
		[Learn more here!](https://platform.openai.com/tokenizer)

	- **top_p** *(optional)*: OpenAI description:
		>An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both.

	- **frequency_penalty** *(optional)*: OpenAI description:
		>Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

		[Learn more here!](https://platform.openai.com/docs/guides/text-generation/parameter-details)

	- **presence_penalty** *(optional)*: OpenAI description:
		>Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

		[Learn more here!](https://platform.openai.com/docs/guides/text-generation/parameter-details)

	- **clear_history** *(optional)*: Set `true`, if you want to clear the chat history before sending the request, otherwise set `false`
		> This script stores the conversation history in `%appdata%\AECOder\dynamochatgpt\history.json`

![](/assets/02-node-descriptions.png)


## License
This sample is licensed under the terms of the [MIT License](http://opensource.org/licenses/MIT).
Please see the [LICENSE](LICENSE) file for more details.