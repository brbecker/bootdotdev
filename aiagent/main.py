import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from config import MAX_LLM_STEPS
from prompts import system_prompt


def main():
    print("Hello from aiagent!")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--debug", action="store_true", help="Enable debugging output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY not defined")

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]

    client = genai.Client(api_key=api_key)

    for _ in range(MAX_LLM_STEPS):
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
        if args.debug:
            print(f"Messages: {messages}")

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
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.candidates:
            for candidate in response.candidates:
                content = candidate.content
                if content:
                    messages.append(content)
                    if args.debug:
                        print(f"- Adding response candidate to messages: {content}")

        if response.function_calls is None:
            print("Final response:")
            print(response.text)
            return
        else:
            function_responses = []
            for function_call in response.function_calls:
                # print(f"- Calling function: {function_call.name}({function_call.args})")
                function_call_result = call_function(function_call, args.verbose)

                fcr_parts = function_call_result.parts
                if fcr_parts is None:
                    raise Exception("Error: function call result parts list is None")

                function_response = fcr_parts[0].function_response
                if function_response is None:
                    raise Exception("Error: no function response found")
                if args.verbose:
                    print(f"-> {function_response.response}")

                function_responses.append(fcr_parts[0])

            messages.append(types.Content(role="user", parts=function_responses))
            if args.debug:
                print(f"- Added function responses to messages: {messages[-1]}")

    # If we reached a final solution, we would have returned from the loop. Print error
    # message and exit with error code 1.
    print(f"Error: Exceeded maximum of {MAX_LLM_STEPS} calls to the LLM.")
    sys.exit(1)

if __name__ == "__main__":
    main()
