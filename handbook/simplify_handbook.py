import re
import os
import time
import google.generativeai as genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not set.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'text:\s*`([^`]+)`', re.MULTILINE)
matches = list(pattern.finditer(content))

print(f"Found {len(matches)} topics to upgrade...")

new_content = content
offset = 0

for i, match in enumerate(matches):
    original_text = match.group(1)
    
    # Skip if it's already very short
    if len(original_text) < 400 and "latency tax" not in original_text:
        continue
        
    print(f"Upgrading topic {i+1}/{len(matches)}...")
    
    prompt = f"""
    Read the following highly complex technical engineering text.
    Write a 2-3 paragraph plain, simple English explanation suitable for a beginner to build up the basics before they read the complex part. Use analogies.
    Do NOT include the original text in your output. Just return the simple explanation paragraphs wrapped in standard <p> tags.
    
    Original Text:
    {original_text}
    """
    
    try:
        response = model.generate_content(prompt)
        simplified_text = response.text.strip()
        
        if simplified_text.startswith("```html"):
            simplified_text = simplified_text[7:]
        if simplified_text.endswith("```"):
            simplified_text = simplified_text[:-3]
            
        simplified_text = simplified_text.strip()
        
        # Combine them: Basics first, then Complex
        combined_text = f"""
<div style="background: rgba(0, 229, 255, 0.05); border-left: 4px solid var(--cy); padding: 18px; margin-bottom: 24px; border-radius: 4px;">
    <h4 style="color: var(--cy); margin-top: 0; margin-bottom: 12px; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">🌱 The Basics (Plain English)</h4>
    {simplified_text}
</div>
<div style="opacity: 0.9;">
    <h4 style="color: #fff; margin-bottom: 12px; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">🔬 Deep Engineering Breakdown</h4>
    {original_text}
</div>"""
        
        start = match.start(1) + offset
        end = match.end(1) + offset
        
        new_content = new_content[:start] + combined_text + new_content[end:]
        offset += len(combined_text) - len(original_text)
        
        time.sleep(2)
        
    except Exception as e:
        print(f"Error on topic {i+1}: {e}")
        time.sleep(5)

with open("index_ultimate.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Finished! Saved as index_ultimate.html")
