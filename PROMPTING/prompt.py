import json 
from LLM.llm_OpenAI import get_question as openai_question
import os 

'''
I will save each of the prompting experiments here in this file.
'''
db = [
    {
        "prompt": "X",
        "response": "X"
    }
]

prompt_mine = """Give me a physics question using the following variables and words.

 You may use the following environment - train, and it's properties and topic words - ball, train acceleration = 79.57 ms^-2 at an angle 152 degrees with the horizontal, train velocity = 57.91 m/s at an angle 8 degrees with the horizontal, train length = 544.05 m, train height = 68.69 m. ['ms^-2', 'm/s', 'm'
"""

prompt_normal = """Give me a physics question on electrostatics?"""

if __name__ == "__main__":
    with open("LLM_CONFIG/config.json", "r") as f:
        config = json.load(f)
    for k, v in config.items():
        if k[-3:] == "KEY" or k[-5:] == "TOKEN":
            os.environ[k] = str(v)
    print(openai_question(prompt_mine, config["LLM_MODEL"]["INNER_MODEL"]))