# The script of the game goes in this file.

default gen_rating = 0

label increase:
    $ gen_rating += 1
    return
label decrease:
    $ gen_rating += -1
    return



# character section

define u = Character("???", color="ababab")
define s = Character("Sass", color="5f9afa")
define m = Character("Mängija", color="f7a736")
define j = Character("Jeremy", color="36d160")
define l = Character("Liia", color="6250eb")
define n = Character("Narrator", color="367d32")
define b = Character("Raamatukoguhoidja", color="b5b5b5")
define h = Character("Richard", color="f5f1b3")
define d = Character("Dan", color="7dc4fa")
define kd = Character("KD", color="689c80")
define ri = Character("Riri", color="a6ffcf")

#image section
image Liiaidle = "Liiaidle.png"
image Liiasmirk = "Liiasmirk.png"
image Liiafrown = "Liiafrown.png"
image Jidle = "Jeremyidle.png"
image Jsmile = "Jeremysmile.png"
image Jfrown = "Jeremyfrown.png"
image Sidle = "Sassidle.png"
image Ssmirk = "Sasssmirk.png"
image Sannoyed = "Sassannoyed.png"
image Richidle  = "Richidle.png"
image Richsmile = "Richsmile.png"
image Richfrown = "Richfrown.png"
image Danidle = "Danidle.png"
image Dansmirk = "Dansmirk.png"
image Dand = "Dandisappointed"
image Libidle = "Libidle.png"
image Libsmirk = "Libsmirk.png"
image Libd = "Libdisappointed.png"
image kdidle = "kdidle.png"
image kdsmile = "kdsmile.png"
image kdwtf = "kdwtf.png"
image kdsleep = "kdsleep.png"
image kdawake = "kdawake.png"
image kdamad = "kdawakemad.png"
image kdasmirk = "kdawakesmirk.png"
image ririidle = "ririidle.png"
image ririhappy = "ririhappy.png"
image ririmad = "ririmad.png"



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene ent

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # Dialouges yippe!
    n "Ilus koolipäev, eks?"
    # These display lines of dialogue.
    menu:
        "*Sisenen F korpusesse*":
            n "Sisened F korpusesse"
        "*Pööran ümber ja lähen koju*":
            n "..."
            "Vau"
            "Lihtsalt vau"
            "ehk sina tea, et kui sa lihtsalt keerad perse ukse poole ja sihkertad koju tagasi, et mängu ei toimu ju?"
            menu bro:
                "Tõsiselt? Oih.":
                    n "vot. {i}ahem{/i},"
                    "Sisened F korpusesse"
                "Mul savi":
                    n "..."
                    "meil ka savi, tõsiselt"
                    "meil on türa 13. juunini vaja ära teha, me oleksime midagi pannud siia texti mõttes aga meil on kiire, vot sulle su {i}easter egg{/i}."
                    jump bro
    scene fkorpo
    n "Oled F korpuses."
    "Vasakul pool on riietusruum, sirge trepp teisele korrusele ja kuulipilduja, paremal toolid. Kuhu sa esimesena lähed?"
    menu fopt:
        "*Riietusruumi*":
            scene cloth 
            n "Sisened riietusruumi, võtad seljast õueriided ja riputad nad riietuspuu külge."
            scene fkorpo
            jump foptnew
        "*2. korrusele*":
            n "ei tahagi üleriideid ära võtta? noh OK"
            jump fIIfloor
        "*Lähed kooli automaadi juurde*":
            n "Kas sul on raha?"
            menu money:
                "Jah":
                    n "Lähed masina juurde ja ostad endale midagi."
                    jump fopt
                "Ei":
                    n "geenius."
                    jump fopt
        "*Lähed istuma*":
            n "Sa istusid toolile."
            "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
            "..."
            jump fopt

    menu foptnew:
        "*2. korrusele*":
            jump fIIfloor
        "*Lähed kooli automaadi juurde*":
            n "Kas sul on raha?"
            menu moneynew:
                "Jah":
                    n "Lähed masina juurde ja ostad endale midagi."
                    jump foptnew
                "Ei":
                    n "geenius."
                    jump foptnew
        "*Lähed istuma*":
            n "Sa istusid toolile."
            "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
            "..."
            jump foptnew

label fIIfloor:
    scene fkorpt
    show Liiaidle at center
    u "Tšau."
    m "Noh tšau. Mis su nimi on?"
    l "Liia. Uus oled või?"
    menu liiaintro:
        "noh jah":
            hide Liiaidle
            show Liiasmirk at center
            l "Nagu arvasinki."
            m "Kus ma olen siis? oled siin kaua õppind?"
            hide Liiasmirk
            show Liiaidle at center
            l "Kolmas kursus, jah, olen kaua olnd. oled F korpuses."
            m "Mis siis F korpuses on?"
            l "Siin on peamiselt mehhaanikud ja keevitajad, see on see suur praktika korpus, siin veel käivad IT tüübid ka, arvuti klassid on olemas küll."
            m "Selge, aga siis siit midagi muud ei ole peale seda?"
            l "Su taga on E korpus, minu taga aga raamatukogu, kust saad raamatu või õpiku võtta."
            menu questions:
                "Kogu aeg nii väsind oled või?":
                    hide Liiaidle
                    show Liiasmirk at center
                    l "ega kas programmeeria ole programmeeria kui ta ei ole iga päev oma päeva kõige madalamas punktis ja ei maga stressi tõttu?"
                    m "Noh. Jah."
                    hide Liiasmirk
                    show Liiaidle at center
                    jump questions
                "Mis eriala õpid?":
                    hide Liiaidle
                    show Liiafrown at center
                    l "Tarkvaraarendust. Ei soovitaks kui sulle meeldib psüühikat hoida. statistilest suurem osa programmeeriatest läksid oma erialale, sest vihkavad ennast."
                    hide Liiafrown
                    show Liiaidle at center
                    jump questions
                "Oma erialaga saad hästi hakkama?":
                    l "Noh, nagugi iga inimene, päris normaalselt."
                    m "Ega mingeid raskusi ei too?"
                    hide Liiaidle
                    show Liiasmirk at center
                    l "Ja veel ütle, et hobused lennata oskavad, muidugi on raskusi, ega see lihtne asi ole."
                    m "Arusaadav."
                    hide Liiasmirk
                    show Liiaidle at center
                    jump questions
                "*tagasi menüü juurde*":
                    jump liiaintro
        "Teoorias nagu tean mida teen...":
            hide Liiaidle
            show Liiasmirk at center
            l "Noh see küll üllatus."
            hide Liiasmirk
            menu options:
                "*Raamatukogu*":
                            jump WayLibrary
                "*E korpus*":
                        jump EkorpusII
                "*1. korrus*": 
                    hide Liiaidle
                    scene fkorpo
                    jump foptnewnew
        "*edasi*":
            jump options

menu foptnewnew:
    "*2. korrusele*":
        jump fIIfloornew
    "*Lähed kooli automaati*":
        n "Kas sul on raha?"
        menu moneynewnew:
            "Jah":
                n "Lähed masina juurde ja ostad endale midagi."
                jump foptnewnew
            "Ei":
                n "geenius."
                jump foptnewnew
    "*Lähed istuma*":
        n "Sa istusid toolile."
        "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
        "..."
        jump foptnewnew

            

label fIIfloornew:
    scene fkorpt
    show Liiaidle at center
    l "..."
    menu optionsnew:
        "*Raamatukogu*":
                    jump WayLibrary
        "*E korpus*":
                jump EkorpusIInew
        "*1. korrus*": 
            hide Liiaidle
            scene fkorpo
            jump foptnewnew


label WayLibrary:
    scene library
    n "Oled raamatukogus."
    n "Raamatukoguhoidja paneb sind tähele ja tuleb sinu juurde"
    show libidle at center
    b "Tere!"
    m "Tere."
    b "Soovite midagi?"
    menu libopt:
        "Raamatut":
            b "Mis raamatu?"
            m "kas teil on soovitusi?"
            hide libidle
            show libsmirk at center
            b "isiklikult soovitaksin klassikuid, kuid teile võiks rohkem midagi uuemat meeldida."
            m "selge."
            hide libsmirk
            show libidle at center
            jump libopt
        "Õpikut":
            b "Mis aine?"
            m "Inglise keel."
            b "Selge, aga tagastage aasta lõpuks, eks?"
            m "Yep."
            jump libopt
        "Miks üldse siin raamatukogu vaja on?":
            hide libidle
            show libsmirk at center
            b "Noh, siin saab võtta raamatut või õpikut. Siin on veel arhiiv kah olemas."
            m "Selge."
            hide libsmirk
            show libidle at center
            jump libopt
        "*tagasi menüü juurde*":
            hide libidle
            jump options


label EkorpusII:
    scene ekorpu
    n "Vaatad ringi ja näed E-tähte"
    n "Oled E korpuses"
    n "järsku paistab sulle keegi silma"
    m "Hei!"
    show Danidle at center
    u "?"
    u "Hei...?"
    u "Sa minuga räägid või?"
    m "Muidugi sinuga! Mis su nimi on?"
    d "Daniel."
    m "Mis E korpuses toimub?"
    d "Siin on peamiselt laborid, siin käivad IT tüübid, mäetehnikud, laborandid, elektrikud, ja nii edasi."
    m "Selge siis."
    menu Danquestions:
        "Mis kursuses oled?":
            hide Danidle
            hide Dansmirk
            show Danidle at center
            d "Teisel."
            jump Danquestions
        "Mis eriala õpid?":
            hide Danidle
            hide Dansmirk
            show Danidle at center
            d "Õpin laborandiks."
            jump Danquestions
        "Saad erialaga hästi hakkama?":
            show Dansmirk at center
            d "Idiootne küsimus, muidugi saan."
            menu ego:
                "Kas su ego on hiigel või?":
                    call decrease from _call_decrease
                    hide Dansmirk
                    show Dand at center
                    d "ei."
                    hide Dand
                    show Danidle at center
                    jump Danquestionsnew
                "*jää vait, aga mõtled, et ta on hiigel nartsissist*":
                    jump Danquestionsnew

                "Tore! Parem kui paljud teised, olen kuulnud!":
                    call increase from _call_increase
                    hide Danidle
                    show Dansmirk at center
                    d "Lahe, eks?"
                    m "eks..."
                    hide Dansmirk
                    show Danidle at center
                    jump Danquestionsnew

        "*edasi*":
            menu EIIoptnew:
                "*F korpusesse*":
                    jump fIIfloornew
                "*1. korrusele*":
                    jump EkorpusI

                
    menu Danquestionsnew:
        "Mis kursuses oled?":
            d "Teisel."
            jump Danquestions
        "Mis eriala õpid?":
            d "Õpin laborandiks."
            jump Danquestions

        "*edasi*":
            menu EIIopt:
                "*F korpusesse*":
                    jump fIIfloornew
                "*1. korrusele*":
                    jump EkorpusI

label EkorpusIInew:
    scene ekorpu
    hide Liiaidle
    show Danidle at center
    d "..."
    menu EIIoptnewnew:
        "*F korpusesse*":
                jump fIIfloornew
        "*1. korrusele*":
                jump EkorpusI

    
label EkorpusI:
    scene ekorpo
    n "Oled E korpuse esimesel korrusel."
    n "Näed, et keegi tuleb väljas su ees olevast uksest ja märkab sind."
    show Jsmile at center
    u "Noh Tšau!"
    m "Tšau."
    u "Nagu aru saan, oled uus?"
    m "Jep, praegu lihtsalt vaatan ringi."
    u "Tore! Muideks, olen Jeremy."
    m "Tore."
    m "mis siis esimesel korrusel teevad?"
    j "siin on köök praktiliste tööde jaoks ja kõik."
    menu Jeremyquestions:
        "Mis kursusel oled?":
            hide Jsmile
            show Jsmile at center
            j "Esimeses!"
            hide Jeremysmile
            show Jidle at center
            jump Jeremyquestions

        "Mis eriala õpid?":
            hide Jidle
            show Jsmile at center
            j "Õpin kokaks!"
            hide Jsmile
            show Jidle at center
            jump Jeremyquestions

        "Saad erialaga hästi hakkama?":
            hide Jidle
            show Jfrown at center
            j "Noh... Nii hästi kui saan..."
            menu comfort:
                "Küll sa hakkama saad!":
                    call increase from _call_increase_1
                    hide Jfrown
                    show Jsmile at center
                    j "Aitäh."
                    hide Jsmile
                    show Jidle at center
                    m "Hea, et sa tarkvaraarendaja ei ole, eks?"
                    hide Jidle
                    show Jsmile at center
                    j "Rääkisid Liiaga või?"
                    m "Jep."
                    j "Juba saan aru, ta on päris pessimistlikku mõtlemisega"
                    hide Jsmile
                    show Jidle at center
                    jump Jeremyquestionsnew

                "Noh, mis juhtub, juhtub, eks?":
                    hide Jidle
                    show Jsmile at center
                    j "Noh, jah."
                    hide Jsmile
                    show Jidle at center
                    jump Jeremyquestionsnew

                "Võib-olla oleksid pidanud valima teise eriala?":
                    call decrease from _call_decrease_1
                    hide Jidle
                    show Jfrown
                    j "Ega sina ei tea, mis mulle parim on. Jää vait."
                    hide Jfrown
                    show Jidle at center
                    jump Jeremyquestionsnew

        "*Edasi*":
            menu EkorpIopt:
                "*2. korrusele*":
                    jump EkorpusIInew
                "*C korpusesse*":
                    jump CKorpI

    menu Jeremyquestionsnew:
        "Mis kursusel oled?":
            hide Jsmile
            show Jsmile at center
            j "Esimeses!"
            hide Jeremysmile
            show Jidle at center
            jump Jeremyquestionsnew

        "Mis eriala õpid?":
            hide Jidle
            show Jsmile at center
            j "Õpin kokaks!"
            hide Jsmile
            show Jidle at center
            jump Jeremyquestionsnew

        "*Edasi*":
            menu EkorpIoptnew:
                "*2. korrusele*":
                    jump EkorpusIInew
                "*C korpusesse*":
                    jump CKorpI

label EkorpusInew:
    scene ekorpo
    show Jidle at center
    j "..."
    menu EkorpIoptnewnew:
        "*2. korrusele*":
            jump EkorpusIInew
        "*C korpusesse*":
            jump CKorpInew


label CKorpI:
    scene ckorpent
    n "Oled C korpuses."
    n "sinu ees on söökla ja edasi C korpusesse, su taga aga D korpus."
    menu move:
        "*D korpusesse*":
            n "Sisened D korpusesse."
            jump sport
        "*Edasi*":
            m "Lähed edasi"
            jump sleepy
        "*Sööklasse*":
            jump fod

label Ckorpopts:
    scene ckorpent
    menu movenew:
        "*D korpusesse*":
            n "Sisened D korpusesse."
            jump sport
        "*Edasi*":
            m "Lähed edasi"
            jump sleepy
        "*Sööklasse*":
            jump fod

label Ckorpoptsnew:
    scene ckorpent
    menu movenewnew:
        "*D korpusesse*":
            n "Sisened D korpusesse."
            jump sportnew
        "*Edasi*":
            m "Lähed edasi"
            jump sleepy
        "*Sööklasse*":
            jump fod

label Ckorpoptsnewnew:
    scene ckorpent
    menu movenewnewII:
        "*D korpusesse*":
            n "Sisened D korpusesse."
            jump sportnew
        "*Edasi*":
            m "Lähed edasi"
            jump sleepy
        "*Sööklasse*":
            jump fodnew

label sport:
    scene dakorp
    n "Oled D korpuses."
    n "Näed, et keegi mängib saalis. Ta märkab sind ja tuleb su juurde."
    show Ssmirk at center
    u "Hei!"
    m "...hei"
    hide Ssmirk
    show Sidle at center
    u "Uus oled?"
    m "Jep."
    hide Sidle
    show Ssmirk at center
    u "Lahe! Hea näha uusi inimesi siin jälle."
    m "Kes sa oled?"
    u "olen Sass!"
    m "Ja mis see kõik on?"
    hide Ssmirk
    show Sidle at center
    s "See on jõusaal ja spordihoone."
    m "Ja kõik?"
    s "Jap."
    menu Sassquestions:
        "Mis kursusel oled?":
            hide Sidle
            show Ssmirk at center
            s "Kolmandas."
            hide Ssmirk
            show Sidle at center
            jump Sassquestions
        "Mis eriala õpid?":
            s "Keevitust."
            menu odd:
                "Ega ei ole kõik keevitajad idioodid?":
                    call increase from _call_increase_2
                    hide Sidle
                    show Ssmirk at center
                    s "Naljakas. Mulle meeldib."
                    s "Suurem osa, natuke, aga üldiselt nad pole pahad."
                    hide Ssmirk
                    show Sidle at center
                    jump oddnew

                "Keevitaja olla on vist tore, eks?":
                    hide Sidle
                    show Ssmirk at center
                    s "muidugi. Sa saad metalliga mässata, muidugi on tore!"
                    hide Ssmirk
                    show Sidle at center
                    jump oddnew

                "Kõik peaksid suhtuma sinusse hästi, eks?":
                    call decrease from _call_decrease_2
                    hide Sidle
                    show Sannoyed at center
                    s "Muidugi mitte."
                    s "Keevitajad on need, kes lihtsalt tulid, sest pidid minema, teiste arvates, vot miks on neid nii palju."
                    hide Sannoyed
                    show Sidle at center
                    jump oddnew
        "*Edasi*":
                menu oddopts:
                    "*C korpusesse*":
                        jump move

    menu oddnew:
        "Mis kursusel oled?":
            hide Sidle
            show Ssmirk at center
            s "Kolmandas."
            hide Ssmirk
            show Sidle at center
            jump Sassquestions

        "*Edasi*":
                menu oddoptsnew:
                    "*C korpusesse*":
                        jump Ckorpoptsnew

label sportnew:
    scene dakorp
    show Sidle at center
    s "..."
    jump Ckorpoptsnewnew

label fod:
    scene food
    n "Lähed sööklasse."
    n "Tühi on, peale ühe inimese."
    show Richidle at center
    m "Noh, Tšau."
    hide Richidle
    show Richsmile at center
    h "Tšau, tšau!"
    hide Richsmile
    show Richidle
    n "ega sa küsima hakka, mis söökla on? seal söövad, seda teavad kõik."
    menu Ricardquestions:
        "Mis kursusel oled?":
            hide Richidle
            show Richidle at center
            h "Esimesel."
            hide Richidle
            show Richidle at center
            jump Ricardquestions
        "Mis eriala õpid?":
            hide Richidle
            show Richsmile at center
            h "Automaatikat!"
            hide Richsmile
            show Richidle at center
            menu auto:
                "Ega ei ole automaatika lihtsalt täiskasvanute robootika?":
                    call increase from _call_increase_3
                    hide Richidle
                    show Richsmile at center
                    h "Oih! Nüüd seda ma kuulnud küll ei ole! Päris naljakas!"
                    hide Richsmile
                    show Richidle at center
                    jump autonew
                "Tore ka on?":
                    hide Richidle
                    show Richfrown at center
                    h "Noh, nii ja naa, aga mõned asjad võivad päris huvitavad olla."
                    hide Richfrown
                    show Richidle at center
                    jump autonew
                
                "Mille jaoks on sul seda üldse vaja?":
                    call decrease from _call_decrease_3
                    hide Richidle
                    show Richfrown at center
                    h "Sest huvitav ja vajalik on! Automaatikuid on väga vaja nüüd!"
                    hide Richfrown
                    show Richidle at center
                    jump autonew

        "*Edasi*":
            jump Ckorpopts


    menu autonew:
        "Mis kursusel oled?":
            hide Richidle
            show Richidle at center
            h "Esimesel."
            hide Richidle
            show Richidle at center
            jump Ricardquestions

        "*Edasi*":
            jump Ckorpoptsnewnew

label fodnew:
    scene food
    show Richidle at center
    h "..."
    jump Ckorpoptsnew


label sleepy:
    scene ckorpswi
    n "Olete sisenenud hoone C koridori."
    n "Ja sa kuulsid kohe, et keegi magas."
    show kdsleep at center
    u "*Zzz*"
    m "Oh, ta magab, ma arvan, et oleks hea mõte ta üles äratada"
    menu WAKEUP:
        "Ärata ta üles":
            jump waking
        "Jäta ta rahule":
            call increase from _call_increase_4
            n "Arvad, et jätad ta rahule"
            n "Otsustasid minna B korpusesse"
            jump Bkorpus

label waking:
    show kdsleep
    m "Hei, ärka üles!"
    "..."
    m "Noh! ärka!"
    hide kdsleep
    show kdawake at center
    u "eh?"
    u "mis sul vaja on?"
    m "Tšau. Miks sa siin üldse magad?"
    hide kdawake
    show kdasmirk at center
    u "Ma tahan magada, sellepärast"
    hide kdasmirk
    show kdamad at center
    u "Ma töötasin 3 päeva järjest ilma magamata ühe programmi peal, ÜHE peal."
    m "Noh see on nõme."
    m "Kuule, kas sa tead, mis on 2. ja 3. korrusel?"
    hide kdamad
    show kdawake at center
    u "Ja sellepärast sa mind äratasid?"
    hide kdawake
    show kdamad
    u "...jumal."
    scene end
    "aga mis su nimi on?"
    "KD."
    "...Ka Dee?"
    "...Ei. Kay Dii."
    "Ah. KD."
    "Ja sina oled...?"
    "Andrei."
    n "Te läksite teisele korrusele"
    scene ckorpu
    show kdidle at center
    kd "Lühidalt, sa ei leia midagi peale kott-toolide, pinkide ja kapide"
    hide kdidle
    show kdsmile at center
    kd "Kuigi seal on üks huvitav klass, kus lauad pole nagu teistes klassides."
    hide kdsmile
    show kdidle at center
    m "Selge..."
    m "Lähme siis kolmandale korrusele?"
    hide kdidle
    show kdwtf at center
    kd "Ja kas sa arvad tõsiselt, et kolmandal korrusel tuleb midagi teistmoodi?"
    hide kdwtf
    show kdidle at center
    kd "Ei. Parem näitan sulle null korrust"
    m "Kus see on?"
    hide kdidle
    show kdwtf at center
    kd "Kas sa küsisid seda tõsiselt? Kas sul pole isegi aimu, kus see olla võib?"
    m "Okei okei, loll küsimus."
    scene ckorpb
    n "Te lähete alla 0. korrusele"
    show kdidle at center
    kd "Ja siin on lauatenniselaud."
    hide kdidle
    show kdwtf at center
    kd "Nad ei anna sulle reketeid ega tennisepalle."
    hide kdwtf
    show kdsmirk at center
    kd "Kuigi kui sul nad on, mida ma loodan, et sul on, siis saame mängida ühe mängu."
    m "Kahjuks mul neid esemeid pole."
    hide kdsmirk
    show kdidle at center
    kd "Noh, see tähendab, et ma lähen uuesti magama."
    m "Noh, aitäh, et vähemalt ennast näitasid."
    kd "Peaasi, et mind üles ei ärataks."
    hide kdidle
    scene ckorpswi
    n "Te läksite tagasi esimesele korrusele."
    n "KD läks toolile magama"
    n "Ja sa otsustasid minna B korpusesse"
    jump Bkorpus

label Bkorpus:
    scene bkorp
    n "Jõudsid B korpusesse ja said kohe aru, kui kitsas ta on võrreldes teiste korpustega."
    n "Näed, et keegi tuleb su juurde."
    show ririidle at center
    u "Tšau!"
    m "Tšau."
    m "Enne kui sa küsid; jah, olen uus."
    hide ririidle
    show ririhappy at center
    u "Paljud küsisid seda juba?"
    hide ririhappy
    show ririidle
    m "Muidugi."
    m "Kes sa siis oled?"
    hide ririidle
    show ririhappy at center
    u "Olen Riri."
    m "Kena."
    hide ririhappy
    show ririidle at center
    menu ririquestions:
        "Mis kursusel oled?":
            hide ririidle
            show ririhappy at center
            ri "Kolmandal."
            hide ririhappy
            show ririidle at center
            jump ririquestions

        "Mis eriala õpid?":
            hide ririidle
            show ririidle at center
            ri "Õpin juuksuriks."
            menu hairq:
                "Ega sa erinevaid haigusi ei saa juuksurina olles?":
                    call decrease from _call_decrease_4
                    hide ririidle
                    show ririmad at center
                    ri "idioot oled või?"
                    ri "väga harva saab igasugusi haigusi läbi minu töö."
                    hide ririmad
                    show ririidle at center
                    jump ririquestionsnew

                "Huvitav on, eks?":
                    call increase from _call_increase_5
                    hide ririidle
                    show ririhappy at center
                    ri "Muidugi! Kogu aeg saab uusi asju provida, väga lahe on!"
                    hide ririhappy
                    show ririidle at center
                    jump ririquestionsnew

                "Mõtled edasi juuksurina tööle minna kah?":
                    hide ririidle
                    show ririhappy at center
                    ri "Loodan küll!"
                    hide ririhappy
                    show ririidle at center
                    jump ririquestionsnew

        "*Edasi*":
            jump LastChoice

    menu ririquestionsnew:
        "Mis kursusel oled?":
            hide ririidle
            show ririhappy at center
            ri "Kolmandal."
            hide ririhappy
            show ririidle at center
            jump ririquestions

        "*Edasi*":
            jump LastChoice

label LastChoice:
    hide ririidle
    n "Noh, nüüd on sul kõik läbi vaadatud, vist."
    n "Võid minema hakata."
    menu:
        "Välju B korpuse kaudu.":
            n "Läksid kohe õue."
            n "Kõnnid kuni näed kooli peaust."
            jump Conclusion
        "Välju C korpuse kaudu.":
            scene ckorpswi
            n "Oled tagasi C korpuses."
            n "Nägid KD jälle toolil magamas."
            n "Kuid sa otsustasid teda mitte äratada, sa ei tea kunagi, mida ta sinuga teeb."
            n "Kõndisid edasi, kuni nägid ust tänavale."
            n "Sa läksid C korpusest välja ja kõnnid kuni näed kooli peaust."
            jump Conclusion
        "Välju F korpuse kaudu.":
            scene fkorpo
            n "Oled tagasi F-korpuses."
            n "ja näed, et Liia kohtus sinuga jälle"
            show Liiaidle at center
            l "Tšau veel kord, siis."
            m "Tšau."
            l "Kuidas C korpuses oli?"
            m "Noh, okei oli, ma tegelesin lollustega"
            hide Liiaidle
            show Liiasmirk at center
            l "Ma näen seda küll"
            m "Muideks, kas ma ei jätnud midagi vahele?"
            hide Liiasmirk
            show Liiaidle at center
            l "Ei"
            m "Hästi. Ma lähen siis koju. Edu"
            hide Liiaidle
            show Liiasmirk at center
            l "Jah, sama sulle"
            hide Liiasmirk
            n "Ja siis sa läksid majast läbi F korpuse välja."
            jump Conclusion

label Conclusion:
    scene ent
    n "Oled nüüd tänaval"
    n "Ja lähed südamerahuga koju"
    scene end
    n "Kõik"
    n "Selle mängu lugu on läbi"
    n "Loodan, et sulle meeldis see, mida me selle aja jooksul tegime."
    if gen_rating <= -3:
        jump BadEnding
    elif -3 < gen_rating < 2:
        jump NeutralEnding
    elif gen_rating >= 2:
        jump GoodEnding
label BadEnding:
    n "Aga noh,"
    n "kuna sa solvasid kõiki, ei taha keegi sind isegi näha."
    n "Sa mõistsid seda kohe ja otsustasid seetõttu sinna mitte minna."
    n "Ja ma arvan, et sinust saab mingi korrapidaja, või Hesburgeri töötaja."
    n "Vali paremaid teekondi järgmine kord."
    n "Aitäh mängimast!"
    return

label NeutralEnding:
    n "Kuna sind võtsid päris normaalselt vastu,"
    n "Sulle on määratud sisseastumiseksam ja vestlus."
    n "Tulid sel ajal."
    n "Kirjutasid sisseastumiseksami ja sooritasid ivestluse ja..."
    n "Sa ei suutnud."
    n "Otsustasid oma arengu nimel õhtukooli minna."
    n "Kuid sul on vedanud, et olid teistega sõbraks saanud ja seetõttu suhtled nendega."
    n "Aitäh mängimast!"
    return

label GoodEnding:
    n "Palju õnne!"
    n "Oled otsustanud IVKHK-ga liituda pärast sisseastumiseksami ja vestluse sooritamist!"
    n "Arvasid, et sõpru on raske leida, kuid eksisid,"
    n "Kuna sa said seal sõpru juba enne, kui siia sisenesid."
    n "Ja ma õnnitlen sind, et suutsid saavutada kõrge hinnangu ja saada hea lõpu!"
    n "Ja..."
    n "Aitäh mängimast!"
    return