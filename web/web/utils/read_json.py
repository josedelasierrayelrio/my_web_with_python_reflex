import json


class ReadJson:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_json()

    def _load_json(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: El archivo {self.file_path} no fue encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.file_path} no es un JSON válido.")
            return None

    def get_about_me(self):
        return self.data.get("about_me", {})

    def get_social_links(self):
        return self.data.get("social_links", {})

    def get_personal_links(self):
        return self.data.get("personal_links", {})

    def get_support_links(self):
        return self.data.get("support_links", {})

    def get_contact_links(self):
        return self.data.get("contact_links", {})

    def get_skills(self):
        return self.data.get("skills", [])

    def get_contact(self):
        return self.data.get("contact", {})

    def get_full_name(self):
        return self.data.get("about_me", {}).get("name", "")

    def get_profession(self):
        return self.data.get("about_me", {}).get("profession", "")

    def get_alt_profession(self):
        return self.data.get("about_me", {}).get("alt_profession", "")

    def get_bio(self):
        return self.data.get("about_me", {}).get("bio", "")

    def get_specific_link(self, category, platform):
        return self.data.get(category, {}).get(platform, "")

    def to_dict(self):
        return self.data
