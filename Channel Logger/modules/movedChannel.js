// Imports
const { ChannelType, EmbedBuilder } = require('discord.js');

let updatesQueue = []; // Update Queue  
let movingChannels = new Set(); // Stores channels currently being moved  
let initialChannelPositions = new Map(); // Stores initial channel positions  
let channelUpdateTimeout; // Timeout delay between channel updates  
let isProcessing = false; // Boolean to indicate channel updates are currently being processed. Prevents channelUpdate infinite loop

// Timeout delay variable function for channel movement
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));  

function channelUpdateHandler(client) {  
    client.once('ready', () => {  
        client.guilds.cache.forEach(guild => {  
            guild.channels.cache.forEach(channel => {  
                if (channel.type === ChannelType.GuildText) {  
                    initialChannelPositions.set(channel.id, channel.position);  
                }  
            });  
            console.log(`Initial channel positions for guild "${guild.name}" logged.`);  
        });  
    });  

    client.on("channelUpdate", async (oldChannel, newChannel) => {  
        if (oldChannel.position !== newChannel.position && !isProcessing) {  
            // Adds to queue if the channel isn't already being processed  
            if (!movingChannels.has(newChannel.id)) {  
                updatesQueue.push({ oldChannel, newChannel });  
                movingChannels.add(newChannel.id);  

                clearTimeout(channelUpdateTimeout);  

                // Starts channel processing  
                channelUpdateTimeout = setTimeout(() => {  
                    processQueue(client);  
                }, 1000);
            }  
        }  
    });  

    client.on("channelCreate", () => {  

        // Future feature commit

        // If channel is created
        // Update initialChannelPositions variable
    });  
}  

async function processQueue(client) {  
    clearTimeout(channelUpdateTimeout);  

    if (updatesQueue.length === 0) return;  

    // Set the processing flag  
    isProcessing = true;  

    let maxMovement = 0; // Max distance traveled   
    let channelToNotify; // Channel of max distance traveled  

    // Process all updates in the queue  
    for (const { oldChannel, newChannel } of updatesQueue) {  
        try {  
            console.log ("Old Channel Position: " + oldChannel.position)
            console.log ("New Channel Position: " + newChannel.position)
            const distanceChanged = Math.abs(oldChannel.position - newChannel.position);  

            console.log (oldChannel.name + " changed by " + distanceChanged + " positions");
            
            // Check if this is the largest distance moved
            if (distanceChanged > maxMovement) {  
                maxMovement = distanceChanged;  
                channelToNotify = { channel: newChannel, oldChannel }; // Stores moving channel and associated data  
            }  
        } catch (error) {  
            console.error('Error processing channel update:', error);  
        } finally {  
            // Removes the moved channel from the set  
            movingChannels.delete(newChannel.id);  
        }  
    }  
    
    if (channelToNotify && maxMovement > 0) {  
        const { channel, oldChannel } = channelToNotify;  

        const embed = new EmbedBuilder()   
            .setTitle("Channel Update Detected!")  
            .setDescription(`Channel "${oldChannel.name}" moved by ${maxMovement} positions! \nNew position: ${channel.position}`)
            .setTimestamp()  
            .setColor("#2dbb17")   
            .setFooter({ text: "AYOO" });  
        await client.channels.cache.get('1281665907286081536').send({  embeds: [embed] });  
        
        // Channel Movement Implementation  (Unfinished)
            // console.log ("\nOld Channel Category: " + oldChannel.parentId);
            // console.log ("Old Channel Position: " + oldChannel.position);
            // console.log ("Old Channel Name: " + oldChannel.name);
            // console.log ("New Channel Category: " + channel.parentId);
            // console.log ("New Channel Position: " + channel.position);
            // console.log ("Old Channel Name: " + channel.name + "\n---------------------------");
            
            // await sleep(5000);
            // await channel.setParent(oldChannel.parentId);
            // await channel.setPosition(Math.abs(oldChannel.position - 1));  
            // await client.channels.cache.get('1281665907286081536').send({  content: "Channel position fixed!" });  
        
    }  

    // Resets queue and processing flag  
    updatesQueue = [];  
    isProcessing = false;
}  

module.exports = channelUpdateHandler;