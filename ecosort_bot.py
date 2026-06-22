# ==============================================================================
# PROJECT: EcoSort AI - Household Waste Segregation Assistant
# TARGET: United Nations SDG 12 (Responsible Consumption and Production)
# ==============================================================================

import sys

# Simulation of the Botpress Vector Knowledge Base
WASTE_KNOWLEDGE_BASE = {
    "recyclables": ["plastic bottle", "aluminum can", "cardboard", "paper", "glass jar", "soda can"],
    "compost": ["food scraps", "fruit peel", "vegetable", "coffee grounds", "eggshell", "greasy pizza box", "wet pizza box"],
    "trash": ["styrofoam", "bubble wrap", "plastic wrapper", "chip bag", "ceramics", "diaper"],
    "hazardous": ["battery", "phone", "electronics", "lightbulb", "chemicals", "smartphone"]
}

def eco_sort_agent(user_input):
    """Processes user queries mimicking the Botpress Autonomous Knowledge Base node."""
    query = user_input.lower().strip()
    
    # 1. Simple matching logic simulating the vector search
    if any(item in query for item in WASTE_KNOWLEDGE_BASE["recyclables"]):
        return ("🔵 Blue Bin (Recyclables):\n"
                "-> Place this item here. Ensure it is completely rinsed and free of food residue!")
                
    elif any(item in query for item in WASTE_KNOWLEDGE_BASE["compost"]):
        return ("🟢 Green Bin (Compost/Organics):\n"
                "-> This belongs in the compost. Organic matter and soiled paper items are perfect for composting.")
                
    elif any(item in query for item in WASTE_KNOWLEDGE_BASE["trash"]):
        return ("⚫ Black/Grey Bin (Landfill/General Trash):\n"
                "-> This item cannot be recycled or composted efficiently. Please place it in general waste.")
                
    elif any(item in query for item in WASTE_KNOWLEDGE_BASE["hazardous"]):
        return ("🔴 Hazardous & E-Waste Depot:\n"
                "-> WARNING: Do NOT toss this in standard household bins. Please take it to your local electronics recycling drop-off point.")
                
    # 2. Default fallback response if item isn't in our localized dataset
    else:
        return ("🤔 I'm not entirely sure about that specific item.\n"
                "-> Fallback Action: Please consult your municipal waste website to prevent bin contamination!")

def main():
    # Mimicking the exact EcoSort custom greeting message you built in Botpress
    print("="*65)
    print("Hi! I'm EcoSort 🌲. I can help you figure out exactly how to dispose \n"
          "of your household waste to protect our planet.")
    print("="*65)
    print("What item are you trying to throw away right now? (Type 'exit' to stop)")
    
    while True:
        user_query = input("\nYou: ")
        if user_query.lower() == 'exit':
            print("\nThanks for keeping the planet clean! 🌍 Goodbye.")
            break
        
        # Simulating the looping Autonomous Node execution
        response = eco_sort_agent(user_query)
        print(f"\nEcoSort Assistant:\n{response}")
        print("-" * 40)

if __name__ == "__main__":
    main()
