from simple_llm_api import GeminiAPI


gemini = GeminiAPI("YOUR_API_KEY")

response = gemini.simple_request("Hi!")
print(response)
