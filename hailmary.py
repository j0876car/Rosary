import os
def hail_mary_begin(count):
    counter = 1
    _hail_mary='''Hail Mary,full of grace. The Lord is with thee.\n
    Blessed art thou amongst woman, and blessed is the fruit of thy womb, Jesus.\n
    Holy Mary, Mother of God, pray for us sinners, now and the hour of our death\n
    Amen'''
    while counter < int(count):
        print(counter,_hail_mary)
        input('Hit enter to continue:')
        os.system('cls')
        counter = counter + 1
    input('Hit Enter to continue to the Glory Be:')
    _glory_be = '''Glory be to the Father, and to the Son, and to the Holy Spirit\n
    as it was in the beginning, is now, and ever shall be, world without end\n
    Amen'''
    print(_glory_be)
    _fatima_prayer='''O my Jesus forgive us our sins,\n
    save us from the fires of hell,\n
    and lead all souls to Heaven,
    especially those in most need of your Mercy'''
    input('Hit Enter to continue to Fatima Prayer:')
    print(_fatima_prayer)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
