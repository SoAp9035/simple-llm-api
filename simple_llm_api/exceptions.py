class OpenAIError(Exception):
    def __init__(self, message: str = "OpenAIAPI Error"):
        super().__init__(message)

class AnthropicError(Exception):
    def __init__(self, message: str = "AnthropicAPI Error"):
        super().__init__(message)

class GeminiError(Exception):
    def __init__(self, message: str = "GeminiAPI Error"):
        super().__init__(message)

class MistralError(Exception):
    def __init__(self, message: str = "MistralAPI Error"):
        super().__init__(message)

class DeepSeekError(Exception):
    def __init__(self, message: str = "DeepSeekAPI Error"):
        super().__init__(message)
