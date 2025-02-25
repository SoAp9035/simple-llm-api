import requests


class OpenAIError(Exception):
    def __init__(self, message: str = "OpenAIAPI Error"):
        super().__init__(message)

class AnthropicError(Exception):
    def __init__(self, message: str = "AnthropicAPI Error"):
        super().__init__(message)

class MistralError(Exception):
    def __init__(self, message: str = "MistralAPI Error"):
        super().__init__(message)

class GeminiError(Exception):
    def __init__(self, message: str = "GeminiAPI Error"):
        super().__init__(message)


class OpenAIAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "gpt-4o") -> None:
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 1, top_p: float = 1, max_completion_tokens: int = 2048) -> str:
        self.openai_endpoint = f"https://api.openai.com/v1/chat/completions"

        data = {
            "model": self._model,
            "temperature": temperature,
            "top_p": top_p,
            "max_completion_tokens": max_completion_tokens,
            "messages": [
                {
                    "role": "developer",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }

        response = requests.post(self.openai_endpoint, json=data, headers=self._headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            try:
                error_msg = response.json()["error"]["message"]
            except Exception:
                error_msg = response.text
            finally:
                raise OpenAIError(f"Error {response.status_code} - {error_msg}")


class AnthropicAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "claude-3-7-sonnet-20250219") -> None:
        self._headers = {
            "x-api-key": f"{api_key}",
            "anthropic-version": "2023-06-01"
        }
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 1, max_tokens: int = 2048) -> str:
        self.anthropic_endpoint = f"https://api.anthropic.com/v1/messages"

        data = {
            "model": self._model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": system_prompt,
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        }

        response = requests.post(self.anthropic_endpoint, json=data, headers=self._headers)
        if response.status_code == 200:
            return response.json()["content"][0]["text"]
        else:
            try:
                error_msg = response.json()["error"]["message"]
            except Exception:
                error_msg = response.text
            finally:
                raise AnthropicError(f"Error {response.status_code} - {error_msg}")


class GeminiAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "gemini-2.0-flash") -> None:
        self._parameters = {"key": api_key}
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 1, top_k: int = 40, top_p: float = 0.95, max_output_tokens: int = 2048) -> str:
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
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        else:
            try:
                error_msg = response.json()["error"]["message"]
            except Exception:
                error_msg = response.text
            finally:
                raise GeminiError(f"Error {response.status_code} - {error_msg}")


class MistralAPI:
    def __init__(self, api_key: str = "YOUR_API_KEY", model: str = "mistral-large-latest") -> None:
        self._headers = {"Authorization": f"Bearer {api_key}"}
        self._model = model

    def simple_request(self, user_prompt: str, system_prompt: str = "You are a helpful assistant.", temperature: float = 0.7, top_p: float = 1, max_tokens: int = 2048) -> str:
        self.mistral_endpoint = f"https://api.mistral.ai/v1/chat/completions"

        data = {
            "model": self._model,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
        }

        response = requests.post(self.mistral_endpoint, json=data, headers=self._headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            try:
                error_msg = response.json()["detail"][0]["msg"]
            except Exception:
                error_msg = response.text
            finally:
                raise MistralError(f"Error {response.status_code} - {error_msg}")
