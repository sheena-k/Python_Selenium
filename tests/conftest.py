from datetime import datetime
import os
import pytest
import pytest_html
from selenium import webdriver

@pytest.fixture
def browser_load():
    driver = webdriver.Chrome()
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
@pytest.fixture(params=["chrome", "firefox"])
def crossBrowser(request):
    """Fixture to create a driver instance for each test."""
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.get("https://groceryapp.uniqassosiates.com/admin/login")
    driver.implicitly_wait(10)
    yield driver  # Yield the driver to the test


REPORT_FOLDER = None
# =========================
#  PYTEST CONFIGURE
# =========================
def pytest_configure(config):
    """
    Create timestamped report folder
    Configure pytest-html dynamically
    """
    global REPORT_FOLDER

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    REPORT_FOLDER = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "reports", timestamp)
    )

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    # Configure HTML report path
    if hasattr(config.option, "htmlpath"):
        config.option.htmlpath = os.path.join(REPORT_FOLDER, "report.html")


# =========================
#  CAPTURE SCREENSHOT ON FAILURE
# =========================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global REPORT_FOLDER

    outcome = yield
    report = outcome.get_result()

    # Only act on test failure during execution
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("browser_load")

        if driver and REPORT_FOLDER:

            safe_name = report.nodeid.replace("::", "_").replace("/", "_")
            screenshot_path = os.path.join(REPORT_FOLDER, f"{safe_name}.png")

            driver.save_screenshot(screenshot_path)

            # ===== Attach to pytest-html =====
            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html and os.path.exists(screenshot_path):
                extra = getattr(report, "extras", [])
                html = f'''
                <div>
                    <img src="{screenshot_path}"
                         style="width:300px;height:200px;"
                         onclick="window.open(this.src)"
                         align="right"/>
                </div>
                '''
                extra.append(pytest_html.extras.html(html))
                report.extras = extra
