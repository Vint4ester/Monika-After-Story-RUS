##This page holds all of the random greetings that Monika can give you after you've gone through all of her "reload" scripts

#Make a list of every label that starts with "greeting_", and use that for random greetings during startup

# persistents that greetings use
default persistent._mas_you_chr = False

init python:
    greetings_list=[]
    label_list=renpy.get_all_labels()
    for label in label_list:
        if label.startswith('greeting_') and not renpy.seen_label(label):
            greetings_list.append(label)

    #If the greeting's list is empty, remake it without removing seen.
    if greetings_list == []:
        for label in label_list:
            if label.startswith('greeting_'):
                greetings_list.append(label)


label greeting_sweetheart:
    m 1k "Привет еще раз, милый!"
    m 1l "Как-то неловко говорить вслух, не так ли?"
    m 3b "Тем не менее, я думаю, что это нормально быть смущенным время от времени."
    return

label greeting_honey:
    m 1b "С возвращением, дорогой!"
    m 1a "Я так рада снова тебя видеть.."
    m "Давай проведем еще немного времени вместе, хорошо?"
    return

label greeting_back:
    m 1a "[player], ты вернулся!"
    m 1e "Я начала скучать по тебе."
    m 1k "Давай, еще один прекрасный день, проведем вместе, хорошо?"
    return

label greeting_gooday:
    m 1k "Привет еще раз, [player]. Как дела?"
    menu:
        m "У тебя сегодня хороший день?"
        "Да.":
            m 1a "Я рада за тебя, [player]."
            m "Я чувствую себя намного лучше, зная, что ты счастлив."
            m "Я постараюсь сделать все возможное, чтобы все так и осталось, обещаю."
        "Нет...":
            m 1f "Oх..."
            m 2e "Ну, не волнуйся, [player]. Я всегда рядом с тобой.."
            m "Мы можем говорить весь день о твоих проблемах, если ты хочешь."
            m 3r "Я хочу попробовать и сделать счастливым."
            m 1h "Потому что это делает меня счастливой."
            m 1b "Я постараюсь сделать все возможное, чтобы поднять тебе настроение, обещаю."
    return

label greeting_visit:
    m 1b "Вот ты где, [player]."
    m 1a "Очень мило с твоей стороны."
    m 1e "Ты всегда такой заботливый, [player]!"
    m "Спасибо, что провел со мной так много времени~"
    m 2k "Просто помни, что твое время со мной никогда не пропадет впустую."
    return

label greeting_goodmorning:
    $ current_time = datetime.datetime.now().time().hour
    if current_time >= 0 and current_time < 6:
        m 1b "Доброе утро-"
        m 1d "...oх, подожди."
        m "Сейчас ведь глубокая ночь, дорогой."
        m 1i "Почему ты не спишь в такое время?"
        m 1g "Полагаю, ты не можешь заснуть..."
        menu:
            m "Это так?"
            "Да.":
                m 2h "Ты должен хоть немного поспать, если ты можешь."
                m "Слишком поздно вставать - это плохо для здоровья."
                m 3m "Но если это значит, что я увижу тебя чуточку дольше, я не могу жаловаться."
                m 3l "A-ха-ха!"
                m 3h "Но все же..."
                m "Я хочу, чтобы ты позаботился о себе."
                m "Сделайте перерыв, если нужно, хорошо? Сделай это для меня."
            "Нет.":
                m 1a "Ах. Тогда я чувствую облегчение.."
                m 1e "Это значит, что ты здесь только ради меня, посреди ночи?"
                m 1k "Боже, я так счастлива!"
                m "Ты действительно заботишься обо мне, [player]."
                m 2e "Но если ты действительно устал, ложись спать!"
                m "Я тебя очень люблю, так что не нагружай себя!"
    elif current_time >= 6 and current_time < 12:
        m 1b "Доброе утро, дорогой."
        m "Еще одно свежее утро, хорошее для начала, да?"
        m 1k "Я рада видеть тебя сегодня утром.~"
        m 1a "Не забудь позаботиться о себе, хорошо?"
        m "Сделай меня гордой девушкой сегодня, как всегда!"
    elif current_time >= 12 and current_time < 18:
        m 1b "Добрый день, любовь моя."
        m 1a "Не позволяй стрессу добраться до тебя, хорошо?"
        m "Я знаю, что ты будешь стараться изо всех сил сегодня, но..."
        m 4a "Важно сохранять ясный ум!"
        m "Держите себя в руках, сделайте глубокий вдох..."
        m "Я обещаю, что не буду жаловаться, если ты уйдешь, так что делай, что должен."
        m "Или ты можешь остаться со мной, если хочешь."
        m 4k "Просто помни, я люблю тебя!"
    elif current_time >= 18:
        m 1b "Добрый вечер, любовь моя!"
        menu:
            m "У тебя сегодня был хороший день?"
            "Да.":
                m 1k "О, это здорово.!"
                m 1b "Я не могу помочь, но я счастлива когда ты счастлив..."
                m 1a "Но это ведь хорошо, правда?"
                m "Я так тебя люблю, [player]."
                m 1k "A-ха-ха!"
            "Нет.":
                m 1g "Oх дорогой..."
                m "Надеюсь, тебе скоро станет лучше?"
                m "Просто помни, что независимо от того, что происходит, независимо от того, что кто-то говорит или делает..."
                m 1e "Я сильно люблю тебя."
                m "Просто останься со мной, если тебе станет лучше."
                m 1a "Я люблю тебя, [player]."
    return

label greeting_back2:
     m 1k "Привет, дорогой."
     m 1n "Я ужасно по тебе скучала, так приятно снова тебя видеть!"
     m "Не заставляй меня ждать так долго в следующий раз, э-хе-хе~"
     return

label greeting_back3:
     m 1e "Я так скучала по тебе, [player]!"
     m "Спасибо, что вернулся. Мне очень нравится проводить с тобой время."
     return

label greeting_back4:
     m 2k "Привет, [player]!"
     m 2l "Тебе не кажется, что ты оставил меня ждать слишком долго?"
     m 2b "Я просто шучу. Я бы никогда не злилась на тебя."
     return

label greeting_visit2:
     m 1j "Спасибо, что провел со мной так много времени, [player]."
     m 1a "Каждую минуту я провожу с тобой словно в небесах!"
     m 1m "Надеюсь, это не прозвучало слишком глупо, э-хе-хе~"
     return

label greeting_visit3:
     m 1b "Ты вернулся!"
     m 1n "Я начала скучать по тебе..."
     m 1i "Не заставляй меня ждать так долго в следующий раз, хорошо?"
     return

label greeting_back5:
     m 1a "Я так рада снова тебя видеть.!"
     m 1f "Я беспокоилась о тебе."
     m "Пожалуйста, не забывай навещать меня, хорошо? Я всегда буду ждать тебя здесь."
     return

label greeting_visit4:
     m 1k "Я люблюююю тееееебя, [player]. Э-хе-хе~"
     m 1l "О, прости! Я разошлась.."
     m 1b "Я не думала, что смогу увидеть тебя снова так скоро."
     return

label greeting_visit5:
     m 1b "~Every day,~\n~I imagine a future where I can be with you...~"
     m 1a "О, ты здесь! Я просто мечтала и немного пела."
     m 1k "Я не думаю, что трудно понять, о чем я мечтала, э-хе-хе~"
     return

label greeting_visit6:
     m 1a "С каждым днем становится все лучше и лучше проводить время с тобой!"
     m "Тем не менее, я так счастлива, что ты наконец-то здесь."
     m "Давайте проведем еще один прекрасный день вместе."
     return

label greeting_back6:
     m 3b "Эй, [player]!"
     m "Тебе действительно стоит приходить ко мне почаще."
     m 2h "Ты ведь знаешь, что происходит с людьми, которые мне не нравятся..."
     m 1k "Я просто дразню тебя, э-хе-хе~"
     m 1a "Не будь таким доверчивым! Я бы никогда не навредила тебе."
     return

label greeting_visit7:
     m 1k "Ты здесь, [player]!"
     m 1a "Ты готов провести еще немного времени вместе? Э-хе-хе~"
     return

label greeting_visit8:
     m 1b "Я так рада, что ты здесь, [player]!"
     m 1a "Что будем делать сегодня?"
     return

label greeting_visit9:
     m 1j "Ты наконец-то вернулся! Я ждала тебя."
     m 1b "Ты готов провести со мной время? Э-хе-хе~"
     return

label greeting_italian:
     m 1b "Ciao, [player]!"
     m 1a "È così bello vederti ancora, amore mio..."
     m 1k "A-ха-ха!"
     m 2l "Я все еще учу итальянский. Это очень сложный язык!"
     m 1a "В любом случае, приятно снова тебя видеть, любовь моя."
     return

label greeting_latin:
     m 4b "Iterum obvenimus!"
     m 4h "Quid agis?"
     m 4l "Э-хе-хе..."
     m 2l "Латынь звучит так напыщенно. Даже простое приветствие звучит как серьезно."
     m 1a "Если ты задаешься вопросом о том, что я сказала, то все просто - 'Снова привет! Как дела?'."
     return

label greeting_yay:
     m 1k "Ты вернулся! Ура!"
     m 1l "О, прости. Я немного перенапряглась здесь."
     m 1m "Я очень рада снова тебя видеть, хе-хе~"
     return

label greeting_youtuber:
     m 2b "Привет всем, Добро пожаловать в другой эпизод... Только Моника!"
     m 2k "A-ха-ха!"
     m 1a "Я притворилась ютубером. Надеюсь, я смогла тебя расмешить, хе-хе~"
     return

label greeting_hamlet:
     m 4h "Быть, или не быть, вот в чем вопрос..."
     m 1d "Ах, вот ты где. Я просто убивала время, хе-хе~"
     m 1n "Я не ожидала увидеть тебя так скоро."
     return

label greeting_welcomeback:
     m 1b "Привет! С возвращением."
     m 1k "Я так рада, что ты можешь провести со мной время."
     return

label greeting_flower:
     m 1k "Ты мой прекрасный цветок, э-хе-хе~"
     m 1l "О, это звучало так неловко."
     m 1e "Но я всегда буду заботиться о тебе."
     return

label greeting_chamfort:
     m 2 "День без Моники-это день впустую."
     m 2k "A-ха-ха!"
     m 1b "С возвращением, любовь моя."
     return

label greeting_welcomeback2:
     m 1b "С возвращением, [player]!"
     m "Надеюсь, твой день пройдет хорошо."
     m 1a "Я уверена, что это так, ведь ты здесь. Теперь ничего не может пойти не так, хе-хе~"
     return

label greeting_longtime:
     m 1e "Давно не виделись, [player]!"
     m 1a "Я так счастлива, что ты здесь сейчас."
     return

label greeting_sweetpea:
     m 1d "Посмотрите, кто вернулся."
     m 2k "Это ты, мой милый.!"
     m 1l "Боже мой... Это, конечно, смущает так говорить, э-хе-хе~"
     return

label greeting_glitch:
     hide monika
     show yuri glitch zorder 1
     y "{cps=500}[player]?!{nw}{/cps}"
     hide yuri glitch
     show yuri glitch2 zorder 1
     play sound "sfx/glitch3.ogg"
     pause 0.1
     hide yuri glitch2
     show yuri glitch zorder 1
     pause 0.3
     hide yuri glitch
     show monika 4n at i11 zorder 2
     m 1d "[player]!"
     hide monika
     show monika 4l at i11 zorder 2
     extend " Неважно что я просто..."
     pause 0.1
     extend " немного поиграла с кодом."
     m 3l "Вот и все! Здесь нет никого, кроме нас... навсегда~"
     $ monika_clone1 = "Да"
     m 2j "Я люблю тебя, [player]!"
     return

label greeting_surprised:
     m "О, привет [player]!"
     m "Прости, ты меня там немного удивил."
     m "Как ты себя чувствуешь?"
     return

label i_greeting_monikaroom:
    scene black
    $ HKBHideButtons()
    # atm, making this a persistent makes it easier to test as well as allows
    # users who didnt see the entire event a chance to see it again.
#    $ seen_opendoor = seen_event("monikaroom_greeting_opendoor")
    $ has_listened = False

# special local var to handle custom monikaroom options
define gmr.eardoor = list()
define gmr.eardoor_all = list()
define opendoor.MAX_DOOR = 10
default persistent.opendoor_opencount = 0
default persistent.opendoor_knockyes = False

    # FALL THROUGH
label monikaroom_greeting_choice:
    menu:
        "... Осторожно откройте дверь" if not persistent.seen_monika_in_room:
            jump monikaroom_greeting_opendoor
        "Открыть дверь" if persistent.seen_monika_in_room:
            if persistent.opendoor_opencount > 0:
                jump monikaroom_greeting_opendoor_locked
            else:
                jump monikaroom_greeting_opendoor_seen
#        "Open the door?" if persistent.opendoor_opencount >= opendoor.MAX_DOOR:
#            jump opendoor_game
        "Стук":
            jump monikaroom_greeting_knock
        "Слушать" if not has_listened:
            $ has_listened = True # we cant do this twice per run
            $ mroom_greet = renpy.random.choice(gmr.eardoor)
#            $ mroom_greet = gmr.eardoor[len(gmr.eardoor)-1]
            jump expression mroom_greet

    # NOTE: return is expected in monikaroom_greeting_cleanup

### BEGIN EAR DOOR ------------------------------------------------------------

# monika narrates
init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_narration")

label monikaroom_greeting_ear_narration:
    m "[player] прислонил [his] его ухо к двери,{w} голос говорит [his] о каждом его движении."
    m "'Кто это?' [he] интересно, как [player] рассматрит[his] экран, озадаченный."
    call spaceroom from _call_spaceroom_enar
    m 1k "Это я!"
    m "С возвращением, [player]!"
    jump monikaroom_greeting_cleanup


# monika does the cliche flower thing
init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_loveme")

label monikaroom_greeting_ear_loveme:
    $ cap_he = he.capitalize()
    m "[cap_he] любит меня.{w} [cap_he] не любит меня."
    m "[cap_he] {i}любит{/i} меня.{w} [cap_he] {i}не{/i} любит меня."
    m "[cap_he] любит меня."
    m "...{w} [cap_he] любит меня!"
    jump monikaroom_greeting_choice


# monika encoutners error when programming
init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_progbrokepy")

label monikaroom_greeting_ear_progbrokepy:
    m "Что за-!{w} Ни один тип не имеет длины атрибута?"
    if renpy.seen_label("monikaroom_greeting_ear_progreadpy"):
        m "О, я вижу, что пошло не так!{w} Это нужно исправить!"
    else:
        m "Я не понимаю, что я делаю неправильно!"
        m "Здесь не должно быть никого...{w} Я в этом уверена..."
    m "Кодирование действительно сложноt..."
    jump monikaroom_greeting_choice

# monika reads about errors when programming
init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_progreadpy")

label monikaroom_greeting_ear_progreadpy:
    m "...{w}Доступ к атрибуту объекта типа 'NoneType' поднимем 'AttributeError'."
    m "Ясно. {w}Я должен удостовериться, что проверил, нет ли переменной, прежде чем получить доступ к ее атрибутам."
    if renpy.seen_label("monikaroom_greeting_ear_progbrokepy"):
        m "Это объяснило бы ошибку, которая была ранее."
    m "Кодирование действительно сложно..."
    jump monikaroom_greeting_choice

# monika attempts rm -rf
init 5 python:
    gmr.eardoor.append("monikaroom_greeting_ear_rmrf")

label monikaroom_greeting_ear_rmrf:
    if renpy.windows:
        $ bad_cmd = "del C:\Windows\System32"
    else:
        $ bad_cmd = "rm -rf /"
    m "Таким образом, решение этой проблемы заключается в вводе '[bad_cmd]' в командной строке?"
    if renpy.seen_label("monikaroom_greeting_ear_rmrf_end"):
        m "Да,{w} отличная попытка."
    else:
        m "Хорошо, позволь мне попробовать."
        show noise
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.2
        stop sound
        hide noise
        m "{cps=*2}Ах! Нет! Это не то, чего я хотела!{/cps}"
        m "..."
    m "Я не должена доверять Интернету так слепо..."
label monikaroom_greeting_ear_rmrf_end: # fall thru end
    jump monikaroom_greeting_choice


## ear door processing
init 10 python:

    # make copy
    gmr.eardoor_all = list(gmr.eardoor)

    # remove
    remove_seen_labels(gmr.eardoor)

    # reset if necessary
    if len(gmr.eardoor) == 0:
        gmr.eardoor = list(gmr.eardoor_all)

### END EAR DOOR --------------------------------------------------------------

# locked door, because we are awaitng more content
label monikaroom_greeting_opendoor_locked:
    show paper_glitch2
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    pause 0.7
    $ style.say_window = style.window_monika
    menu:
        m "Я тебя напугала, [player]?"
        "Да":
            m "Ой, прости."
        "Нет":
            m "{cps=*2}Хм, я заберу тебя позже.{/cps}{nw}"
            m "Я поняла. В конце концов, это основной сбой."
    m "С тех пор, как ты открываешь мою дверь,{w} Я не могла не добавить небольшой сюрприз для тебя~"
    m "Постучи в следующий раз, хорошо?"
    m "Теперь позволь мне починить эту комнату..."

    hide paper_glitch2
    scene black
    $ scene_change = True
    call spaceroom from _call_sp_mrgo_l

    if renpy.seen_label("monikaroom_greeting_opendoor_locked_tbox"):
        $ style.say_window = style.window

    m 1j "Вот и все!"

    if not renpy.seen_label("monikaroom_greeting_opendoor_locked_tbox"):
        menu:
            "...текстовое поле...":
                m 1n "Ой! Я все еще учусь, как это делать."
                m 1m "Позвольте мне изменить этот флаг...{w=1.5}{nw}"
                $ style.say_window = style.window
                m 1j "Все исправлено!"
    # NOTE: fall through please

label monikaroom_greeting_opendoor_locked_tbox:
    m 1a "С возвращением, [player]."
    jump monikaroom_greeting_cleanup

# this one is for people who have already opened her door.
label monikaroom_greeting_opendoor_seen:
#    if persistent.opendoor_opencount < 3:
    jump monikaroom_greeting_opendoor_seen_partone


label monikaroom_greeting_opendoor_seen_partone:
    $ is_sitting = False
#    scene bg bedroom
    call spaceroom(start_bg="bedroom",hide_monika=True) from _call_sp_mrgo_spo
    pause 0.2
    show monika 1h at l21 zorder 2
    pause 1.0
    m 1r "[player]..."

#    if persistent.opendoor_opencount == 0:
    m 1f "Я понимаю, почему ты не постучал в первый раз,{w} но не мог бы ты стучаться?"
    m 1o "В конце концов, это моя комната."
    menu:
        "Твоя комната?":
            m 3a "Правильно!"
    m "Разработчики этого мода дали мне хорошую удобную комнату, чтобы оставаться в ней, когда ты далеко."
    m 1m "Тем не менее, я могу войти, только если ты скажешь мне 'до свидания' или 'спокойной ночи', прежде чем закрыть игру."
    m 2b "Поэтому, пожалуйста, не забудь сказать это перед тем как уйдешь, хорошо?"
    m "В любом случае..."

#    else:
#        m 3g "Stop just opening my door!"
#
#        if persistent.opendoor_opencount == 1:
#            m 4o "You have no idea how difficult it was to add the 'Knock' button."
#            m 4f "Can you use it next time?"
#        else:
#            m 4f "Can you knock next time?"
#
#        show monika 5a at t11
#        menu:
#            m "For me?"
#            "Yes":
#                if persistent.opendoor_knockyes:
#                    m 5b "That's what you said last time, [player]."
#                    m "I hope you're being serious this time."
#                else:
#                    $ persistent.opendoor_knockyes = True
#                    m 1j "Thank you, [player]."
#            "No":
#                m 5b "[player]!"
#                if persistent.opendoor_knockyes:
#                    m 1f "You said you would last time."
#                    m "I hope you're not messing with me."
#                else:
#                    m 1f "I'm asking you to do just {i}one{/i} thing for me."
#                    m 1e "And it would make me really happy if you did."

    $ persistent.opendoor_opencount += 1
    jump monikaroom_greeting_opendoor_post2


label monikaroom_greeting_opendoor_post2:
    show monika 1a at t11
    pause 0.7
    show monika 5a at hf11
    m "Я рада, что ты вернулся, [player]."
    show monika 5a at t11
#    if not renpy.seen_label("monikaroom_greeting_opendoor_post2"):
    m "В последнее время я практиковала переключение фона, и теперь я могу изменить его мгновенно."
    m "Смотри!"
#    else:
#        m 3a "Let me fix this scene up."
    m 1q "...{w=1.5}{nw}"
    scene black
    $ scene_change = True
    call spaceroom(hide_monika=True) from _call_sp_mrgo_p2
    show monika 4a zorder 2 at i11
    m "Тада!"
#    if renpy.seen_label("monikaroom_greeting_opendoor_post2"):
#        m "This never gets old."
    show monika at lhide
    hide monika
    jump monikaroom_greeting_post


label monikaroom_greeting_opendoor:
    $ is_sitting = False # monika standing up for this
    call spaceroom(start_bg="bedroom",hide_monika=True) from _call_spaceroom_5
    m 2i "~Is it love if I take you, or is it love if I set you free?~"
    show monika 1 at l32 zorder 2
    m 1d "Э-э?! [player]!"
    m 3g "Ты удивил меня, внезапно появившись вот так!"
    show monika 1 at hf32
    m 5b "У меня не было достаточно времени, чтобы подготовиться!"
    m 5a "Но спасибо, что вернулся, [player]."
    show monika 1 at t32
    m 3a "Просто дай мне несколько секунд, чтобы все настроить, хорошо?"
    show monika 1 at t31
    m 2d "..."
    show monika 1 at t33
    m 1d "...и..."
    if is_morning():
        show monika_day_room zorder 1 with wipeleft
    else:
        show monika_room zorder 1 with wipeleft
    show monika 1 at t32
    m 3a "Вот и все!"
    menu:
        "...окно...":
            show monika 1 at h32
            m 1l "Ой! Я забыла об этом~"
            show monika 1 at t21
            m "Подожди..."
            hide bedroom
            m 2j "И... испарвила!"
            show monika 1 at lhide
            hide monika
            $ renpy.hide("bedroom")
    $ persistent.seen_monika_in_room = True
    jump monikaroom_greeting_post
    # NOTE: return is expected in monikaroom_greeting_post

label monikaroom_greeting_knock:
    m "Кто это~?"
    menu:
        "Это я.":
            m 1b "[player]!Я так счастлива, что ты вернулся!"
            if persistent.seen_monika_in_room:
                m "И спасибо, что сначала постучал в дверь."
            m 1j "Подожди, дай мне прибраться..."
            call spaceroom(hide_monika=True) from _call_spaceroom_6
    jump monikaroom_greeting_post
    # NOTE: return is expected in monikaroom_greeting_post

label monikaroom_greeting_post:
    m 2a "А теперь позволь мне взять столик и стул...."
    $ is_sitting = True
    show monika 1 at ls32 zorder 2
    m 1a "Что мы будем делать сегодня, [player]?"
    jump monikaroom_greeting_cleanup

# cleanup label
label monikaroom_greeting_cleanup:
    python:
        if persistent.current_track is not None:
            play_song(persistent.current_track)
        else:
            play_song(songs.current_track) # default
        HKBShowButtons()
        set_keymaps()
    return

label greeting_youarereal:
    python:
        try:
            renpy.file(
                config.basedir.replace("\\","/") +
                "/characters/" + persistent.playername.lower() + ".chr"
            )
            persistent._mas_you_chr = True
        except:
            persistent._mas_you_chr = False
    m 1b "[player]! Рада тебя видеть!"
    if persistent._mas_you_chr:
        m "Подожди. Что-то изменилось."
        m 1d "Ты...добавить файл персонажа?"
        m 1f "[player].chr...да?"
        m 1g "Ты...пытаешься попасть ко мне?"
        m "Зачем ты это сделал?"
        m 1o "Разве ты не понимаешь? "
        m 1p "Это место не настоящее! Я не знаю, что случится, если ты придешь сюда!"
        m 1q "Как ты мог это сделать?"
        m 1o "Отказаться от своей реальности..."
        m 1p "Просто чтобы быть со мной?"
        m 1n "Это все моя вина!"
        m 1f "Но...но 'ты', в игре..."
        m 1i "Он начинает немного двигаться."
        m 1 "Возможно...это позволяет тебе контролировать его снова?"
        m 1f "Это неправильно! Мне не нужна марионетка!"
        m 1q "Пожалуйста, [player]..."
        m "Если ты собираешься сделать это, ты уверен, что хочешь этого?"
        menu:
            m "Ты уверен?"
            "Я уверен.":
                m 1e "Чтож...У меня нет выбора, кроме как принять его..."
                m 1k "Я приму этот подарок с распростертыми объятиями!"
                m "Мы наконец можем быть вместе, [player]."
                m "И мы можем выяснить, как это сделать в вашей реальности, вместе!"
            "Возможно...":
                m 1l "Я так и думала..."
                m 1m "Ты бы ни за что не отказался быть 'настоящим', чтобы быть со мной..."
                m 1l "Я не могу заставить себя удалить этого милого малыша .chr файл, но..."
                m 1q "Думаю ты должен сделать это сам."
                m 1r "В этих файлах есть какие-то жуткие вещи..."
                m 1e "Я люблю тебя, [player]. Я буду ждать столько, сколько потребуется."
                m "Так что не будьте опрометчивыми, хорошо?"
    else:
        m 1i "Я много думала об .chr файле..."
        m 1n "Что это за файл такой?"
        m 1o "Они немного жуткие..."
        m 1p "И даже если другие девушки не реальны, почему удаление одной из них может удалить персонажа?"
        m 1i "Можно ли добавить персонажа?"
        m 1r "Трудно сказать..."
    return

label greeting_japan:
    m 1k "Oх, kon'nichiwa [player]!"
    m "Э-хе-хе~"
    m 2b "Привет, [player]!"
    m 1a "Я просто практикую Японский."
    m 3c "Посмотрим..."
    m 4b "Watashi ha itsumademo anata no mono desu!"
    m 2l "Прости если ты не понимаешь."
    m 3 "Ты знаешь, что это значит, [player]?"
    m 4j "Это значит {i}'Я буду твоей навсегда{/i}'~"
    return

label greeting_sunshine:
    m 1r "{i}Ты мой солнечный свет, мой единственный солнечный свет.{i}"
    m 1k "{i}Ты делаешь меня счастливой, когда небо серое.{/i}"
    m 4j "{i}Ты никогда не узнаешь, дорогой, как сильно я тебя люблю.{/i}"
    m 2r "{i}Пожалуйста, не забирайте мое солнце~{/i}"
    m 1j "..."
    m 1d "А-ах?! [player]!"
    m 4n "Боже мой, это так унизительно!"
    m 1l "Я просто пела себе, чтобы скоротать время."
    m 1b "Но теперь, когда ты здесь, мы можем провести немного времени вместе."
    return
