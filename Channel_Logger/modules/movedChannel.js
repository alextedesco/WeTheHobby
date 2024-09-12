const { AuditLogEvent } = require('discord.js');  

let updatesQueue = []; // Queue to store channel updates  

function setupChannelUpdateHandler(client) {  
    client.on("channelUpdate", (oldChannel, newChannel) => {  
        updatesQueue.push({ oldChannel, newChannel });  
        processQueue(client);
    });  
}  

async function processQueue(client) {  
    if (updatesQueue.length === 0) return;  

    const { oldChannel, newChannel } = updatesQueue.shift();  

    if (oldChannel.position !== newChannel.position) {  
        try {  
            await new Promise(resolve => setTimeout(resolve, 1000)); 

            const fetchedLogs = await newChannel.guild.fetchAuditLogs({  
                limit: 1,  
                type: AuditLogEvent.ChannelUpdate,  
            });  

            const log = fetchedLogs.entries.first();  

            if (log) {  
                const { executor } = log;
                const executorName = executor.globalName || executor.username;
                await client.channels.cache.get('1281665907286081536').send({ content: `Channel "${oldChannel.name}" position changed! \nMoved to position: ${newChannel.position} \nChanged by: ${executorName}` });  
            } else {  
                console.log('No audit logs found for this channel update.');  
            }  
        } catch (error) {  
            console.error('Error fetching audit logs:', error);  
        }  
    }  

    setTimeout(() => processQueue(client), 1000);   
}  

module.exports = setupChannelUpdateHandler;