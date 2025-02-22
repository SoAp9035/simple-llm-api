import requests


class GeminiError(Exception):
    def __init__(self, message: str = "GeminiAPI Error"):
        super().__init__(message)


class MistralError(Exception):
    def __init__(self, message: str = "MistralAPI Error"):
        super().__init__(message)


class OpenAIError(Exception):
    def __init__(self, message: str = "OpenAIAPI Error"):
        super().__init__(message)


class GeminiAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "gemini-2.0-flash") -> None:
        self._parameters = {"key": api_key}
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 0, top_k: int = 40, top_p: float = 0.95, max_output_tokens: int = 8192) -> str:
        self.gemini_endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self._model}:generateContent"

        data = {
            "contents": [{"role": "user", "parts": [{"text": user_prompt}]}],
            "systemInstruction": {"role": "user", "parts": [{"text": system_prompt}]},
            "generationConfig": {
                "temperature": temperature,
                "topK": top_k,
                "topP": top_p,
                "maxOutputTokens": max_output_tokens,
                "responseMimeType": "text/plain",
            },
        }

        response = requests.post(self.gemini_endpoint, json=data, params=self._parameters)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
        elif response.status_code == 400:
            raise GeminiError(f"Error {response.status_code}: {response.json()["error"]["details"][0]["reason"]}")
        else:
            raise GeminiError(f"Error {response.status_code}: {response.text}")


class MistralAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "mistral-large-latest") -> None:
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 0, top_p: float = 1, max_tokens: int = 4096) -> str:
        self.mistral_endpoint = f"https://api.mistral.ai/v1/chat/completions"

        data = {
            "model": self._model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens
        }

        response = requests.post(self.mistral_endpoint, json=data, headers=self._headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        elif response.status_code == 422:
            raise MistralError(f"Error {response.status_code}: {response.json()["detail"][0]["msg"].strip()}")
        else:
            raise MistralError(f"Error {response.status_code}: {response.text}")


class OpenAIAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "gpt-4o") -> None:
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 1, top_p: float = 1, max_completion_tokens: int = 4096) -> str:
        self.openai_endpoint = f"https://api.openai.com/v1/chat/completions"

        data = {
            "model": self._model,
            "messages": [
                {
                    "role": "developer",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": temperature,
            "top_p": top_p,
            "max_completion_tokens": max_completion_tokens
        }

        response = requests.post(self.openai_endpoint, json=data, headers=self._headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            raise OpenAIError(f"Error {response.status_code}: {response.text}")
