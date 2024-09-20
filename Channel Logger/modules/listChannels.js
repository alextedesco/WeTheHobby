const { EmbedBuilder } = require('discord.js');  

async function handleChannelListCommand(message) {  
    if (message.author.bot) return; // Ignores bot messages  

    if (message.content.includes("$channels")) {  
        const channelInfo = {  
            categories: [],  
            channels: [],  
        };  

        // Gets all channels and sorts them into categories and text channels  
        message.guild.channels.cache.sort((a, b) => a.rawPosition - b.rawPosition).forEach(channel => {  
            // Checks if it is a category
            if (channel.parentId === null) {  
                channelInfo.categories.push({
                    name: channel.name,
                    id: channel.id
            });
            // If not, it is a text channel  
            } else {  
                channelInfo.channels.push({  
                    name: channel.name,   
                    parentId: channel.parentId // Associates text channel with Category 
                });  
            }  
        });  

        let description = ""; 
        channelInfo.categories.forEach(category => {  
            description += `- ${category.name}\n`; 
            channelInfo.channels.forEach (channel => {
                if (channel.parentId === category.id) {
                    description += `  - ${channel.name}\n`
                }
            })
        });  
        
        const channelembed = new EmbedBuilder()   
            .setTitle("Category/Channel List")  
            .setDescription(description.trim())
            .setTimestamp()  
            .setColor("#2dbb17")   
            .setFooter({ text: "AYOO" });  

        await message.channel.send({ embeds: [channelembed] });   
    }  
}  

module.exports = handleChannelListCommand;