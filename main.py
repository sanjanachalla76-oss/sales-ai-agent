from agent import SalesAgent

if __name__ == "__main__":
    lead_info = {
        "name": "Sanjana",
        "budget": 800,
        "interest_level": "high",
        "timeline": "immediate"
    }

    agent = SalesAgent()
    agent.run(lead_info)