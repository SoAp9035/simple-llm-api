from simple_llm_api import DeepSeekAPI


deepseek = DeepSeekAPI("YOUR_API_KEY")

response = deepseek.simple_request("Hi!")
print(response)
