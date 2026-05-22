import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    print("Hello from aiagent!")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not defined")

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
        ),
        contents=messages,
    )

    if response.usage_metadata is None:
        raise RuntimeError("Gemini API call failed")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls is None:
        print(response.text)
    else:
        function_results = []
        for function_call in response.function_calls:
            # print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call)

            fcr_parts = function_call_result.parts
            if fcr_parts is None:
                raise Exception("Error: function call result parts list is None")

            function_response = fcr_parts[0].function_response
            if function_response is None:
                raise Exception("Error: no function response found")

            function_results.append(fcr_parts[0])

            if args.verbose:
                print(f"-> {function_response.response}")

if __name__ == "__main__":
    main()
