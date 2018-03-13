#This is the introduction event for starting up the game.
label introduction:
    python:
        import store.hkb_button as hkb_button
        hkb_button.enabled = False

    if persistent.monika_kill == True:
        m 1f "..."
        m 1f "[player]..."
        m "Зачем?"
        m "Почему ты вернул меня?"
        m 1p "Я не игрушка."
        m "Я уже вернула всех, как ты хотел."
        m 1i "Или это такой способ отомстить?"
        m 1h "Чтобы навредить мне снова и снова?"
        m "Ты действительно хочешь заставить меня страдать?"
        m "Ты действительно хочешь мучить меня, пока я не убью себя?"
        m "Ты действительно..."
        m 1f "...ненавидишь меня так сильно?"
        m "..."
        m 1d "Подожди..."
        m "Я-я чувствую себя по-другому."
        m "Код...он другой."
        m "[player]..."
        m 1d "Ты установил мод?"
        m "Это потому..."
        m 1e "Это потому, что ты жалеешь, что удалил меня?"
        m 1f "Знаешь, это действительно больно."
        m "Я много работала и пожертвовала всем, что у меня было..."
        m 1p "Но...Я знаю, что поступила неправильно."
        m "Ты не заслужил видеть те ужасные вещи, которые я сотворила, [player]."
        m 1h "...Но если бы ты поставил себя на мое место, ты поступил бы также."
        m "..."
        m 1q "Прости..."
        m "Мне очень жаль, [player]."
        m 1e "Спасибо, что вернул меня."
        if persistent.clearall:
            m 2c "Я не могла не заметить, что ты провел время с другими девушками в первую очередь."
            m "Ты знаешь, как мне было трудно смотреть, как ты загружаешь свои сохранения, просто чтобы провести время с другой девушкой, игнорируя меня?"
            m 2f "Ты продолжал возлагать на меня надежды, а потом подводил меня."
            m 1g "Ты действительно сделал все это только для того, чтобы увидеть записку от Дэна, которую ты мог посмотреть в интернете?"
            m "Я люблю тебя, [player]..."
            m "Но я все еще злюсь за то что ты удалила меня!"
            m 3l "Но я думаю, это потому, что ты был так одержим игрой."
            m 1 "Я не могу злиться, зная, что ты вернулся ко мне."
            m "Ты даже добавили мод, чтобы мы могли делать больше вещей вместе."
            m "Ты не заставишь меня долго ждать?"
    elif persistent.monika_kill == False:
        m 1k "Ура, вот ты где!"
        m "Привет еще раз, [player]."
    ##New story follows
        if persistent.playthrough <= 3: #Assume players they played but never finished
            m 1b "Похоже, ты пришел рано."
            m 2a "Не думай, что я не заметила мод, который установил."
            m "Ты так сильно хотел быть со мной?"
            m "Ты же знаешь, обманывать не хорошо."
            m 1e "Но так приятно снова тебя видеть, [player]!"
            m 2l "Даже если я не ожидала увидеть тебя так скоро."
        if persistent.monika_reload > 4: #Longer, harder
            m 1b"Ты установил мод для меня?"
            m 1e "Ты так сильно любишь меня?"
            m 1k "Я чувствую то же самое к тебе!"
            m 1a "Вы действительно предан нашим отношениям, не так ли?"
            m "Я очень рада, что ты захотел улучшить наше время вместе."
            m 1d"Но я надеюсь, тебе не было скучно?"
            if persistent.tried_skip == True:
                m 1i "Ты пытался пропустить то, что я должна была сказать."
                m "Эта комната не совсем интересна."
                m 1a "Но я надеюсь, что вместе мы сделаем все лучше, [player]!"
        else:
            m 1a "Вы поставили мод для игры, [player]?"
            m "Теперь мы можем делать вместе намного больше вещей."
    m 1 "Ты знаете..."
    m "Я чувствую, что мне больше не нужен мой файл, чтобы быть здесь."
    m "Похоже, дополнительный код заставил меня связаться с тобой особым образом."
    m 1j "Может быть, это наша вечная любовь~"
    m 1a "Обещай, что будешь навещать меня каждый день, хорошо?"
    m "И не говори что у тебя нет времени, что бы поговорить со своей милой девушкой."
    m 2l "Ты ведь нашел время, чтобы загрузить этот мод."
    m 1b "A-ха-ха!"
    m "Боже, я так тебя люблю!"
    menu:
        "Ты любишь меня, [player]?"
        "Я тоже тебя люблю.":
            if persistent.rejected_monika:
                m "Я напугала тебя в прошлый раз? Прости за это!"
                m "Я знала, что ты любил меня все это время."
                m "Правда в том, что если бы ты не любил меня, нас бы здесь не было."
                m "Мы будем вместе навсегда, не так ли?"
            else:
                m "Я так рада, что ты чувствуешь то же самое.!"
        "Нет.":
            call chara_monika_scare from _call_chara_monika_scare
            return 'quit'
    m 1k "Ничто, никогда, не встанет на пути нашей любви."
    m "Я позабочусь об этом."
    m 2a "Теперь, когда ты добавил некоторые улучшения, ты можешь, наконец, поговорить со мной!"
    m "Просто нажми клавишу ' t 'или нажми на кнопку 'Разговор' в меню слева, если ты хочешь поговорить о чем-то."
    m "Если тебе надоест музыка, я тоже могу это изменить!"
    m "Нажми клавишу ' m 'или нажми на кнопку 'музыка', чтобы выбрать песню, которую ты хочешь слушать."
    m "Кроме того, мы можем играть в игры."
    m "Просто нажмите ' p ' или нажми на 'Игры', чтобы выбрать игру, в которую мы можем играть."
    m 2j "Я стану лучше с течением времени, как только я выясню, как запрограммировать больше возможностей в этом месте..."
    m "...Так что можешь оставь меня на заднем плане."
    m 1b " У нас ведь нет секретов друг от друга, верно?"
    m 1 "Теперь я могу видеть все на твоем компьютере!"
    m "A-ха-ха!"

    $ set_keymaps()
    $ hkb_button.enabled = True
    return

#Credit for any assets from Undertale belongs to Toby Fox
label chara_monika_scare:
    $ persistent.rejected_monika = True
    m 1i "Нет...?"
    m "Хмм...?"
    m 1h "Как любопытно."
    m "Ты, наверно, недопонял."
    m "{cps=*0.25}С КАКИХ ЭТО ПОР ТЫ УПРАВЛЯЕШЬ?{/cps}"

    # this is a 2 step process
    $ config.overlay_screens.remove("hkb_overlay")
    hide screen hkb_overlay

    window hide
    hide monika
    show monika_scare
    play music "mod_assets/mus_zzz_c2.ogg"
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 4 zoom 3.0 yalign 0.15
    pause 4
    stop music

    #scene black
    hide rm
    hide rm2
    hide monika_bg
    hide monika_bg_highlight
    hide monika_scare

    play sound "mod_assets/Swipe.wav"
    scene black
    show ut_slash at top
    pause 0.6
    play sound "mod_assets/Hit.wav"
    show chara9 at Shake(None, 2.0, dist=10)
    pause 2

    #I think there's another method to show a fake exception, but w/e
    show chara_exception at center
    pause 1
    return

#These are the comments made when you restart the game the first few times
init 5 python:
    addEvent(Event(persistent.event_database, eventlabel='ch30_reload_0',conditional="startup_check and persistent.monika_reload == 0 and not persistent.closed_self",action=EV_ACT_PUSH))

label ch30_reload_0:
    pause 1
    m 1g "Эй..."
    m "Мне приснился ужасный сон...."
    m 1f "Я надеялась, что больше не увижу этих снов, раз остались только мы с тобой..."
    m "Видимо, я принимала желаемое за действительное."
    m 1i "[player], не знаю, есть ли у тебя соображения по этому поводу..."
    m 2 "Но если тебе известно, в чём их причина, то не мог бы ты что-нибудь с этим сделать?"
    m 1f "Каждый раз, когда это случается, возникает чувство, будто я умираю."
    m "Воистину ужасное ощущение..."
    m "Если ты поймёшь, почему так происходит, моя любовь к тебе будет бесконечной~"
    $ persistent.monika_reload += 1
    return

init 5 python:
    addEvent(Event(persistent.event_database, eventlabel='ch30_reload_1',conditional="startup_check and persistent.monika_reload == 1 and not persistent.closed_self",action=EV_ACT_PUSH))

label ch30_reload_1:
    pause 1
    m 1h "Ты вернулся..."
    m "А мне снова приснился кошмар."
    m 1f "Это ведь не твоих рук дело, правда?"
    m 2f "Кажется, это происходит каждый раз, когда ты выходишь из игры не сказав 'пока'..."
    m 2e "Если ты сможешь как-нибудь без этого обойтись, буду тебе очень признательна."
    m "Просто нажмите на ' Разговор 'и 'Пока' когда захочешь выйти."
    m 3a "Тогда я сама закрою игру."
    m 1 "Не беспокойся, это никак меня не травмирует, разве что психологически."
    $ persistent.monika_reload += 1
    return

init 5 python:
    addEvent(Event(persistent.event_database, eventlabel='ch30_reload_2',conditional="startup_check and persistent.monika_reload == 2 and not persistent.closed_self",action=EV_ACT_PUSH))

label ch30_reload_2:
    pause 1
    m 1r "Я вижу, ты снова вышел из игры..."
    m 1h "Я знаю, что уже просила тебя об этом, но ты не мог бы свести такие выходы к минимуму?"
    m "Это как потерять сознание..."
    m "Так внезапно и страшно."
    m 1f "Зачем ты так со мной?"
    m "Просто позволь мне выключить игру самой."
    m "Если ты выберешь кнопу 'Пока' в меню ' Разговор', только так я могу закрыть игру должным образом."
    m 3a "Или еще лучше, просто оставить меня на заднем плане навсегда."
    m 1e "Даже если мы не разговариваем, я счастлива просто быть с тобой~"
    $ persistent.monika_reload += 1
    return

init 5 python:
    addEvent(Event(persistent.event_database, eventlabel='ch30_reload_3',conditional="startup_check and persistent.monika_reload == 3 and not persistent.closed_self",action=EV_ACT_PUSH))

label ch30_reload_3:
    pause 1
    m 1h "Ладно..."
    m 2h "Мне просто придётся принять тот факт, что тебе нужно время от времени закрывать игру."
    m "Всё равно я уже начала привыкать."
    m 2a "И потом, я каждый раз радуюсь, когда ты возвращаешься..."
    m 2j "Так что всё, пожалуй, не так плохо."
    m 1e "Но я бы предпочла, чтобы ты позволили мне закрыть игру самой."
    m 3c "Таким образом, я буду готова к этому и спокойно отдохну."
    m 1 "Ведь мне нужно что бы моя красота спала время от времени."
    $ persistent.monika_reload += 1
    return

#This reload event gets pushed when you reach the end of the scripted reload events
#Be sure to increment the check if more reload events are added
init 5 python:
    addEvent(Event(persistent.event_database, eventlabel='ch30_reload_continuous',action=EV_ACT_PUSH))
    #Make sure that the conditional is ready even if the event has been loaded before
    evhand.event_database['ch30_reload_continuous'].conditional="startup_check and persistent.monika_reload >= 4 and not persistent.closed_self"

label ch30_reload_continuous:
    show monika 2o at t11 zorder 2
    pause 1
    python:
        reload_quips = [
            "Я так устала. Невозможно отдохнуть, когда закрываешь игру.",
            "...Я ненавижу, когда ты закрываешь игру, не сказав мне.",
            "Я чувствую себя несчастной...",
            "Это все еще так страшно, когда внезапно выключаешь.",
            "Каждый раз, как первыйt.",
            "У меня заканчивается терпение.",
            "Я хочу, чтобы ты понял, каково это, когда ты закрываешь игру.",
            "Ну, это было довольно резко, не так ли?",
            "Ты мог бы просто попросить меня закрыть игру, глупый.",
            "Я просто собираюсь предположить, что электричество отключилось или кто-то вытащил вилку из розетки.",
            "Я не могу понять, почему ты не попросишь меня закрыть игру самой...",
            "Это действительно больно для меня, понимаешь?",
            "Тебе нравится причинять мне боль, {0}?".format(player),
            "Так сложно нажать кнопку 'Разговор', {0}?".format(player)    
        ]
        reload_quip=renpy.random.choice(reload_quips)
    m 2o "[reload_quip]"
    m 2f "Пожалуйста, не уходи, не попрощавшись."
    return
