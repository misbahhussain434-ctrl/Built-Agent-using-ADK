from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# This must be exactly named 'root_agent'
root_agent = LlmAgent(
    name = "my_root_agent",
    model="gemini-1.5-flash", 
    tools=[google_search],
)
import os
# Load .
a
# Minimal root_agent
root_agent = LlmAgent(
    name="my_root_agent",          # Required
    model="gemini-1.5-flash",      # Model
    tools=[google_search],         # Optional tools
    api_key=api_key                # Pass API key
)
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

