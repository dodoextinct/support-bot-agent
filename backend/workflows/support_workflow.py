from typing import Iterator
from agno.workflow import Workflow, RunResponse

from user_agents.support_agent import get_support_agent


class SupportWorkflow(Workflow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def load_support_agent(self):
        return get_support_agent(session_id=self.session_id)

    def run_workflow(self, prompt: str) -> Iterator[RunResponse]:
        try:

            agent = self.load_support_agent()
            result = agent.run(prompt)

            message = result.content.strip()
            if not message or "I don't know" in message:
                message = "I don't know."

            yield RunResponse(
                content={
                    "message": message,
                }
            )

        except Exception as e:
            print(f"[ERROR] SupportWorkflow: {e}")
            yield RunResponse(
                content={
                    "message": f"An error occurred: {str(e)}",
                }
            )
