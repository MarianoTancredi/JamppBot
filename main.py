import bot
import atmreader

#Main Function: Loads for the first and only time the atm dataset for later usage. They are stored at a K Dimensional Tree. 
#It also inicializes the bot
def main():
    tree,atm_list = atmreader.atmArray()
    bot.initialize_bot(tree,atm_list)

main()