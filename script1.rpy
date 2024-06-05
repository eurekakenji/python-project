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
image Rfrown = "Richfrown.png"
image Ridle = "Richidle.png"
image Rsmile = "Richidle.png"
image Ddisappointed = "Dandisappointed.png"
image Didle = "Danidle.png"
image Dsmirk = "Dansmirk.png"
image Libdissapointed = "Libdisappointed.png"
image Libidle = "Libidle.png"
image Libsmirk = "Libsmirk.png"

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
    scene Fkorp1
    n "Olete F korpuses."
    "Vasakul pool on riietusruum, sirge trepp teisele korrusele ja kuulipilduja, paremal toolid. Kuhu sa esimesena lähed?"
    menu:
        "Riietusruumi":
            scene cloth 
            n "Sisened riietusruumi, võtad seljast õueriided ja riputad nad riietuspuu külge."
        "Maja F 2 korrusele":
            scene Fkorp2
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

label Liiaintro:
    show Liiaidle at center
    u "Tšau."
    m "Noh tšau. Mis su nimi on?"
    l "Liia. Uus oled või?"
    menu:
    "noh jah":
        show Liiasmirk at center
        l "nagu arvasinki."
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
                show Liiafrown at center
                l "ega kas programmeeria ole programmeeria kui ta ei ole iga päev oma päeva kõige madalamas punktis ja ei maga stressi tõttu?"
                m "noh. jah."
                jump questions
            "Mis eriala õpid?":
                l "Tarkvaraarendust. Ei soovitaks kui sulle meeldib psüühikat hoida. statistilest suurem osa programmeeriatest läksid oma eialale, sest vihkavad ennast."
                jump questions
            "Oma erialaga saad hästi hakkama?":
                show Liiasmirk at center
                l "Noh, nagugi iga inimene, päris normaalselt."
                m "Ega midagi raskusi ei too?"
                show Liiaidle at center
                l "Ja veel ütle, et hobused lennata oskavad, muidugi on raskusi, ega see lihtne asi ole."
                m "arusaadav."
                jump questions
            "*tagasi menüü juurde*":
                jump liiaintro
    "Teoorias nagu tean mida teen...":
        l "noh see küll üllatus."
        hide Liia
        menu options:
            "Raamatukogu":
                hide Liiasmirk
                hide Liiaidle
                hide Liiafrown
                        jump WayLibrary
            "E korpus":
                    jump EkorpusII
            "Ei": 
                show Liiafrown at center
                l "No sa oled vastik :("
                jump EkorpusII

label WayLibrary:
    scene lib
    n "Ootate raamatukoguhoidjat tagasi."
    n "Ja ootad"
    n "Ja ootad...."
    n "Näete, et ta tuleb sisse ja istub oma kohale. Sa lähened talle"
    m "Tere, kas saaksite mulle ühe raamatu kinkida? Mu sõber otsib just retseptiraamatut, sest talle meeldib süüa teha."
    b "Tere. Jah, meil on retseptiraamat. Kui kaua teil selle raamatu tagastamiseks aega kulub?"
    m "3 nädala pärast."
    n "Ta annab teile täitmiseks lehe."
    b "Hästi. Palun kirjutage sellele paberile oma ees- ja perekonnanimi ning allkiri."
    n "Sa hakkad kirjutama, mida ta ütles."
    b "See on kõik, võtke retseptiraamat."
    m "Aitäh!"
    n "Võtsid raamatu ja läksid sõbra juurde. See polnud nii raske, ah?"
    l "Noh, kas sa võtsid raamatu?"
    m "Jah, siin on raamat"
    l "Suurep- oodake. Kas võtsite retseptiraamatu tõsiselt kätte?"
    l "Saate aru, et ma ei ole kokanduse fänn, eks?"
    m "Noh, loogiliselt võttes on see juba teie süü, kuna te ei täpsustanud, millist raamatut võtta."
    l "Õiglane. Olgu, sul on abi eest 5 eurot."
    m "Vau. 5 eurot nii lihtsa ülesande eest? Aitäh!"
    hide Liiafrown
    hide Liiasmirk
    hide Liiaidle
    jump EkorpusII

label EkorpusII:
    hide Liiafrown
    hide Liiasmirk
    hide Liiaidle
    m "Niisiis, kus ma olen?"
    n "Vaatad ringi ja näed E-tähte"
    m "Olen vist E korpuses"
    m "Tahtsin järsku tualetti minna. Loodan, et siia tuleb tualett."
    n "Jalutad E-hoones ringi, et leida tualett."
    n "Leidsid tualeti, sisenesid"
    n "Ja läks välja"
    m "Oh, ja ma nägin seal laborit, tahtsin alati keemias katsetada"
    n "Lähed laborisse, sisened sinna ja näed kohe vedelikega kolbe"
    m "Vau, kolvid"
    m "Huvitav, mis siis, kui ma need omavahel segan."
    n "Kuuled samme enda poole tulemas."
    m "Oh pagan, ma arvan, et mul on probleeme."
    m "Seda ainult siis, kui"
    menu:
        "Peida":
            n "Leiad suurepärase koha peitmiseks"
            n "Järsku tuleb keegi sisse. Sa ei saa aru, milline ta välja näeb, aga sa võid vaadata tema varju"
            n "(sel hetkel peaks olema paus.)"
            m "Pheh, tundub, et ta on läinud"
            m "Eei, see oleks minu jaoks ohtlik."
            n "Sa lahkusid laborist ja läksid esimesele korrusele."
            jump EkorpusI
        "Lahkuge kontorist":
            m "Ma pean kiiresti välja minema."
            n "Näete teda ukse lähedal seismas"
            n "Avad ukse ja sind märgatakse kohe."
            jump MAD
        "Sulgege kontor":
            m "Oh ma tean, ma panen kontori kinni"
            n "Paned kontori ukse kinni."
            j "Oeh olgu. Ma ei sulgenud seda kontorit, kuidas see suleti?"
            j "Ja mul pole võtit. Kurat, ma pean võtme järele tagasi minema."
            m "Kas ta on lahkunud?"
            m "....Omamoodi jah"
            n "Lahkud laborist ja lähed kohe alla, enne kui keegi sind märkab."
            jump EkorpusI
        "Mõtle":
            m "Kurat, mida ma peaksin tegema..."
            n "Ta astub laborisse ja märkab sind"
            jump MAD

label MAD:
    show Jfrown at center
    j "Kes sa oled?"
    m "Emmm"
    j "Ma küsin, kes sa oled?"
    m "Ma?"
    j "Ära ole rumal, ma ei näe kedagi peale sinu"
    m "Minu nimi on...."
    m "Peter Griffin"
    j "..."
    m "Andrei Vorobjov.."
    j "See on teine ​​teema."
    "Selgitage, miks te siin olete ja miks tahtsite kolvid võtta?"
    menu:
        "Räägi tõtt":
            m "Tead, ma olen alati tahtnud midagi teha laboris ja üldse keemias."
            m "Meil polnud koolis ainsatki laboratoorset tööd, vaid ainult mõned ülesanded."
            m "Kui laborit nägin, tekkis tahtmine kohe midagi teha."
            j "Ja?"
            m "Mida sa silmas pead?"
            show Jidel at center
            j "Jumal küll, kui tahad midagi teha, aga küsi enne minult, sest ma ei saa kedagi üksi jätta järelevalveta."
            j "Palun tulge nüüd laborist välja."
            jump EkorpusI
        "Räägi valet":
            m "Mu ülemus palus mul kolvid tuua"
            j "Ma uskusin seda"
            m "Ma kinnitan teile, et ta küsis minult."
            j "Jah? Ja mis ta nimi on?"
            m "..."
            m "Ma ei mäleta, aga mäletan, et ta istub alati F206-s."
            show Jidel at center
            j "Oota siin."
            hide Jidel
            hide Jfrown
            n "Ta lahkus kontorist."
            m "See on minu võimalus olukorrast põgeneda."
            n "Lahkute kontorist ja lähete esimesele korrusele."
            jump EkorpusI
    
label EkorpusI:
    m "Esimene korrus.. Huvitav"
    m "Ei, noh, kui ma kuskile ei peida, võivad nad mu üles leida."
    n "Vaatad ringi ja näed kuskil uksi"
    m "Noh, ma arvan, et kui ma nende uste taha peitun, siis ta ei leia mind?"
    n "Otsustasite end ukse taha peita."
    n "Otsustasite kontoris ringi vaadata ja saite aru, et see on köök."
    m "Jama. Selle aja jooksul jõudsin nälga jääda."
    m "Ma lähen valmistan endale midagi."
    show Rforwn at center
    r "Mitte minu nugadega."
    menu TINIBDD:
        "Kes...":
            m "Kes sa oled ja kuidas sa siia sattusid?"
            r "Loogiliselt võttes peaksin sinult küsima."
            m "See ei tohiks teid muretseda."
        "Olgu...":
            m "Olgu, ma teen endale snäki."
            r "Tundub, et sind ei huvita tõsiasi, et ma siin seisan."
            m "Mind ei huvita."
    m "Ma olen tegelikult näljane."
    r "Noh... sa näed välja nagu TikToker, kes juhib süüdistust, et paks olemine on 'keha positiivne' ja et 'väidetavalt' sööte ainult tervislikku toitu."
    r "Kui tahad normaalselt süüa ja gastriiti mitte haigestuda, siis saan aidata ühe roa retseptiga."
    menu Food:
        "Olgu, ma kuulan":
            show Ridle at center
            r "Mul on üks retsept."
            r "See roog saab olema Kreeka salat."
            r "See valmib väga kiiresti, seega piisab 5-10 minutist."
            menu Salad:
                "Ma üritan.":
                    r "Niisiis."
                    r "Tomatid..."
                    n "Ta lõikab tomatid tükkideks."
                    r "Kurgid...."
                    n "Ta lõikab kurgi kolmnurkadeks."
                    r "Jääsalat..."
                    n "Ta lõikab salati väikesteks tükkideks."
                    r "Juustud Feta...."
                    n "Ta lõikab fetajuustu kuubikuteks."
                    r "Punane sibul..."
                    n "Ta lõikab punase sibula õhukesteks poolrõngasteks."
                    r "Ja oliiviõli..."
                    n "Ta lisab salatile veidi oliiviõli."
                    r "Ta segab kõik kokku."
                    r "TA-dah! Siin on salat, naudi."
                    n "Ta annab sulle proovimiseks salatit."
                    r "Sa sööd salatit."
                    r "Noh? Kuidas salatiga läheb?"
                    menu taste:
                        "Nii maitsev.":
                            show Rsmile at center
                            r "Ma ütlesin sulle, et mulle meeldiks"
                            n "Sõid oma salati südamerahus ära."
                            m "Noh, mul on kõht täis. Tänan teid väga."
                            r "Jah. Nüüd palun mine ära, ma ei taha, et me mõlemad hätta jääme."
                            m "Olgu olgu. Edu"
                            hide Rsmile
                            hide Ridle
                            hide Rfrown
                            jump FIP2
                        "Hästi":
                            show Rsmile at center
                            r "See tähendab, et ma tegin täna hästi süüa."
                            n "Otsustasite selle kõik ära süüa."
                            m "Noh, mul on kõht täis. Ma lähen kaugemale, kuhu mu silmad mind viivad."
                            r"Jah. Ja kiiresti, ma ei taha jääda vahele, et lihtsalt kellelegi midagi valmistasin."
                            jump FIP2
                        "Оeh..":
                            show Rfrown at center
                            r "Raiskasin salati koostisosad, mida keegi ei söö. Klass"
                            m "Vau, ära pane pahaks."
                            r "No muidugi, Body Positive'ile salateid ei meeldi."
                            jump BODI

                "Ei aitäh":
                    show Rfrown at center
                    r "No muidugi, Body Positive'ile salateid ei meeldi."
                    jump BODI

        "Mul on vaja kiirustada":
            jump BODI

label BODI:
    show Rfrown at center
    r "Noh, söö oma doshirak ära."
    r "Ei, tead mida, tule köögist välja."
    m "Okei"
    n "Lahkusite, sest mõistsite, et kui jääte, tuleb siin tõsiseid jõukatsumisi."
    hide Rfrown
    hide Ridle
    hide Rsmile
    jump FIP2

label FIP2:
    show Lidle at center
    l "Aga me nägime teineteist jälle."
    m "Jah, ja nüüd kohtume jälle"
    l "Noh, nagu ma aru saan, olid sa E korpuses."
    l "Nagu seal?"
    menu opinion:
        "Jah, see tundub normaalne.":
            show Lsmile at center
            l "Mul on hea meel, et teile E-juhtum meeldis"
            l "Nüüd kus?"
            l "Soovita. Olin ainult kahes majas."
            l "Noh. võite minna jõusaali, kui soovite treenida."
            l "Või võite minna C-hoonesse."
            l "See on teie äranägemisel"
            menu NextPart:
                "Jõusaalis":
                    show Lidle at center
                    l "Hästi. Siis näete neid väikseid samme?"
                    m "Jah. Ma näen."
                    l "Ühesõnaga, sa tõused püsti ja kõnnid otse."
                    l "Pärast seda minge vasakule, kus on uksed"
                    l "Siis lähed otse ja lõpus keerad paremale."
                    m "Okei aitäh."
                    jump sport
                "C-koortel":
                    show Lidle at center
                    l "Hästi. Siis näete neid väikseid samme?"
                    m "Jah. Ma näen."
                    l "Ühesõnaga, sa tõused püsti ja kõnnid otse."
                    l "ja siis keera paremale."
                    m "Okai aitäh"
                    jump CKorpI
        "Mitte.":
            show Lidle at center
            l "Noh. ma saan sellest aru. Väga adekvaatseid inimesi seal minu arust ei ole."
            m "Jah ma saan aru. Kõik on millegipärast vihased."
            l "ja see on tõsi."
            l "Kuhu sa nüüd lähed?"
            m "Soovita. Olin ainult kahes majas."
            l "Noh. võite minna jõusaali, kui soovite treenida."
            l "Või võite minna C-hoonesse."
            l "See on teie äranägemisel"
            hide Lidle
            hide Lsmile
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
    show Sidle at center
    s "Oih, vabandust"
    m "Mul ei olnud aega sisse tulla ja mul oli juba peavigastus."
    show Sannoyed at center
    s "No, kurat, see pole minu süü, et ma ei saa tulevikku vaadata ega näe sind palliga pähe löömas."
    m "Sul on õigus. Mida sa üldse teed?"
    s "Mina? palli sisse"
    m "Äkki oskate öelda, millega täpsemalt tegelete?"
    s "Viskan palli rõngasse."
    m "Korvpall"
    s "Ahhh, okei"
    show Ssmirk at center
    s "Mängime?"
    m "Nagu mul oleks valida."
    hide Sidle
    hide Sannoyed
    hide Ssmirk
    n "Hakkad korvpalli mängima"
    n "Viskasite edukalt rõngasse"
    n "Ta viskab ka rõngasse."
    n "Saate aru, et see mäng saab olema raske."
    n "Teie vastasel oli pall."
    n "Sa võtad temalt palli ära."
    n "Sa jõuad vastase rõngale lähedale."
    n "Valmistute palli rõngasse viskama ja..."
    "Aeg on läbi"
    show Ssmirk at center
    m "Nii kiire?"
    s "Jah, ma panin selle 10 minutiks"
    m "Oh. Muide, meil on viik"
    s "Ma tean, ma tean"
    s "Noh. See oli lahe"
    m "Nõus. Olgu, ma lähen C hoonesse"
    s "Okei näeme"
    hide Ssmirk
    jump CKorpIContinue

label CKorpIContinue:
    n "Sa jätkasid oma teed"
    n "Sa nägid allakäiku. Ja kummalisel kombel otsustasid sa alla minna"
    n "Sa nägid seal joont."
    m "Hm. Tundub, et see on söögituba"
    n "Ootad, kuni järjekorda pole."
    n "Nägid, et seal on söömiseks õpilasluba vaja."
    n "Sul vedas, et sul oli õpilasluba."
    n "tulid üles, andsid kaardi ja..."
    "Piiks!"
    n "Teie kaart töötas. Jätkate oma teed toidu hankimiseks."
    n "Võtsid toidu ja istusid kuskile söögitoa taha."
    u "Kas ma võin sinuga istuda?"
    menu talbk:
        "Istu maha":
            u "Aitäh"
            m "Palun"
            jump moretalking
        "Ei":
            u "Olgu siis"
            n "Sõid südamerahus"
            n "Sa kandsid taldrikut ja kandikut"
            n "Lähete tagasi C-hoonesse."
            jump sleepy

label moretalking:
    u "Noh, mis su nimi on?"
    m "Andrei"
    u "See on selge"
    m "Mulle tundub imelik, et sa minuga maha istusid"
    u "Ma tõesti ei taha üksi süüa."
    u "Ja üldiselt nendega, kellega ma tavaliselt istun, on nad lihtsalt vait ja seetõttu muutub söögitoas söömine igavaks."
    m "Ma näen, aga mida sa minult ootad?"
    u "Oh, kas sa pole ka seltskondlik?"
    u "See valutab. Kas teil pole isegi huvitavaid lugusid?"
    m "Ei."
    u "Isegi igavad?"
    m "Isegi igavad."
    u "Ah ole nüüd."
    u "Olgu, kuulake mu lugu:"
    u "Ühel hetkel olin vanaemal külas"
    u "Selles külas oli tall hobustega"
    u "ma mõtlesin"
    u "'Mis siis, kui proovin hobusega ratsutada'"
    u "Niisiis, istusin hobuse selga ja sõitsin järve äärde."
    u "Kui olime järve lähedal, otsustas hobune ujuma minna"
    u "Ja uppus..."
    m "See oli nali? või juhtus see tõesti?"
    u "See on nali. Ta viskas mu järve ja ma olin üleni märg."
    m "Oh haha.. ma ei tea, kas see oli naljakas?"
    u "Ma just rääkisin loo, see on sinu arvamus, kas see oli naljakas või mitte."
    u "Noh, ma olen toiduga läbi"
    u "Tänan teid veel kord, et lubasite mul teiega koos istuda."
    m "Võta meiega ühendust"
    n "Sa sõid kõike, mis taldrikul oli."
    n "Sa kandsid taldriku ja kandiku."
    n "Lähete tagasi C-hoonesse."

label sleepy:
    n "Olete sisenenud hoone C koridori."
    n "Ja sa kuulsid kohe, et keegi magas."
    d "*Norskab*"
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
    m "..."
    m "TERE, NAD HELISTAVAT TEIE JÄRELE!!!"
    show Didle at center
    d "Oh! Kurat miks karjuda??"
    d "Mida sul vaja on?"
    m "Tere. Miks sa siin üldse magasid?"
    d "Ma tahan magada, sellepärast"
    d "Ma töötasin 3 päeva järjest ilma magamata ühe programmi, ÜHE jaoks"
    m "oh see on nõme"
    m "Kuule, kas sa tead, mis on 2. ja 3. korrusel?"
    show Ddisappointed at center
    d "Ja sellepärast sa mind äratasid?"
    d "...Jumal"
    n "Sa läksid teisele korrusele"
    show Didle at center
    d "Lühidalt, te ei leia midagi peale ottomanide, pingid ja kapid"
    d "Kuigi seal on üks huvitav kontor, kus töölauad pole nagu teistes kontorites."
    m "See on selge"
    m "Lähme siis kolmandale korrusele?"
    show Ddisappointed at center
    d "Ja kas sa arvad tõsiselt, et kolmandal korrusel tuleb midagi teistmoodi?"
    d "Ei. Parem näitan teile esimest korrust"
    m "Kus see on?"
    d "Kas sa küsisid seda tõsiselt? Kas teil pole isegi aimu, kus see olla võib?"
    m "ok ok, loll küsimus"
    n "Te lähete alla 0. korrusele"
    d "Ja siin on lauatenniselaud"
    d "Nad ei anna sulle reketeid ega tennisepalle."
    d "Kuigi kui teil on see, mida ma loetlesin, siis saame mängida ühe mängu."
    m "Kahjuks mul neid esemeid pole."
    d "Noh, see tähendab, et ma lähen uuesti magama."
    m "Oh, aitäh, et vähemalt keha ennast näitasid."
    show Dsmirk at center
    d "Peaasi, et mind üles ärataks."
    hide Didle
    hide Ddisappointed
    hide Dsmirk
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

label LastChoice:
    m "No ma arvan, et olen ringi vaadanud, nüüd võin koju minna."
    m "Olgu siis"
    menu:
        "Väljuda B-korpuse kaudu.":
            m "Olgu, ma lähen"
            n "Sa läksid kohe õue"
            jump Conclusion
        "Väljuda C-korpuse kaudu.":
            m "Olgu, ma lähen"
            d "Olete tagasi C-korpuses"
            d "Nägid 'Tegelase nime' jälle toolil magamas"
            d "Kuid sa otsustasid teda mitte äratada, sa ei tea kunagi, mida ta sinuga teeb."
            d "Kõndisid edasi, kuni nägid ust tänavale."
            d "Sa läksid hoonest C välja."
            jump Conclusion
        "Väljuda F-korpuse kaudu.":
            m "Olgu, ma lähen"
            d "Olete tagasi F-korpuses"
            d "Nägid 'Tegelase nime' jälle toolil magamas"
            d "Kuid sa otsustasid teda mitte äratada, sa ei tea kunagi, mida ta sinuga teeb."
            d "Kõndisid edasi, kuni nägid ust tänavale."
            d "Olete jõudnud F koprusse."
            d "Liia kohtus sinuga"
            show Liiaidle at center
            l "Tere jälle"
            m "Ku"
            l "Kuidas C-hoones on?"
            m "Jah, okei, ma tegelesin lollustega"
            show Liiasmirk at center
            l "See on selge"
            m "Muide, ma ei tundnud millestki ilma"
            hide Liiasmirk
            l "Ei"
            m "Hästi. Ma lähen siis koju. Edu"
            l "Jah, sama sulle"
            n "Sa läksid majast F välja."
            jump Conclusion

label Conclusion:
    d "Olete nüüd tänaval"
    d "Ja lähed südamerahuga koju"
    d "Kõik"
    d "Selle mängu lugu on läbi"
    d "Loodan, et teile meeldis see, mida me selle aja jooksul tegime"
    d "Aitäh mängimast!"
    return
