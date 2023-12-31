# У цьому файлі міститься скрипт гри.
# Оголошення символів, які використовуються в цій грі. Колірний аргумент розфарбовує
# ім'я персонажа.
define Billy = Character("Billy Herington")
define mother = Character(_('Матір'), color="#c8ffc8")
define eslow = Character(what_slow_cps=20)
# Гра починається тут.
label start:
    #play music "approaching-storm.mp3" fadeout 1
 
    # Це показує фон. За замовчуванням використовується заповнювач, але ви можете
    # додати файл (з назвою "bg room.png" або "bg room.jpg") до
    # теки images, щоб показати його.
    scene bg gachi
    with Dissolve(.5)
    pause .5
    # Це показує спрайт персонажа. Використовується заповнювач, але ви можете
    # замінити його, додавши до зображень файл із назвою "eileen happy.png".
    # до теки.
    # Це репліки діалогу.
    "Людина- найбільша загадка природи"
    "Незважаючи на свою зовнішню схожість і приналежність до одного виду, кожен утворює свій власний внутрішній світ, що як безмежний всесвіт розширяється, щоб йти в ногу з нашим насиченим темпом життя."
    "А людина і є творцем цього світу, художником, що відображає все те, що бачить і відчуває."
    "На жаль, не завжди кольори бувають яскраві, переливчасті, що так подобаються усім, {w}разом з ними йде все те, чого б кожен хотів би позбавитись:{color=#fff000} біль, сум, утрата.{/color}{w=.5} "
    "Кожен раз впадаючи у відчай власне его бажає вийти з нього і змінитися, щоб більше не відчувати нічого подібного."
    "На фоні відчаю і розчарування і утворюються внутрішні суперечки і конфлікти, які розбивають людину зсередини і занурюють її ще глибше, {b}на дно.{/b}" 
    "Ось ця моторошна історія відбулася рівно 100 років назад, може раніше, може пізніше,{w} але її відголоски ехом розтікаються по сірому місцевому небі. {w=.5}{nw}"
    eslow "{i}Так переживіть це все самотужки,{/i}{nw}{w} {b}тільки вам вирішувати бути або...{/b}{w=.5}"
        #with flashbulb
    pause(.5)
    python:
        name = renpy.input("Але для початку, як до тебе звертатися")
        name = name.strip() or "Guy Shy"
    define me = Character("[name]")
    "Добре провести час, [name]"
    menu:
        "Почати гру":
            jump choice0_done
    label choice0_done:
        "Тоді почнемо" 
     
    scene bg 1
    with Dissolve(.5)
    pause(1)
    me "Важко прокидатися рано-вранці"
    show mother angry
    mother "Синку, у нас закінчилася вода, сходи до річки по неї"

          




    # На цьому гра закінчується.

    return