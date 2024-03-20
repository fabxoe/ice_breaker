from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from agent.linkedin_lookup_agent import lookup as linkedin_lookup_agent
import os

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")

    print(os.environ["OPENAI_API_KEY"])

    summary_template = """
    given the Linkedin {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    print(chain.run(information=linkedin_data))
