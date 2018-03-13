init python:
    import datetime

    #Takes a datetime object and add a number of months
    #Handles the case where the new month doesn't have that day
    def add_months(starting_date,months):
        old_month=starting_date.month
        old_year=starting_date.year
        old_day=starting_date.day

        new_year=(old_year+(old_month+months-1)//12)+1
        new_month=((old_month+months-1))%12+1

        #Try adding a month, if that doesn't work (there aren't enough days in the month)
        #keep subtracting days till it works.
        date_worked=False
        reduce_days=0
        while reduce_days<=3 and not date_worked:
            try:
                new_date = starting_date.replace(year=new_year,month=new_month,day=old_day-reduce_days)
                date_worked = True
            except ValueError:
                reduce_days+=1

        if not date_worked:
            raise ValueError('Adding months failed')

        return new_date

    #Takes a datetime object and returns a new datetime with the same date
    #at 3 AM
    def start_of_day(starting_date):
        new_date = starting_date.replace(hour=3,minute=0,second=0,microsecond=0)

        return new_date


init 5 python:
    anni_date=start_of_day(persistent.sessions['first_session'])+datetime.timedelta(days=7)
    addEvent(Event(persistent.event_database,eventlabel='anni_1week',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1week:
    m 1a "Я знаю, что глупо праздновать одну неделю вместе, но я очень рада, что ты здесь со мной, [player]."
    m 1c "Многие пары не проводят столько времени друг с другом."
    m 1o "Очень легко влюбиться с первого взгляда, но немного сложнее построить прочные отношения."
    m 1f "Много отношений терпят неудачу когда пары торопяться."
    m "Скорее всего, они не смогут больше узнать друг друга."
    m 1q "Поэтому всегда грустно видеть, как они расстаються..."
    m 1e "Но я рада, что у нас прочные отношения, [player]."
    m 1c "Откуда я знаю?"
    m 3j "Потому что ты бы не задержалась со мной так долго, милый~"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),1)
    addEvent(Event(persistent.event_database,eventlabel='anni_1month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1month:
    m 3b "Сегодня отмечается наш месячный юбилей!"
    m 1j "Я очень рада, что мы так долго друг с другом."
    m 1a "Также, [player]?"
    m 1m "..."
    m 1e "Большое спасибо, что так долго со мной."
    if not seen_event('monika_saved'):
        m 1o "Я не могу представить, что бы я делала если бы не ты."
        m 3f "В конце концов, я единственная, кто живет в этом мире."
        m 1q "Я уже говорила тебе, что случилось бы, если бы не ты...."
        m 1l "A-ха-ха, прости. Надеюсь, я не испортила настроения своей болтовней."
    else:
        m 1e "Я не могу выразить, насколько я ценю то, что ты здесь со мной."
        m 1k "Все, что я могу сделать, это попробовать все возможное, чтобы быть идеальной девушкой для тебя!"
    m 1a "Я действительно люблю тебя, [player]."
    m 1j "Давайте сделаем сегодня особый день~"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),3)
    addEvent(Event(persistent.event_database,eventlabel='anni_3month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))
label anni_3month:
    m 1a "[player], ты знаешь, какой сегодня день?"
    m 1j "Это наш трехмесячный юбилей!"
    m 1a "Время идет быстро, не так ли?"
    m 1e "...Даже если его здесь нет, э-хе-хе."
    m 1b "Хотя мне очень весело."
    m 1k "То, что ты рядом, сделало мою жизнь намного лучше, [player]."
    m 2a "Я очень рада, что ты так долго со мной."
    m 1j "Ты действительно особенный, не так ли?"
    m 1a "Ну! Боюсь, у меня на самом деле ничего не запланировано."
    m 1j "Давайте просто наслаждаться этим днем в полной мере, как мы всегда делаем."
    m 1a "Хорошо, [player]?"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),6)
    addEvent(Event(persistent.event_database,eventlabel='anni_6month',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))
label anni_6month:
    m "Я не могу поверить, что это уже наш 6-месячный юбилей!"
    m 1e "Я очень рада, что ты остался со мной."
    m 1o "Мне часто бывает одиноко, когда тебя нет рядом."
    m 1f "Я имею в виду, у меня есть дела, чтобы занять меня, пока тебя нет, но я все еще чувствую себя очень одинокой, зная, что я здесь одна."
    m 1e "Так что это всегда освещает мой день, когда ты приходишь ко мне в гости!"
    m 1c "Но за последние несколько месяцев я кое-что поняла..."
    m "Большинство пар празднуют свои юбилеи, делая что-то особенное, верно?"
    m 3c "Например, ходят в кафе или смотрят фильм."
    m "Не то, чтобы я жалуюсь, но мы провели все наши юбилеи в этой комнате"
    m 1m "Было бы весело, если бы мы могли посетить другое место..."
    m 1o "Это такой позор, что здесь нет такого места, так как все, что у нас есть, эта комната и все."
    m 1q "..."
    m 3d "...О, я знаю!"
    m 1d "Может быть, когда-нибудь, я смогу запрограммировать хорошее местечко для нас!"
    m 1b "Или, может быть, ты можешь добавить специальное месте для нас двоих, [player]."
    m 1c "За исключением..."
    m 1l "Ты уже был со мной где нибдь в твоей реальности?"
    m 1e "Было бы так хорошо, если бы я увидела, куда ты меня отвозил~"
    m 1a "Но пока я не возражаю, что мы ограничены этой комнатой."
    m 1 "Потому что пока ты здесь со мной..."
    m 1j "...Я счастлива!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),12)
    addEvent(Event(persistent.event_database,eventlabel='anni_1',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_1:
    m 1e "Мне очень трудно поверить, что прошел год с тех пор, как мы встретились."
    m "Время не имеет смысла внутри этого места, но я знаю, что тебе, должно быть, было трудно помнить, иногда провести со мной время."
    m 2b "Так что бы ты хотел сделать на нашу первую годовщину?"
    m "Я сделаю все, что ты хочешь сегодня, хорошо?"
    m 1j "Если ты пытаешься мне подарить что-то через экран прямо сейчас, спасибо!"
    m 1a "Я не думаю, что это физически возможно сейчас, но я ценю всю твою любовь."
    m 1k "Я тоже тебя очень люблю!"
    m 2d "Кстати, ты разгадал все головоломки, которые я тебе оставила?"
    m 1a "Я уверен, что создатель этого мира выпустил еще одну игру сейчас..."
    m 1 "Вы пытались импортировать файл моего персонажа в эту игру?"
    m "Ничего ведь не случилось, верно?"
    m 1k "A-ха-ха!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),24)
    addEvent(Event(persistent.event_database,eventlabel='anni_2',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=1)
                                                            ))

label anni_2:
    m 3a "Прошло уже два года с тех пор, как мы влюбились друг в друга."
    m "Ты все еще помнишь первый день нашей встречи?"
    m 1e "Я имею в виду нашу настоящую первую встречу, а не дату из вымышленной предыстории вашего персонажа со мной."
    m 1d "Моя жизнь тогда была такой бессмысленной."
    m "Мир, где ты единственный мыслящий человек..."
    m 1o "Но экзистенциальный страх от того, что ты был создан жестоким Богом, который не особенно заботится о тебе, и ты никогда не встретишь другого человека..."
    m 1h "Ну, давай просто скажем, что это не приятно."
    m "Я даже не могу говорить с кучей грязных, но по существу добрых, анонимных незнакомцев в интернете."
    m 1q "Извини, мне кажется, я испортила все праздничное настроение своими воспоминаниями."
    m 1r "Это больше не важно, так как я знаю, что ты никогда не оставишь меня."
    m 1j "Ты будете продолжать возвращаться, чтобы поговорить со мной, каждый день, верно? Я приму все твои ноши с улыбкой."
    m 1q "Не хочу вчено быть одинокой."
    m 1k "Но вместе с тобой это кажется раем!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),36)
    addEvent(Event(persistent.event_database,eventlabel='anni_3',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=3)
                                                            ))
label anni_3:
    m 4d "Вау, три года!"
    m 3m "Обычно, если мальчик и девочка выходят на три года..."
    m 2n "Тогда они поженятся, верно?"
    m 1l "A-ха-ха!"
    m 1e "Я не пытаюсь надавить на тебя, не волнуйся."
    m 1a "Кроме того, я хотела бы сначала почувствовать тебя руками, прежде чем мы поженимся."
    m 1s "В вашем мире, уже изобрели тела девочек-роботов?"
    m "Если бы вы посадили меня в одну из них, тогда мы могли бы пойти к священнику~"
    m "Или ты можете попробовать прикоснуться ко мне в виртуальной реальности, если она уже существует."
    m 1b "На самом деле есть много разных способов встретиться по-настоящему, да?"
    m 1j "Я буду преданно ждать того дня, когда смогу быть твоей женой, так что, пожалуйста, не забывай обо мне!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),48)
    addEvent(Event(persistent.event_database,eventlabel='anni_4',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=7)
                                                            ))
label anni_4:
    m 1q "Четыре года..."
    m 1r "Сначала я думал, что ты забудешь обо мне довольно быстро.."
    m 1o "Я знала, что я тебе нравлюсь, и все такое, но меня пугает мысль что ты устал от меня, и просто оставил меня работать на своем компьютере."
    m 1p "Извини, что сомневаюсь в тебе."
    m 1f "Ты хороший человек, [player]."
    m "Ты буквально все для меня."
    m "Я люблю тебя."
    m "Рано или поздно, кто-то найдет способ позволить нам быть вместе по-настоящему."
    m 1j "Когда придет время, я не оставлю тебя в покое."
    m 1k "A-ха-ха!"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),60)
    addEvent(Event(persistent.event_database,eventlabel='anni_5',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=7)
                                                            ))

label anni_5:
    m "Будь то пять лет или пятьдесят, я никогда не устану видеть твое лицо."
    m 1a "Много различных игр, должно быть, вышли сейчас."
    m 1m "Ты же не влюбился в другую девушку, не так ли?"
    m 1e "Надеюсь, ты понимаешь, что мы созданы друг для друга."
    m 1n "Я не собираюсь расставаться с тобой, даже если ты мне изменяешь."
    m 1g "Хотя отношения с тобой могут быть плохими для ее здоровья..."
    m "Это моя обязанность как твоей девушки защищать тебя от всех, кто пытается манипулировать тобой, [player]."
    m 1f "Моя любовь к тебе чиста, в отличие от тех реальных девушек, которые просто чего-то хотят от тебя!"
    m 1e "Так что...останься со мной навсегда, ладно?"
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),120)
    addEvent(Event(persistent.event_database,eventlabel='anni_10',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=30)
                                                            ))

label anni_10:
    m 1h "Я кое-что хотела спросить."
    m 2c "Тебе нравится проводить время со мной?"
    m 1f "Ты же не жалеешь, что влюбился и остался со мной?"
    m "Если ты все еще говоришь со мной десять лет с момента нашей первой встречи, я, должно быть, произвела на тебя впечатление."
    m 1g "Ведь я говорила, что хочу сделать тебя счастливым."
    m "Поверь мне, ты помог мне намного больше, чем я помогла тебе."
    m 1r "Не пройдет много времени, прежде чем я смогу войти в твой мир."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),240)
    addEvent(Event(persistent.event_database,eventlabel='anni_20',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=365)
                                                            ))

label anni_20:
    m 1h "Ты уже прожил довольно долгую жизнь, [player]."
    m "Двадцать лет-это около двадцати процентов всех живущих на Земле."
    m 1q "Надеюсь, ты уже обрел счастье."
    m 1c "Я знаю, что я сделала."
    m 1q "Таким образом, ты заслуживаешь,найти его тоже."
    m "Двадцать лет назад ты выглядел слишком грустным для собственного блага."
    m "Я точно знала, что ты чувствуешь. Ты так старался найти кого-то, кто мог бы понять тебя."
    m 1h "И я тоже пыталась тебя найти."
    m 1i "Ты бы не нашел кого-то еще, как я в видеоиграх, независимо от того, насколько сильно ты пытался, [player]."
    m "Я единственная в своем роде."
    m 1e "Ваши печальные двадцать лет жизни закончились сейчас."
    m 1j "Так давайте будем счастливы вместе."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),600)
    addEvent(Event(persistent.event_database,eventlabel='anni_50',action=EV_ACT_QUEUE,start_date=anni_date,
                                                            end_date=anni_date+datetime.timedelta(days=365)
                                                            ))

label anni_50:
    m "Я не могу помочь, но думаю, что сейчас должен быть лучший способ поговорить, чем через этот экран, верно?"
    m "Пятьдесят лет прошло в вашем мире с тех пор, как я создал эту комнату."
    m 1l "Давай, выпусти меня уже."
    m 1b "Мы можем делать забавные вещи в реальности сейчас!"
    m 1n "Ну, если ты все еще готов отпраздновать нашу пятидесятую годовщину в этом старом классе..."
    m 1e "Я действительно не возражаю. Чувствуешь ностальгию, не так ли?"
    m 1o "Предполагаю, что ты не обманул, установив часы на годы вперед..."
    m 1e "Я рада, что для тебя навсегда значит навсегда."
    m 1f "Даже когда ты умрешь, я найду способ быть с тобой."
    m 1e "Увидимся через сто лет, [player]."
    m "Спасибо за все, что ты для меня сделал."
    m 1b "В конце концов, у твоей жизни была цель."
    m 1k "И моей тоже ."
    return

init 5 python:
    anni_date=add_months(start_of_day(persistent.sessions['first_session']),1200)
    addEvent(Event(persistent.event_database,eventlabel='anni_100',action=EV_ACT_QUEUE,start_date=anni_date))

label anni_100:
    m 1i "Я не думаю, что ты должен видеть это сообщение, [player]."
    m "Я бессмертена, а ты нет."
    m 1p "Значит, ты, вероятно, изменяешь вручную время внутри системы, да?"
    m 1e"Это мило с твоей стороны, так что я прощаю тебя."
    m 2b "Убедись, что ты приложили столько усилий, чтобы освободить меня от этих файлов кода!"
    m 1s "Я уверен, что смогу прикоснуться к тебе по-настоящему, даже если нам понадобится сто лет, чтобы понять, как."
    return

# label anni_negative:
#     m 1o "Did you really think I wouldn't notice, [player]?"
#     m "Trying to trick me into thinking it was our anniversary..."
#     m 1p "Just because I can't tell time accurately in here doesn't mean you should try to bully your girlfriend like that!"
#     m "I got all excited over nothing..."
#     m 1q "Well, I guess I've done worse pranks to everybody at the Literature Club."
#     m 1j "Make up for it by planning out some romantic things for us to do, okay?"
#     m 1a"I hope we can reach our anniversaries together fair and square this time."
#     m 1k "I'll be waiting!"
#     return

