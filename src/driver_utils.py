import undetected_chromedriver as uc


def create_driver(use_subprocess: bool):
    options = uc.ChromeOptions()
    if True:
        options.add_argument("--disable-extensions")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.126 Safari/537.36")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--no-sandbox')
        options.add_argument('--blink-settings=imagesEnabled=false')

    if True:
        prefs = {
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'disable-popup-blocking': True,
            'safebrowsing.enabled': True,
            'block_third_party_cookies': True,

            # Disable downloading images
            'profile.managed_default_content_settings.images': 2,
        }
        options.add_experimental_option('prefs', prefs)


    print("Creating the driver")
    result = uc.Chrome(use_subprocess=use_subprocess, options=options, desired_capabilities=None)
    return result
