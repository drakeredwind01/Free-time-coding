    checkbox = page.query_selector("#checkbox")
    checkbox.click()
    button = page.query_selector("#free_play_form_button")
    button.click()

'''
except KeyboardInterrupt:
    # Handle Ctrl+C to close the browser gracefully
    browser.close()
'''
    page.click('button[type=submit]')  # type="submit"
