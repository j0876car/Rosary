import os

def sign_of_the_cross():
    _sign_of_the_cross = 'In the name of the Father, and of the Son, and of the Holy Spirt. Amen'
    print(_sign_of_the_cross)
    input('Hit Enter to continue to Apostle Creed!')

def Apostle_Creed():
    _Apostle_creed='''I BELIEVE in God, the father almighty, creator of heaven and earth.\n
    I believe in Jesus Christ, his only Son, our lord. He was conceived by the power of the\n
    Holy Spirit and born of the Virgin Mary. \n
    He suffered under Pontius Pilate, was crucified, died, and was buried. \n
    He descended to the dead. On the third day he rose again. \n
    He ascended into heaven, and is seated at the right hand of the Father. \n
    He will come again to Judge the living and the dead. \n
    I believe in the Holy Spirt, the Holy catholic Church, the communion of saints,\n
    the forgiveness of sins, the resurrection of the body, and the life everlasting\n
    Amen.
    '''
    print(_Apostle_creed)
    input('Hit Enter to continue to our Father!')
def Our_Father():
    _our_father='''Our Father, Who art in heaven Hallowed be Thy Name;\n
    Thy Kingdom come, Thy will be done, on earth as it is in heaven.\n
    Give us this day our daily bread, and forgive us our trespasses,\n
    as we forgive those who trespass against us, and lead us not into temptation,\n
    but deliver us from evil\n
    Amen'''
    print(_our_father)
    input('Hit Enter to continue to Hail Mary!')
def hail_mary_begin(count):
    counter = 1
    _hail_mary='''Hail Mary,full of grace. The Lord is with thee.\n
    Blessed art thou amongst woman, and blessed is the fruit of thy womb, Jesus.\n
    Holy Mary, Mother of God, pray for us sinners, now and the hour of our death\n
    Amen'''
    while counter < int(count):
        print(counter)
        print(_hail_mary)
        input('Hit Enter to continue:')
        os.system('cls')
        counter = counter + 1
def glory_be():
    _glory_be='''Glory be to the Father, and to the Son, and to the Holy Spirit\n
    as it was in the beginning, is now, and ever shall be, world without end\n
    Amen'''
    print(_glory_be.strip())
