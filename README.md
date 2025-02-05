### NBA Interview Annotation Dataset

## Overview
This dataset consists of NBA player interview transcripts (pre-game and post-game) collected for annotation purposes. The primary goal is to analyze these transcripts and evaluate the player's speech based on five traits: Charisma, Confidence, Authenticity, Energy, and Inspiration. Each transcript is assigned a binary score (Yes = 1, No = 0) for each trait, leading to a final Aura Score ranging from 0 to 5.

## Data Source and Collection Method
- **Source:** Official NBA press conferences, player interviews from reputable sports media outlets.

- **Collection Process:** The transcripts were manually extracted from publicly available interview videos and articles.

- **Sampling Method:** The dataset includes a mix of high-profile players, role players, and rookies to ensure a diverse range of speech patterns.

- **Collection Date:** Data was gathered between January 2025 - February 2025.

- **Ethical Considerations:** This dataset only includes publicly available statements and does not violate any media terms of service.

## Dataset Format

The dataset is split into eight CSV files (dataset1.csv to dataset8.csv) with each row representing an individual interview transcript.

The key columns in each file:

- **Index:** Unique identifier for the transcript.

- **Quote:** The text of the player's statement.

- **Charisma:** (1 = Yes, 0 = No)

- **Confidence:** (1 = Yes, 0 = No)

- **Authenticity**: (1 = Yes, 0 = No)

- **Energy:** (1 = Yes, 0 = No)

- **Inspiration:** (1 = Yes, 0 = No)

- **Total Score:** Sum of the five traits, ranging from 0 to 5.

## Annotation Process

- Each transcript is labeled by multiple annotators to ensure reliability.

- To measure annotation agreement, 15% of the transcripts are duplicated across different files.

- Annotators are provided with detailed labeling instructions to standardize scoring.

## Estimated Annotation Time

From experimentation, it took each member an average of 5 minutes and 3 seconds to label 10 points; therefore, pilot testing suggests that annotating one transcript takes ~30 seconds.

Each annotator is expected to label an average of 102 unique quotes + 20 duplicate quotes per dataset, which results in a total of 122 transcripts taking 1 hour and 1 minute per dataset. 

## Sensitive Content Disclaimer

This dataset contains real NBA player statements, which may include emotionally charged or controversial remarks.

If you encounter any sensitive or inappropriate content, please notify the dataset curators.

## Contact Information

- JC Abanto, abantoj

- Derek Li, li920

- Temituoyo Ugborogho, ugborogt

- Stanley Chen, chens313

You can reach out to any of these members via Microsoft Teams.

### Setup

1. Download the zip file, click "extract here", and open it up in VSCode
2. Open up the terminal, use Bash

### Run the program

python annotator.py dataset1

python annotator.py dataset2

python annotator.py dataset3

etc...

Note: Each dataset contains two fields. The first column, `Quote`, contains the interviewee quote and the second column, `Aura Points`, is an empty column that will be filled upon annotation.

### Results

The output results are written into the output folder
