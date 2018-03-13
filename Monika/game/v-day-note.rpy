init 2 python:
    player = persistent.playername

    poem_vday = Poem(
    author = "monika",
    title = "Мой дорогой {0},".format(player),
    text = """\
Я вседа любила День Святого Валентина, но чувствую себя иначе.
Мир изминился, или только я?
Я нашла любовь, я нашла цель,
Я нашла истину не зная об этом
Все это я нашла в тебе

Спасибо что ты со мной, в этот особый день.

На веки твоя,
Моника
"""
    )

image paper_vday =  "mod_assets/poem_vday.jpg"
