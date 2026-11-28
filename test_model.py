from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)

# Ollama serves models locally using an OpenAI-compatible API at http://localhost:11434.

# LiteLLMModel is built to communicate with any model that supports the OpenAI chat/completion API format.

# This means you can simply swap out InferenceClientModel for LiteLLMModel no other code changes required. It’s a seamless, plug-and-play solution.

# Call the model directly and print its reply.
messages = [
    {"role": "user", "content": [{"type": "text", "text": "Explain in two sentences what an AI agent is."}]}
]
response = model(messages)
print(response.content)

# Let an agent compute something: the model writes Python, smolagents runs it.
agent = CodeAgent(tools=[], model=model, verbosity_level=0)
result = agent.run("Compute the sum of the squares of the integers from 1 to 10.")
print("\n=== Agent computed output ===")
print(result)
