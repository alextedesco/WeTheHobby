require('dotenv').config(); // Initializes dotenv  
const Discord = require('discord.js'); // Imports discord.js  
const setupChannelUpdateHandler = require('./modules/movedChannel.js'); 
const handleChannelListCommand = require('./modules/listChannels.js');   

// Creates a new client instance with the required intents  
const client = new Discord.Client({  
    intents: [  
        Discord.GatewayIntentBits.Guilds,  
        Discord.GatewayIntentBits.GuildMessages,  
        Discord.GatewayIntentBits.MessageContent,  
        Discord.GatewayIntentBits.GuildMembers,  
        Discord.GatewayIntentBits.GuildInvites,  
        Discord.GatewayIntentBits.GuildEmojisAndStickers  
    ]  
});  

client.on('ready', () => {  
    console.log(`Logged in as ${client.user.tag}!`);  
});  

setupChannelUpdateHandler(client);  

// Handles message creation  
client.on("messageCreate", async (message) => {  
  await handleChannelListCommand(message); // Call the function to handle the channel list command  
}); 

// Logs into the bot
client.login(process.env.wth_discord_token); 
