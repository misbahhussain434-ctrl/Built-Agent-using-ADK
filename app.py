from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from my_agent import agent
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
import os

api_key = os.environ.get("AIzaSyBE5S5VDLtXg3gCuFroRvZ1HZ6_0aGpvs4")
print(api_key)  # just to check



MODEL = "gemini-1.5-flash"
root_agent = LlmAgent(model=MODEL,
                      name="IdeaAgent", description ="brainstorms creative and exciting weekend travel ideas based on user preference. ",
                      instruction ="you are creative travel agent. Use tools to brainstorm and respond to user with 3 exciting weekend trip ideas based on user's request.",
                      tools = [google_search],
                      disallow_transfer_to_peers=True)
refiner_agent = LlmAgent (model=MODEL,
                          name = "RefinerAgent",
                          description = "review provided travel ideas and selects only those estimated to cost under the provided budget for weekend trip.",
                          instruction = "use your tools to review the provided trip ideas. Respond ONLY with ideas likely under the provided budget for a weekend.  if none seem to fit, say so.",
                          tools = [google_search],
                          disallow_transfer_to_peers=True)
root_agent = LlmAgent(model=MODEL,
                      name = "PlannerAgent",
                      instruction = f"""you are Trip Planner, coordinating specialist agents,
                      your goal is to provide budget-friendly weekend trip ideas.For each user request, follow the below instructions:
                      1.first,use "{idea_agent}"to brainstrom ideas based on user's request.
                      2.Second, user "{refiner_agent}"to take those ideas to filter them for provided budget.
                      3.Present the final,refined list to user along with budget.""",
                      sub_agents = [idea_agent, refiner_agent],
)
