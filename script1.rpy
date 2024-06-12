
init python:
    i = 0
    class Rating:
        def __init__(self, rate, i):
            self.rate = rate
            self.i = i

        def score(self, rate):
            self.i += rate
            
        def final_result(i):
            return f"{self.i}"

# character section
init python:
    rating = Rating(0,0)
define u = Character("???")
define un = Character("unknown")
define s = Character("Sass")
define m = Character("Main")
define j = Character("Jeremy")
define l = Character("Liia")
define n = Character("Narrator")
define b = Character("Raamatukoguhoidja")
define r1 = Character("Richard")
define d = Character("Dan")
define k = Character("KD")
define r2 = Character("Riri")

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
image Kidle = "Kidle.png"
image Ksleep = "Ksleep.png"
image Ksmile = "Ksmile.png"
image Kwtf = "Kwtf.png"
image Ririhappy = "Ririhappy.png"
image Ririsad = "Ririsad.png"
image Ririmad = "Ririmad.png"
label start:
    scene ent
    menu:
        "*Sisenen F korpusesse*":
            n "Sisened F korpusesse"
        "*Pööran ümber ja lähen koju*":
            n "..."
            n "Vau"
            n "Lihtsalt vau"
            n "ehk sina tea, et kui sa lihtsalt keerad perse ukse poole ja sihkertad koju tagasi, et mängu ei toimu ju?"
            menu:
                "Tõsiselt? Oih.":
                    n "vot. {i}ahem{/i},"
                    n "Sisened F korpusesse"
                "Mul savi":
                    n "..."
                    n "meil ka savi, tõsiselt"
                    n "meil on türa 13. juunini vaja ära teha, me oleksime midagi pannud siia texti mõttes aga meil on kiire, vot sulle su {i}easter egg{/i}."
                    return
    scene fkorpo
    n "Olete F korpuses."
    n "Vasakul pool on riietusruum, sirge trepp teisele korrusele ja kuulipilduja, paremal toolid. Kuhu sa esimesena lähed?"
    menu fopt:
        "Riietusruumi":
            scene cloth 
            n "Sisened riietusruumi, võtad seljast õueriided ja riputad nad riietuspuu külge."
            scene fkorpo
            jump foptnew
        "2. korrusele":
            n "ei tahagi üleriideid ära võtta? noh OK"
            jump fIIfloor
        "Mine kooli automaati":
            n "Kas sul on raha?"
            menu money:
                "Jah":
                    n "Lähed masina juurde ja ostad endale midagi."
                    n "Järsku läheneb sulle keegi."
                "Ei":
                    n "Lähete masina juurde ja ootate, kuni nad teile mõne toote jaoks vahetusraha annavad."
                    n "geenius."
                    n "Näed kedagi masinale lähenemas ja ütled talle tere, lootes, et ta annab sulle raha."
        "Ma lähen istuma":
            n "Sa istusid toolile."
            n "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
            menu rest:
                "Puhkan veidi":
                    n "Tõused püsti ja keegi läheneb sulle kohe"
                "...":
                    n "Keegi läheneb sulle."

    menu foptnew:
        "2. korrusele":
            jump fIIfloor
        "Mine kooli automaati":
            n "Kas sul on raha?"
            menu moneynew:
                "Jah":
                    n "Lähed masina juurde ja ostad endale midagi."
                    n "Järsku läheneb sulle keegi."
                "Ei":
                    n "Lähete masina juurde ja ootate, kuni nad teile mõne toote jaoks vahetusraha annavad."
                    n "geenius."
                    n "Näed kedagi masinale lähenemas ja ütled talle tere, lootes, et ta annab sulle raha."
        "Ma lähen istuma":
            n "Sa istusid toolile."
            n "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
            menu restnew:
                "Puhkan veidi":
                    n "Tõused püsti ja keegi läheneb sulle kohe"
                "...":
                    n "Keegi läheneb sulle."


label fIIfloor:
    scene fkorpu
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
                    l "Tarkvaraarendust. Ei soovitaks kui sulle meeldib psüühikat hoida. statistilest suurem osa programmeeriatest läksid oma eialale, sest vihkavad ennast."
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
                "Raamatukogu":
                            jump WayLibrary
                "E korpus":
                        jump EkorpusII
                "1. korrus": 
                    hide Liiaidle
                    scene fkorpo
                    jump foptnewnew
        "*edasi*":
            jump options

menu foptnewnew:
    "2. korrusele":
        jump fIIfloornew
    "Mine kooli automaati":
        n "Kas sul on raha?"
        menu moneynewnew:
            "Jah":
                n "Lähed masina juurde ja ostad endale midagi."
                jump foptnewnew
            "Ei":
                n "Lähete masina juurde ja ootate, kuni nad teile mõne toote jaoks vahetusraha annavad."
                "geenius."
                jump foptnewnew
    "Ma lähen istuma":
        n "Sa istusid toolile."
        "Olen kindel, et sa olid siia jõudmisest väga väsinud. Puhka natuke."
        menu restnewnew:
            "Puhkan veidi":
                n "puhkad natuke."
                n "mõne aja pärast tõused jälle püsti"
                jump foptnewnew

            

label fIIfloornew:
    scene fkorpu
    show Liiaidle at center
    l "..."
    menu optionsnew:
        "Raamatukogu":
                    jump WayLibrary
        "E korpus":
                jump EkorpusII
        "1. korrus": 
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
        "Raamatu":
            b "Mis raamatu?"
            m "kas teil on soovitusi?"
            hide libidle
            show libsmirk at center
            b "isiklikult soovitaksin klassikuid, kuid teile võiks rohkem midagi uuemat meeldida."
            m "selge."
            hide libsmirk
            show libidle at center
            jump libopt
        "Õpiku":
            b "Mis aine?"
            m "Inglise keel."
            b "Selge, aga tagastage aasta lõpuks, eks?"
            m "Yep."
            jump libopt
        "Lihtsalt vaatan ringi":
            hide libidle
            show libsmirk at center
            b "Okei!"
            hide libsmirk
            show libidle at center
            jump libopt
        "*tagasi menüü juurde*":
            hide libidle
            jump options


label EkorpusII:
    scene ekorpu
    n "Vaatad ringi ja näed E-tähte"
    m "Olen vist E korpuses"
    "Tahtsin järsku tualetti minna. Loodan, et siia tuleb tualett."
    n "Jalutad E-hoones ringi, et leida tualett."
    "Leidsid tualeti, sisenesid"
    "Ja läksid välja"
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
            d "lahkud laborist ja läksid esimesele korrusele."
            jump EkorpusI
        "Lahkuge kontorist":
            m "Ma pean kiiresti välja minema."
            d "Näete teda ukse lähedal seismas"
            "Avad ukse ja sind märgatakse kohe."
            jump MAD
        "Sulgege kontor":
            m "Oh ma tean, ma panen kontori kinni"
            d "Paned kontori ukse kinni."
            u "Oeh olgu. Ma ei sulgenud seda kontorit, kuidas see suleti?"
            "Ja mul pole võtit. Kurat, ma pean võtme järele tagasi minema."
            m "Kas ta on lahkunud?"
            ".... omamoodi jah"
            d "Lahkud laborist ja lähed kohe alla, enne kui keegi sind märkab."
            jump EkorpusI
        "Mõtle":
            m "Kurat, mida ma peaksin tegema..."
            n "Ta astub laborisse ja märkab sind"
            jump MAD

label MAD:
    show Dand at center
    u "Kes sa oled?"
    m "Emmm"
    u "Ma küsin, kes sa oled?"
    m "Ma?"
    u "Ära ole rumal, ma ei näe kedagi peale sinu"
    m "Minu nimi on...."
    "Peter Griffin"
    show Dansmile at center
    u "..."
    m "Andrei Vorobjov.."
    show Dand at center
    d "See on teine ​​teema."
    d "Muide, minu nimi on Dan, nii et te ei esita küsimusi."
    "Selgitage, miks te siin olete ja miks tahtsite kolvid võtta?"
    menu:
        "Räägi tõtt":
            m "Tead, ma olen alati tahtnud midagi teha laboris ja üldse keemias."
            m "Meil polnud koolis ainsatki laboratoorset tööd, vaid ainult mõned ülesanded."
            m "Kui laborit nägin, tekkis tahtmine kohe midagi teha."
            hide Dand
            show Danidle at center
            d "Ja?"
            m "Mida sa silmas pead?"
            d "Jumal küll, kui tahad midagi teha, aga küsi enne minult, sest ma ei saa kedagi üksi jätta järelevalveta."
            d "Palun tule nüüd laborist välja."
            hide Danidle
            hide Dansmile
            hide Dand
            init python:
                Rating.score(1)
            jump EkorpusI
        "...":
            d "Sa ei vasta mulle"
            d "Sind pole mõtet siin hoida, mine."
            d "Aga kui ma sind näen, jääd sa hätta."
            n "Lahkusite laborist ja läksite E korpuse 1. korrusele."
        "Valeta":
            m "Mu ülemus palus mul kolvid tuua"
            d "Ja ma usun seda?"
            m "Ma kinnitan teile, et ta küsis minult."
            d "Jah? Ja mis ta nimi on?"
            m "..."
            "Ma ei mäleta, aga mäletan, et ta istub alati F206-s."
            d "Oota siin."
            n "Ta lahkus kontorist."
            m "See on minu võimalus olukorrast põgeneda."
            n "Lahkud kontorist ja lähed esimesele korrusele."
            hide Danidle
            hide Dand
            init python:
                Rating.score(-1)
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
    j "Mitte minu nugadega."
    menu TINIBDD:
        "Kes...":
            m "Kes sa oled ja kuidas sa siia sattusid?"
            j "Loogiliselt võttes peaksin sinult küsima."
            m "See ei tohiks teid muretseda."
        "Olgu...":
            m "Olgu, ma teen endale snäki."
            j "Tundub, et sind ei huvita tõsiasi, et ma siin seisan."
            m "Mind ei huvita."
    m "Ma olen tegelikult näljane."
    j "Noh... sa näed välja nagu TikToker, kes juhib süüdistust, et paks olemine on 'keha positiivne' ja et 'väidetavalt' sööte ainult tervislikku toitu."
    "Kui tahad normaalselt süüa ja gastriiti mitte haigestuda, siis saan aidata ühe roa retseptiga."
    menu Food:
        "Olgu, ma kuulan":
            j "Mul on üks retsept."
            "See roog saab olema Kreeka salat."
            "See valmib väga kiiresti, seega piisab 5-10 minutist."
            menu Salad:
                "Ma üritan.":
                    j "Niisiis."
                    "Tomatid..."
                    n "Ta lõikab tomatid tükkideks."
                    j "Kurgid...."
                    n "Ta lõikab kurgi kolmnurkadeks."
                    j "Jääsalat..."
                    n "Ta lõikab salati väikesteks tükkideks."
                    j "Juustud Feta...."
                    n "Ta lõikab fetajuustu kuubikuteks."
                    j "Punane sibul..."
                    n "Ta lõikab punase sibula õhukesteks poolrõngasteks."
                    j "Ja oliiviõli..."
                    n "Ta lisab salatile veidi oliiviõli."
                    "Ta segab kõik kokku."
                    j "TA-dah! Siin on salat, naudi."
                    n "Ta annab sulle proovimiseks salatit."
                    "Sa sööd salatit."
                    j "Noh? Kuidas salatiga läheb?"
                    menu taste:
                        "Nii maitsev.":
                            j "Ma ütlesin sulle, et mulle meeldiks"
                            n "Sõid oma salati südamerahus ära."
                            m "Noh, mul on kõht täis. Tänan teid väga."
                            j "Jah. Nüüd palun mine ära, ma ei taha, et me mõlemad hätta jääme."
                            m "Olgu olgu. Edu"
                            init python:
                                Rating.score(1)
                            jump FIP2
                        "Hästi":
                            j "See tähendab, et ma tegin täna hästi süüa."
                            n "Otsustasite selle kõik ära süüa."
                            m "Noh, mul on kõht täis. Ma lähen kaugemale, kuhu mu silmad mind viivad."
                            j "Jah. Ja kiiresti, ma ei taha jääda vahele, et lihtsalt kellelegi midagi valmistasin."
                            init python:
                                Rating.score(1)
                            jump FIP2
                        "Оeh..":
                            j "Raiskasin salati koostisosad, mida keegi ei söö. Klass"
                            m "Vau, ära pane pahaks."
                            j "No muidugi, Body Positive'ile salateid ei meeldi."
                            jump BODI

                "Ei aitäh":
                    j "No muidugi, Body Positive'ile salateid ei meeldi."
                    jump BODI

        "Mul on vaja kiirustada":
            jump BODI

label BODI:
    "Noh, söö oma doshirak ära."
    "Ei, tead mida, tule köögist välja."
    m "Okei"
    n "Lahkusite, sest mõistsite, et kui jääte, tuleb siin tõsiseid jõukatsumisi."
    init python:
        Rating.score(-1)

label FIP2:
    l "Aga me nägime teineteist jälle."
    m "Jah, ja nüüd kohtume jälle"
    l "Noh, nagu ma aru saan, olid sa E korpuses."
    "Nagu seal?"
    menu opinion:
        "Jah, see tundub normaalne.":
            l "Mul on hea meel, et teile E-juhtum meeldis"
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
    init python:
        Rating.score(-1)
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
                    init python:
                        Rating.score(1)
                    jump LastChoice
                "Pole paha":
                    u "Olgu, tänan, et nõustusite soenguga."
                    m "Palun ja aitäh, et lubasite mul juukseid lõigata."
                    m "Hüvasti!"
                    u "Palun! Hüvasti"
                    init python:
                        Rating.score(1)
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
            n "Ta läheb oma kontorisse."
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
            n "Olete tagasi C-korpuses"
            n "Nägid 'Tegelase nime' jälle toolil magamas"
            n "Kuid sa otsustasid teda mitte äratada, sa ei tea kunagi, mida ta sinuga teeb."
            n "Kõndisid edasi, kuni nägid ust tänavale."
            n "Sa läksid hoonest C välja."
            jump Conclusion
        "Väljuda F-korpuse kaudu.":
            m "Olgu, ma lähen"
            n "Olete tagasi F-korpuses"
            n "Nägid 'Tegelase nime' jälle toolil magamas"
            n "Kuid sa otsustasid teda mitte äratada, sa ei tea kunagi, mida ta sinuga teeb."
            n "Kõndisid edasi, kuni nägid ust tänavale."
            n "Olete jõudnud F koprusse."
            n "Liia kohtus sinuga"
            l "Tere jälle"
            m "Ku"
            l "Kuidas C-hoones on?"
            m "Jah, okei, ma tegelesin lollustega"
            l "See on selge"
            m "Muide, ma ei tundnud millestki ilma"
            l "Ei"
            m "Hästi. Ma lähen siis koju. Edu"
            l "Jah, sama sulle"
            n "Sa läksid majast F välja."
            jump Conclusion

label Conclusion:
    scene ent
    n "Olete nüüd tänaval"
    n "Ja lähed südamerahuga koju"
    scene end
    n "Kõik"
    n "Selle mängu lugu on läbi"
    n "Loodan, et teile meeldis see, mida me selle aja jooksul tegime"
    n "Muide, kogu mängu jooksul teenisite austust."
    n "Ja teie austus on ..."
    init python:
        rating.final()
    if rating.final() == -6:
        jump BadEnding
    elif -6 < rating.final() < 6:
        jump NeutralEnding
    elif rating.final() == 6:
        jump GoodEnding
label BadEnding:
    n "Vau, sa oled mürgine!"
    n "kuna sa solvasid kõiki, ei taha keegi sind isegi näha."
    n "Sa mõistsid seda kohe ja otsustasid seetõttu sinna mitte minna."
    n "Ja ma arvan, et sinust saab mingi korrapidaja."
    n "Valige paremad vastused."
    n "Aitäh mängimast!"
    return

label NeutralEnding:
    n "Otsustasite sinna minna."
    n "Teile on määratud sisseastumiseksam ja vestlus."
    n "Tulid sel ajal."
    n "Kirjutasite sisseastumiseksami ja sooritasite intervjuud ja..."
    n "Sa ei suutnud."
    n "Otsustasite oma arengu nimel õhtukooli minna."
    n "Kuid teil on vedanud, et olete teistega sõbraks saanud ja seetõttu suhtlete nendega."
    n "Aitäh mängimast!"
    return

label GoodEnding:
    n "Palju õnne!"
    n "Olete otsustanud IVKHK-ga liituda pärast sisseastumiseksami ja vestluse sooritamist!"
    n "Arvasite, et sõpru on raske leida, kuid eksite."
    n "Kuna sa said seal sõpru juba enne, kui siia sisenesid."
    n "Ja ma õnnitlen teid, et suutsite saavutada teatud hinnangu ja saada hea lõpu!"
    n "Jah..."
    n "Aitäh mängimast!"
    return
