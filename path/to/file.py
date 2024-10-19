import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Debug: Print environment variables
print("Debug: OPENAI_API_KEY set:", "OPENAI_API_KEY" in os.environ)

# Define the model and parser
model = ChatOpenAI(temperature=0)  # Set temperature to 0 for deterministic output
parser = StrOutputParser()

print("Debug: Model initialized:", model)
print("Debug: Parser initialized:", parser)

# Create a prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

print("Debug: Prompt template created:", prompt_template)

# Create the chain
chain = prompt_template | model | parser

print("Debug: Chain created:", chain)

# Example usage
try:
    result = chain.invoke({"language": "italian", "text": "hi"})
    print("Debug: Chain invocation result:", result)
except Exception as e:
    print("Debug: Error in chain invocation:", str(e))

# For comparison, let's keep the original example
messages = [
    SystemMessage(content="Translate the following from English into French"),
    HumanMessage(content="hi!"),
]

print("Debug: Messages created:", messages)

# Invoke the model and save the result
try:
    result = model.invoke(messages)
    print("Debug: Model invocation result:", result)
except Exception as e:
    print("Debug: Error in model invocation:", str(e))

# Pass the result to the parser
try:
    parsed_result = parser.invoke(result)
    print("Debug: Parsed result:", parsed_result)
except Exception as e:
    print("Debug: Error in parsing:", str(e))

# Chaining the model with the output parser
chain = model | parser

print("Debug: New chain created:", chain)

# Invoke the chain
try:
    chained_result = chain.invoke(messages)
    print("Debug: Chained result:", chained_result)
except Exception as e:
    print("Debug: Error in chain invocation:", str(e))

# Additional debug: Check types
print("Debug: Type of model:", type(model))
print("Debug: Type of parser:", type(parser))
print("Debug: Type of chain:", type(chain))

# Test with different languages
test_languages = ["Spanish", "German", "Japanese"]
test_text = "Hello, world!"

for lang in test_languages:
    try:
        result = chain.invoke({"language": lang, "text": test_text})
        print(f"Debug: Translation to {lang}:", result)
    except Exception as e:
        print(f"Debug: Error translating to {lang}:", str(e))