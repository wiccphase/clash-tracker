import requests
import telebot
import logging
import json
import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_clan_current_war(tag):
    base_url = "https://api.clashofclans.com/v1/clans/"
    url = f"{base_url}{tag}/currentwar"
    headers = {"Accept": "application/json", "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc2NWQ4NmY5LWJlMzUtNDc0My05OTJiLWM0ODMzZWFjMDAxYiIsImlhdCI6MTcyMjg2NzI1MCwic3ViIjoiZGV2ZWxvcGVyLzVlZmE4ZmFhLTBhNGUtYjc3NS1jMWZmLTAyZmRmZDljZTk1NSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjg5LjIzMi43Ny4xMzgiXSwidHlwZSI6ImNsaWVudCJ9XX0.p-_yz6JBYfsAPXOU-QFW4VpOVOvYo5tlRbItzKCKX8ArIv5EBRTi4GSPBo8fvi68J_bFJIExrY6UBeAPUK3lvQ"}
    logger.debug(f"Sending request to {url}")
    response = requests.get(url, headers=headers)

    try:
        response.raise_for_status()
        logger.debug("Request successful")
        return response.json()
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
        return None
    




def get_clan_info(tag):
    base_url = "https://api.clashofclans.com/v1/clans/"
    url = f"{base_url}{tag}"
    headers = {"Accept": "application/json", "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc2NWQ4NmY5LWJlMzUtNDc0My05OTJiLWM0ODMzZWFjMDAxYiIsImlhdCI6MTcyMjg2NzI1MCwic3ViIjoiZGV2ZWxvcGVyLzVlZmE4ZmFhLTBhNGUtYjc3NS1jMWZmLTAyZmRmZDljZTk1NSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjg5LjIzMi43Ny4xMzgiXSwidHlwZSI6ImNsaWVudCJ9XX0.p-_yz6JBYfsAPXOU-QFW4VpOVOvYo5tlRbItzKCKX8ArIv5EBRTi4GSPBo8fvi68J_bFJIExrY6UBeAPUK3lvQ"}

    logger.debug(f"Sending request to {url}")
    response = requests.get(url, headers=headers)

    try:
        response.raise_for_status()
        logger.debug("Request successful")
        return response.json()
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
        return None
    


    
def get_player_info(player_tag):

    base_url = "https://api.clashofclans.com/v1/players/"
    modified_tag = player_tag.replace('#', '%23')
    full_url = base_url + modified_tag
    headers = {"Accept": "application/json", "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijc2NWQ4NmY5LWJlMzUtNDc0My05OTJiLWM0ODMzZWFjMDAxYiIsImlhdCI6MTcyMjg2NzI1MCwic3ViIjoiZGV2ZWxvcGVyLzVlZmE4ZmFhLTBhNGUtYjc3NS1jMWZmLTAyZmRmZDljZTk1NSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjg5LjIzMi43Ny4xMzgiXSwidHlwZSI6ImNsaWVudCJ9XX0.p-_yz6JBYfsAPXOU-QFW4VpOVOvYo5tlRbItzKCKX8ArIv5EBRTi4GSPBo8fvi68J_bFJIExrY6UBeAPUK3lvQ"}
    
    response = requests.get(full_url, headers=headers)
    
    response.raise_for_status()

    player_data = response.json()  # Преобразуем ответ в JSON

    # Проверяем, есть ли в ответе ожидаемые данные
    if 'reason' in player_data:
        return "Ошибка: " + player_data['reason']  # Пример обработки ошибки
    else:
        # Извлекаем нужные данные из player_data
        # Например, имя игрока

        return response.json()
    
    
def format_member_list(member_list):
    formatted_members = []
    for index, member in enumerate(member_list, start=1):  # Используем enumerate для нумерации участников
        name = member.get('name', 'Аноним')
        tag = member.get('tag', 'a')
        role = member.get('role', 'Неизвестная роль')
        town_hall_level = member.get('townHallLevel', 'Неизвестный уровень')
        experience_level = member.get('expLevel', 'Неизвестный уровень')
        donations = member.get('donations', 0)
        donations_received = member.get('donationsReceived', 0)
        trophies = member.get('trophies', 0)
        builder_base_trophies = member.get('builderBaseTrophies', 0)
        formatted_members.append(f"{index}. {name}\n   Роль: {role}\n  Уровень ТХ: {town_hall_level}\n   Опыт: {experience_level}\n   Донаты дано: {donations}\n   Донаты получено: {donations_received}\n   Трофеи: {trophies}\n   Трофеи строительной базы: {builder_base_trophies} \n")
    return "\n".join(formatted_members)



TOKEN = '7324731202:AAFo0_FokFHa4LaKzcI6YdnEthjX1SA69Ms'
bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def handle_start_command(message):

    clan_info = get_clan_info("%232G8GJGYCL")
    current_war = get_clan_current_war("%232G8GJGYCL")

    clan_name = clan_info.get('name', 'neizves')
    members_list = clan_info.get('memberList', [])
    members_info = format_member_list(members_list)
    opponent_name = current_war.get('opponent', {}).get('name', 'Не нашлась ')
    opponent_attacks = current_war.get('opponent', {}).get('attacks', 'Не нашлась ')
    opponent_exp_earned = current_war.get('opponent', {}).get('expEarned', 'Нет ')
    startTime = current_war.get('startTime', 'date')
    endTime = current_war.get('endTime', '')
    clan_attacks = current_war.get('clan', {}).get('attacks', 'Не нашлась ')
    clan_exp_earned = current_war.get('clan', {}).get('expEarned', 'Нет ')
    



    message_text = f"*Название клана:* {clan_name}'\nКоличество участников: {len(members_list)}\nУчастники:\n{members_info} \n \n \n \n Клановая война с: \n {opponent_name} \n Аттак противника: {opponent_attacks} \n Наши аттаки: {clan_attacks} \n Опыта у противника: {opponent_exp_earned} \n У нас опыта: {clan_exp_earned} \n Время старта {startTime} \n endTime: {endTime}"
    bot.send_message(message.chat.id, message_text)
    bot.send_message(message.chat.id, 'иди нах отсюда')







@bot.message_handler(commands=['members'])
def handle_start_command(message):
    clan_info = get_clan_info("%232G8GJGYCL")  
    members_list = clan_info.get('memberList', [])

    for member in members_list:
        player_tag = member.get('tag', '') 
        player_info = get_player_info(player_tag)  

        player_name = player_info.get('name', 'Данные не найдены')
        iconUrls = player_info.get('iconUrls', 'noneurls')
        townHallLevel = player_info.get('townHallLevel', 'hz')
        donations = player_info.get('donations', 'hz')
        donationsReceived = player_info.get('donationsReceived', 'hz')
        warStars = player_info.get('warStars', 'hz')
        playerHouse = player_info.get('playerHouse', 'hz')

        
        # Добавляем информацию о текущем участнике в текст сообщения
        message_text = f"Имя пидора:{player_name}\n \n Тут мб фотку подгружу:{iconUrls} \n \n ЛВЛ Ратушки: {townHallLevel} \n \n Сколько задонатил: {donations} \n Сколько сожрал: {donationsReceived} \n \n Сколько всего звезд военных:{warStars} \n \n !!В разработке: {playerHouse}"
        bot.send_message(message.chat.id, message_text)

if __name__ == '__main__':
    bot.polling(none_stop=True)


