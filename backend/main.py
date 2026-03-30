import os
import asyncio
import random
from agents import Agent, ItemHelpers, Runner, function_tool, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from dotenv import load_dotenv

load_dotenv()

set_tracing_disabled(disabled = True)

input_text = input("Enter the text: ")

MODEL = 'gemini/gemini-2.5-flash'
gemini_api_key = os.environ.get('GEMINI_API_KEY')

@function_tool
def how_many_jokes() -> int:
    return random.randint(1, 10)


async def main(model:str , api_key:str):
    agent = Agent(
        name="Joker",
        instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
        tools=[how_many_jokes],
        model=LitellmModel(model=model, api_key =api_key),
    )

    result = await Runner.run(
        agent,
        input="Hello",
    )
    print("=== Run starting ===")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main(model=MODEL, api_key=gemini_api_key))