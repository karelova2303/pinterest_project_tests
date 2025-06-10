import os

from selene import browser, be, have

from pinterest_project import utils
from pinterest_project.data.data import description, web_site


class UserPage:
    def __init__(self):
        self.header_profile = browser.element('[data-test-id="header-profile"]')

        self.button_view_profile = browser.element('[data-test-id="selfProfileHeader-view-profile-button"]')
        self.pins_tab = browser.element('#_pins-profile-tab')
        self.pin = browser.element('[data-test-id="pin"]')

        self.profile_name = browser.element('[data-test-id="profile-name"]')
        self.profile_username = browser.element('[data-test-id="profile-username"]')
        self.following_count = browser.element('[data-test-id="profile-following-count"]')
        self.share_profile_button = browser.element('[data-test-id="share-profile-auth"] > [type = "button"]')
        self.edit_profile_button = browser.element('[data-test-id="edit-button"]')
        self.created_profile_tab = browser.element('#_profile\/_created-profile-tab > a')
        self.saved_profile_tab = browser.element('#_profile\/_saved-profile-tab > a')

        self.boards_tab = browser.element('#_boards-profile-tab')
        self.board = browser.element('[data-test-id="pwt-grid-item"]')

        self.copy_link_icon = browser.element('[data-test-id="copy-link-share-icon-auth"]')
        self.whatsapp_icon = browser.element('[data-test-id="whatsapp-share-icon-auth"]')
        self.messenger_icon = browser.element('[data-test-id="messenger-share-icon-auth"]')
        self.facebook_icon = browser.element('[data-test-id="facebook-share-icon-auth"]')
        self.twitter_icon = browser.element('[data-test-id="twitter-share-icon-auth"]')

        self.edit_form_button = browser.element('[data-test-id="edit-profile-form"] * [type="button"]')
        self.file_input = browser.element('#file-input')
        self.about = browser.element('#about')
        self.website_url = browser.element('#website_url')
        self.done_button = browser.element('[data-test-id="done-button"] > [type="button"]')

        self.avatar_svg = browser.element('[data-test-id="gestalt-avatar-svg"] * [src$=".jpg"]')


    def open_profile_user(self):
        self.header_profile.click()

    def open_public_profile_user(self):
        self.open_profile_user()
        self.button_view_profile.click()

    def open_pins_tab(self):
        self.pins_tab.click()

    def should_be_visible_pins(self):
        self.pin.should(be.visible)

    def open_boards_tab(self):
        self.boards_tab.click()

    def should_be_visible_boards(self):
        self.board.should(be.visible)

    def should_be_visible_profile_name(self, value):
        self.profile_name.should(have.exact_text(value))

    def should_be_visible_profile_username(self, value):
        self.profile_username.should(have.exact_text(value))

    def should_be_visible_following_count(self, value):
        self.following_count.should(have.exact_text(value))

    def should_be_visible_share_profile_button(self):
        self.share_profile_button.should(be.visible)

    def should_be_visible_edit_profile_button(self):
        self.edit_profile_button.should(be.visible)

    def should_be_visible_created_profile_tab(self):
        self.created_profile_tab.should(be.visible)

    def should_be_visible_saved_profile_tab(self):
        self.saved_profile_tab.should(be.visible)

    def click_share_profile_button(self):
        self.share_profile_button.click()

    def should_be_visible_copy_link_icon(self):
        self.copy_link_icon.should(be.clickable)

    def should_be_visible_whatsapp_icon(self):
        self.whatsapp_icon.should(be.clickable)

    def should_be_visible_messenger_icon(self):
        self.messenger_icon.should(be.clickable)

    def should_be_visible_facebook_icon(self):
        self.facebook_icon.should(be.clickable)

    def should_be_visible_twitter_icon(self):
        self.twitter_icon.should(be.clickable)

    def click_edit_profile_button(self):
        self.edit_profile_button.click()

    def upload_foto(self, value):
        self.edit_form_button.click()
        self.file_input.send_keys(utils.file.path_images(value))

    def input_about(self, value):
        self.about.type(value)

    def input_website_url(self, value):
        self.website_url.set_value(value)

    def click_done_button(self):
        self.done_button.click()

    def should_be_saved_data(self):
        self.avatar_svg.should(be.visible)
        self.about.should(have.exact_text(description))
        self.website_url.should(have.value(web_site))