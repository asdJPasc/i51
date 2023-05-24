# I51 script

Powerful screenshot script designed by i51 packed with features to make screen capturing of websites effortless. 

With the script, you can capture the full height of any website, including the date, time, and row id at the top of each screenshot. 

The script also enables automatic folder creation for every screenshot and supports both automatic file naming and customization options, ensuring that your files are organized and personalized to your preferences. 

Moreover, you can easily set intervals for screen captures, streamlining your workflow and maximizing your efficiency. The script also includes an automatic cookie acceptance feature, ensuring that your screenshots remain uncluttered with extraneous elements. Additionally, the script generates a text file for logs to track screen captures.

Furthermore, to avoid the blocking of any critical elements in the captured screenshot, the script has also been enhanced with an automatic pressing of the allow cookies button, ensuring that your screenshots are accurate and comprehensive.


*NOTE: Please be aware that using the script is at your own risk and the creator of the script is not liable for any damages that may result from using it.

[ Instruction ]

1. First, create a new folder on your computer where you want to store the script and its captured screenshots.

2. Next, Send a private message to i51 to download the script. Save the script file to the folder you just created.

3. Once the script is downloaded, navigate to the folder and right-click on the script file. Select "Open With" and choose a text editor like Notepad, Sublime Text, or Visual Studio Code.

4. Inside the script file, locate the code for url and replace for the specific allocation(s) assigned to you to capture for screenshot.

5. After updating the script, save the changes by clicking "File" and "Save" or "CTRL + S" in your text editor.

6. Now, open your command prompt by pressing the Windows key and typing "cmd" into the search bar. Once the command prompt window opens, navigate to the folder where you saved the script file using the "cd" command followed by the folder path. (eg. C:\Users\i51\Desktop\i51 scripts folder)

7. Once you're in the correct folder in the command prompt, type "pip install playwright" and hit Enter to install the necessary library.

8. Once the installation is complete, you can execute the script by double-clicking on the script file. The script will automatically begin taking screenshots at regular intervals, based on the settings you defined in the script. The captured screenshots will be saved in a new folder within the folder you created earlier.

[ Changelog ]

Version 1.1 - 04-20-2023

New features:

1. Added an automatic presser for the accept cookies button.

2. Enhanced the print display to provide more informative progress information during screenshot capture.

3. Included a timeout print display to indicate when a URL fails to capture a screenshot
Added a log.txt file to track issues that arise while the script is running.

4. Implemented a keyboard shortcut "ctrl + c" to stop the script and save the log.txt file properly.

Version 1.2 - 05-24-2023

1. Removed the accept_button function and implemented a headless browser set to False, allowing manual acceptance of cookies initially. The accepted cookies are then saved to the "Do not delete" folder as cache, instead of using hard-coded functions.

2. Added a custom step function to handle websites that require filtering before capturing screenshots.


[ Bug fixes ]

1. Addressed a timeout issue that was causing the script to stop

2. Improved the retry URL timeout functionality to reload a failed URL and recapture the screenshot, instead of proceeding to another URL if a timeout occurred.

