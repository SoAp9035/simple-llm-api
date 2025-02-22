from simple_llm_api import OpenAIAPI


openai = OpenAIAPI("YOUR_API_KEY")

response = openai.simple_request("Hi!")
print(response)
