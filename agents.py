from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

## Create senior Bog content Resarcher
blog_researcher = Agent(
    role = 'Blog Reseracher from youtube videos',
    goal = 'Get the relevant video content for the topic {topic} from yt channel',
    name = 'test_name',
    verbose = True, #show information on terminal
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    tools = [yt_tool],
    allow_dlegation = True  # Transferring work to someone else
)

##Creating a Blog Writer Agent with Yt Tool
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)

