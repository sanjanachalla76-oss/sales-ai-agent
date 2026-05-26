from tools import qualify_lead, recommend_product, draft_email


class SalesAgent:
    def __init__(self):
        self.tools = {
            "qualify": qualify_lead,
            "recommend": recommend_product,
            "email": draft_email
        }

    def think(self, lead_info):
        return ["qualify", "recommend", "email"]

    def act(self, actions, lead_info):
        results = {}

        for action in actions:
            tool = self.tools[action]
            results[action] = tool(lead_info)

        return results

    def run(self, lead_info):
        print("Thinking...")
        actions = self.think(lead_info)

        print("Acting...")
        results = self.act(actions, lead_info)

        print("\nResults:")
        for k, v in results.items():
            print(f"\n{k.upper()}:\n{v}")

        return results