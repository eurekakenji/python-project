# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("???")
define h = Character("unknown")
define e = Character("Scout")
define m = Character("Main")
define t = Character("Pyro")
define y = Character("Liia")
define d = Character("Dictator")
define b = Character("Raamatukoguhoidja")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene r

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # Dialouges yippe!
    d "Ilus koolipäev, eks?"
    menu:
        "*Sisenen F korpusesse*":
            d "Sisened F korpusesse"
        "*Pööran ümber ja lähen koju*":
            d "..."
            "Vau"
            "Lihtsalt vau"
            "ehk sina tea, et kui sa lihtsalt keerad perse ukse poole ja sihkertad koju tagasi, et mängu ei toimu ju?"
            menu:
                "Tõsiselt? Oih.":
                    d "vot. {i}ahem{/i},"
                    "Sisened F korpusesse"
                "Mul savi":
                    d "..."
                    "meil ka savi, tõsiselt"
                    "meil on türa 16. juunini vaja ära teha, me oleksime midagi pannud siia texti mõttes aga meil on kiire, vot sulle su {i}easter egg{/i}."
                    return
    d "Olete F korpuses."
    "Vasakul pool on riietusruum, sirge trepp teisele korrusele ja kuulipilduja, paremal toolid. Kuhu sa esimesena lähed?"
    menu:
        "Riietusruumi":
            d "Sisened riietusruumi, võtad seljast õueriided ja riputad nad riietuspuu külge."
        "Maja F 2 korrusele":
            d "Kas te ei taha kunagi ülerõivaid seljast võtta? Noh, nagu soovite"
            d "Mõni inimene läheneb sulle"
        "Mine kooli automaati":
            d "Kas sul on raha?"
            menu:
                "Jah":
                    d "Lähed masina juurde ja ostad endale midagi."
                    "Järsku läheneb sulle keegi."
                "Ei":
                    d "Lähete masina juurde ja ootate, kuni nad teile mõne toote jaoks vahetusraha annavad."
                    "geenius."
                    "Näed kedagi masinale lähenemas ja ütled talle tere, lootes, et ta annab sulle raha."
        "Ma lähen istuma":
            d "Sa istusid toolile."
            "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
            menu:
                "Puhkan veidi":
                    d "Tõused püsti ja keegi läheneb sulle kohe"
                "...":
                    d "Keegi läheneb sulle."
        "Lähen koju":
            d "."
            d "."
            d "😭"
            return
    # These display lines of dialogue.

image Liia = im.Scale("Liia.jpg", 500, 900)
show Liia at center
u "Tšau."
m "Noh tšau. Mis su nimi on?"
y "Liia. Uus oled või?"
menu liiaintro:
    "Noh jah":
        y "Nagu arvasinki."
        m "Kus ma olen siis? oled siin kaua õppind?"
        y "Kolmas kursus, jah, olen kaua olnd. oled F korpuses."
        m "Mis siis F korpuses on?"
        y "Siin on peamiselt mehhaanikud ja keevitajad, see on see suur praktika korpus, siin veel käivad IT tüübid ka, arvuti klassid on olemas küll."
        m "Selge, aga siis siit midagi muud ei ole peale seda?"
        y "Su taga on E korpus, minu taga aga raamatukogu, kust saad raamatu või õpiku võtta."
        menu questions:
            "Kogu aeg nii väsind oled või?":
                y "ega kas programmeeria ole programmeeria kui ta ei ole iga päev oma päeva kõige madalamas punktis ja ei maga stressi tõttu?"
                m "noh. jah."
                jump questions
            "Mis eriala õpid?":
                y "Tarkvaraarendust. Ei soovitaks kui sulle meeldib psüühikat hoida. statistilest suurem osa programmeeriatest läksid oma eialale, sest vihkavad ennast."
                jump questions
            "Oma erialaga saad hästi hakkama?":
                y "Noh, nagugi iga inimene, päris normaalselt."
                m "Ega midagi raskusi ei too?"
                y "Ja veel ütle, et hobused lennata oskavad, muidugi on raskusi, ega see lihtne asi ole."
                m "arusaadav."
                jump questions
            "*tagasi menüü juurde*":
                jump liiaintro
    "Oota":
        m "Ok, ma ootan."
        jump WayLibrary
        menu:
            "Mine välja ja ütle sellele inimesele":
                                                m "Ei, see võtab kaua aega. Ma ütlen sellele inimesele, et mul pole seda ja võib-olla jätab ta mu rahule."
                                                d "Sa lahkud raamatukogust ja lähed selle inimese juurde."
                                                y "Hei, kas sa tulid kiiresti tagasi ja võtsid raamatu?"
                                                m "Ei, teda polnud seal"
                                                y "Kas sa ei võiks teda lihtsalt oodata?"
                                                m "Saaks küll, aga see võtaks kaua aega ja ma ei taha oma aega raisata ainult raamatukoguhoidja ootamisele."
                                                y "Ta naaseb alati 10 minuti jooksul."
                                                m "Veennud."
                                                d "Lähed tagasi raamatukokku"
                                                jump WayLibrary
            "Varastada raamat":
                            m "Kuigi selline võimalus on olemas."
                            d "Võtsid raamatu ja jooksid raamatukogust minema."
                            m "JOOKSE MINU JÄRELE!"
                            d "Jooksete tundmatusse sihtkohta, kuid teil õnnestus põgeneda enne, kui ta naasis."
                            y "Oot, mis juhtus?"
                            m "Varastasin raamatu ja pidin minema."
                            d "Vaatad raamatu kaant."
                            m ".... ja võtsin Cole ja Lohe Päästesalk."
                            "Olgu, kuulge, ma ei tea, mis raamat see on."
                            y "Lol, sa oled nüüd lindprii, ah?"
                            m "Jah jah, ole vait"
                            y "Ära pabista. Siin on 5 eurot raamatu kohta. Muide, raamatukogu juures oli videovalvekaamera ja see salvestas, kuidas sa raamatu varastasid."
                            m "Mind ei huvita, kui nad kahtlustavad sind varguses, sa ei saa praegu raamatukokku minna, aga 5 eurot on 5 eurot. Aitäh"
                            y "Nüüd oli karm. Ma lähen F-hoone teisest sissepääsust."
                            d "Ta läheb alla."
                            jump EkorpusII
            "Ei": 
                y "No sa oled vastik :("
                jump EkorpusII
label WayLibrary:
    d "Ootate raamatukoguhoidjat tagasi."
    "Ja ootad"
    "Ja ootad...."
    "Näete, et ta tuleb sisse ja istub oma kohale. Sa lähened talle"
    m "Tere, kas saaksite mulle ühe raamatu kinkida? Mu sõber otsib just retseptiraamatut, sest talle meeldib süüa teha."
    b "Tere. Jah, meil on retseptiraamat. Kui kaua teil selle raamatu tagastamiseks aega kulub?"
    m "3 nädala pärast."
    d "Ta annab teile täitmiseks lehe."
    b "Hästi. Palun kirjutage sellele paberile oma ees- ja perekonnanimi ning allkiri."
    d "Sa hakkad kirjutama, mida ta ütles."
    b "See on kõik, võtke retseptiraamat."
    m "Aitäh!"
    d "Võtsid raamatu ja läksid sõbra juurde. See polnud nii raske, ah?"
    y "Noh, kas sa võtsid raamatu?"
    m "Jah, siin on raamat"
    y "Suurep- oodake. Kas võtsite retseptiraamatu tõsiselt kätte?"
    "Saate aru, et ma ei ole kokanduse fänn, eks?"
    m "Noh, loogiliselt võttes on see juba teie süü, kuna te ei täpsustanud, millist raamatut võtta."
    y "Õiglane. Olgu, sul on abi eest 5 eurot."
    m "Vau. 5 eurot nii lihtsa ülesande eest? Aitäh!"
    jump EkorpusII

label EkorpusII:
    "Niisiis, kus ma olen?"
    d "Vaatad ringi ja näed E-tähte"
    m "Olen vist E korpuses"
    "Tahtsin järsku tualetti minna. Loodan, et siia tuleb tualett."
    d "Jalutad E-hoones ringi, et leida tualett."
    "Leidsid tualeti, sisenesid"
    "Ja läks välja"
    m "Oh, ja ma nägin seal laborit, tahtsin alati keemias katsetada"
    d "Lähed laborisse, sisened sinna ja näed kohe vedelikega kolbe"
    m "Vau, kolvid"
    "Huvitav, mis siis, kui ma need omavahel segan."
    d "Huvitav, mis siis, kui ma need omavahel segan."
    m "Oh pagan, ma arvan, et mul on probleeme."
    "Seda ainult siis, kui"
    menu:
        "Peida":
            d "Leiad suurepärase koha peitmiseks"
            "Järsku tuleb keegi sisse. Sa ei saa aru, milline ta välja näeb, aga sa võid vaadata tema varju"
            d "(sel hetkel peaks olema paus.)"
            m "Pheh, tundub, et ta on läinud"
            "Eei, see oleks minu jaoks ohtlik."
            d "Sa lahkusid laborist ja läksid esimesele korrusele."
            jump EkorpusI
        "Lahkuge kontorist":
            m "Ma pean kiiresti välja minema."
            d "Näete teda ukse lähedal seismas"
            "Avad ukse ja sind märgatakse kohe."
            jump MAD
        "Sulgege kontor":
            m "Oh ma tean, ma panen kontori kinni"
            d "Paned kontori ukse kinni."
            t "Oeh olgu. Ma ei sulgenud seda kontorit, kuidas see suleti?"
            "Ja mul pole võtit. Kurat, ma pean võtme järele tagasi minema."
            m "Kas ta on lahkunud?"
            ".... omamoodi jah"
            d "Lahkud laborist ja lähed kohe alla, enne kui keegi sind märkab."
            jump EkorpusI
        "Mõtle":
            m "Kurat, mida ma peaksin tegema..."
            d "Ta astub laborisse ja märkab sind"
            jump MAD

label MAD:
    t "Kes sa oled?"
    m "Emmm"
    t "Ma küsin, kes sa oled?"
    m "Ma?"
    t "Ära ole rumal, ma ei näe kedagi peale sinu"
    m "Minu nimi on...."
    "Peter Griffin"
    t "..."
    m "Andrei Vorobjov.."
    t "See on teine ​​teema."
    "Selgitage, miks te siin olete ja miks tahtsite kolvid võtta?"
    menu:
        "Räägi tõtt":
            m "Tead, ma olen alati tahtnud midagi teha laboris ja üldse keemias."
            m "Meil polnud koolis ainsatki laboratoorset tööd, vaid ainult mõned ülesanded."
            m "Kui laborit nägin, tekkis tahtmine kohe midagi teha."
            t "Ja?"
            m "Mida sa silmas pead?"
            t "Jumal küll, kui tahad midagi teha, aga küsi enne minult, sest ma ei saa kedagi üksi jätta järelevalveta."
            "Palun tulge nüüd laborist välja."
            jump EkorpusI
        "Räägi valet":
            m "Mu ülemus palus mul kolvid tuua"
            t "Ma uskusin seda"
            m "Ma kinnitan teile, et ta küsis minult."
            t "Jah? Ja mis ta nimi on?"
            m "..."
            "Ma ei mäleta, aga mäletan, et ta istub alati F206-s."
            t "Oota siin."
            d "Ta lahkus kontorist."
            m "See on minu võimalus olukorrast põgeneda."
            d "Lahkute kontorist ja lähete esimesele korrusele."
            jump EkorpusI

label EkorpusI:

return