# Python Script to Automate the Google Dinosaur Game

This is a simple Python script that uses the `pyautogui` library to automate the Google Dinosaur Game, also known as the "T-Rex Game," which is a browser-based game that appears when a user's internet connection is lost. The script plays the game by repeatedly pressing the spacebar to make the dinosaur jump over obstacles.

## Requirements

To use this script, you will need to have the following software installed on your computer:

- Python 3.6 or later
- The `pyautogui` library
- The `Pillow` library (for image processing)

You can install these dependencies using `pip`:

```bash
pip install pyautogui pillow
```

## How to Use

1. Start the Google Dinosaur Game in your web browser.
2. Open a terminal window and navigate to the directory where the script is located.
3. Run the script using the following command:

```bash
python dinosaur.py
```


The script will start running after a delay of 3 seconds, allowing you time to set up the game. It will then press the spacebar once to start the game or jump over the first obstacle, and it will enter the main loop of gameplay.

The script controls the gameplay by repeatedly taking a screenshot of the region of the screen around the dinosaur, checking the pixels in the image to see if any of them are the color (83, 83, 83), and pressing the spacebar if it finds a pixel that is this color. This color appears to be the color of the obstacles in the game, so the script is essentially pressing the spacebar whenever it sees an obstacle in the screenshot.

The width of the region of the screen that is included in the screenshot is controlled by the `num` argument of the `play()` function. This value is incremented by 0.7 each time the script presses the spacebar and calls the `play()` function again, causing the region of the screen that is included in the screenshot to gradually increase in size over time. This allows the script to react to obstacles that are further away from the dinosaur.

The script will continue running until you interrupt it by pressing `CTRL + C` or closing the terminal window.

## Notes

- The script may not work perfectly on all systems, as it is dependent on the specific layout and color scheme of the Google Dinosaur Game.
- The script may not perform well at high speeds or with complex obstacle patterns.
- Use of this script may be considered cheating and may be against the terms of service for the Google Dinosaur Game. Use at your own risk.
