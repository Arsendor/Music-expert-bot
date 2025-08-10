from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from logic import *
from logic import select_by_energy, select_by_tempo, select_by_danceability, select_by_playlist_genre, \
    select_by_loudness, select_by_liveness, select_by_valence, select_by_track_artist, \
    select_by_time_signature, select_by_speechiness, select_by_track_popularity, \
    select_by_track_href, select_by_uri, select_by_track_album_name, select_by_playlist_name, \
    select_by_analysis_url, select_by_track_id, select_by_track_name, \
    select_by_track_album_release_date, select_by_instrumentalness, select_by_track_album_id, \
    select_by_mode, select_by_key, select_by_duration_ms, select_by_acousticness, \
    select_by_id, select_by_playlist_subgenre, select_by_type, select_by_playlist_id, \
    get_top_tracks, get_top_artists

bot = TeleBot(TOKEN)

user_search_state = {}

def get_main_menu():
    """Возвращает основное меню"""
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("🎤 Search Artist", callback_data="search_artist")
    button2 = InlineKeyboardButton("💿 Search Album", callback_data="search_album")
    button3 = InlineKeyboardButton("🎵 Search Song", callback_data="search_song")
    button4 = InlineKeyboardButton("🏆 Top Tracks", callback_data="top_tracks")
    button5 = InlineKeyboardButton("⭐ Top Artists", callback_data="top_artists")
    markup.add(button1, button2, button3)
    markup.add(button4, button5)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🎶 Welcome to the Music Bot!")
    bot.send_message(message.chat.id, 
                    "I can help you find information about artists, albums, songs, and discover popular music.\n\n"
                    "Use the buttons below to get started:", 
                    reply_markup=get_main_menu())

@bot.message_handler(commands=['help'])
def help(message):
    help_text = """🎶 **Music Bot Help**

**Available commands:**
• `/start` - Start the bot and show main menu
• `/help` - Show this help message

**What I can do:**
• 🎤 Search for artists by name
• 💿 Search for albums/playlists
• 🎵 Search for songs with various criteria
• 🏆 Show top 10 most popular tracks
• ⭐ Show top artists by popularity

**Search criteria for songs:**
• By name, artist, album, genre
• By popularity, release date, duration
• By audio features (energy, tempo, danceability, etc.)
• By technical IDs (track ID, URI, playlist ID)

Just use the buttons to navigate through options!"""
    
    bot.send_message(message.chat.id, help_text, reply_markup=get_main_menu())

# Обработчики callback для основного меню
@bot.callback_query_handler(func=lambda call: call.data == "search_artist")
def handle_search_artist(call):
    user_search_state[call.message.chat.id] = "artist"
    bot.send_message(call.message.chat.id, "🎤 Please enter the artist's name:")

@bot.callback_query_handler(func=lambda call: call.data == "search_album")
def handle_search_album(call):
    user_search_state[call.message.chat.id] = "album"
    bot.send_message(call.message.chat.id, "💿 Please enter the album/playlist name:")

@bot.callback_query_handler(func=lambda call: call.data == "search_song")
def handle_search_song(call):
    markup = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("🎵 By name", callback_data="search_by_name"),
        InlineKeyboardButton("🎤 By artist", callback_data="search_by_artist"),
        InlineKeyboardButton("💿 By album", callback_data="search_by_album"),
        InlineKeyboardButton("🎼 By genre", callback_data="search_by_genre"),
        InlineKeyboardButton("⭐ By popularity", callback_data="search_by_popularity"),
        InlineKeyboardButton("📅 By release date", callback_data="search_by_release_date"),
        InlineKeyboardButton("⏱️ By duration", callback_data="search_by_duration_ms"),
        InlineKeyboardButton("🎹 By key", callback_data="search_by_key"),
        InlineKeyboardButton("🥁 By tempo", callback_data="search_by_tempo"),
        InlineKeyboardButton("⚡ By energy", callback_data="search_by_energy"),
        InlineKeyboardButton("🕺 By danceability", callback_data="search_by_danceability"),
        InlineKeyboardButton("🔊 By loudness", callback_data="search_by_loudness"),
        InlineKeyboardButton("🎪 By liveness", callback_data="search_by_liveness"),
        InlineKeyboardButton("😊 By valence", callback_data="search_by_valence"),
        InlineKeyboardButton("🗣️ By speechiness", callback_data="search_by_speechiness"),
        InlineKeyboardButton("🎻 By instrumentalness", callback_data="search_by_instrumentalness")
    ]
    
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            markup.add(buttons[i], buttons[i + 1])
        else:
            markup.add(buttons[i])
    
    # Кнопка "Назад"
    markup.add(InlineKeyboardButton("⬅️ Back to main menu", callback_data="back_to_main"))
    
    bot.send_message(call.message.chat.id, "🎵 How would you like to search for the song?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "top_tracks")
def handle_top_tracks(call):
    bot.send_message(call.message.chat.id, "🏆 Getting top tracks...")
    response = get_top_tracks()
    bot.send_message(call.message.chat.id, f"🏆 **TOP 10 TRACKS:**\n\n{response}", 
                    reply_markup=get_main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "top_artists")
def handle_top_artists(call):
    bot.send_message(call.message.chat.id, "⭐ Getting top artists...")
    response = get_top_artists()
    bot.send_message(call.message.chat.id, response, reply_markup=get_main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def handle_back_to_main(call):
    # Очищаем состояние пользователя
    if call.message.chat.id in user_search_state:
        del user_search_state[call.message.chat.id]
    
    bot.send_message(call.message.chat.id, "🎶 Main Menu:", reply_markup=get_main_menu())

# Обработчики критериев поиска
@bot.callback_query_handler(func=lambda call: call.data.startswith("search_by_"))
def handle_search_criteria(call):
    criteria = call.data.replace("search_by_", "")
    user_search_state[call.message.chat.id] = criteria
    
    criteria_names = {
        "name": "🎵 song name",
        "artist": "🎤 artist name",
        "album": "💿 album name",
        "genre": "🎼 genre",
        "popularity": "⭐ popularity (0-100)",
        "release_date": "📅 release date (YYYY-MM-DD)",
        "duration_ms": "⏱️ duration in milliseconds",
        "key": "🎹 key (0-11)",
        "tempo": "🥁 tempo (BPM)",
        "energy": "⚡ energy (0.0-1.0)",
        "danceability": "🕺 danceability (0.0-1.0)",
        "loudness": "🔊 loudness (dB)",
        "liveness": "🎪 liveness (0.0-1.0)",
        "valence": "😊 valence (0.0-1.0)",
        "speechiness": "🗣️ speechiness (0.0-1.0)",
        "instrumentalness": "🎻 instrumentalness (0.0-1.0)"
    }
    
    criteria_name = criteria_names.get(criteria, criteria)
    bot.send_message(call.message.chat.id, f"Please enter the {criteria_name}:")

# Основной обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    criteria = user_search_state.get(message.chat.id)
    
    if criteria:
        # Показываем индикатор "печатает"
        bot.send_chat_action(message.chat.id, 'typing')
        
        try:
            # Вызываем нужную функцию поиска по критерию
            if criteria == "name":
                response = select_by_track_name(message.text)
            elif criteria == "artist":
                response = select_by_track_artist(message.text)
            elif criteria == "album":
                response = select_by_playlist_name(message.text)
            elif criteria == "genre":
                response = select_by_playlist_genre(message.text)
            elif criteria == "popularity":
                response = select_by_track_popularity(message.text)
            elif criteria == "release_date":
                response = select_by_track_album_release_date(message.text)
            elif criteria == "duration_ms":
                response = select_by_duration_ms(message.text)
            elif criteria == "key":
                response = select_by_key(message.text)
            elif criteria == "tempo":
                response = select_by_tempo(message.text)
            elif criteria == "energy":
                response = select_by_energy(message.text)
            elif criteria == "danceability":
                response = select_by_danceability(message.text)
            elif criteria == "loudness":
                response = select_by_loudness(message.text)
            elif criteria == "liveness":
                response = select_by_liveness(message.text)
            elif criteria == "valence":
                response = select_by_valence(message.text)
            elif criteria == "speechiness":
                response = select_by_speechiness(message.text)
            elif criteria == "instrumentalness":
                response = select_by_instrumentalness(message.text)
            else:
                response = f"❌ Unknown search criteria: {criteria}"
            
            bot.send_message(message.chat.id, response)
            
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Error occurred: {str(e)}")
        
        # Очищаем состояние и показываем главное меню
        del user_search_state[message.chat.id]
        bot.send_message(message.chat.id, "🔍 Search another?", reply_markup=get_main_menu())
    else:
        # Если нет активного состояния поиска, показываем справку
        bot.send_message(message.chat.id, 
                        "🤔 I didn't understand that. Please use the buttons below to navigate:",
                        reply_markup=get_main_menu())

# Универсальный обработчик для медиафайлов
def handle_media_message(message, media_type):
    media_icons = {
        'photo': '📸',
        'video': '🎬', 
        'audio': '🎵',
        'voice': '🎤',
        'sticker': '😊',
        'document': '📄'
    }
    
    icon = media_icons.get(media_type, '📎')
    bot.send_message(message.chat.id, f"{icon} Nice {media_type}! How can I help you find music?")
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🎤 Find Artist", callback_data="search_artist"),
        InlineKeyboardButton("💿 Find Album", callback_data="search_album")
    )
    markup.add(InlineKeyboardButton("🎵 Find Song", callback_data="search_song"))
    markup.add(InlineKeyboardButton("❌ No thanks", callback_data="no_help"))
    
    bot.send_message(message.chat.id, 
                    f"Would you like me to help you find something related to your {media_type}?", 
                    reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    handle_media_message(message, 'photo')

@bot.message_handler(content_types=['video'])
def handle_video(message):
    handle_media_message(message, 'video')

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    handle_media_message(message, 'audio')

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    handle_media_message(message, 'voice')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    handle_media_message(message, 'sticker')

@bot.message_handler(content_types=['document'])
def handle_document(message):
    handle_media_message(message, 'document')

@bot.callback_query_handler(func=lambda call: call.data == "no_help")
def handle_no_help(call):
    bot.send_message(call.message.chat.id, "👍 Okay! If you need anything else, just use the menu below:",
                    reply_markup=get_main_menu())

# Обработка всех остальных типов сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_other_messages(message):
    bot.send_message(message.chat.id, 
                    "🤔 I'm not sure how to handle that type of message. Please use the menu:",
                    reply_markup=get_main_menu())

if __name__ == "__main__":
    print("🎶 Music Bot is starting...")
    bot.polling(none_stop=True)