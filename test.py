import google.generativeai as genai

genai.configure(api_key="AIzaSyB8jMViypXYmUXyqkax1pbcep0uZKAkVWA")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Summarize AI in 2 sentences")
print(response.text)

