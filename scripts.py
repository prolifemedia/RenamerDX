class Scripted(object):    


    PROGRESS_DIS = """\n
โญโโโ[**๐Progress Bar๐**]โโโโ
โ
โ<b>๐ : {1} | {2}</b>
โ
โ<b>๐ : {0}%</b>
โ
โ<b>โก : {3}/s</b>
โ
โ<b>โฑ๏ธ : {4}</b>
โฐโโโโโโโโโโโโโโโโโโ"""

    HELP_TEXT = """
<i>๐๐๐ญ๐๐ก ๐๐ข๐๐๐จ ๐๐จ๐ฐ ๐ญ๐จ ๐๐ฌ๐ ๐๐ <a href='https://youtu.be/HnXdu74o34E'>[ แดสษชแดแด สแดสแด ]</a></i>\n
<i>๐๐๐ง๐ ๐ ๐ฉ๐ก๐จ๐ญ๐จ ๐ญ๐จ ๐ฆ๐๐ค๐ ๐ข๐ญ ๐๐ฌ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ (optional)</i>\n
<i>๐๐๐ง๐ ๐ฆ๐ ๐๐ง๐ฒ ๐๐ข๐ฅ๐ (or) ๐๐๐๐ข๐ ๐๐ซ๐จ๐ฆ ๐ญ๐๐ฅ๐๐ ๐ซ๐๐ฆ</i>\n
<i>๐๐จ๐ง๐ฏ๐๐ซ๐ญ ๐๐ข๐ฅ๐๐ฌ ๐ข๐ง๐ญ๐จ ๐ฏ๐ข๐๐๐จ ๐ฎ๐ฌ๐ /convert ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>\n
<i>๐๐๐ฉ๐ฅ๐ฒ ๐ญ๐จ ๐ญ๐ก๐๐ญ ๐๐ข๐ฅ๐ ๐ฐ๐ข๐ญ๐ก /rename ๐ง๐๐ฐ ๐ง๐๐ฆ๐.ext</i>\n
<i>๐๐ข๐๐ฐ ๐ฒ๐จ๐ฎ๐ซ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ /sthumbnail ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>\n
<i>๐๐๐ฅ๐๐ญ๐ ๐ฒ๐จ๐ฎ๐ซ ๐ญ๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ /dthumbnail ๐๐จ๐ฆ๐ฆ๐๐ง๐</i>"""


    ABOUT_TEXT = """
โญโโโโ[๐MY GROUP๐]โโโโ
โ
โ<b>๐ค Bot Name : <a href='https://t.me/RenameProRobot'>๐ Rename-Pro-bot ๐ฎ๐ณ</a></b>
โ
โ<b>๐ข Update Channel : <a href='https://t.me/Tamil_Astrology'>เฎจเฎฉเฏเฎชเฎฐเฏเฎเฎณเฏ เฎเฏเฎดเฏ ๐ฎ๐ณ</a></b>
โ
โ<b>๐ฅ Support Channel : <a href='https://t.me/Tamil_Panchangam'>๐ เฎชเฎเฏเฎเฎพเฎเฏเฎเฎฎเฏ ๐</a></b>
โ
โ<b>๐ข Group Info : <a href='https://t.me/Aanmeekam'>เฎคเฎฎเฎฟเฎดเฎฉเฏ เฎเฎฉเฏเฎฎเฏเฎเฎฎเฏ เฎเฏเฎดเฏ</a></b>
โ
โ<b>๐ Channel Info : <a href='https://t.me/aedaham_library_noolakam'>เฎเฎเฎเฎฎเฏ library เฎเฏเฎดเฏ ๐ฎ๐ณ</a></b>
โ
โ<b>๐ Tamil Mp3 : <a href='https://t.me/Tamil_jukebox_songs/'>Tamil jukebox Song's</a></b>
โ
โ<b>ใ Jallikattu Group : <a href='https://t.me/Tamilnadu_Jallikattu'>เฎคเฎฎเฎฟเฎดเฏเฎจเฎพเฎเฏ เฎเฎฒเฏเฎฒเฎฟเฎเฏเฎเฎเฏเฎเฏ</a></b>
โ
โ<b>๐จโ๐ป Developer : <a href='https://t.me/PXMEDIA_RAJANGAM'>RAJANGAM</a></b>
โ
โ<b>๐ธ Admin Contact : <a href='https://t.me/tamil_message_bot'>Admin Message ๐ฎ๐ณ</a></b>
โ
โฐโโโโโโ[Thanks ๐]โโโโ"""

    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>ยฅou Are Banned ๐ซ</b>"
    BANNED_USER_TEXT = "<i>ยฅou are Banned ๐ซ</i>"
    TRYING_TO_UPLOAD = "<i>Trying to Upload.....</i>"
    CURRENT_THUMBNAIL = "<i>๐๐จ๐ฎ๐ซ ๐๐ฎ๐ซ๐ซ๐๐ง๐ญ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐ญ</i>"
    THUMBNAIL_SAVED = "<i>๐๐จ๐ฎ๐ซ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐๐ฏ๐๐ โ</i>"
    THUMBNAIL_DELETED = "<i>๐๐จ๐ฎ๐ซ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐๐ฅ๐๐ญ๐๐ โ</i>"
    NO_THUMBNAIL_FOUND = "<i>๐๐จ ๐๐ก๐ฎ๐ฆ๐๐ง๐๐ข๐ฅ ๐๐จ๐ฎ๐ง๐ ๐</i>"
    TRYING_TO_DOWNLOAD = "<i>Trying to Download....</i>"
    UPLOAD_SUCCESS = "<u><i>THANKS FOR USING แดแดโค Join @Tamil_Support</i></u>"
    REPLY_TO_MEDIA = "<i>Reply to Media For Converting with Command /convert</i>"
    UPLOAD_START = "<i>๐ค Uploading Your File Please wait...</i>\n"
    DOWNLOAD_START = "<i>๐ฅ Downloading Your File Please wait...</i>\n"
    JOIN_NOW_TEXT = "<code>First Join My Updates Channel to Use Me</code>"
    REPLY_TO_FILE = "<i>Reply to that media with /rename new name .ext</i>"
    CONTACT_MY_DEVELOPER = "<i>Something Wrong Contact in Support Group @Tamil_Support ๐</i>"
    START_TEXT = "<i>This is a Fastest File Renamer and Converter Bot With Permanant Thumbnail Support๐ฏ</i>"
    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/Tamil_Support'>[ Click Here]</a></b>"
