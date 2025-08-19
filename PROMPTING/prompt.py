import json 
from LLM.llm_OpenAI import get_response as openai_question
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

prompt_mine = """Give me a physics question using the following variable and words. 
You may use the following environment - Solar System(B), and it's property and subject words - kepler-22b, 
separation, force acting between gravitational potential, Solar System(B) planets = 20 at an angle 98 degrees with the horizontal. 
force = 5.76e + 19N, mass of body 2 = 5.23e + 30kg, distance between two bodies = 4.27e + 15m, mass of body 1 = unknown.
"""

prompt_normal = """Give me a physics question on electrostatics?"""

if __name__ == "__main__":
    with open("LLM_CONFIG/config.json", "r") as f:
        config = json.load(f)
    for k, v in config.items():
        if k[-3:] == "KEY" or k[-5:] == "TOKEN":
            os.environ[k] = str(v)
    print(openai_question(prompt_mine, config["LLM_MODEL"]["INNER_MODEL"]))