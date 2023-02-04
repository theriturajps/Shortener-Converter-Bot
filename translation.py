from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_MESSAGE = '''**Hello {}
I Am Pro URL Shortener,
I Can Convert Links Directly From Your Given Account.

Contact Admin Using @ProExecBot, If you are facing problem in anythings

👉 /features For More
'''

HELP_MESSAGE = '''Hello {}
I Am Pro URL Shortener,
Bulk Link Converter Bot. I Can Convert Links Directly From Your Given Account**

1. Go to your Url Shortener Website
2. Copy the url of the website
3. Than Type **/base_site** than give a single space and than paste the website link.

(**see example to understand...**)

`/base_site website`
(See Example.👇)
**Example:** `/base_site ziplinks.in`

-----------
-----------

1. Now Copy Your API from your Shortener website
2. Than Type **/api** than give a single space and than paste your API.

(**see example to understand...**)

`/api 9f82a99c8f0acb42d81ac153ae9583e862833e28`
(See Example.👇)
**Example:** `/api 9f82a99c8f0acb42d81ac153ae9583e862833e28`


**👉** /Features To Know More Features Of This Bot.
**👉** /channel Command To Get Help About Adding your channel to bot.
**👉** /footer To Get Help About Adding your Custom Footer to bot.

Contact Admin Using @ProExecBot, If you are facing problem in anythings
'''

ABOUT_TEXT = '''Hello {},

**⚡Features⚡**

• I can Convert any links or posts to your Provided Shortener Website link. 
(Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• Add your custom url shortener website.
👉 /base_site To know more...

• Update or Add your **API** from Your Custom Website.
👉 /api [api] To know more...

• Auto add custom **footer text** to your every post.
👉 /footer To know more...

• Auto add custom **Header text** to your every post.
👉 /Header To know more...

• Replace / remove other's channel links with your channel link.
👉 /channel To know More...

• Automatically Replace Your Banner Image To images in the post.
👉/Banner To Know More... 

• More Commands
👉/info

• **No** need to share **password or email** to convert links.

Anyone who want to use any **other shortner** type /base_site and set your own shortener website for any help **contact** me through @ProExecBot 
(all **shortners support** available.)

**Click On Custom Alias To Create Custom Link**
'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, Send in this format
`[link] | [custom_alias]`

This feature works only in private mode only

Ex: https://t.me/streamerview | StreamerView"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('More Features', callback_data=f'about_command')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Contact Admin', url=f'https://telegram.me/proexecbot')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """Here are the current settings for this bot

- Website: {base_site}

- Base Site {base_site}

- API: `{shortener_api}`

- Username: @{username}

- Header Text: {header_text}

- Footer Text: {footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API.
Get API From {base_site}

**`/api [api]`**

**Ex:-** `/api 9f82a99c8f0acb42d81ac153ae9583e862833e28`

Current Website : {base_site}
API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want
This Text will be added to the top of every message caption or text
For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**
This Text will be added to the **bottom** of every message **caption** or text
For adding **line break** use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """**Hello {}, 
I Am Pro URL Shortener
Bulk Link Converter Bot. I Can Convert Links Directly From Your Given Account**
**🌟** /channel (channel link or username)

**example:**
/channel @ProDownload_In
Or
/channel https://t.me/ProDownload_In

**👉** /features To Know More Features Of This Bot.

**- Message @proexecbot For More Help -**"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
