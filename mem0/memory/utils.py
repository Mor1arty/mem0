import json

from ..configs.prompts import FACT_RETRIEVAL_PROMPT


def get_fact_retrieval_messages(message):
    return FACT_RETRIEVAL_PROMPT, f"Input: {message}"


def parse_messages(messages):
    response = ""
    for msg in messages:
        if msg["role"] == "system":
            response += f"system: {msg['content']}\n"
        if msg["role"] == "user":
            response += f"user: {msg['content']}\n"
        if msg["role"] == "assistant":
            response += f"assistant: {msg['content']}\n"
    return response

def format_entities(entities):
    if not entities:
        return ""
        
    formatted_lines = []
    for entity in entities:
        simplified = f"{entity['source'] if 'source' in entity else entity['source_entity']} -- {entity['relation'].upper()} -- {entity['destination'] if 'destination' in entity else entity['destination_entity']}"
        formatted_lines.append(simplified)

    return "\n".join(formatted_lines)