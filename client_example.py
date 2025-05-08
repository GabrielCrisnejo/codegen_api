import requests
import os
import uuid

url = "http://localhost:8000/generate"

payload = {
    "prompt": "Create a Python function to sort a list of integers",
    "language": "Python",
    "max_length": 300
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    generated_code = data["generated_code"]
    
    # Mostrar en pantalla
    print("\n✅ Generated Code:\n")
    print(generated_code)

    # Guardar en archivo
    os.makedirs("output", exist_ok=True)
    file_id = uuid.uuid4().hex[:8]
    filename = os.path.join("output", f"generated_from_client_{file_id}.py")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Prompt:\n# {payload['prompt']}\n\n")
        f.write(generated_code)
    
    print(f"\n📁 Code saved to {filename}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
