from simple_llm_api import MistralAPI


mistral = MistralAPI("YOUR_API_KEY")

response = mistral.simple_request("Hi!")
print(response)
