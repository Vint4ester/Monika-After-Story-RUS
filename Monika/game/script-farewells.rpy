##This file contains all of the variations of goodbye that monika can give.
##Default behavior is to select a random farewell from the list, if the farewell
##is non-specific, it can stay available, but if it's too specific it should
##unset its own random flag.
##Label must start with "bye" to prevent being pushed back onto the stack if closed

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_leaving_already",random=True),eventdb=evhand.farewell_database)

label bye_leaving_already:
    m 1c "Оу, уже уходишь?"
    m 1e "Это очень грустно, когда тебе нужно идти..."
    m 3a "Просто не забудь вернуться как можно скорее, хорошо?"
    m "Я тебя люблю, [player]. Береги себя!"
    #Don't show this farewell again
    $evhand.farewell_database["bye_leaving_already"].random=False
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_goodbye",random=True),eventdb=evhand.farewell_database)

label bye_goodbye:
    m 1c "До свидания, [player]!"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_sayanora",random=True),eventdb=evhand.farewell_database)
    
label bye_sayanora:
    m 1j "Сайонара, [player]~"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_farewellfornow",random=True),eventdb=evhand.farewell_database)
    
label bye_farewellfornow:
    m 1e "Прощай, любовь моя~"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_untilwemeetagain",random=True),eventdb=evhand.farewell_database)

label bye_untilwemeetagain:
    m 2e "'{i}Прощание не навсегда, прощание не конец. Это просто означает, что я буду скучать по тебе, пока мы не встретимся снова.{/i}'"
    m "Э-хе-хе, до тех пор пока, [player]!"
    return 'quit'
