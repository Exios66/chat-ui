from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

# Debug: Print the parser object to verify its creation
print("Debug: StrOutputParser object created:", parser)

# Debug: Demonstrate basic usage of the parser
sample_output = "This is a sample output string."
parsed_result = parser.parse(sample_output)
print("Debug: Parsed result:", parsed_result)

# Debug: Check the type of the parsed result
print("Debug: Type of parsed result:", type(parsed_result))