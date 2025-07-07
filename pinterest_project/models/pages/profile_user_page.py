from allure_commons._allure import step
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
        with step('Открыть профиль пользователя'):
            self.header_profile.click()

    def open_public_profile_user(self):
        with step('Открыть публичный профиль'):
            self.open_profile_user()
            self.button_view_profile.click()

    def open_pins_tab(self):
        with step('Кликнуть таб "Пины"'):
            self.pins_tab.click()

    def pins_should_be_visible(self):
        with step('Отображается вкладка с сохраненными пинами'):
            self.pin.should(be.visible)

    def open_boards_tab(self):
        with step('Кликнуть таб "Доски"'):
            self.boards_tab.click()

    def boards_should_be_visible(self):
        with step('Отображается вкладка с сохраненными досками'):
            self.board.should(be.visible)

    def profile_name_should_be_visible(self, profile_name):
        with step(f'Имя профиля "{profile_name}"'):
            self.profile_name.should(have.exact_text(profile_name))

    def profile_username_should_be_visible(self, profile_username):
        with step(f'Имя пользователя "{profile_username}"'):
            self.profile_username.should(have.exact_text(profile_username))

    def following_count_should_be_visible(self, follower_count):
        with step(f'Количество подписок "{follower_count}"'):
            self.following_count.should(have.exact_text(follower_count))


    def click_share_profile_button(self):
        with step('Кликнуть кнопку "Поделиться"'):
            self.share_profile_button.click()

    def copy_link_icon_should_be_clickable(self):
        with step('Иконка "Копировать ссылку" кликабельна'):
            self.copy_link_icon.should(be.clickable)

    def whatsapp_icon_should_be_clickable(self):
        with step('Иконка "WhatsApp" кликабельна'):
            self.whatsapp_icon.should(be.clickable)

    def messenger_icon_should_be_clickable(self):
        with step('Иконка "Messenger" кликабельна'):
            self.messenger_icon.should(be.clickable)

    def facebook_icon_should_be_clickable(self):
        with step('Иконка "Facebook" кликабельна'):
            self.facebook_icon.should(be.clickable)

    def twitter_icon_should_be_clickable(self):
        with step('Иконка "X" кликабельна'):
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

    def edit_form_profile(self, foto, description, web_site):
        with step('Кликнуть кнопку "Изменить профиль"'):
            self.click_edit_profile_button()
        with step('Загрузить фото профиля'):
            self.upload_foto(foto)
        with step('Добавить текст в поле "Описание"'):
                self.input_about(description)
        with step('Добавить ссылку в поле "Веб-сайт"'):
            self.input_website_url(web_site)
        with step('Кликнуть кнопку "Сохранить"'):
            self.click_done_button()

    def data_should_be_saved(self):
        with step('Внесенные изменения отображаются'):
            self.avatar_svg.should(be.visible)
            self.about.should(have.exact_text(description))
            self.website_url.should(have.value(web_site))