import yaml
import re

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def extract_version(file_id):
    # Extract version number from the file ID
    match = re.search(r':(\d+\.\d+\.\d+)', file_id)
    if match:
        return match.group(1)
    return "Unknown version"

def generate_card(component):
    version = extract_version(component.get('id', ''))
    return f"""
<div class="card">
    <h3>{component['name']}</h3>
    <p>Version: {version}</p>
    <p>{component['description']}</p>
    <p><a href="{component['trainingTutorialsUrl']}">Training Tutorials</a></p>
</div>
"""

def generate_cards(yaml_data):
    cards = ""
    for component in yaml_data.get('components', []):
        if component.get('trainingTutorialsAvailable', False):
            cards += generate_card(component)
    return cards

def write_to_index(content, index_file_path):
    with open(index_file_path, 'w') as file:
        file.write(content)

def main():
    yaml_file_path = 'docs/master.yaml'
    index_file_path = 'docs/index.md'

    yaml_data = load_yaml(yaml_file_path)
    cards_content = generate_cards(yaml_data)
    
    full_content = "# ICICLE Training Catalog\n\n" + cards_content
    
    write_to_index(full_content, index_file_path)

if __name__ == "__main__":
    main()
