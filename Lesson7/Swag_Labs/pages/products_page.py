from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME, 'inventory_item')
        self.add_to_cart_buttons = {
            'backpack': (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'),
            'tshirt': (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'),
            'onesie': (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
        }
        self.cart_link = (By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')

    def add_items_to_cart(self, *item_names):
        for item_name in item_names:
            item_locator = self.add_to_cart_buttons.get(item_name)
            if item_locator:
                self.driver.find_element(*item_locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
