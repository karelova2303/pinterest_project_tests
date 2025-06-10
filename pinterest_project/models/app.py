from pinterest_project.models.pages.authorization_page import AuthorizationPage
from pinterest_project.models.pages.profile_user_page import UserPage
from pinterest_project.models.pages.search_page import SearchPage


class ApplicationManager:
    def __init__(self):
        self.authorization = AuthorizationPage()
        self.user_page = UserPage()
        self.search_page = SearchPage()


app = ApplicationManager()
