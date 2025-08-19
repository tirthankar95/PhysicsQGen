from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os 
if __name__ == '__main__':
    import sys 
    import os 
    sys.path.insert(0, os.getcwd())
from UTILS.utils import load_env_vars


def get_llm(m_name):
    if m_name == "local":
        llm = ChatOpenAI(
            base_url = "http://localhost:8080/v1",
            api_key = "X"
        )
    else:
        llm = ChatOpenAI(
            model_name = m_name, 
            api_key = os.environ["OPENAI_API_KEY"]
        ) 
    return llm

def get_response(prompt, m_name):
    llm = get_llm(m_name)
    prompts = [
        HumanMessage(content=f"{prompt}")
    ]
    return llm.invoke(prompts).content

if __name__ == '__main__':
    load_env_vars()
    print(get_response("Who are you?", "gpt-4o-mini"))