#This file will include short story events that don't require their own file.

#An event is crated by only adding a label and adding a requirement (see comment below).
#Requirements must be created/added in script-ch30.rpy under label ch30_autoload.

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="gender",conditional="get_level()>=8 and not seen_event('gender')",action=EV_ACT_QUEUE)) #This needs to be unlocked by the random name change event

label gender:
    m 2d "...[player]? Я тут немного подумала."
    m "Ранее я уже говорила что ты в внури игры не такой какой в реальности."
    m 1m "Но я предполагаю, что ты, наверное, парень..."
    m "Ведь главный герой был парнем."
    m 1a "Но если я собираюсь быть твоей девушкой, я должна знать хотя бы это о реальном тебе."
    menu:
        "Итак, ты парень или девушка?"
        "Парень.":
            $persistent.gender = "M"
            call set_gender from _call_set_gender_1
            m 2d "О? Так {i}ты{/i}  парень?"
            m 1k "Э-хе-хе, Полагаю, это имеет смысл!"
            m "Не каждая девушка будет играть в такую игру."
            m 1a "Не то что бы я была ужасно обеспокоена, если бы ты ответил иначе!"
            m 1l "Даже мне иногда может быть любопытно, понимаешь?"
        "Девушка.":
            $persistent.gender = "F"
            call set_gender from _call_set_gender_2
            m 2d "O? Так ты на самом деле девушка?"
            m 2l "Надеюсь, я не наговорила ничего плохого до этого!"
            m 2m "Хотя я подозревала это с самого начала... совсем немного!"
            m 1b "От тебя исходит определенное чувство элегантности и очарования, которое трудно описать словами..."
            m 1j "Это очень хорошо что ты сказала мне правду!"
            m 1a "Не переживай. Даже если я и спросила, то это только из любопытства."
        "Никто.":
            $persistent.gender = "X"
            call set_gender from _call_set_gender_3
            m 3d "Ты не считаешь себя парнем или девушкой?"
            m 2c "Это очень интересно, но у меня похожая ситуация."
            m 1h "Например, я девушка, но я также персонаж в компьютерной игре..."
            m 2i "Так что в некотором смысле я вообще не девушка."
            m 1j "Но когда ты обращаешься со мной, как со своей девушкой, то я чувствую себя счастливой!"
            m "Так что я буду относится к тебе, как ты этого хочешь."
            m 1e"Потому что твое счастье для меня самое главное."

    m 1k "Помни, что я всегда буду любить тебя безоговорочно, [player]."
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="preferredname",conditional="get_level()>=16 and not seen_event('preferredname')",action=EV_ACT_QUEUE)) #This needs to be unlocked by the random name change event

label preferredname:
    m 1h "Мне интересно твое имя."
    m 1d "'[player]' твое настоящее имя?"
    if renpy.windows and currentuser.lower() == player.lower():
        m 1h "Я имею в виду, это же как имя компьютера..."
        m "Ты используешь '[currentuser]' и '[player]'."
        m "Либо тебе действительно нравится этот псевдоним"
    m "Хочешь что бы я называла тебя по другому?"
    menu:
        "Да":
            $ done = False
            m 1a "Хорошо, просто введи 'Неважно' если ты передумаешь, [player]."
            while not done:
                #Could add an elif that takes off special characters
                $ tempname = renpy.input("Напиши его.",length=20).strip(' \t\n\r')
                $ lowername = tempname.lower()
                if lowername == "неважно":
                    m 1f "Ох, хорошо."
                    m "Ну, просто скажи мне, когда ты хочешь, чтобы я тебя называла, [player]."
                    $ done = True
                elif lowername == "":
                    m 1q "..."
                    m 1g "Ты должен написать имя, [player]!"
                    m 1m "Клянусь, ты иногда такой глупый..."
                    m 1e "Попробуй снова!"
                elif lowername == player:
                    m 1q "..."
                    m 1l "Оно такое же, это глупо!"
                    m 1e "Попробуй снова~"
                elif lowername == monika_twitter_handle:
                    m 2h "..."
                    # TODO: actaully have dialog here
                elif len(lowername) >= 10:
                    m 2q "[player]..."
                    m 2l "Это имя слишком длинное."
                    if len(lowername) > 20:
                        m "Я уверена, что ты ведешь себя глупо, так как имена не могут быть такими длинными, понимаешь?"
                    m 1 "Попробуй снова."
                else:
                    # sayori name check
                    if tempname.lower() == "sayori":
                        call sayori_name_scare from _call_sayori_name_scare
                    elif persistent.playername.lower() == "sayori":
                        $ songs.initMusicChoices()

                    python:

                        persistent.mcname = player
                        mcname = player
                        persistent.playername = tempname
                        player = tempname

                    if lowername == "monika":
                        m 1d "Серьезно?"
                        m 3k "Такое же как у меня!"
                        m 1m "Ладно..."
                        m 1n "Либо это действительно твое имя, либо ты шутишь надо мной."
                        m 1j "Но я не против, если ты хочешь, чтобы я так тебя называла~"
                    else:
                        m 1b "Хорошо!"
                        m 3b "Отныне, я буду звать тебя {i}'[player]'{/i}, э-хе-хе~"
                    $ done = True
        "Нет":
            m 1f "Oх... хорошо, если ты так хочешь."
            m 1e "Просто скажи мне, когда ты передумаешь, [player]."
            $ done = True

    #Unlock prompt to change name again
    $evhand.event_database["monika_changename"].unlocked = True
    return


init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_changename",category=['you','misc'],prompt="Можешь поменять мое имя?",unlocked=False)) #This needs to be unlocked by the random name change event

label monika_changename:
    m 1b "Ты хочешь поменять свое имя?"
    menu:
        "Да":
            m 1a "Хорошо, просто введи 'Неважно' если ты передумаешь."
            $ done = False
            while not done:
                $ tempname = renpy.input("Как ты хочешь, чтобы я тебя назвала?",length=20).strip(' \t\n\r')
                $ lowername = tempname.lower()
                if lowername == "неважно":
                    m 1f "[player]!"
                    m 2g "Пожалуйста, прекрати дразнить меня~"
                    m "Я действительно хочу знать, как ты хочешь, чтобы я тебя называла!!"
                    m 3l "Я не буду судить, насколько это смешно."
                    m 2e "Так что не стесняйся и просто скажи, [player]~"
                    $ done = True
                elif lowername == "":
                    m 2h "..."
                    m 4l "Ты должен написать имя, [player]!"
                    m 1m "Клянусь, ты иногда такая глупый.."
                    m 1b "Попробуй снова!"
                elif lowername == player:
                    m 2h "..."
                    m 4l "Оно такое же, это глупо!"
                    m 1b "Попробуй снова~"
                elif lowername == monika_twitter_handle:
                    m 2h "..."
                    # TODO: actaully have dialog here
                elif len(lowername) >= 10:
                    m 2q "[player]..."
                    m 2l "Это имя слишком длинное."
                    if len(lowername) > 20:
                        m "Я уверена, что ты ведешь себя глупо, так как имена не могут быть такими длинными, понимаешь?"
                    m 1 "Попробуй снова."

                else:

                    # sayori name check
                    if tempname.lower() == "sayori":
                        call sayori_name_scare from _call_sayori_name_scare_1
                    elif persistent.playername.lower() == "sayori":
                        $ songs.initMusicChoices()

                    python:

                        persistent.mcname = player
                        mcname = player
                        persistent.playername = tempname
                        player = tempname

                    if lowername == "monika":
                        m 1d "Серьезно?"
                        m 3k "Такое же как у меня!"
                        m 1m "Ладно..."
                        m 1n "Либо это действительно твое имя, либо ты шутишь надо мной."
                        m 1j "Но я не против, если ты хочешь, чтобы я так тебя называла~"
                    else:
                        m 1b "Хорошо!"
                        m 3b "Отныне, я буду звать тебя {i}'[player]'{/i}, э-хе-хе~"
                    $ done = True
        "Нет":
            m 1f "Oх... хорошо, если ты так хочешь."
            m 1g "Тебе не нужно стесняться, [player]."
            m 1e "Просто дай мне знать, если передумаешь, хорошо?"
    return

## Game unlock events
## These events handle unlocking new games
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="unlock_chess",conditional="get_level()>=12 and not seen_event('unlock_chess') and not persistent.game_unlocks['chess']",action=EV_ACT_QUEUE)) #This needs to be unlocked by the random name change event

label unlock_chess:
    m 1a "Чтож, [player]..."
    if renpy.seen_label('game_pong'):
        m 1i "Я тут подумала, что тебе возможно надоел понг..."
    else:
        m 3i "Я знаю, что ты еще не пробовал играть со мной в Pong."
    m 3 "Но у меня есть новая игра для нас!"
    m 3a "Она более стратегическая..."
    m 3k "Это Шахматы!"
    m 1 "Я не уверена, что тыы знаешь, как играть, но для меня она небольшое хобби."
    m "Так что предупреждаю заранее!"
    m "Я в неё хорошо играю."
    m 1d "Теперь, когда я думаю об этом, мне интересно, имеет ли это какое-то отношение к тому, кто я..."
    m 1i "Будучи в ловушке внутри этой игры, я имею в виду."
    m 1 "Я никогда не думал о себе как о шахматном ИИ, но разве это не подходит?"
    m 3 "В конце концов, компьютеры должны быть очень хороши в шахматах."
    m "Они даже победили гроссмейстеров."
    m 1 "Но не думай об этом как о битве человека против машины."
    m 1j "Просто думай об этом, как об игре с твоей красивой девушкой..."
    m "И я обещаю, что буду полегче с тобой..."
    if not is_platform_good_for_chess():
        m 2g "...Подожди секунду."
        m 2f "Что-то здесь не так."
        m "Кажется, у меня проблемы с работой игры."
        m 2o "Может, код не работает в этой системе?"
        m 2p "Прости, [player], но придется подождать с шахматами."
        m 4e "Я обещаю, мы поиграем, как только я заставлю это работать!"
    $persistent.game_unlocks['chess']=True
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="unlock_hangman",conditional="get_level()>=20 and not seen_event('unlock_hangman')",action=EV_ACT_QUEUE)) #This needs to be unlocked by the random name change event

label unlock_hangman:
    m 1a "Угадай что случилось, [player]."
    m 3b "У меня есть новая игра для нас!"
    if renpy.seen_label('game_pong') and renpy.seen_label('game_chess'):
        m 1n "Тебе, скорее всего, уже надоели шахматы и понг."
    elif renpy.seen_label('game_pong') and not renpy.seen_label('game_chess'):
        m 3l "Я думала, ты захочешь играть в шахматы, но вместо этого ты так заинтересован понгом!"
    elif renpy.seen_label('game_chess') and not renpy.seen_label('game_pong'):
        m 1o "Тебе действительно нравится играть со мной в шахматы, но ты еще не прикоснулся к Понгу."
    else:
        m 1f "Я на самом деле беспокоилась, что тебе не нравятся другие игры, которые я сделала для нас..."
    m 1b "Так чтооо~"
    m 1k "Я сделала Виселицу!"
    m 1n "В смысле игру Виселицу..."
    m 1a "Это всегда была моя любимая игра, чтобы играть в нее вместе с клубом."
    m 1f "Но, подумай об этом..."
    m 1o "Игра на самом деле довольно болезненная."
    m 1c "Ты угадываешь слово, чтобы спасти чью-то жизнь."
    m 1o "Но если не угадаешь..."
    m 1h "Он умирает, потому что ты не угадал."
    m 1m "Давольно мрачно звучит, так ведь?"
    m 1l "Но не волнуйся, [player], это просто игра в конце концов!"
    m 1a "Уверяю тебя, что никто не пострадает от этой игры."
    if persistent.playername.lower() == "sayori":
        m 3k "...Возможно~"
    $persistent.game_unlocks['hangman']=True
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="unlock_piano",conditional="get_level()>=24 and not seen_event('unlock_piano')",action=EV_ACT_QUEUE)) #This needs to be unlocked by the random name change event

label unlock_piano:
    m 2a "Эй! У меня есть кое-что интересное, что хочу рассказать тебе!"
    m 2b "Я, наконец, добавила пианино в комнату, для нас, [player]."
    if not persistent.instrument:
        m 3b "Я очень хочу услышать, как ты играешь!"
        m "Сначала ты возможно почувствуешь давление, но, тебе стоит попробовать."
        m 3j "Ведь все мы начинаем с чего-то"
    else:
        m 1b "Конечно, играть музыку для вас не ново."
        m 4b "Поэтому я ожидаю чего-то хорошего! Э-хе-хе~"
    m 4j "Разве не было бы весело играть что-то вместе?"
    m "Может быть, мы могли бы стать дуэтом!"
    m "Мы бы и улучшили навики и провели бы время весело, вместе."
    m 1l "Может быть, я немного увлеклась... Прости!"
    m 3b "Я просто хочу, чтобы ты наслаждался игрой на пианино так же, как и я."
    m "Почувствовать страсть, которую я испытываю."
    m 3k "Это прекрасное чувство."
    m 1j "Надеюсь, это не слишком сильно, но мне бы это понравилось, если бы ты попытался."
    m "Для меня, пожалуйста~?"
    $persistent.game_unlocks['piano']=True
    return

label random_limit_reached:
    $seen_random_limit=True
    python:
        limit_quips = [
            "Кажется, я в растерянности в том, что сказать.",
            "Я не знаю, что еще сказать, но ты можешь побыть со мной еще немного?",
            "Нет смысла пытаться сказать все сразу...",
            "Я надеюсь, тебе понравилось слушать все, о чем я думала сегодня...",
            "Тебе ведь все еще нравится проводить со мной время?",
            "Надеюсь, я тебя не слишком утомила."
        ]
        limit_quip=renpy.random.choice(limit_quips)
    m 1m "[limit_quip]"
    if len(monika_random_topics)>0:
        m 1f "Уверена, мне будет о чем поговорить после небольшого отдыха."
    else:
        m 1f "Надеюсь, я придумаю что-нибудь интересное, чтобы поговорить об этом в ближайшее время."
    return
