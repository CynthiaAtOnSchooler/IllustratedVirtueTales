###PART TWO:  GENERATE ILLUSTRATIONS

# Split response into an array of pages
story_page = response.split('\n')

# This function takes a story_page as input and returns a description of an illustration
def generate_illustration_description(story_page):
    # Define the prompt to generate an illustration description
    prompt = f"Generate an illustration that matches the following text: {story_page}"
    # Generate the description of an illustration
    illustration_description = BasicGeneration(prompt)
    # Return the description of an illustration
    return illustration_description

# Filter out blank rows from story_page
story_page_filtered = [row for row in story_page if row.strip()]

# Generate and store the description of an illustration for each story page
illustration_descriptions = []
for page in story_page_filtered:
    illustration_description = generate_illustration_description(page)
    illustration_descriptions.append(illustration_description)

# Display the story_page array in a table
st.table(story_page_filtered)   
st.table(illustration_descriptions)  