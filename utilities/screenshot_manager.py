import os
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ScreenshotManager:
    SCREENSHOT_DIR = "screenshots"
    @staticmethod
    def capture_screenshot(driver, name):
        try:
            if not os.path.exists(ScreenshotManager.SCREENSHOT_DIR):
                os.makedirs(ScreenshotManager.SCREENSHOT_DIR)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{ScreenshotManager.SCREENSHOT_DIR}/{name}_{timestamp}.png"
            driver.save_screenshot(file_name)
            logger.info(f"Screenshot saved: {file_name}")
            return file_name
        except Exception as e:
            logger.error(f"Failed to capture screenshot: {str(e)}")
            return None

    @staticmethod
    def capture_screenshot_on_failure(driver, test_name):
        safe_name = test_name.replace("::", "_").replace("/", "_")
        return ScreenshotManager.capture_screenshot(driver, f"FAILED_{safe_name}")