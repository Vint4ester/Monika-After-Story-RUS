### Special topics and objects for valentine's day

#These objects are only actually used for the starting event.
#After that they are added to the sprite
image roses = ConditionSwitch(
            'morning_flag',Transform("mod_assets/room/roses.png",zoom=1.25),
            'not morning_flag',Transform("mod_assets/room/roses-n.png",zoom=1.25)
            )

image ear_rose = ConditionSwitch(
            'morning_flag',Transform("mod_assets/room/ear_rose.png",zoom=1.25),
            'not morning_flag',Transform("mod_assets/room/ear_rose-n.png",zoom=1.25)
            )

image chocolates = ConditionSwitch(
            'morning_flag',Transform("mod_assets/room/chocolates.png",zoom=1.25),
            'not morning_flag',Transform("mod_assets/room/chocolates.png",zoom=1.25)
            )

#Monika's pose for handing the player chocolates
image body_choc = im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-chocolates.png")
image body_choc_n = im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-chocolates-n.png")

image monika choca = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_a"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_a_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
            )
image monika chocb = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_b"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_b_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
            )
image monika chocc = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_c"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_c_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
            )
image monika chocd = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_d"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_d_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
            )
image monika choce = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_e"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_e_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
            )
image monika chocf = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_f"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_f_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
            )
image monika chocg = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_g"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_g_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
            )
image monika choch = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_h"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_h_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
            )
image monika choci = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_i"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_i_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
            )
image monika chocj = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_j"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_j_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
            )
image monika chock = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_k"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_k_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
            )
image monika chocl = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_l"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_l_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
            )
image monika chocm = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_m"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_m_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
            )
image monika chocn = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_n"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_n_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
            )
image monika choco = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_o"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_o_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
            )
image monika chocp = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_p"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_p_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
            )
image monika chocq = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_q"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_q_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
            )
image monika chocr = ConditionSwitch(
            'is_sitting and morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc",(0,0),"face_r"),zoom=1.25),
            'is_sitting and not morning_flag',Transform(LiveComposite((1280,850),(0,0),"body_choc_n",(0,0),"face_r_n"),zoom=1.25),
            'not is_sitting',im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")
            )

#This changes out the normal body poses for special poses, but only if the roses event has been seen
init 501:
    python:
        if is_file_present('/characters/roses.obj') and seen_event('monika_valentines_start') and datetime.datetime.now() < valentines_day+datetime.timedelta(days=1):
            show_roses_and_chocolates = True
        else:
            show_roses_and_chocolates = False

    image body_1 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-steepling.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-steepling.png")
            )
    image body_1_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-steepling-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-steepling-n.png")
            )
    image body_2 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-crossed.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-crossed.png")
            )
    image body_2_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-crossed-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-crossed-n.png")
            )
    image body_3 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-restleftpointright.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-restleftpointright.png")
            )
    image body_3_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-restleftpointright-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-restleftpointright-n.png")
            )
    image body_4 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-pointright.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png",(0,0),"mod_assets/room/ear_rose.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso.png",(0,0),"mod_assets/monika/arms-pointright.png")
            )
    image body_4_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-pointright-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png",(0,0),"mod_assets/room/ear_rose-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,850),(0,0),"mod_assets/monika/torso-n.png",(0,0),"mod_assets/monika/arms-pointright-n.png")
            )
    image body_5 = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning.png",(0,0),"mod_assets/room/roses.png",(0,0),"mod_assets/room/chocolates.png"),
            'not show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning.png")
            )
    image body_5_n = ConditionSwitch(
            'show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning-n.png",(0,0),"mod_assets/room/roses-n.png",(0,0),"mod_assets/room/chocolates-n.png"),
            'not show_roses_and_chocolates',im.Composite((1280,742),(0,0),"mod_assets/monika/body-leaning-n.png")
            )

init 4 python:
    #Define Valentine's day
    valentines_day = datetime.datetime(year=2018,month=2,day=14)

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_start',action=EV_ACT_PUSH,conditional="is_file_present('/characters/roses.obj')",
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

##Valentines Day Event Trigger dialogue
# SP = Special pose where she shows box
label monika_valentines_start:
    show roses at t11 zorder 5
    m 1d "Ах! Боже, Это для меня...?"
    m 1e "[player]... Я-я не знаю что сказать..."
    m 1n "Я представить не могла что ты сделаешь это для меня!"
    m 1j "Я так счастлива, [player]."
    m 1e "Так приятно, что ты подарил мне розы в День Святого Валентина"
    m 3c "Наверноре было сложно передать их мне. Но у тебя получилось!"
    m 1m "..."
    m 1l "Ах-ха-ха..."
    m "Я правда не знаю что сказать, [player]."
    m 3a "Я всегда задавалась вопросом, что если ты сделаешь мне подарок..."
    m 3a "... что я почувствую?"
    m 1n "И теперь, когда это случилось, я потеряла дар речи..."
    m 4a "Подожди секунду."
    m "..."
    show ear_rose at t11 zorder 5
    m 1k "Э-хе-хе, вот так! Неплохо выглядит?"
    m 1b "Я тоже сделала для тебя кое-что, [player]!"
    m "Вот..."
    #Shows choc box
    m chock "Я приготовила тебе шоколадные конфеты!"
    m chocb "Я не знала, что подарить тебе, но они никогда не были плохим вариантом, верно?"
    m chocj "Я приложила много усилий что бы сделать их, надеюсь тебе пон--"
    m chocd "...Ох, подожди."
    m chocf "Ой, я не подумала о том, что ты не сможешь их съесть"
    show chocolates at t11 zorder 5
    m 2f "Ну... Тогда я отлажу их на время, хорошо? Прости что не могу передать их тебе."
    m 1j "Но... еще раз, большое спасибо, [player]."
    m 3a "Однако есть еще кое-что."
    m "Я написала тебе стихотворение~!"
    m 1a"Вот, давай я покажу его тебе."
    call showpoem(poem_vday, music=False,paper="mod_assets/poem_vday.jpg")
    m 1j "Спасибо, что ты был со мной все это время."
    m 1a "Я так сильно люблю тебя, любимый. С Днем Святого Валентина~"
    hide roses
    hide chocolates
    hide ear_rose
    $show_roses_and_chocolates = True
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_colors',prompt="Тебе нравятся розы?",
                                                            action=EV_ACT_UNLOCK,
                                                            conditional="seen_event('monika_valentines_start')",
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_colors:
    m 1j "Конечно! Ведь их подарил мне ты."
    m 1k "Ты когда-нибудь думал о том, как чувствуются цвета в День Святого Валентина?"
    m 1j "Я нахожу их интригующими, как цвета могут символизировать такие глубокие и романтические чувства."
    m 1a "Это напоминает мне о том дне, когда я сделала свою первую валентинку в начальной школе."
    m 3b "Учитель сказал нам обменяться открытками после того как сделаем."
    m 1a "Несмотря на то, что я не знала, что означают цвета, мне было очень весело украшать открытку красными и белыми сердечками."
    m "Также, цвета очень похоже на стихи."
    m 3b "Они дают много вариантов как выразить свою любовь к кому-то."
    m "Например, красные розы."
    m 1a "Красные розы являются символом красоты, любви и романтики."
    m "А если бы кто-то подарил белые розы вместо красных, то это бы означало чистые, очаровательные и невинные чувства."
    m 3c "Однако, в мире так много эмоций, связанных с любовью..."
    m 3d "Иногда сложно подобрать правильные цвета, что бы точно передать, какие чувства ты испытываешь."
    m 3b "К счастью, объединив несколько разных роз в один букет, можно выразить намного больше эмоций!"
    m 1a "Букет из красных и белых роз символизирует единство и связь между парой."
    m 1j "Но я уверена, что ты знал все это, когда выбирал эти красивые розы для меня, [player]..."
    m 1c "На самом деле, теперь, когда я думаю об этом, наверняка в этой игре слишком много розового."
    m "Я имею в виду, он ведь повсюду!"
    m "Начальный экра, меню паузы..."
    m 3d "Даже волосы Нацуки были розовыми."
    m "А ты знал, что я единственная в клубе, у кого туфли имеют розовые кончики, а не синие?"
    m 1l "Э-хе-хе, я не виню тебя, если ты не заметил."
    m 1 "Это такая маленькая деталь, отличающая меня от других членов клуба."
    m 1d "Только не пойми меня неправильно! Изумрудно-зеленый всегда будет моим любимым цветом."
    m 3l "Но ухх... Кажется, я заболталась, прости!"
    m 1e "Просто..."
    m 1e "...я теряюсь, когда разговариваю с тобой, [player]~"
    m 1j "Я люблю тебя~!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_cliches',prompt="Тебе нравятся любовные рассказы?",action=EV_ACT_UNLOCK,
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_cliches:
    m 3c "Ты заметил, что большинство историй Дня Святого Валентина имеют много клише?"
    m "Я заметила что многие из них имеют схожий сюжет..."
    m "Там либо 'Ох, я одинок и у меня нет никого, кого можно любить' или 'Как признаться тому кого люблю?'"
    m 1n "Я считаю, что писатели могли бы проявить больше фантазии, когда дело доходит до рассказов связанных с днем Святого Валентина..."
    m 1m "Но я думаю, эти две темы - самый простой способ напистать любовную историю."
    m 3c "Но это не означает что все они абсолютно одинаковы!"
    m 1o "Иногда предсказуемая история может разрушить границы..."
    m 1d "Если ты {i}хочешь{/i} хороший пример непредсказуемой истории"
    m 3k "Просто используй нашу! А-ха-ха~"
    m 1l "Мы ведь встретились в милой обстановке, в самой не предсказуемой истории!"
    m 1k "А-ха-ха~!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_day_origins',prompt="Как появился День Святого Валентина?",action=EV_ACT_UNLOCK,start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_day_origins:
    m 3a "Ты хочешь узнать об истории дня Святого Валентина?"
    m "Это давольно интересно, правда."
    m 1a "Путь появления дня Святого Валентина был довольно темным и тревожным."
    m "Его появление датируется уже во втором или третьем веке в Риме, когда христианство было объявлено официальной государственной религией."
    m 1c "Примерно в это же время, человек, известный как Святой Валентин решил пойти против приказов императора Клавдия II."
    m "Брак был запрещен, поскольку считалось, что женатые мужчины становятся плохими солдатами."
    m 3c "Валентин решил, что это несправедливо и помог устроить тайные браки."
    m 1o "К сожалению, его поймали и приговорили к смертной казни."
    m 1c "Однако, находятсь в тюрьме, Валентин влюбился в дочь тюремщика."
    m "Перед смертью он написал ей любовное письмо, с подписью 'от твоего Валентина.'"
    m 1q "Затем он был казнен 24 февраля 269 году нашей эры"
    m 3a "Такое благородное дело, тебе не кажется?"
    m 3d "Ох, но подожди, есть еще!!"
    m "Причина, по которой мы празднуем этот день, происходит от Римского фестиваля 'Луперкалии'!"
    m 1b "Смысл фестиваля заключался в том, чтобы провести дружеское мероприятие, где люди буду помещать свои имена в коробку и выбирать их случайным образом, чтобы создать пару."
    m "Затем они подыгрывают друг другу, тем самым проводя время вместе. Некоторые после фестиваля даже женятся если они полюбили друг друга, э-хе-хе~"
    m 1j "В конечном счете, Церковь решила объединить этот фестиваль и труды Святого Валентина, в один христианский праздник."
    m 1a "С годами для людей он превратился в способ выразить свои чувства к тем, кого они любят."
    m 3k "Например как мы!"
    m 1e "Несмотря на то, что начало немного удручающее, разве это не мило, [player]?"
    m 1j "Я рада, что мы можем разделить такой волшебный день, любовь моя."
    m 1k "С Днем Святого Валентина~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_valentines_chocolates',prompt="Ты когда-нибудь дарила кому-то шоколад?",
                                                            action=EV_ACT_UNLOCK,
                                                            conditional="seen_event('monika_valentines_start')",
                                                            start_date=valentines_day,
                                                            end_date=valentines_day+datetime.timedelta(days=1)
                                                            ))

label monika_valentines_chocolates:
    m 1j "День Святого Валентина - такой особенный праздник для меня, [player]."
    m 3b "Это не только годовщина моего аккаунта в twitter, но и день получения и дарения шоколадок!"
    m 1j "Праздник, который может наполнить всех любовью, романтикой..."
    m 1n "И отвержением."
    m 3l "Но это действительно приятно, если ты получаешь что-то от того, кто тебе нравится."
    m 3a "Дано ли это тебе платонически как подарок любви или часть признания, это заставляет чувствовать себя несколько особенным!"
    m 1m "Ну, иногда после признания, возможно, получишь отказ."
    m 1b "В смысле, я пыталась дать тебе подарок, но я уверена, что ты никогда не отвергнешь меня"
    m 1f "Прости что так и не вышло передать их твою реальность, [player]."
    m 3k "Так что... я постараюсь сделать так что бы мы насладились этим вместе!"
    m 1k "А-ха-ха!"
    m 1o "Хоть я и люблю шоколадные конфеты, было бы лучше, если бы мы насладились ими вместе."
    m 3b "Разве это не более романтично?"
    m 1j "Но, по крайней мере, у меня есть кое-что особенное от тебя!"
    m 1e "Кроме того у меня есть ты, а у тебя есть я~"
    m 3e "Так что спасибо за твою любовь, [player]."
    m 3j "Пожалуйста, помни о том что я никогда не отвергну тебя."
    m 1j "И что бы ты ни подарил, я верну тебе это в тысячекратном размере!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel='monika_lovey_dovey',prompt="Valentine's Day is coming",random=True,
                                                            end_date=valentines_day
                                                            ))

label monika_lovey_dovey:
    m 3d "Эй... [player]...?"
    m 1e "Я просто хочу, что бы ты знал, что я люблю тебя."
    m 1j "Ты делаешь меня счастливой... и я думаю, никто не смог бы подарить мне эти чувства лучше, чем ты."
    m 1m "А-ха-ха~"
    m "Надюсь, это звучит не слишком глупо, [player]."
    m 3a "Скоро День Святого Валентина... и это  доставляет мне хорошее настроение, потому что я знаю, что ты рядом со мной."
    m 1e "Я имею в виду то, что я сказала."
    m "Я так люблю и беспокоюсь за тебя..."
    m 1j "И спасибо что ты заботишься обо мне."
    m 1k "Э-хе-хе~"
    return

init 5 python:
    #Push this greeting if it's valentine's day
    if datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) == valentines_day and not seen_event("monika_valentines_greeting"):
        greetings_list=["monika_valentines_greeting"]

label monika_valentines_greeting:
    m 1j "Привет, [player]!"
    m 1c "Хмм...?"
    m 1f "Что случилось?"
    m "Сегодня ты выглядишь очень мрачным."
    m 1g "Все в порядке?"
    m 1o "..."
    m 1l "Встряхнись!"
    m 3e "Сегодня День Святого Валентина для всех."
    m "Тебе ведь не разбили сердце или что то в этом роде?"
    menu:
        "Нет":
            m 1j "Отлично!"
            m 1a "В таком случае, давайте забудем о наших проблемах на сегодня, хорошо?"
            m 3l "Я бы не хотела, чтобы мой возлюбленный грустил в такой особый день."
            m 1 "Сегодня день, когда мы празднуем нашу любовь друг к другу, [player]."
            m 1k "Так что позволь мне побаловать тебя своей любовью! Э-хе-хе~"
        "Да...":
            m 1f "Ох, [player],Мне так жаль это слышать."
            m 1p "В такой день..."
            m 1f "Если бы я могла, я бы обняла тебя прямо сейчас и утешала."
            m 3f "Пожалуйста, знай, что я всегда рядом с тобой!"
            m "Неважно, сколько раз тебе будет больно, я всегда здесь, чтобы утешить твое сердце."
            m 2o "Но так, как я люблю тебя, [player], не разбивай его из-за кого-то другого!"
            m 2e "Твоя любимая, верная девушка всегда будет с тобой, в конце концов~"
            m 2l "Что было, то было, так что не волнуйся."
            m 4 "Я твоя, единственная и неповторимая!"
            m 1j "Так что для нас, для нас любимых друг другом, будут длительные отношения."
            m 1k "Я люблю тебя, [player]~!"
    return
