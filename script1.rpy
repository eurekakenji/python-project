# The script of the game goes in this file.


# character section
define u = Character("???")
define un = Character("unknown")
define s = Character("Sass")
define m = Character("Main")
define j = Character("Jeremy")
define l = Character("Liia")
define n = Character("Narrator")
define b = Character("Raamatukoguhoidja")
define r = Character("Richard")
define d = Character ("Dan")

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
    d "Ilus koolipäev, eks?"
    menu:
        "*Sisenen F korpusesse*":
            n "Sisened F korpusesse"
        "*Pööran ümber ja lähen koju*":
            n "..."
            "Vau"
            "Lihtsalt vau"
            "ehk sina tea, et kui sa lihtsalt keerad perse ukse poole ja sihkertad koju tagasi, et mängu ei toimu ju?"
            menu:
                "Tõsiselt? Oih.":
                    n "vot. {i}ahem{/i},"
                    "Sisened F korpusesse"
                "Mul savi":
                    n "..."
                    "meil ka savi, tõsiselt"
                    "meil on türa 16. juunini vaja ära teha, me oleksime midagi pannud siia texti mõttes aga meil on kiire, vot sulle su {i}easter egg{/i}."
                    return
    scene fkorpo
    n "Olete F korpuses."
    "Vasakul pool on riietusruum, sirge trepp teisele korrusele ja kuulipilduja, paremal toolid. Kuhu sa esimesena lähed?"
    menu:
        "Riietusruumi":
            scene cloth 
            n "Sisened riietusruumi, võtad seljast õueriided ja riputad nad riietuspuu külge."
        "Maja F 2 korrusele":
            n "Kas te ei taha kunagi ülerõivaid seljast võtta? Noh, nagu soovite"
            n "Mõni inimene läheneb sulle"
        "Mine kooli automaati":
            n "Kas sul on raha?"
            menu:
                "Jah":
                    n "Lähed masina juurde ja ostad endale midagi."
                    "Järsku läheneb sulle keegi."
                "Ei":
                    n "Lähete masina juurde ja ootate, kuni nad teile mõne toote jaoks vahetusraha annavad."
                    "geenius."
                    "Näed kedagi masinale lähenemas ja ütled talle tere, lootes, et ta annab sulle raha."
        "Ma lähen istuma":
            n "Sa istusid toolile."
            "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
            menu:
                "Puhkan veidi":
                    n "Tõused püsti ja keegi läheneb sulle kohe"
                "...":
                    n "Keegi läheneb sulle."
        "Lähen koju":
            n "."
            n "."
            n "😭"
            return
    # These display lines of dialogue.


show Liia at center
    u "Tšau."
    m "Noh tšau. Mis su nimi on?"
    y "Liia. Uus oled või?"
menu:
    "noh jah":
        y "nagu arvasinki."
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
    "Teoorias nagu tean mida teen...":
        y "noh see küll üllatus."
        hide Liia
        menu options:
            "Raamatukogu":
                        jump WayLibrary
            "E korpus":
                    jump EkorpusII
            "Ei": 
                y "No sa oled vastik :("
                jump EkorpusII
        menu:
            "Mine välja ja ütle sellele inimesele":
                                                m "Ei, see võtab kaua aega. Ma ütlen sellele inimesele, et mul pole seda ja võib-olla jätab ta mu rahule."
                                                n "Sa lahkud raamatukogust ja lähed selle inimese juurde."
                                                y "Hei, kas sa tulid kiiresti tagasi ja võtsid raamatu?"
                                                m "Ei, teda polnud seal"
                                                y "Kas sa ei võiks teda lihtsalt oodata?"
                                                m "Saaks küll, aga see võtaks kaua aega ja ma ei taha oma aega raisata ainult raamatukoguhoidja ootamisele."
                                                y "Ta naaseb alati 10 minuti jooksul."
                                                m "Veennud."
                                                n "Lähed tagasi raamatukokku"
                                                jump WayLibrary
            "Varastada raamat":
                            m "Kuigi selline võimalus on olemas."
                            n "Võtsid raamatu ja jooksid raamatukogust minema."
                            m "JOOKSE MINU JÄRELE!"
                            n "Jooksete tundmatusse sihtkohta, kuid teil õnnestus põgeneda enne, kui ta naasis."
                            y "Oot, mis juhtus?"
                            m "Varastasin raamatu ja pidin minema."
                            n "Vaatad raamatu kaant."
                            m ".... ja võtsin Cole ja Lohe Päästesalk."
                            "Olgu, kuulge, ma ei tea, mis raamat see on."
                            y "Lol, sa oled nüüd lindprii, ah?"
                            m "Jah jah, ole vait"
                            y "Ära pabista. Siin on 5 eurot raamatu kohta. Muide, raamatukogu juures oli videovalvekaamera ja see salvestas, kuidas sa raamatu varastasid."
                            m "Mind ei huvita, kui nad kahtlustavad sind varguses, sa ei saa praegu raamatukokku minna, aga 5 eurot on 5 eurot. Aitäh"
                            y "Nüüd oli karm. Ma lähen F-hoone teisest sissepääsust."
                            n "Ta läheb alla."
                            jump EkorpusII
            "Ei": 
                y "No sa oled vastik :("
                jump EkorpusII
label WayLibrary:
    n "Ootate raamatukoguhoidjat tagasi."
    "Ja ootad"
    "Ja ootad...."
    "Näete, et ta tuleb sisse ja istub oma kohale. Sa lähened talle"
    m "Tere, kas saaksite mulle ühe raamatu kinkida? Mu sõber otsib just retseptiraamatut, sest talle meeldib süüa teha."
    b "Tere. Jah, meil on retseptiraamat. Kui kaua teil selle raamatu tagastamiseks aega kulub?"
    m "3 nädala pärast."
    n "Ta annab teile täitmiseks lehe."
    b "Hästi. Palun kirjutage sellele paberile oma ees- ja perekonnanimi ning allkiri."
    n "Sa hakkad kirjutama, mida ta ütles."
    b "See on kõik, võtke retseptiraamat."
    m "Aitäh!"
    n "Võtsid raamatu ja läksid sõbra juurde. See polnud nii raske, ah?"
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
    n "Vaatad ringi ja näed E-tähte"
    m "Olen vist E korpuses"
    "Tahtsin järsku tualetti minna. Loodan, et siia tuleb tualett."
    n "Jalutad E-hoones ringi, et leida tualett."
    "Leidsid tualeti, sisenesid"
    "Ja läks välja"
    m "Oh, ja ma nägin seal laborit, tahtsin alati keemias katsetada"
    n "Lähed laborisse, sisened sinna ja näed kohe vedelikega kolbe"
    m "Vau, kolvid"
    "Huvitav, mis siis, kui ma need omavahel segan."
    n "Huvitav, mis siis, kui ma need omavahel segan."
    m "Oh pagan, ma arvan, et mul on probleeme."
    "Seda ainult siis, kui"
    menu:
        "Peida":
            n "Leiad suurepärase koha peitmiseks"
            "Järsku tuleb keegi sisse. Sa ei saa aru, milline ta välja näeb, aga sa võid vaadata tema varju"
            n "(sel hetkel peaks olema paus.)"
            m "Pheh, tundub, et ta on läinud"
            "Eei, see oleks minu jaoks ohtlik."
            n "Sa lahkusid laborist ja läksid esimesele korrusele."
            jump EkorpusI
        "Lahkuge kontorist":
            m "Ma pean kiiresti välja minema."
            n "Näete teda ukse lähedal seismas"
            "Avad ukse ja sind märgatakse kohe."
            jump MAD
        "Sulgege kontor":
            m "Oh ma tean, ma panen kontori kinni"
            n "Paned kontori ukse kinni."
            t "Oeh olgu. Ma ei sulgenud seda kontorit, kuidas see suleti?"
            "Ja mul pole võtit. Kurat, ma pean võtme järele tagasi minema."
            m "Kas ta on lahkunud?"
            ".... omamoodi jah"
            n "Lahkud laborist ja lähed kohe alla, enne kui keegi sind märkab."
            jump EkorpusI
        "Mõtle":
            m "Kurat, mida ma peaksin tegema..."
            n "Ta astub laborisse ja märkab sind"
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
            n "Ta lahkus kontorist."
            m "See on minu võimalus olukorrast põgeneda."
            n "Lahkute kontorist ja lähete esimesele korrusele."
            jump EkorpusI
    
label EkorpusI:
    m "Esimene korrus.. Huvitav"
    "Ei, noh, kui ma kuskile ei peida, võivad nad mu üles leida."
    n "Vaatad ringi ja näed kuskil uksi"
    m "Noh, ma arvan, et kui ma nende uste taha peitun, siis ta ei leia mind?"
    n "Otsustasite end ukse taha peita."
    "Otsustasite kontoris ringi vaadata ja saite aru, et see on köök."
    m "Jama. Selle aja jooksul jõudsin nälga jääda."
    m "Ma lähen valmistan endale midagi."
    e "Mitte minu nugadega."
    menu TINIBDD:
        "Kes...":
            m "Kes sa oled ja kuidas sa siia sattusid?"
            e "Loogiliselt võttes peaksin sinult küsima."
            m "See ei tohiks teid muretseda."
        "Olgu...":
            m "Olgu, ma teen endale snäki."
            e "Tundub, et sind ei huvita tõsiasi, et ma siin seisan."
            m "Mind ei huvita."
    m "Ma olen tegelikult näljane."
    e "Noh... sa näed välja nagu TikToker, kes juhib süüdistust, et paks olemine on 'keha positiivne' ja et 'väidetavalt' sööte ainult tervislikku toitu."
    "Kui tahad normaalselt süüa ja gastriiti mitte haigestuda, siis saan aidata ühe roa retseptiga."
    menu Food:
        "Olgu, ma kuulan":
            e "Mul on üks retsept."
            "See roog saab olema Kreeka salat."
            "See valmib väga kiiresti, seega piisab 5-10 minutist."
            menu Salad:
                "Ma üritan.":
                    e "Niisiis."
                    "Tomatid..."
                    n "Ta lõikab tomatid tükkideks."
                    e "Kurgid...."
                    n "Ta lõikab kurgi kolmnurkadeks."
                    e "Jääsalat..."
                    n "Ta lõikab salati väikesteks tükkideks."
                    e "Juustud Feta...."
                    n "Ta lõikab fetajuustu kuubikuteks."
                    e "Punane sibul..."
                    n "Ta lõikab punase sibula õhukesteks poolrõngasteks."
                    e "Ja oliiviõli..."
                    n "Ta lisab salatile veidi oliiviõli."
                    "Ta segab kõik kokku."
                    e "TA-dah! Siin on salat, naudi."
                    n "Ta annab sulle proovimiseks salatit."
                    "Sa sööd salatit."
                    e "Noh? Kuidas salatiga läheb?"
                    menu taste:
                        "Nii maitsev.":
                            e "Ma ütlesin sulle, et mulle meeldiks"
                            n "Sõid oma salati südamerahus ära."
                            m "Noh, mul on kõht täis. Tänan teid väga."
                            e "Jah. Nüüd palun mine ära, ma ei taha, et me mõlemad hätta jääme."
                            m "Olgu olgu. Edu"
                            jump FIP2
                        "Hästi":
                            e "See tähendab, et ma tegin täna hästi süüa."
                            n "Otsustasite selle kõik ära süüa."
                            m "Noh, mul on kõht täis. Ma lähen kaugemale, kuhu mu silmad mind viivad."
                            e "Jah. Ja kiiresti, ma ei taha jääda vahele, et lihtsalt kellelegi midagi valmistasin."
                            jump FIP2
                        "Оeh..":
                            e "Raiskasin salati koostisosad, mida keegi ei söö. Klass"
                            m "Vau, ära pane pahaks."
                            e "No muidugi, Body Positive'ile salateid ei meeldi."
                            jump BODI

                "Ei aitäh":
                    e "No muidugi, Body Positive'ile salateid ei meeldi."
                    jump BODI

        "Mul on vaja kiirustada":
            jump BODI

label BODI:
    "Noh, söö oma doshirak ära."
    "Ei, tead mida, tule köögist välja."
    m "Okei"
    n "Lahkusite, sest mõistsite, et kui jääte, tuleb siin tõsiseid jõukatsumisi."

label FIP2:
    y "Aga me nägime teineteist jälle."
    m "Jah, ja nüüd kohtume jälle"
    y "Noh, nagu ma aru saan, olid sa E korpuses."
    "Nagu seal?"
    menu opinion:
        "Jah, see tundub normaalne.":
            y "Mul on hea meel, et teile E-juhtum meeldis"
            "Nüüd kus?"
            m "Soovita. Olin ainult kahes majas."
            y "Noh. võite minna jõusaali, kui soovite treenida."
            "Või võite minna C-hoonesse."
            "See on teie äranägemisel"
            menu NextPart:
                "Jõusaalis":
                    y "Hästi. Siis näete neid väikseid samme?"
                    m "Jah. Ma näen."
                    y "Ühesõnaga, sa tõused püsti ja kõnnid otse."
                    "Pärast seda minge vasakule, kus on uksed"
                    "Siis lähed otse ja lõpus keerad paremale."
                    m "Okei aitäh."
                    jump sport
                "C-koortel":
                    y "Hästi. Siis näete neid väikseid samme?"
                    m "Jah. Ma näen."
                    y "Ühesõnaga, sa tõused püsti ja kõnnid otse."
                    "ja siis keera paremale."
                    m "Okai aitäh"
                    jump CKorpI
        "Mitte.":
            y "Noh. ma saan sellest aru. Väga adekvaatseid inimesi seal minu arust ei ole."
            m "Jah ma saan aru. Kõik on millegipärast vihased."
            y "ja see on tõsi."
            "Kuhu sa nüüd lähed?"
            m "Soovita. Olin ainult kahes majas."
            y "Noh. võite minna jõusaali, kui soovite treenida."
            "Või võite minna C-hoonesse."
            "See on teie äranägemisel"
            jump NextPart

label CKorpI:
    n "Sa läksid C-hoonesse."
    n "C-hoone sissepääsu lähedal nägite ust, mis viib jõusaali."
    m "Või äkki..."
    menu nvm:
        "Jõusaalis":
            m "Mis takistab mind praegu jõusaalis käimast?"
            n "Sisened jõusaali."
            jump sport
        "Jätka":
            m "Mitte. tähenduses"
            jump CKorpIContinue

label sport:
    n "Olete sisenenud D-hoonesse"
    n "Kas sa ikka kõnnid..."
    m "Niisiis. Ta ütles mulle, et pärast D-hoonesse sisenemist pidin selle koridori lõpus paremale pöörama."
    m "Nagu ma aru saan, on see jõusaal."
    n "Enne kui jõuad siseneda, maandub pall sulle pähe."
    # Siin on üks tegelane, kas Dan või Sass või Jeremy
    u "Oih, vabandust"
    m "Mul ei olnud aega sisse tulla ja mul oli juba peavigastus."
    u "No, kurat, see pole minu süü, et ma ei saa tulevikku vaadata ega näe sind palliga pähe löömas."
    m "Sul on õigus. Mida sa üldse teed?"
    u "Mina? palli sisse"
    m "Äkki oskate öelda, millega täpsemalt tegelete?"
    u "Viskan palli rõngasse."
    m "Korvpall"
    u "Ahhh, okei"
    u "Mängime?"
    m "Nagu mul oleks valida."
    n "Hakkad korvpalli mängima"
    n "Viskasite edukalt rõngasse"
    n "Ta viskab ka rõngasse."
    n "Saate aru, et see mäng saab olema raske."
    n "Teie vastasel oli pall."
    n "Sa võtad temalt palli ära."
    n "Sa jõuad vastase rõngale lähedale."
    n "Valmistute palli rõngasse viskama ja..."
    "Aeg on läbi"
    m "Nii kiire?"
    u "Jah, ma panin selle 10 minutiks"
    m "Oh. Muide, meil on viik"
    u "Ma tean, ma tean"
    u "Noh. See oli lahe"
    m "Nõus. Olgu, ma lähen C hoonesse"
    u "Okei näeme"
    jump CKorpIContinue

label CKorpIContinue:
    n "Sa jätkasid oma teed"
    "Sa nägid allakäiku. Ja kummalisel kombel otsustasid sa alla minna"
    "Sa nägid seal joont."
    m "Hm. Tundub, et see on söögituba"
    n "Ootad, kuni järjekorda pole."
    n "Nägid, et seal on söömiseks õpilasluba vaja."
    n "Sul vedas, et sul oli õpilasluba."
    n "tulid üles, andsid kaardi ja..."
    "Piiks!"
    n "Teie kaart töötas. Jätkate oma teed toidu hankimiseks."
    n "Võtsid toidu ja istusid kuskile söögitoa taha."
    h "Kas ma võin sinuga istuda?"
    menu talbk:
        "Istu maha":
            h "Aitäh"
            m "Palun"
            jump moretalking
        "Ei":
            h "Olgu siis"
            n "Sõid südamerahus"
            n "Sa kandsid taldrikut ja kandikut"
            n "Lähete tagasi C-hoonesse."
            jump sleepy

label moretalking:
    h "Noh, mis su nimi on?"
    m "Andrei"
    h "See on selge"
    m "Mulle tundub imelik, et sa minuga maha istusid"
    h "Ma tõesti ei taha üksi süüa."
    h "Ja üldiselt nendega, kellega ma tavaliselt istun, on nad lihtsalt vait ja seetõttu muutub söögitoas söömine igavaks."
    m "Ma näen, aga mida sa minult ootad?"
    h "Oh, kas sa pole ka seltskondlik?"
    h "See valutab. Kas teil pole isegi huvitavaid lugusid?"
    m "Ei."
    h "isegi igavad?"
    m "isegi igavad."
    h "Ah ole nüüd."
    h "Olgu, kuulake mu lugu:"
    h "Ühel hetkel olin vanaemal külas"
    h "Selles külas oli tall hobustega"
    h "ma mõtlesin"
    h "'Mis siis, kui proovin hobusega ratsutada'"
    h "Niisiis, istusin hobuse selga ja sõitsin järve äärde."
    h "Kui olime järve lähedal, otsustas hobune ujuma minna"
    h "ja uppus..."
    m "See oli nali? või juhtus see tõesti?"
    h "See on nali. Ta viskas mu järve ja ma olin üleni märg."
    m "Oh haha.. ma ei tea, kas see oli naljakas?"
    h "Ma just rääkisin loo, see on sinu arvamus, kas see oli naljakas või mitte."
    h "Noh, ma olen toiduga läbi"
    h "Tänan teid veel kord, et lubasite mul teiega koos istuda."
    m "Võta meiega ühendust"
    n "Sa sõid kõike, mis taldrikul oli."
    n "Sa kandsid taldriku ja kandiku."
    n "Lähete tagasi C-hoonesse."

label sleepy:
    n "Olete sisenenud hoone C koridori."
    n "Ja sa kuulsid kohe, et keegi magas."
    u "*Norskab*"
    m "Oh, ta magab, ma arvan, et oleks hea mõte ta üles äratada"
    menu WAKEUP:
        "Ärata ta üles":
            jump waking
        "Jäta ta rahule":
            m "Olgu, ma lähen mööda."
            n "Otsustate minna teisele korrusele."
            n "Teisel korrusel näete rohkem kappe ja otomaneid"
            m "Okei.. ma lähen siis kolmanda juurde"
            n "Sa lähed kolmandale korrusele"
            n "Ja seal on kõik endine"
            m "Oeh olgu"
            n "sa lähed alla esimesele korrusele."
            n "Otsustasite minna B-hoonesse"
            jump Bkorp

label waking:
    m "oh ärka üles"
    "..."
    m "TERE, NAD HELISTAVAT TEIE JÄRELE!!!"
    u "Oh! Kurat MIKS karjuda??"
    u "mida sul vaja on?"
    m "Tere. Miks sa siin üldse magasid?"
    u "Ma tahan magada, sellepärast"
    u "Ma töötasin 3 päeva järjest ilma magamata ühe programmi, ÜHE jaoks"
    m "oh see on nõme"
    m "Kuule, kas sa tead, mis on 2. ja 3. korrusel?"
    u "Ja sellepärast sa mind äratasid?"
    u "...jumal"
    n "Sa läksid teisele korrusele"
    u "Lühidalt, te ei leia midagi peale ottomanide, pingid ja kapid"
    u "Kuigi seal on üks huvitav kontor, kus töölauad pole nagu teistes kontorites."
    m "See on selge"
    m "Lähme siis kolmandale korrusele?"
    u "Ja kas sa arvad tõsiselt, et kolmandal korrusel tuleb midagi teistmoodi?"
    u "Ei. Parem näitan teile esimest korrust"
    m "Kus see on?"
    u "Kas sa küsisid seda tõsiselt? Kas teil pole isegi aimu, kus see olla võib?"
    m "ok ok, loll küsimus"
    n "Te lähete alla 0. korrusele"
    u "Ja siin on lauatenniselaud"
    u "Nad ei anna sulle reketeid ega tennisepalle."
    u "Kuigi kui teil on see, mida ma loetlesin, siis saame mängida ühe mängu."
    m "Kahjuks mul neid esemeid pole."
    u "Noh, see tähendab, et ma lähen uuesti magama."
    m "Oh, aitäh, et vähemalt keha ennast näitasid."
    u "Peaasi, et mind üles ärataks."
    n "Sa läksid esimesele korrusele."
    n "Ta läks toolile magama"
    n "Ja sa otsustasid minna B-hoonesse"
    jump Bkorp

label Bkorp:
    n "Jõudsite B-hoone juurde ja saite kohe aru, kui kitsas see on võrreldes teiste hoonetega."
    n "Sa kõndisid parukate kontorist mööda."
    n "Ja keegi jooksis kohe teie juurde."
    u "Tere, kas soovite oma juukseid meie juures lõigata?"
    m "Tere, miks?"
    u "Meil on praegu lihtsalt praktika ja me vajame inimesi."
    menu hair:
        "Jah, ma saan":
            u "Suurepärane! Siis järgi mind"
            n "Sa järgnesid talle tema kabinetti"
            u "Võta istet."
            n "Istusid maha ja nad hakkavad juba su juukseid lõikama."
            n "Sa naudid seda hetke, et jääd peaaegu magama!"
            n "20 minutit on möödas"
            u "Noh, kuidas sulle su uus soeng meeldib?"
            menu newhair:
                "ja see sobib mulle!":
                    u "Suurepärane, tänan, et nõustusite soenguga."
                    m "Jah, mul on hea meel selle üle, et see soeng mulle sobib! Loodan, et teie jaoks läheb kõik hästi."
                    m "Hüvasti!"
                    u "Aitäh! Hüvasti"
                    jump LastChoice
                "Pole paha":
                    u "Olgu, tänan, et nõustusite soenguga."
                    m "Palun ja aitäh, et lubasite mul juukseid lõigata."
                    m "Hüvasti!"
                    u "Palun! Hüvasti"
                    jump LastChoice
                "D:":
                    u "Ou. Kas sulle ei meeldi su soeng?"
                    m "Ei."
                    u "Meil on väga kahju, et rikkusime teie soengu ära."
                    m "Mitte midagi. Ma lähen, hüvasti."
                    u "Hüvasti"
                    jump LastChoice
        "Lõikasin hiljuti oma juukseid":
            u "Olgu, tänan vastamast."
            m "Palun"
            d "Ta läheb oma kontorisse."
            jump LastChoice
return
