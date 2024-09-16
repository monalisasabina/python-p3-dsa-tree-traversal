class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]

    while nodes_to_visit:
      current = nodes_to_visit.pop()
      if current['id'] == id:
        return current

      nodes_to_visit = nodes_to_visit + current['children']
    return None


root = {
    'tag_name': 'div',
    'id': 'root',
    'text_content': '',
    'children': [
        {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Welcome',
            'children': []
        },
        {
            'tag_name': 'p',
            'id': 'intro',
            'text_content': 'This is an intro paragraph.',
            'children': []
        },
        {
            'tag_name': 'div',
            'id': 'container',
            'text_content': '',
            'children': [
                {
                    'tag_name': 'button',
                    'id': 'submit-btn',
                    'text_content': 'Submit',
                    'children': []
                }
            ]
        }
    ]
}

# Create an instance of the Tree class with the root node
tree = Tree(root)

# Call the get_element_by_id method
result = tree.get_element_by_id('submit-btn')

# Output the result
if result:
    print(f"Found element: {result['tag_name']} with ID: {result['id']}")
else:
    print("Element not found")



# Call the get_element_by_id method
result = tree.get_element_by_id('add-btn')

# Output the result
if result:
    print(f"Found element: {result['tag_name']} with ID: {result['id']}")
else:
    print("Element not found")