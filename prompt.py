import openai
import json

def parse_resume_to_json(resume_text):
  """Parses a resume into JSON format using GPT-3.5-turbo.

  Args:
    resume_text: The text content of the resume.

  Returns:
    A dictionary representing the parsed resume data, or None if an error occurs.
  """

  openai.api_key = "YOUR_API_KEY"  # Replace with your API key

  prompt = f"""
  Parse the following resume into a structured JSON format. Include sections for personal information, education, work experience, skills, and any other relevant categories. For each work experience entry, include job title, company, dates, and key responsibilities or achievements. Ensure the JSON is properly formatted and easily readable.

  Resume:
  {resume_text}
  """

  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a skilled resume parser."},
        {"role": "user", "content": prompt}
      ]
    )

    json_string = response.choices[0].message.content
    parsed_json = json.loads(json_string)
    return parsed_json
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

# Example usage
resume_text = """
# ... Your resume text here ...
"""

parsed_resume = parse_resume_to_json(resume_text)

if parsed_resume:
  print(json.dumps(parsed_resume, indent=2))
