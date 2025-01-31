#include <X11/Xlib.h>
#include <X11/extensions/XTest.h>
#include <opencv2/opencv.hpp>
#include <unistd.h>
#include <stdio.h>

// Define the regions where to search
struct Region {
    int x, y, width, height;
};

// Example regions (change as per your screen)
Region regions[] = {
    {343, 382, 682, 57},  // Region 1
    {343, 607, 665, 36},  // Region 2
    {343, 814, 665, 60}   // Region 3
};

// Color ranges for green and yellow (in HSV)
cv::Scalar lower_green(44, 150, 200);
cv::Scalar upper_green(47, 255, 255);

cv::Scalar lower_yellow(44, 150, 200);
cv::Scalar upper_yellow(47, 255, 255);

Display *dpy;
Window root;

// Function to capture the screen in a specified region
cv::Mat captureScreen(int x, int y, int width, int height) {
    XImage *image = XGetImage(dpy, root, x, y, width, height, AllPlanes, ZPixmap);
    cv::Mat screen(height, width, CV_8UC4, image->data); // Assuming 32-bit (ARGB)
    return screen.clone();
}

// Function to click at a specified point (x, y)
void clickAt(int x, int y) {
    XTestFakeMotionEvent(dpy, -1, x, y, CurrentTime);
    XTestFakeButtonEvent(dpy, 1, True, CurrentTime);  // Press left mouse button
    usleep(100000);                                   // 100ms delay
    XTestFakeButtonEvent(dpy, 1, False, CurrentTime); // Release left mouse button
}

// Function to search for a color in a region and click the first match
bool searchAndClickColor(const cv::Mat &screen, const cv::Scalar &lower_bound, const cv::Scalar &upper_bound, Region region) {
    cv::Mat hsv;
    cv::cvtColor(screen, hsv, cv::COLOR_BGR2HSV);
    cv::Mat mask;
    cv::inRange(hsv, lower_bound, upper_bound, mask);
    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    if (!contours.empty()) {
        // Click at the first contour's center
        cv::Rect bounding_box = cv::boundingRect(contours[0]);
        int click_x = region.x + bounding_box.x + bounding_box.width / 2;
        int click_y = region.y + bounding_box.y + bounding_box.height / 2;
        clickAt(click_x, click_y);
        printf("Clicked at (%d, %d)\n", click_x, click_y);
        return true;
    }
    return false;
}

int main() {
    dpy = XOpenDisplay(NULL);
    root = DefaultRootWindow(dpy);

    while (true) {
        // Iterate over the defined regions
        for (auto &region : regions) {
            cv::Mat screen = captureScreen(region.x, region.y, region.width, region.height);

            // Search for green color
            if (searchAndClickColor(screen, lower_green, upper_green, region)) {
                usleep(100000); // Delay before next action
                continue;
            }

            // Search for yellow color if green is not found
            searchAndClickColor(screen, lower_yellow, upper_yellow, region);
            usleep(100000); // Delay before next action
        }

        // Simple escape mechanism (press 'q' to quit)
        char key;
        read(0, &key, 1);  // Read keyboard input (Linux-specific; replace for other OS)
        if (key == 'q') break;

        usleep(100000);  // Delay to reduce CPU usage
    }

    XCloseDisplay(dpy);
    return 0;
}
