# GuayaBot

Introducing GuayaBot: an interactive Discord bot crafted by and for the [GuayaHack](guayahack.co) community.

## Table of Contents

- [GuayaBot](#guayabot)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [How does it work?](#how-does-it-work)
  - [Requirements](#requirements)
  - [Setup](#setup)
  - [Use](#use)
  - [Contribution](#contribution)
  - [License](#license)

## Description

GuayaBot is a Discord chat bot designed to suit the necessities and ideas of [GuayaHack](https://guayahack.co). From a simple quotes bot to greater things, imagination is the limit.

## How does it work?

GuayaBot operates by listening to messages on your Discord server. When it detects a command prefixed by `!`, like `!quote`, it responds with the corresponding output. It currently provides a set of quotes to select from randomly, but its capabilities can be extended based on user needs.

## Requirements

- docker

## Setup

For convenience, we have implemented a Dockerfile for this project. Follow these steps to set up the bot:

1. Create a `.env` file in the project root.
2. Add the following line to the `.env` file, replacing `tokenForDiscord` with your actual Discord token:

   ```plaintext
   TOKEN=tokenForDiscord
   ```

3. Run the following command to build the Docker image for the bot:

   ```bash
   docker build -t guayabot:latest .
   ```

4. Finally, run the container:

   ```bash
   docker run -d guayabot
   ```

## Use

To use the bot, simply type the commands in your Discord chat. For example:

- `!quote` : GuayaBot will respond with a random quote from the GuayaHack community.
- `!addquote "quote" - Author` : Guayabot will add the quote to quotes.yaml

## Contribution

- The community is encouraged to contribute to the project.

- Contributions, whether they are bug fixes, improvements, or new features, are welcome.

- All contributions will be warmly received and appropriately reviewed before being incorporated into the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
