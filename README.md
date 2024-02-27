# Prismic Custom Types Analysis Utility

This utility script analyses JSON configurations of Prismic custom types and generates two CSV files providing you with a structured overview of how slices are used across your custom types and which custom types utilize specific slices.

## Output Files

The script produces two CSV files:

1. **Types CSV (`types.csv`)**: Lists all custom types and the slices in use within each type.
2. **Slices CSV (`slices.csv`)**: Lists all unique slices found across the JSON files, along with the custom types where they are used.

## How to Use

### Preparation

1. **Collect your Custom Types JSON files**: Gather all the JSON files representing your custom types. These should be the original files used in your Prismic legacy configuration (e.g., `blog_article.json`).

2. **Create a Directory**: Create a directory on your local machine to store these JSON files. This directory will be used by the script to locate and process the files.

3. **Place the Script**: Ensure the script is located in the same directory as your JSON files. 

### Running the Script

1. **Open Terminal**: Navigate to the terminal or command prompt on your computer.

2. **Navigate to the Directory**

3. **Run the Script**: Execute the script by running the following command in your terminal:
   ```
   python audit.py
   ```
### After Execution

After running the script, check the directory for the two generated CSV files (`types.csv` and `slices.csv`). These files will provide you with a structured overview of how slices are used across your custom types and which custom types utilize specific slices.
