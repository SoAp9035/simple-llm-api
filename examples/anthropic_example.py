from simple_llm_api import AnthropicAPI


anthropic = AnthropicAPI("YOUR_API_KEY")

response = anthropic.simple_request("Hi!")
print(response)
