import pandas as pd
from pathlib import Path
import argparse

# Define the labels (traits) to be scored
labels = ["Charisma", "Confidence", "Authenticity", "Energy", "Inspiration"]

# Instructions for the annotator
instructions = \
"""
Thank you for participating in our annotation task!
Your job is to analyze NBA player interview transcripts and score them based on the following traits:
1. Charisma: Is the player's speech compelling or inspiring? (Yes/No)
2. Confidence: Does the player sound self-assured and assertive? (Yes/No)
3. Authenticity: Does the player appear honest, genuine, or vulnerable? (Yes/No)
4. Energy: Is the player's tone enthusiastic or dynamic? (Yes/No)
5. Inspiration: Are the player's statements motivational or uplifting? (Yes/No)

For each transcript, you will be asked to answer Yes (1) or No (0) for each of the 5 traits.
The final score for each transcript will be the sum of the Yes responses (maximum score = 5).
"""

data_col = "Quote"
delimiter = "=" * 20

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Annotate NBA player interviews based on traits.')
    parser.add_argument('filename', type=str, help='The CSV file containing the interview data')
    args = parser.parse_args()

    # Construct the file path for the dataset in the "data" folder
    input_file = Path("data") / f"{args.filename}.csv"
    
    if not input_file.is_file():
        print(f"Error: The file {input_file} does not exist.")
        return

    # Read the data file
    my_data = pd.read_csv(input_file)
    my_data = my_data.reset_index()

    # Create the output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get the output filename based on the input file name
    input_filename = Path(args.filename).stem  # Extract the name without extension
    out_filename = output_dir / f"{input_filename}_output.csv"

    # Write headers to the output file
    with open(out_filename, "w") as handle:
        handle.write("Index,Quote," + ",".join(labels) + ",Total Score\n")

    print(instructions)

    # Loop over data and request labels
    for index, row in my_data.iterrows():
        print(delimiter)
        print("Instance " + str(index) + ":")
        print(row[data_col] + "\n")

        # Initialize a dictionary to store scores for this instance
        scores = {}

        # Prompt the annotator for a Yes/No response for each trait
        for trait in labels:
            while True:
                response = input(f"Is the player's {trait} evident? (Yes/No): ").strip().lower()
                if response in ["yes", "no", "y", "n", "1", "0"]:
                    # Convert response to 1 (Yes) or 0 (No)
                    scores[trait] = 1 if response in ["yes", "y", "1"] else 0
                    break
                else:
                    print("Invalid input. Please enter Yes (1) or No (0).")

        # Calculate total score
        total_score = sum(scores.values())

        # Write the quote, scores, and total score to the output file
        with open(out_filename, "a") as handle:
            handle.write(f"{index},{row[data_col]}," + ",".join([str(scores[trait]) for trait in labels]) + f",{total_score}\n")

if __name__ == '__main__':
    main()
