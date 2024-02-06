from flask import Blueprint,render_template, jsonify, request
from urllib.parse import urlparse, parse_qs
import requests
import asyncio
import aiohttp


bp = Blueprint("seznam", __name__)


incomes = [
    { 'title': 'test', 'id': 'EaRL3co1NQ8', 'url': 'https://www.youtube.com/watch?v=EaRL3co1NQ8', 'thumbnail': 'https://i.ytimg.com/vi/EaRL3co1NQ8/maxresdefault.jpg', 'description': '123 223' }
]

    

@bp.route('/incomes')
def get_incomes():
    return jsonify(incomes)


@bp.route('/incomes', methods=['POST'])
async def add_income():
    params = request.get_json()
    if 'https://youtu.be/' in params["url"]:
        id=params["url"].split('https://youtu.be/')[1].split('?')[0]
        print(id)
        params['id'] = id
        await getInfo(id)
        return 'be', 201
    if 'https://www.youtube.com/' or 'https://youtube.com/' in params["url"]:
        parsed_url = urlparse(params["url"])
        id = parse_qs(parsed_url.query)['v'][0]
        params['id'] = id
        await getInfo(id)
        return 'com', 201
    else:
        print(params["url"])
        return request.get_json(), 406 # Not acceptable - sprejema samo youtube linke 

def getSeznam():
    return incomes

async def getInfo(id):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.googleapis.com/youtube/v3/videos?part=snippet&id=' + id + '&key=AIzaSyDwEqiktbQNW295zLxA0ItlZEzlJfuZZro') as response:
            data = await response.json()
    
    #print('data: ', data['items'][0]['snippet']['thumbnails'])
    title = data['items'][0]['snippet']['title']
    description = data['items'][0]['snippet']['description']
    thumbnail=''
    if 'maxres' in data['items'][0]['snippet']['thumbnails']:
        #print('maxres')
        thumbnail = data['items'][0]['snippet']['thumbnails']['maxres']['url']

    elif 'high' in data['items'][0]['snippet']['thumbnails']: ##else if
        #print('high')
        thumbnail = data['items'][0]['snippet']['thumbnails']['high']['url']

    elif 'medium' in data['items'][0]['snippet']['thumbnails']: ##else if
        #print('medium')
        thumbnail = data['items'][0]['snippet']['thumbnails']['medium']['url']

    elif 'standard' in data['items'][0]['snippet']['thumbnails']: ##else if
        #print('standard')
        thumbnail = data['items'][0]['snippet']['thumbnails']['standard']['url']

    elif 'default' in data['items'][0]['snippet']['thumbnails']: ##else if
        #print('default')
        thumbnail = data['items'][0]['snippet']['thumbnails']['default']['url']
    povezava = 'https://youtube.com/watch?v=' + id
    object = {'id': id, 'title': title, 'description': description, 'thumbnail': thumbnail, 'url': povezava} 
    incomes.append(object)