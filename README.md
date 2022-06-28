# U-Cursed

Discord Bot that web-scraps U-Cursos and U-Campus to get information about engineering courses from the Universidad de Chile.

## Description

Discord.py bot that uses beautifulsoup to embed information obtained from both U-Cursos and U-Campus according to the given course, it uses public data and does not require to log in.

I suggest that you don't overuse this bot since U-Cursos gets a lot of traffic depending on the time of year. This project is both for entertainment and learning purposes only.

Check the self-hosting section to get more information about the project's structure and how to run this by yourself.

## Getting Started

### Inviting the bot

The bot is currently being hosted at Heroku, not very efficient and runs out of Dynos by the end of the month but gets the job done (might make new schedules to turn it on and off). You can invite it to your server by using this [link](https://discord.com/oauth2/authorize?client_id=745371842570879027&permissions=51200&scope=bot).

### Useful commands

#### u help

Gets you general info about the bot and how to use it to your discord DMs.

#### u status

Information about the bot ping, guilds and version.

#### u post

This embeds the last post in said course and section if it's publicly available, you can click it if logged in your browser to get to the post inmediately. The syntax is as follows:

> u post required_course_code (optional_section=1)

![u post example](https://i.ibb.co/q9DnC7q/0upost.png)

#### u horario

This embeds the course's section schedule for the current, previous or next week. The syntax is a follows:

> u post required_course_code required_section (optional_week = prev|act|sig)

![u horario example](https://i.ibb.co/j5rgBKt/0uhorario.png)

### u info

This embeds general course information, such as credits, requirements and the program if available. The syntax is as follows:

> u info required_course_code

![u info example](https://i.ibb.co/LZw73wC/0uinfo.png)

## Self-Hosting

First o

### Dependencies

* Python 3.8 and above
* PIL, BeautifulSoup and Discord.

## Authors

Polarisu

## Version History

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details
