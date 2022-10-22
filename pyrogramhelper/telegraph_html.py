from html_telegraph_poster import TelegraphPoster

async def tgpost(Res,text):
 client = TelegraphPoster(use_api=True)
 client.create_api_token(Res)
 page = client.post(
        title=Res,
        author="Link Shortner Bot",
        author_url="https://t.me/Link_Shortner_tr_Bot",
        text=text,
 )
 re=page['url']
 return re
