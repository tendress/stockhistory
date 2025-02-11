from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeDriverManager

# Set up the WebDriver (Edge in this case)
driver = webdriver.Edge(service=Service(EdgeDriverManager().install()))

# Use the web page I have open in the example

driver.get("https://www.orioneclipse.com/#/eclipse/strategy/model/list")

# Find the search box using its name attribute value
search_box = driver.find_element(By.NAME, "q")

# Type a search query into the search box
search_box.send_keys("Python programming")

# Press Enter to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for the results to load and display the title
driver.implicitly_wait(5)  # seconds

# Click on the first search result
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# Close the browser
driver.quit()