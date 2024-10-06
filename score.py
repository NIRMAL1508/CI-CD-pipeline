from rapidfuzz import fuzz
import Levenshtein
import json

def compare_names_combined(json_input):
    # Parse the JSON input
    data = json.loads(json_input)
    
    name1 = data.get('name1', "")
    name2 = data.get('name2', "")
    
    # RapidFuzz similarity score (0 to 100)
    fuzzy_score = fuzz.ratio(name1, name2)
    
    # Levenshtein similarity (1 - normalized distance)
    lev_distance = Levenshtein.distance(name1, name2)
    max_len = max(len(name1), len(name2))
    lev_similarity = 1 - (lev_distance / max_len) if max_len > 0 else 1
    

    combined_score = (fuzzy_score / 100 + lev_similarity) / 2
    
    return {
        "fuzzy_score": fuzzy_score,
        "levenshtein_similarity": lev_similarity,
        "combined_score": combined_score
    }



user_input = input("Please enter the names in JSON format (e.g., {\"name1\": \"John Doe\", \"name2\": \"Jonny Do\"}): ")

try:
    result = compare_names_combined(user_input)
    print("Comparison result:", result)
except json.JSONDecodeError:
    print("Invalid JSON format. Please provide the input in correct JSON format.")
