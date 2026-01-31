from playwright.sync_api import sync_playwright

# ==============================================================================
# Your configuration area
# ==============================================================================
# Make sure to keep the quotes '' on both sides!
MY_USERNAME = 'USERNAME' # paste your Bright Data username here
MY_PASSWORD = 'PASSWORD' # paste your Bright Data password here
MY_HOST = 'HOST_URL' # paste your Bright Data host URL here
# ==============================================================================

def run_test():
    print("--- Starting: Connecting to Bright Data... ---")
    
    # Building the full connection URL
    sbr_connection_string = f'wss://{MY_USERNAME}:{MY_PASSWORD}@{MY_HOST}'
    
    with sync_playwright() as p:
        print("Trying to open remote browser...")
        # Connect to Bright Data browser
        browser = p.chromium.connect_over_cdp(sbr_connection_string)
        
        try:
            page = browser.new_page()
            
            # --- Budget protection: blocking images and media ---
            # This command says: if it's an image or font - don't load it!
            page.route("**/*", lambda route: route.abort() 
                       if route.request.resource_type in ["image", "media", "font"] 
                       else route.continue_())
            
            # --- The test: accessing an Airbnb article ---
            url = "PROPERTY_URL" # paste your property URL here
            print(f"Navigating to: {url}")
            
            # Give it up to 2 minutes to load (sometimes it takes time to bypass blocks)
            page.goto(url, timeout=120000)
            
            # Check if we managed to read the title
            if page.locator('h1').count() > 0:
                title = page.inner_text('h1')
                print("\n" + "="*30)
                print("Success! We managed to access Airbnb through Bright Data")
                print(f"Article title found: {title}")
                print("="*30 + "\n")
            else:
                print("We entered the page, but couldn't find a title (maybe the page changed)")

        except Exception as e:
            print(f"Oops, an error occurred: {e}")
            
        finally:
            browser.close()
            print("--- Done, browser closed ---")

if __name__ == '__main__':
    run_test()
