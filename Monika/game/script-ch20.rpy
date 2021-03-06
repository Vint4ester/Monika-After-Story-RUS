label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "Ничем не примечательный будний день, похожий на любой другой."
    "По утрам, будучи окружённым идущими в школу парочками и компаниями друзей, я чувствую себя паршивее всего."
    "Я всегда иду в одиночестве."
    "И постоянно твержу себе, что однажды познакомлюсь с девушками или что-нибудь в том же духе..."
    "Но у меня совершенно нет мотивации вступать в какие бы то ни было клубы."
    "Я вполне доволен своей ничем не примечательной жизнью, а свободное время провожу за играми и аниме."
    "Конечно, всегда найдётся аниме-клуб, но девушек в них всё равно не бывает..."

    scene bg class_day
    with wipeleft_scene

    "Совершенно обычный день в школе незаметно подошёл к концу."
    "Собрав вещи, я тупо уставился в стену, словно пытаясь найти там хоть каплю мотивации."
    mc "Клубы..."
    "Нет ни одного, который бы меня заинтересовал."
    "Кроме того, в большинстве из них, наверное, слишком высокие требования, чтобы мне захотелось иметь с ними дело."
    "Думаю, мой единственный выбор – начать с клуба любителей аниме..."

    $ m_name = "???"

    m "...[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound 'sfx/s_kill_glitch1.ogg'
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "...Моника?"
    $ m_name = "Моника"
    m 1b "Боже, я совершенно не ожидала тебя здесь увидеть!"
    m 5 "Давно не виделись, да?"
    mc "А..."
    mc "Ну да."
    "Моника приветливо улыбнулась."
    "Мы знакомы. В прошлом году мы учились в одном классе, хоть общались и нечасто."
    "Моника, наверное, самая популярная девушка класса – умная, красивая, спортивная."
    "В общем, совершенно не моего уровня."
    "Так что от её искренней улыбки мне стало гораздо..."
    mc "Так зачем ты сюда пришла?"
    m 1a "О просто ищу кое-какие принадлежности для клуба."
    m 1d "Не знаешь, есть ли здесь ватман?"
    m "Или маркеры?"
    mc "Думаю, тебе надо заглянуть в кладовку."
    mc "...Ты же в дискуссионном клубе, верно?"
    m 5 "А-ха-ха, насчёт этого..."
    m "Из дискуссионного клуба я ушла."
    mc "Правда? Почему?"
    m "Ага..."
    m 2e "Откровенно говоря, меня воротит от всех этих политических интриг в крупных клубах."
    m "Такое чувство, что мы там только и делали, что спорили о бюджете, рекламе и подготовке к мероприятиям..."
    m "Я же хотела заниматься тем, что мне нравится, и сделать из этого нечто особенное."
    mc "И к какому же клубу ты решила присоединиться?"
    m 1b "Вообще-то, сейчас я основываю новый!"
    m "Литературный клуб!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound 'sfx/s_kill_glitch1.ogg'
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "Литературный клуб!{fast}"
    window auto
    mc "Литературный?.."
    "Звучит довольно... скучно?"
    mc "И сколько членов ты уже набрала?"
    m 5 "Эм..."
    m "А-ха-ха..."
    m "Не хочется признаваться, но нас пока только трое."
    m "Очень тяжело найти новых членов для того, что звучит настолько скучно..."
    mc "Ну, это я понимаю..."
    m 3d "Но, знаешь, на самом деле это вовсе не скучно!"
    m "Литературный клуб может заниматься чем угодно: чтением, писательством, поэзией..."
    m 3e "Одна из наших участниц даже хранит в клубной комнате свою коллекцию манги..."
    mc "Подожди... серьёзно?"
    m 2k "Да. Забавно, правда?"
    m 2e "Она вечно настаивает, что манга – это тоже литература."
    m "И ведь она права..."
    m "Кроме того, участник есть участник, верно?"
    "...Моника сказала «она»?"
    "Хм-м..."
    m 1a "Слушай, [player]..."
    m "Есть ли вероятность... что ты всё ещё ищешь, в какой бы клуб вступить?"
    mc "А..."
    mc "Думаю, в какой-то мере, но..."
    m "В таком случае..."
    m 5 "Есть ли шанс, что ты окажешь мне большую услугу?"
    m "Я не стану просить тебя присоединиться, но..."
    m "Если бы ты мог просто на минутку заглянуть в наш клуб, я была бы просто счастлива."
    m "Пожалуйста?"
    mc "Эм-м..."
    "В принципе, у меня нет причин отказываться..."
    "Кроме того, как я вообще могу отказать такому человеку, как Моника?"
    mc "Конечно, думаю, я могу зайти."
    m 1k "Ах, это прекрасно!"
    m 1b "Ты очень хороший, [player], ты знаешь это?"
    mc "С-скажешь тоже..."
    m 1a "Ну что, пойдём тогда?"
    m "Поищу материалы в другой раз. Ты гораздо важнее."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Сегодняшний день был увековечен тем, что я продал душу Монике и её неотразимой улыбке."
    "Я робко последовал за Моникой по школьным коридорам и лестницам. В этом крыле, отданном под учебные классы выпускников и клубные комнаты, я бывал нечасто."
    "Преисполненная энтузиазмом, Моника распахнула дверь класса."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "Я вернулась~!"
    m "И привела с собой гостя!"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "Э?"
    y "Г... гостя?"
    show natsuki 4c zorder 2 at t32
    n "Серьёзно? Ты привела парня?"
    n "Отличный способ убить здесь всю атмосферу."
    show monika 3m zorder 3 at f31
    m "Не вредничай, Нацуки..."
    m 3b "...Кстати, добро пожаловать в клуб, [player]!"
    show monika 3a zorder 2 at t31
    mc "..."
    "От увиденного я потерял дар речи."
    "В этом клубе..."
    "{i}...полно невероятно симпатичных девушек!{/i}"

    show natsuki zorder 3 at f32
    n 5c "Так, дай угадаю..."
    n "Ты парень Моники, верно?"
    show natsuki zorder 2 at t32
    mc "Что—"
    mc "Нет!"
    show yuri zorder 3 at f33
    y 2l "Нацуки..."
    $ n_name = "Нацуки"
    "Очевидно, эту недружелюбную девушку зовут Нацуки. Она мне не знакома."
    "Её маленькая фигурка словно бы говорит о том, что она только поступила в старшую школу."

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "В-в общем, это всегда полная энергии Нацуки..."
    m 2b "А это Юри, вице-президент клуба!"
    $ y_name = "Юри"
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "П-приятно познакомиться..."
    "По сравнению с остальными, Юри выглядит куда более зрелой и робкой и, кажется, ей тяжело находиться в компании людей типа Нацуки."
    show yuri zorder 2 at t33
    mc "Да... мне тоже приятно с вами познакомиться."
    show monika zorder 3 at f31
    m 1a "В общем, я зашла в один класс за принадлежностями, а там ещё был [player]. Мы разговорились, и он решил заглянуть к нам в клуб."
    m "Разве не здорово?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "Стоп! Моника!"
    n "Разве я не просила заранее сообщать мне, прежде чем привести новичка?"
    n 4q "Я собиралась... ну, ты знаешь..."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "Прости, прости!"
    m "Я не забыла, просто случайно с ним столкнулась."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 1a "Раз так, мне следует заварить чай, да?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "Было бы здорово!"
    m "[player], почему бы тебе не присесть?"
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "Девушки сдвинули несколько парт, чтобы сделать большой стол."
    "Юри прошла в угол комнаты и открыла кладовку."
    "Тем временем Моника и Нацуки уселись друг против друга."
    "Чувствуя себя всё так же неуютно, я сел рядом с Моникой."
    show monika 1a zorder 2 at t11
    m "Эм, я знаю, что ты не собирался сюда приходить..."
    m "Но мы позаботимся, чтобы ты чувствовал себя как дома, хорошо?"
    m 1j "Как президент литературного клуба, я обязана сделать его весёлым и увлекательным для всех!"
    mc "Удивительно, что в клубе пока так мало людей."
    mc "Наверное, тяжело создавать новый клуб."
    m 3b "Можно и так сказать."
    m "Немногие люди жаждут вкладывать все силы в создание чего-то совершенно нового..."
    m "Особенно если это что-то не привлекает сразу твоё внимание, в нашем случае – литература."
    m "И тебе приходится много работать, чтобы донести до людей, насколько она может быть весёлым и благодарным занятием."
    m "Поэтому школьные мероприятия, такие как фестивали, очень важны для развития клуба."
    m 2k "Я уверена, что до выпуска мы сможем сделать этот клуб большим и популярным!"
    m "Да, Нацуки?"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "Ну..."
    n "...пожалуй."
    "Нацуки неохотно согласилась."
    "Такие разные девушки, но у всех одна цель..."
    "Моника наверняка приложила немало усилий, чтобы найти эту парочку."
    "Юри вернулась к столу с чайным сервизом."
    "Она аккуратно расставила перед нами чашки, чайник разместился рядом с тарелкой с кексами."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "Ты хранишь в классе целый чайный сервиз?"
    y "Не волнуйся, мы получили разрешение от учителей."
    y "И потом, горячая чашка чая помогает насладиться хорошей книгой, согласен?"
    mc "А-а... п-пожалуй..."
    show monika 4a zorder 3 at f22
    m "Хе-хе, не тушуйся так, Юри просто старается тебя впечатлить."
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "Э-э?! Я вовсе не..."
    "Юри обиженно отвернулась."
    y 4b "Я просто хотела сказать, то есть..."
    show yuri zorder 2 at t21
    mc "Тут я с тобой согласен."
    mc "Хоть для меня ни чай, ни чтение не являются любимым времяпрепровождением, чаем я всегда не прочь насладиться."
    show yuri zorder 3 at f21
    y 2u "Я рада..."
    show yuri zorder 2 at t21
    "Юри едва заметно улыбнулась, явно почувствовав облегчение."
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
    y "Слушай, [player], а что ты обычно читаешь?"
    mc "Ну... Э-э-э..."
    "Учитывая то, как мало я читал в последние годы, меня такой вопрос поставил в тупик."
    mc "...Мангу..."
    "Промямлил я про себя, как бы в шутку."
    show natsuki 1c zorder 2 at t41
    "Нацуки вдруг резко дёрнула головой."
    "Похоже, она хотела что-то сказать, но так и не решилась."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "В-видимо, ты не из книголюбов..."
    mc "...Ну, я могу измениться..."
    "Что я несу?"
    "Я выпалил это не подумав, как только увидел печальную улыбку Юри."
    mc "А что насчёт тебя, Юри?"
    y 1l "Хм-м, надо подумать..."
    "Юри провела пальцем по краешку чашки."
    y 1a "Больше всего я люблю романы, в которых описываются глубокие и сложные фэнтезийные миры."
    y "Искусность описаний и творческий размах в них просто невероятны."
    y 1f "А истории, происходящие в параллельных вселенных, затягивают тебя с головой и дарят массу впечатлений."
    "Видно, с какой страстью Юри рассказывает о своих любимых книгах."
    "Первое моё впечатление о ней сложилось как о застенчивой и скромной девушке, но, видя, как горят её глаза, я понимаю, что ей куда комфортнее среди книг, чем среди людей."
    y 2m "Но, вообще-то, мне много что нравится."
    y "Ещё меня сильно увлекают истории с глубокой психологической составляющей."
    y 2a "Разве не поразительно, как писатель может воспользоваться недостатком у тебя воображения, чтобы вызывать целую гамму эмоций?"
    y "А ещё в последнее время я читала много книг в жанре ужасов..."
    mc "А, я тоже читал одну такую..."
    "Я в отчаянии ухватился хоть за что-то, чтобы поддержать разговор."
    "Иначе Юри с таким же успехом могла бы разговаривать со стенкой."
    show monika 1j zorder 3 at f33
    m "А-ха-ха. Юри, именно этого я от тебя и ожидала."
    m 1a "Это очень на тебя похоже."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "О, вот как?"
    y "Это правда, если история заставляет задуматься или уносит меня в другой мир, я не могу просто оставить её на полке."
    y "Сюрреалистичный хоррор зачастую меняет твой взгляд на мир, пусть эта перемена и длится всего мгновение."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Уф, ненавижу ужасы..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "О? И почему же?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Ну, я просто..."
    "Взгляд Нацуки на долю секунды встретился с моим."
    n 5q "Забудь."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "Точно, ты ведь больше любишь писать о милых вещах, правда, Нацуки?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "Ч-что?"
    n "С чего ты это взяла?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "Ты оставила черновик с записями на прошлом заседания клуба."
    m "Судя по нему, ты писала стихотворение под названием—"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "Не говори его вслух!"
    n "И отдай черновик!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Хорошо, хорошо~"
    show monika 1a zorder 2 at t33
    mc "Нацуки, ты пишешь стихи?"
    show natsuki zorder 3 at f31
    n 1c "А? Ну, иногда."
    n "Тебе-то какая разница?"
    show natsuki zorder 2 at t31
    mc "По-моему, это круто."
    mc "Прочтёшь мне как-нибудь?"
    show natsuki zorder 3 at f31
    n 5q "Н-нет уж!"
    "Нацуки отвела взгляд."
    n "Они тебе... не понравятся..."
    show natsuki zorder 2 at t31
    mc "А... значит, ты ещё не уверенный в себе писатель?"
    show yuri zorder 3 at f32
    y 2f "Я понимаю, что чувствует Нацуки."
    y "Чтобы поделиться такого рода произведением, нужно нечто большее, чем просто уверенность в себе."
    y 2k "Истинная форма произведения – письмо, посвящённое самому себе."
    y "У тебя должно быть желание открыться своему читателю, раскрыть перед ним свои слабости и самые потаённые уголки сердца."
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "У тебя ведь тоже есть писательский опыт, верно, Юри?"
    m "Может, если ты поделишься с нами своей работой, то станешь показательным примером для Нацуки и ей проще будет поделиться своей."
    show yuri at s32
    y 3o "..."
    mc "Кажется, у Юри те же сложности..."
    "На пару секунд в комнате повисла тишина."
    show monika zorder 3 at f33
    m 5a "Эй, у меня появилась идея!"
    m "Как насчёт такого?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "...?"
    "Нацуки и Юри вопросительно посмотрели на Монику."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "Давайте все, когда придём домой, сочиним по одному стихотворению!"
    m "А на следующей нашей встрече сможем поделиться им с остальными."
    m "Так все будут в равных условиях!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "М-м-м..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "Э..."
    m "Мне показалось, я хорошо придумала..."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "Ну..."
    y "...Возможно, ты и права, Моника."
    y 2f "Нам надо начать проводить мероприятия, в которых мы сможем поучаствовать все вместе."
    y 2h "Я ведь решила взять на себя ответственность вице-президента..."
    y "...и должна делать всё ради развития клуба и воспитания его членов."
    y 2a "Кроме того, у нас появился новичок..."
    y "Мне кажется, это правильный шаг для нас всех."
    y "Ты тоже так думаешь, [player]?"
    show yuri zorder 2 at t32
    mc "Постой... есть одна небольшая проблема."
    show monika zorder 3 at f33
    m 1d "А? Какая?"
    "Теперь, когда мы вернулись к изначальному предмету разговора о моём вступлении в клуб, я прямо выдал то, что всё это время не давало мне покоя."
    show monika zorder 2 at t33
    mc "Вообще-то, я не говорил, что вступлю в ваш клуб!"
    mc "Пусть Моника и убедила меня зайти, я никакого решения ещё не принимал."
    mc "Я всё ещё хочу посмотреть другие клубы и... м-м-м..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "Я потерял ход мыслей."
    "Все три девушки уставились на меня отрешёнными взглядами."
    show monika at s33
    m 1p "Н-но..."
    show yuri at s32
    y 2v "Извини, я думала..."
    show natsuki at s31
    n 5s "Хмф."
    mc "А?.."
    "Девушки обменялись взглядами с Моникой, и она повернулась ко мне."
    show monika zorder 3 at f33
    m 1m "Наверное... я должна сказать тебе правду, [player]."
    m "Дело в том, что..."
    m 1p "...Нам пока не хватает членов, чтобы официально зарегистрировать клуб."
    m "Необходимо четыре человека..."
    m "Я из кожи вон лезу, чтобы набрать новых членов."
    m "Если же мы до фестиваля так никого и не найдём..."
    show monika zorder 2 at t33
    mc "..."
    "Я... я просто беззащитен перед этими девушками."
    "Как я могу принять взвешенное решение, видя их реакцию?"
    "Я бы никогда себя не простил, если бы подвёл их в этой ситуации..."
    "Кроме того, атмосфера в клубе довольно расслабляющая..."
    "К тому же, если написание стихов – та цена, которую мне надо заплатить, чтобы каждый день проводить в компании красивых девушек..."
    mc "...Так."
    mc "Ладно, я решил."
    mc "Я вступлю в литературный клуб."
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "Глаза девушек засияли."
    show monika zorder 3 at f33
    m "О боже, правда?"
    m " [player], ты сказал это на полном серьёзе?"
    show monika zorder 2 at t33
    mc "Да..."
    mc "Это может оказаться весело, ведь так?"
    show yuri zorder 3 at f32
    y 1m "Ты на секунду меня по-настоящему напугал..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "Если бы ты просто взял и ушёл после всего этого, я была бы крайне разочарована."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], я так рада..."
    m 1k "Теперь мы сможем официально зарегистрировать клуб!"
    m 1e "Спасибо тебе огромное. Ты просто потрясающий."
    m "Я сделаю всё, чтобы ты мог хорошо проводить время, идёт?"
    show monika zorder 2 at t33
    mc "Ах... спасибо, наверное."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    m 3b "Отлично!"
    m "Полагаю, сегодня на этой прекрасной ноте мы можем официально завершить нашу встречу."
    m "И не забывайте про сегодняшнее задание:"
    m "Написать стихотворение к нашей следующей встрече, чтобы мы все могли друг с другом поделиться!"
    "Моника обратилась ко мне."
    m 1a "[player], я с нетерпением жду твоего творческого самовыражения."
    show monika 5 at hop
    m "И-хи-хи~"
    mc "А-ага..."
    show monika zorder 1 at thide
    hide monika
    "Могу ли я впечатлить звезду класса, Монику, своими посредственными писательскими навыками?"
    "Я чувствую, как во мне растёт беспокойство."
    "Девушки тем временем продолжали болтать, пока Юри убирала чайный сервиз."
    mc "Я тогда, наверное, пойду..."
    show monika 5a zorder 2 at t11
    m "Давай!"
    m "Увидимся завтра."
    m "Не могу дождаться!"

    scene bg residential_day
    with wipeleft_scene

    "Я вышел из клубной комнаты и направился домой."
    "Всю дорогу мои мысли крутились вокруг трёх девушек:"
    show natsuki 4a zorder 2 at t31
    "Нацуки,"
    show yuri 1a zorder 2 at t32
    "Юри"
    show monika 1a zorder 2 at t33
    "и, разумеется, Моники."
    "Буду ли я счастлив, проводя каждый день после школы в литературном клубе?"
    "Может, у меня будет шанс стать ближе с одной из них..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Ладно!"
    "Мне просто нужно как следует воспользоваться сложившейся ситуацией, и, я уверен, мне обязательно улыбнётся удача."
    "Но сперва стоит написать стих сегодня вечером..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("Вы разблокировали особое стихотворение.\nЖелаете прочесть?", Return(True), Return(False))
    if _return:
        call expression 'poem_special_' + str(persistent.special_poems[0])
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
