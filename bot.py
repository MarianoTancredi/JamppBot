from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import googlemap
from constants import BOT_API_KEY



#Despite being a class, i think is better to leave it here beacuse of the function content and the updater/context way of working
class MyBot(object):
    def __init__(self, tree,atms,bot):
        self.tree = tree
        self.atms = atms
        self.bot = bot
    #Start: Greets the user
    def start(self, update: Update,context: CallbackContext):
        update.message.reply_text("""Hola! Mi nombre es JamppBot! Un amigable bot para ayudarte a encontrar tus cajeros mas cercanos.Actualmente
                                    solo funciono para CABA. Para comenzar, necesito que me envies tu ubicacion. Para ayuda o comandos, porfavor escribi \ayuda""")
    
    #Location: Gets the user latitude and longitude, then creates the map if the city is from CABA
    def getLocation(self, update: Update,context: CallbackContext):
        lat_user = float(update.message.location.latitude)
        lon_user= float(update.message.location.longitude)
        possible_city = googlemap.localidad(lat_user,lon_user)
        
        if(possible_city):
            atms = googlemap.map(self.tree,lon_user,lat_user,self.atms)
            if(len(atms)>0):
                reply = "Por orden de proximidad:\n"
                i = 1
                for atm in atms:
                    adress = f"{i} Cajero - Banco: {atm.bank} - Red: {atm.net} - Direccion: {atm.adress}\n "
                    reply = reply + adress
                    i+=1
                
                try:
                    map = open('map.png','rb')
                    self.bot.bot.send_photo(update.message.chat_id,map,reply)
                    map.close()
                except:
                    update.message.reply_text('Tuvimos problemas para poder visualizar tu mapa')
            else:
                update.message.reply_text('Parece que no tienes ningun cajero cercano. Prueba con otra ubicacion')
        else:
            update.message.reply_text('La aplicacion solo funciona para localidades de CABA. Porfavor, ingresa una nueva ubicacion')    
    
    #Help: Tells the user how to send their location
    def help(self, update: Update,context: CallbackContext):
        update.message.reply_text("""Para comenzar, tenes que enviarme tu ubicacion. Para esto, toca el simbolo de Clip en la barra de mensaje y ve a 
                                    la pestaña que dice Ubicacion.""")
    #Unknow comands
    def unknown(self, update: Update,context: CallbackContext):
        update.message.reply_text("Disculpa, eso no es un comando valido")
  
    #Unkown messages
    def unknown_text(self, update: Update,context: CallbackContext):
        update.message.reply_text("Disculpa, eso no lo se!")

#Initialize Bot Function: With the KD Tree created and the ATM dataset, they are loaded into the Bot class and then
#used inside the Bot functions

def initialize_bot(tree,atm_list):
    bot = Updater(BOT_API_KEY,use_context=True)
    bot_functions = MyBot(tree,atm_list,bot)
    
    bot.dispatcher.add_handler(CommandHandler('start', bot_functions.start))
    bot.dispatcher.add_handler(CommandHandler('ayuda', bot_functions.help))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, bot_functions.unknown_text))
    bot.dispatcher.add_handler(MessageHandler( Filters.command, bot_functions.unknown))  # Filters out unknown commands
    bot.dispatcher.add_handler(MessageHandler(Filters.location,bot_functions.getLocation,pass_user_data=True))

    bot.start_polling()
    bot.idle()
