<h1>🤖 WeTheHobby Discord Bot 🤖</h1>
<h2>Features:</h2>
<ul>
    <li>Twilio SMS Push Implementation 📱</li>
    <li>Basic Output Commands 📝</li>
</ul>

<br>

<h2>Installation Guide: 📜</h2>

<h3>1 - Create Discord Bot Application 🤖</h3>
<p>1.1 - Go to <a>https://discord.com/developers/applications</a> and click "new application" in the top right. </p>
<p>1.2 - Enter the application name and assign it to the Top Shelf Enterprises team </p>
<p>1.3 -  In the application settings go to "Bot" in the left Nav and add a profile picture, profile banner, and username (if desired)</p>
<p>1.4 - In the application settings go to "OAuth2" in the left Nav and in the OAuth2 URL generator, click the "bot" option. Scroll down and copy the link, this is how you will invite the bot to a Discord server</p> 
<p>1.5 - In the copied link replace the value in "permissions=0" with "permission=563364418145344". This value is the minimum required permissions the bot needs to execute its functions</p>
<p>1.6 - In the application settings go to "Bot" in the left Nav and click the "Reset Token" box. Enter your two-factor authentication code (if turned on). Click copy and make note of this token as it can only be viewed once</p>

<br>

<h3>2 - Create Environmental Variables 🌎</h3>

<p><b>Envirionemal Variables to add:</b></p>
<ul>
    <li>TWILIO_ACCOUNT_SID - Value found at <a>https://console.twilio.com</a></li>
    <li>TWILIO_AUTH_TOKEN - Value found found at <a>https://console.twilio.com</a></li>
    <li>wth_discord_token - Value found in Discord Application Settings under "Bot". Refer to 1.6</li>
</ul>

<p><b>Windows 🪟</b></p>
<p>2.1 - Type "env" in the Windows search bar and click "Edit the system environmental variables"</p>
<p>2.2 - Click the environmental variables box</p>
<p>2.3 - Click new in the User Variables box and type in the variable name and it's associated value</p>
<p>2.4 - Click new in the System Variables box and type in the variable name and it's associated value</p>
<p>2.5 - Repeat this process for each environmental variable</p>

<p><b>Linux 🖥️</b></p>
<p>2.1 - Open a terminal</p>
<p>2.2 - Enter "export ENV_NAME=ENV_VALUE"</p>
<p>2.3 - Repeat this process for each environmental variable</p>

<br>

<h3>3 - Install Python & Required Packages 🐍</h3>
<p>3.1 - Install Python 🐍</p>
    <ul>
        <li>🪟 Windows - Download and run the .exe for Python 3.12 - <a>https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe</a>
        <li>🖥️ Linux (Ubuntu) - "sudo apt install python3.12"</li>
    </ul>
<p>3.2 - Install Discord package - "pip install discord"</p>
<p>3.3 - Install Twilio package - "pip install twilio"</p>

<br>

<h3>4 - Configuration Info 🔐</h3>
<p>4.1 - Configuration file in located in the main directory as "configs.json" and stores info including Discord IDs, names, phone numbers, subscribed channels, and permissable roles</p>
<p>4.2 - Regular maintenance is optimal with current implementation if new tech development employees are ever hired. To obtain Discord IDs, go to settings -> advanced and enable Developer options. Then right click on the user and click "Copy User ID". After that add to "configs.json".</p>
<p>*UserID maintenance to be automated in V3 (Refer to additional notes)*</p>
<p>*Manaual config changes down externally from the bot requires bot restart*</p>


<br>

<h3>5 - Run the Discord Bot 🏃‍♂️💨</h3>
<p>5.1 - Spin up a VM or local machine to host Discord bot source code</p>
<p>5.2 - Run the main.py file</p>

<br>

<h2>Additional Notes: 📎</h2>
<ul>
    <li>Permissions Value (563364418145344) -  Read Messages/View Channels, Send Messages, Send Messages in Threads, Embed Links, Attach Files, Read Message History, Use External Emojis, Use External Stickers, Add Reactions, Use Slash Commands, & Create Polls</li>
    <li>Cost of each SMS Message = $0.0079</li>
    <li>Adding user IDs to the configuration file will be automated in Version 3.0 in the subscribe command</li>
</ul>