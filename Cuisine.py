class CuisineSuggestionEngine:
    def _init_(self):
        self.cuisine_map = {
            "spicy": ["Indian: Chicken Curry, Spicy Biryani", "Mexican: Tacos, Enchiladas"],
            "comfort food": ["American: Mac and Cheese, Meatloaf", "Italian: Lasagna, Risotto"],
            "seafood": ["Japanese: Sushi, Sashimi", "Spanish: Seafood Paella, Grilled Octopus"],
            "vegetarian": ["Indian: Paneer Tikka, Dal", "Mediterranean: Falafel, Hummus"],
            "sweet": ["French: Crème Brûlée, Macarons", "Turkish: Baklava, Turkish Delight"],
            "savory": ["Chinese: Dumplings, Peking Duck", "Greek: Moussaka, Souvlaki"]
        }
        self.user_inputs = []

    def display_potential_inputs(self):
        print("Potential inputs you can use:", ", ".join(self.cuisine_map.keys()))

    def get_user_inputs(self):
        self.display_potential_inputs()
        while len(self.user_inputs) < 3:
            input_text = input(f"\nInput {len(self.user_inputs)+1} - Enter a cuisine type or flavor: ").lower()
            if any(key in input_text for key in self.cuisine_map.keys()):
                for key in self.cuisine_map:
                    if key in input_text and key not in self.user_inputs:
                        self.user_inputs.append(key)
                        break
            else:
                print("Invalid input, please try again.")

    def generate_final_suggestion(self):
        suggestions = [item for key in self.user_inputs for item in self.cuisine_map[key]]
        print("\nCuisine Suggestions based on your inputs:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
        final_choice = input("\nSelect a cuisine from the list by typing its name (e.g., 'Indian'): ").capitalize()
        selected_suggestion = next((s for s in suggestions if final_choice in s), None)
        if selected_suggestion:
            print(f"\nGreat choice! {selected_suggestion.split(': ')[1]} are popular dishes in {final_choice} cuisine. Enjoy!")

if _name_ == "_main_":
    engine = CuisineSuggestionEngine()
    engine.get_user_inputs()
    engine.generate_final_suggestion()
