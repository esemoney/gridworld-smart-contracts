```python
import os
import git
import markdown

class Agent:
    def __init__(self):
        self.repo = git.Repo(os.getcwd())
        self.readme = "./readme.md"
        self.features = []

    def parse_readme(self):
        with open(self.readme, 'r') as file:
            content = file.read()
            md = markdown.Markdown()
            html = md.convert(content)
            self.features = self.extract_features_from_html(html)

    def extract_features_from_html(self, html):
        # This is a placeholder. In a real application, you would use an HTML parser
        # to extract the features from the HTML content.
        return []

    def implement_features(self):
        for feature in self.features:
            self.implement_feature(feature)

    def implement_feature(self, feature):
        # This is a placeholder. In a real application, you would write code to
        # implement the feature here.
        pass

    def create_branch(self, branch_name):
        self.repo.git.checkout('-b', branch_name)

if __name__ == "__main__":
    agent = Agent()
    agent.parse_readme()
    agent.implement_features()
    agent.create_branch("feature-implementation")
```