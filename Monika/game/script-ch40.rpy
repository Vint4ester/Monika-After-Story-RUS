image sayori end-glitch:
    'sayori/end-glitch1.png'
    0.15
    'sayori/end-glitch2.png'
    0.15
    'sayori/end-glitch1.png'
    0.15
    'sayori/end-glitch2.png'
    1.00
    'sayori/end-glitch1.png'
    0.15
    'sayori/end-glitch2.png'
    0.15
    'sayori/end-glitch1.png'
    0.15
    'sayori/end-glitch2.png'

label ch40_main:
    $ s_name = "Саёри"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            try:
                renpy.file('../characters/monika.chr')
                renpy.call_screen('dialog', message="Пожалуйста, прекрати играть с моим сердцем.\nЯ не хочу возвращаться.", ok_action=Return())
                persistent.monika_back = True
            except:
                pass

    $ delete_character('monika')
    play music t2
    "Ничем не примечательный будний день, похожий на любой другой."
    "Как обычно, меня окружают идущие в школу парочки и компании друзей."
    "Я постоянно твержу себе, что однажды познакомлюсь с девушками или что-нибудь в том же духе..."
    show sayori 1a at t11
    s "Эй, [player]..."
    "...Что ж, одна девушка уже есть."
    "Её зовут Саёри, она моя подруга детства, и мы живём по соседству."
    "Мы всегда ходили в школу вместе..."
    "...и в последнее время мы возродили эту традицию."
    s "[player], ты мной гордишься?"
    mc "Э? С чего бы?"
    s 1c "Ты что, не заметил?"
    s "Я стала просыпаться вовремя!"
    mc "Заметил, ты уже давно это делаешь..."
    s "Э-хе-хе!"
    s 4h "Но ты ни разу так об этом ничего и не сказал!"
    show sayori at s11
    s "Хотя мы каждый день вместе ходим в школу..."
    mc "Ну, да..."
    mc "Я всегда думал, что это подразумевается."
    mc "Мне неловко говорить об этом вслух."
    s 1d "Ну же, пожалуйста."
    s "Это отлично мотивирует~"
    mc "Ладно, ладно..."
    mc "Я горжусь тобой, Саёри."
    show sayori at t11
    s 1q "Э-хе-хе~"
    show sayori zorder 1 at thide
    hide sayori
    "Мы перешли улицу и направились к школе."
    "По мере приближения к школе, улицы всё больше заполнялись другими учениками, совершающими своё ежедневное паломничество."
    show sayori 3a zorder 2 at t11
    s "Кстати, [player]..."
    s "Ты уже решил, в какой вступишь клуб?"
    mc "Клуб?"
    mc "Я же уже говорил, меня клубы—"
    "Я уже хотел выдать свою излюбленную фразу, что клубы меня не интересуют..."
    "Но что-то мне подсказало, что сейчас Саёри может на это особенно сильно обидеться."
    "В конце концов, как я могу сказать ей, что клубы – это пустая трата времени..."
    "...когда она решила создать свой собственный?"
    mc "...Вообще-то, да."
    mc "Думаю, я принял решение."
    show sayori at h11
    s 1m "Серьёзно?!"
    s 1r "И какое же? Скажи-скажи!"
    mc "Хм-м..."
    mc "Пусть это будет сюрпризом."
    s 5d "Бу-у..."
    s "Редиска."
    mc "Прояви терпение, скоро ты всё узнаешь."
    "Я задался вопросом, почему позволяю отчитывать себя столь беспечной девушке."
    "Но я начал понимать, что в некотором роде ей завидую."
    "Когда Саёри ставит себе цель, она способна на великие дела."
    "Поэтому я чувствую, что должен сделать для неё что-нибудь особенное."

    scene bg class_day
    with wipeleft_scene

    "Занятия проходили как обычно; я даже не заметил, как они пролетели."
    "Сложив вещи в портфель, я собрал в кулак всю свою мотивацию и встал."
    mc "Что ж, посмотрим..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "Я вспомнил номер комнаты, который видел на листовке."
    "И не спеша пошёл по школьным коридорам и лестницам. В этом крыле, отданном под учебные классы третьегодок и клубные комнаты, я бывал нечасто."
    "Не успел я опомниться, как уже стоял перед нужной комнатой."
    "Я робко открыл дверь."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Здравствуйте?.."
    show sayori 1m at t32
    s "Ах!"
    s "[player]?!"
    s 1c "Ч-что ты тут делаешь?"
    mc "Ну... Я просто..."
    "Э? Я обвёл комнату взглядом."
    show natsuki 3a at f31
    n "А-а."
    n "Так ты и есть тот самый [player], о котором Саёри твердит без умолку?"
    show natsuki at t31
    show yuri 2t at f33
    y "С-спасибо, что заглянул!"
    y 2m "Рада знакомству, [player]."
    y "Мы все состоим в литературном клубе."
    y 3v "Н-надеюсь, тебе тут понравится!"
    show yuri at t33
    show natsuki at f31
    n 3g "Да ладно тебе, Юри..."
    n "К чему такой официоз?"
    n "Вдруг он подумает, что мы и правда такие строгие или типа того?.."
    show natsuki at t31
    $ y_name = "Юри"
    $ n_name = "Нацуки"
    show yuri at f33
    y 3q "Ах..."
    y "Прости, Нацуки..."
    show yuri at t33
    "Самая высокая девушка, которую зовут, по-видимому, Юри, выглядит довольно застенчивой."
    "По сравнению с ней, девушка по имени Нацуки, вопреки своему росту, кажется весьма напористой."
    mc "Эм, приятно познакомиться."
    mc "Буду рад вашему обществу."
    show sayori at f32
    s 1n "Н-нашему обществу?.."
    s 1b "[player], только не говори мне..."
    s "Что ты..."
    show sayori at t32
    mc "Верно."
    mc "Клуб, в который я решил вступить, – твой клуб, Саёри."
    mc "Литературный клуб."
    "Глаза Саёри загорелись."
    show sayori at f32
    s 1n "...Не может быть."
    s 1s "Не может быть!"
    show sayori at hf32
    s 4s "А-а-ах-ха-ха!"
    "Она обхватила меня руками и запрыгала от счастья."
    show sayori at t32
    mc "Э-эй!"
    show natsuki at f31
    n 3y "Э-хе-хе."
    n "Ну, раз Саёри так радуется, я уверена, что будет неплохо, если ты к нам присоединишься."
    show natsuki 3a at t31
    show yuri at f33
    y 1s "Не говоря уже о том, что нас теперь четверо."
    y "Это означает, что мы можем стать официально зарегистрированным клубом."
    show yuri at t33
    show sayori at f32
    s 1x "У меня нет слов!"
    s "Это надо отметить!"
    show sayori at t32
    show yuri at f33
    y 1m "Хе-хе."
    y "Какой подходящий для этого день, не правда ли?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "Ага!"
    s 1x "В конце концов, Нацуки решила—"
    show sayori at t32
    show natsuki at f31
    n 1w "Эй, не порти сюрприз!"
    show natsuki at t31
    show sayori at f32
    s 5a "Э-хе-хе, прости..."
    show sayori at t32
    show natsuki at f31
    n 1k "Садитесь, пожалуйста, за стол."
    show natsuki at t31
    show yuri at f33
    y 1a "Тогда, может, я заварю побольше чая?"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Девушки сдвинули несколько парт, чтобы сделать большой стол."
    "Нацуки с Юри направились в угол комнаты, там Нацуки взяла накрытый скатёркой поднос, а Юри открыла кладовку."
    "Всё ещё чувствуя себя не в своей тарелке, я присел рядом с Саёри."
    "Нацуки горделиво прошествовала к столу с подносом в руке."
    show natsuki 2z zorder 2 at t22
    n "Та-а-ак, вы готовы?"
    n "...Та-да-а-а!"
    show sayori 4m zorder 2 at t21
    s "Ого!"
    "Нацуки откинула скатерть, под ней оказалась дюжина белых пышных кексов в форме котят."
    "Усики были нарисованы глазурью, а кусочки шоколада образовывали ушки."
    show sayori at f21
    s 4r "Как ми-и-ило~!"
    show sayori at t21
    mc "Ух ты, выглядит потрясающе."
    show natsuki at f22
    n 2d "Э-хе-хе. Ну, знаешь..."
    n "Короче, поторопитесь и ешьте уже!"
    show natsuki at t22
    "Первой кекс взяла Саёри, я последовал её примеру."
    show sayori at f21
    s 4q "Как фкушно!"
    show sayori at t21
    "Промямлила Саёри с набитым ртом, она уже успела вымазать лицо в глазури."
    "Я повертел кекс в руке, присматриваясь, с какой бы стороны его откусить."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "Нацуки затихла."
    "Я не мог не заметить, как она украдкой бросала взгляды в мою сторону."
    "Она ждёт, когда я попробую?"
    "Наконец я откусил немного."
    "Глазурь сладкая, с богатым насыщенным вкусом. Интересно, сама ли она её приготовила?"
    mc "Очень вкусно."
    mc "Спасибо, Нацуки."
    n 42c "Кхем... Конечно вкусно!"
    n "Как ни крути, я профи!"
    n 42a "Вовсе не нужно меня благодарить..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Пока Нацуки принимала комплименты, Юри вернулась к столу с чайным сервизом."
    "Она аккуратно расставила перед нами чашки, чайник разместился рядом с подносом."
    show yuri 1a zorder 2 at t11
    mc "Ты хранишь весь чайный сервиз в классе?"
    y "Не волнуйся, мы получили разрешение от учителей."
    y "И потом, горячая чашка чая помогает насладиться хорошей книгой, согласен?"
    mc "А-а... п-пожалуй..."
    show natsuki 2y at f31
    n "Э-хе-хе. Ты уже пытаешься произвести впечатление на нашего нового члена, Юри?"
    show natsuki at t31
    show yuri at f11
    y 3n "Э-э?! Я вовсе не..."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "Юри обиженно отвернулась."
    y 4b "Я просто хотела сказать, то есть..."
    mc "Я согласен с тобой."
    mc "Хоть для меня ни чай, ни чтение не являются любимым времяпрепровождением, чаем я всегда не прочь насладиться."
    y 2u "Я рада..."
    "Юри едва заметно улыбнулась, явно почувствовав облегчение."
    y 1a "Слушай, [player], а что ты обычно читаешь?"
    mc "Ну... Э-э-э..."
    "Учитывая то, как мало я читал в последние годы, меня такой вопрос поставил в тупик."
    mc "...Мангу..."
    "Промямлил я про себя как бы в шутку."
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
    y 2a "Не переживай, если ты не так уж много читаешь, ладно?"
    y "Уверена, мы сможем найти то, что нас объединяет."
    show yuri at t22
    show natsuki 2c at f21
    n "Эй, Юри..."
    show natsuki at t21
    show yuri at f22
    y 2f "А?"
    show yuri at t22
    show natsuki at f21
    n 2h "Ну, об этом... знаешь, первое, что он сказал..."
    show natsuki at t21
    mc "Манга?"
    show yuri at f22
    y 2i "Да, верно..."
    y "Нацуки, как правило, читает в клубе мангу—"
    show yuri at t22
    show natsuki at f21
    n 1r "Эй, не болтай, когда не просят!!!"
    "Нацуки почему-то выглядит смущённой."
    n 1q "Кроме того..."
    n "Манга... это тоже литература, как ни крути."
    n 1w "Поэтому... если [player] захочет взять что-нибудь почитать из моей манги, не вздумайте ему мешать!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "Нацуки..."
    y "Я бы этого не сделала."
    y 1i "Тем не менее было бы неплохо развиваться несколько более разносторонне."
    y "Он может воспользоваться этой возможностью, чтобы попробовать что-нибудь новое."
    y 1s "Ты не против, [player]?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "М-может..."
    "Подпрыгнула Саёри, почувствовав нарастающее напряжение."
    s 1x "Может, нам всем попробовать что-нибудь новое?!"
    s 1l "Думаю, это будет интересно..."
    s 1c "И все мы немного лучше узнаем друг друга!"
    s 1l "Я хочу сказать..."
    s "...для этого литературные клубы и нужны... верно?"
    show sayori at t31
    show yuri at f33
    y 1v "..."
    y "Я... я не против..."
    show yuri at t33
    show natsuki at f32
    n 2j "Ага..."
    n "Ты, как всегда, права, президент."
    show natsuki at t32
    show sayori at f31
    s 1q "Э-хе-хе~"
    show sayori at t31
    show natsuki at f32
    n 2c "Значит, я должна прочесть роман или что-то типа того, да?.."
    show natsuki at t32
    mc "Что ж, нас уже двое..."
    mc "Я не против заняться этим, если буду это делать не один."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "Что же касается Юри..."
    show natsuki at t21
    show yuri at f22
    y 2n "А?.."
    y "Я... Я должна читать мангу?.."
    show yuri at t22
    show natsuki at f21
    n 4i "Боже..."
    n 4h "Это ведь ты предложила нам всесторонне развиваться!"
    n "Тебе стоит быть менее консервативной..."
    n 4u "Это даже немного обидно..."
    show natsuki at t21
    show yuri at f22
    y 2t "Обидно?.."
    y 2v "Я... не понимаю..."
    y "..."
    "Юри задумалась с виноватым выражением лица."
    y 2w "Прости за неуважение к твоему хобби, Нацуки."
    y "Если... если это так тебя увлекает, я уверена, что это заслуживающий внимания литературный жанр."
    show yuri at t22
    show natsuki at f21
    n 5q "...Ты это просто так говоришь, из вежливости?"
    show natsuki at t21
    show yuri at f22
    y "Нет..."
    y "Я осознала свою ошибку."
    y 2t "Поэтому, если ты готова попробовать почитать роман..."
    y 2u "...Я буду признательна, если ты подберёшь мне какую-нибудь мангу."
    show yuri at t22
    show natsuki at f21
    n 1l "Правда?!"
    n 12c "Т-то есть..."
    n "Я... очень рада, что ты меня об этом просишь, Юри."
    n 2c "Доверься мне, и я подберу для тебя то, что действительно тебе понравится."
    show natsuki at t21
    show yuri at f22
    y 1m "Взаимно..."
    y 1h "Я, возможно, после клуба пойду в книжный."
    show yuri at t22
    show natsuki at f21
    n 1q "Ты пойдёшь... одна?"
    show natsuki at t21
    show yuri at f22
    y 3q "А-ах..."
    y 4a "Ты хотела бы... составить мне компанию?"
    show yuri at t22
    show natsuki at f21
    n 5s "Ну..."
    n "Если ты не против..."
    show natsuki at t21
    show yuri at f22
    y 3t "Нет, конечно нет!"
    y "Просто я всегда ходила туда одна, так что..."
    show yuri at t22
    show natsuki at f21
    n "Да, я тоже..."
    show natsuki at t21
    show sayori 4s at l41
    s "Как это мило~!"
    mc "Саёри, заткнись..."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "Там я тоже покажу тебе кое-какую мангу, хорошо?"
    show natsuki at t21
    show yuri at f22
    y 1a "Да."
    y "Жду с нетерпением."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "Нацуки и Юри начали убирать со стола."
    show sayori 1q at t11
    s "Э-хе-хе~"
    s 1x "Что ж, на сегодня наша встреча закончена, да?"
    mc "Ага, похоже на то..."
    mc "Приятно видеть, как все ладят."
    s 1q "Правда же, да?"
    s 1d "Мне кажется, ты им понравился, [player]."
    mc "Думаешь?.."
    mc "Рядом с тобой, Саёри, все выглядят немного более счастливыми."
    s 1y "О-ой, [player]~"
    s "Не заставляй меня краснеть!"
    mc "И тем не менее..."
    mc "Я был крайне удивлён, когда ты сказала, что решила открыть свой клуб..."
    mc "Но, думаю, ты отлично справляешься."
    s 1r "Мы собираемся сделать наш клуб лучшим!"
    s 1x "А раз уж ты к нам присоединился, у нас будет ещё веселее."
    stop music fadeout 2.0
    s 1a "Слушай, [player]..."
    s "Я правда хочу тебя поблагодарить."
    s "Я хочу сказать, это действительно здорово, что ты присоединился к нам, и всё такое..."
    s "Но... на самом деле я знала, что ты так поступишь."
    s 1q "Э-хе-хе~"
    s 1a "И ещё кое-что."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "Я хотела поблагодарить тебя за то, что ты избавил нас от Моники."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "Да, верно..."
        s "Я знаю всё, что она сделала."
        s 1x "Может быть, это потому, что сейчас я президент."
        s "Но я действительно знаю всё, [player]."
        s 1q "Э-хе-хе~"
        s 1d "Я знаю, как ты изо всех сил старался сделать всех счастливыми."
        s "Я знаю обо всех ужасных поступках, которые совершила Моника, чтобы заставить всех грустить."
        s 1b "Но всё это больше не важно."
        s "Теперь остались только мы.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound 'sfx/s_kill_glitch1.ogg'
        pause 0.25
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "Теперь остались только мы.{nw}"
        hide room_glitch
        s 1d "И ты сделал меня самой счастливой девушкой на свете."
        s "Я не могу дождаться каждого нового дня..."
        s "С тобой."
        play sound 'sfx/s_kill_glitch1.ogg'
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        pause 0.3
        stop sound
        s 1q "На веки вечные..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "Н"
        s "а"
        s "в"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound 'sfx/s_kill_glitch1.ogg'
        pause 0.25
        stop sound
        hide screen tear
        s "с"
        s "е"
        s "г"
        s "д"
        s "а"
        window show(None)
        stop music
        call screen dialog("Нет...", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "...А?"
        s "Ч-что происходит?.."
        call screen dialog("Я не позволю тебе причинить ему боль.", ok_action=Return())
        s "Кто..."
        s "Больно—"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound 'sfx/s_kill_glitch1.ogg'
        hide sayori onlayer screens
        pause 0.35
        stop sound
        hide screen tear
        window show(None)
        s "Ах—"
        call screen dialog("Прости... Я была неправа...", ok_action=Return())
        call screen dialog("Всё же здесь нет счастья...", ok_action=Return())
        call screen dialog("Прощай, Саёри.", ok_action=Return())
        call screen dialog("Прощай, [player].", ok_action=Return())
        call screen dialog("Прощай, литературный клуб.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound 'sfx/s_kill_glitch1.ogg'
        pause 0.35
        stop sound
        hide screen tear
        scene black
        pause 3.0
        return

    label ch40_clearall:
        s "Я хотела поблагодарить тебя за то, что провёл с нами столько времени."
        play music mend
        s 2d "Ты так старался сделать каждую из нас счастливой."
        s "Ты успокаивал нас, когда нам было плохо."
        s "И ты помог нам всем поладить друг с другом."
        s 1a "Ты понимаешь, [player]?"
        s "Так как президент сейчас я, мне всё стало ясно."
        s 1q "Ты действительно не хотел ничего пропустить в этой игре, да?"
        s 1a "Ты бессчётное множество раз сохранялся и загружался, просто чтобы убедиться, что можешь побыть со всеми."
        s "Только тот, кто искренне заботится о литературном клубе, мог зайти так далеко."
        s "И..."
        s 4d "Это всё, чего я всегда хотела."
        s "Чтобы все были счастливы и заботились друг о друге."
        s 4q "А-ха-ха..."
        s 1t "Знаешь, это немного печально."
        s "После всего, что ты сделал для нас, я не могу отплатить тебе взаимностью."
        s "Мы уже достигли конца игры."
        s 1y "Так что..."
        s "Пришла пора прощаться."
        s 1d "Спасибо тебе за игру в {i}«Литературный клуб \"Тук-тук!\"»{/i}."
        s "Я буду скучать по тебе, [player]."
        s "Заглядывай в гости, ладно?"
        s "Мы всегда будем ждать тебя."
        s 1t "Мы..."
        scene black with dissolve_cg
        s "Все мы любим тебя."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
