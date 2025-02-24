# Simple LLM API

A simple and easy-to-use Python wrapper for popular LLM APIs (OpenAI, Mistral, Google Gemini).

## Installation

```bash
pip install simple-llm-api
```

## Features

- 🎯 Simple and consistent interface for multiple LLM providers
- 🤖 Support for OpenAI, Mistral, and Google Gemini APIs
- 🚀 Easy to use with minimal configuration
- ⚙️ Customizable parameters for each provider

## Quick Start

### OpenAI

```python
from simple_llm_api import OpenAIAPI

openai = OpenAIAPI("YOUR_API_KEY")
response = openai.simple_request("Hi!")
print(response)
```

### Mistral

```python
from simple_llm_api import MistralAPI

mistral = MistralAPI("YOUR_API_KEY")
response = mistral.simple_request("Hi!")
print(response)
```

### Google Gemini

```python
from simple_llm_api import GeminiAPI

gemini = GeminiAPI("YOUR_API_KEY")
response = gemini.simple_request("Hi!")
print(response)
```

## Easy Advanced Usage

Each API wrapper supports various parameters for customizing the response:

### OpenAI
```python
openai.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=0.7,
    top_p=0.9,
    max_completion_tokens=2048
)
```

### Mistral
```python
mistral.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=0.7,
    top_p=0.9,
    max_tokens=2048
)
```

### Gemini
```python
gemini.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=0.7,
    top_k=40,
    top_p=0.9,
    max_output_tokens=2048
)
```

## Error Handling

The library includes custom exceptions for each API:

- `GeminiError`: GeminiAPI Error
- `MistralError`: MistralError Error
- `OpenAIError`: OpenAIError Error

## Requirements

- requests

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Links

- [GitHub Repository](https://github.com/SoAp9035/simple-llm-api)
- [PyPI Package](https://pypi.org/project/simple-llm-api/)
