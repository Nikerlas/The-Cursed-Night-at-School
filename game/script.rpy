﻿#inventory

    

#transform
transform long_shake:
    ease .06 yoffset 24
    ease .06 yoffset -24
    ease .05 yoffset 20
    ease .05 yoffset -20
    ease .04 yoffset 16
    ease .04 yoffset -16
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0

transform short_shake:
    ease .03 yoffset 12
    ease .03 yoffset -12
    ease .02 yoffset 8
    ease .02 yoffset -8
    ease .01 yoffset 4
    ease .01 yoffset -4
    ease .01 yoffset 0
#END TRANSFORM

init python:
    renpy.music.register_channel("noise")

#BG
image bg club = "images/bg/bg club.png"
image bg black = "images/bg/bg black.png"
image bg district = "images/bg/scene.jpg"
image bg schoolyard = "images/bg/outschool.jpg"
image bg hallway = "images/bg/corridor.jpg"
image bg hallway2 = "images/bg/corridor2.jpg"
image bg aclass = "images/bg/inclass.jpg"
image bg library = "images/bg/perpus.png"
image bg canteen = "images/bg/canteen.jpg"
image bg osisdepan = "images/bg/bg osisdepan.jpg"
#END BG

#IMG CHARA
#ZAKY
#--------> talk
image zakyhappy = "images/zaky/talk/ZakyHappy.png"
image zakyhappy2 = "images/zaky/talk/ZakyHappy2.png"
image zakynormal = "images/zaky/talk/ZakyNormal.png"
image zakysad = "images/zaky/talk/ZakySad.png"
image zakysmile = "images/zaky/talk/ZakySmile.png"
image zakytalk = "images/zaky/talk/ZakyTalk.png"
image zakyworry = "images/zaky/talk/ZakyWorry.png"
#--------> idle
image idlezakyhappy = "images/zaky/idle/ZakyHappy.png"
image idlezakyhappy2 = "images/zaky/idle/ZakyHappy2.png"
image idlezakynormal = "images/zaky/idle/ZakyNormal.png"
image idlezakysad = "images/zaky/idle/ZakySad.png"
image idlezakysmile = "images/zaky/idle/ZakySmile.png"
image idlezakytalk = "images/zaky/idle/ZakyTalk.png"
image idlezakyworry = "images/zaky/idle/ZakyWorry.png"

#KEVIN
#--------> talk
image kevincheerful = "images/kevin/talk/KevinCheerful.png"
image kevinhappy = "images/kevin/talk/KevinHappy.png"
image kevinserious = "images/kevin/talk/KevinSerious.png"
image kevinsmile = "images/kevin/talk/KevinSmile.png"
image kevintalk = "images/kevin/talk/KevinTalk.png"
#--------> Idle
image idlekevintalk = "images/kevin//idle/KevinTalk.png"
image idlekevinhappy = "images/kevin/idle/KevinHappy.png"
image idlekevinserious = "images/kevin/idle/KevinSerious.png"
image idlekevinsmile = "images/kevin/idle/KevinSmile.png"
image idlekevincheerful = "images/kevin/idle/KevinCheerful.png"
#-------->

#YERI
#--------> talk
image yeriangry1 = "images/yeri/talk/YeriAngry.png"
image yeriangry2 = "images/yeri/talk/YeriAngry2.png"
image yericheerful = "images/yeri/talk/YeriCheerful.png"
image yerihappy = "images/yeri/talk/YeriHappy.png"
image yerinormal = "images/yeri/talk/YeriNormal.png"
image yerisad = "images/yeri/talk/YeriSad.png"
image yeriscared = "images/yeri/talk/YeriScared.png"
image yerishy = "images/yeri/talk/YeriShy.png"
image yerismile = "images/yeri/talk/YeriSmile.png"
image yerisurprised = "images/yeri/talk/YeriSurprised.png"
image yeritalk = "images/yeri/talk/YeriTalk.png"
image yeritsundere1 = "images/yeri/talk/YeriTsundere1.png"
image yeritsundere2 = "images/yeri/talk/YeriTsundere2.png"
#--------> idle
image idleyeriangry1 = "images/yeri/idle/YeriAngry.png"
image idleyeriangry2 = "images/yeri/idle/YeriAngry2.png"
image idleyericheerful = "images/yeri/idle/YeriCheerful.png"
image idleyerihappy = "images/yeri/idle/YeriHappy.png"
image idleyerinormal = "images/yeri/idle/YeriNormal.png"
image idleyerisad = "images/yeri/idle/YeriSad.png"
image idleyeriscared = "images/yeri/idle/YeriScared.png"
image idleyerishy = "images/yeri/idle/YeriShy.png"
image idleyerismile = "images/yeri/idle/YeriSmile.png"
image idleyerisurprised = "images/yeri/idle/YeriSurprised.png"
image idleyeritalk = "images/yeri/idle/YeriTalk.png"
image idleyeritsundere1 = "images/yeri/idle/YeriTsundere1.png"
image idleyeritsundere2 = "images/yeri/idle/YeriTsundere2.png"
#-------->

#CITRA
#--------> talk
image citranormal = "images/citra/talk/CitraNormal.png"
image citrahappy = "images/citra/talk/CitraHappyl.png"
image citrahappy2 = "images/citra/talk/CitraHappy2.png"
image citrastartled = "images/citra/talk/CitraStartled.png"
image citrairritated = "images/citra/talk/CitraIrritated.png"
image citratalk = "images/citra/talk/CitraTalk.png"
image citrascared = "images/citra/talk/CitraScared.png"
image citrasmile = "images/citra/talk/CitraSmile.png"
#--------> idle
image idlecitranormal = "images/citra/idle/CitraNormal.png"
image idlecitrahappy = "images/citra/idle/CitraHappyl.png"
image idlecitrahappy2 = "images/citra/idle/CitraHappy2.png"
image idlecitrastartled = "images/citra/idle/CitraStartled.png"
image idlecitrairritated = "images/citra/idle/CitraIrritated.png"
image idlecitratalk = "images/citra/idle/CitraTalk.png"
image idlecitrascared = "images/citra/idle/CitraScared.png"
image idlecitrasmile = "images/citra/idle/CitraSmile.png"



#END IMG CHARA

# CHARACTER
#YERI
define y = Character('Yeri')
define y_shout = Character("Yeri", what_size=50)
define y_whisper = Character("Yeri", what_size=18)
#ZAKY
define z = Character('Zaky')
define z_shout = Character("Zaky", what_size=50)
define z_whisper = Character("Zaky", what_size=18)
#KEVIN
define k = Character('Kevin')
define k_shout = Character("Kevin", what_size=50)
define k_whisper = Character("Kevin", what_size=18)
#CITRA
define c = Character('Citra')
define c_shout = Character("Citra", what_size=50)
define c_whisper = Character("Citra", what_size=18)
#MC
define u = Character('???')
define u_shout = Character("???", what_size=40)
define u_whisper = Character("???", what_size=18)
define p = Character('[name]')
define p_shout = Character("[name]", what_size=50)
define p_whisper = Character("[name]", what_size=18)
#Mix
define kyc = Character("Kevin, Yeri, dan [name]")
define zc = Character("[name] dan Zaky")
define zc_shout = Character("[name] dan Zaky", what_size=50)
#PENJAGA KANTIN
define pk = Character("Penjaga Kantin")
#SECRET
#-------->
#GAME START
#-------->

label start:
    scene bg black
    with dissolve

    python:
        diary01 = Item("Diary 01", image="gui/inventory/inv_diary01.png")  
        diary02 = Item("Diary 02", image="gui/inventory/inv_diary02.png")  
        diary03 = Item("Diary 03", image="gui/inventory/inv_diary03.png")  
        diary04 = Item("Diary 04", image="gui/inventory/inv_diary04.png")  
        diary05 = Item("Diary 05", image="gui/inventory/inv_diary05.png")  
        diary06 = Item("Diary 06", image="gui/inventory/inv_diary06.png")  
        diary07 = Item("Diary 07", image="gui/inventory/inv_diary07.png")  
        diary08 = Item("Diary 08", image="gui/inventory/inv_diary08.png")  
        diary09 = Item("Diary 09", image="gui/inventory/inv_diary09.png")  
        inventory = Inventory()

    #field name
    python:
        name = renpy.input("Siapa namamu: ")

        name = name.strip() or "You"

    scene bg district
    with dissolve

    python:
        renpy.notify("Distrik A")

    stop music fadeout 1.0

    "Pagi hari ini terasa sangat cerah tidak seperti biasa."
    "Dengan semangat pagi yang membara aku pergi menuju sekolahku."

    show idlekevinserious with dissolve

    "Dari kejauhan aku melihat Kevin sedang berjalan dipinggir jalan."

    p 'Hello Kevin. Bagaimana kabarmu?'

    hide idlekevinserious

    show kevincheerful at short_shake, center

    k 'Hai [name], baik kok! bagaimana denganmu?'

    hide kevincheerful
    show idlekevincheerful

    p 'Baik seperti biasa kok ahahahaha...'

    hide idlekevincheerful
    show kevincheerful

    k 'Kamu mau menuju sekolah?'

    hide kevincheerful
    show idlekevincheerful

    p 'Iyalah! Aku sudah memakai pakaian kek gini.'
    p 'Masak ga pergi sekolah.'

    hide idlekevincheerful
    show kevinhappy at short_shake,center

    k 'Ahahaha... Maaf aku cuma bercanda tadi.'

    scene bg schoolyard with dissolve
    python:
        renpy.notify("Halaman Sekolah")

    stop noise fadeout 1.0

    "Kami berdua berjalan menuju sekolah."
    "Sesampainya disekolah, Kevin mengingatkanku tentang rapat OSIS sehabis pulang sekolah nanti."

    show kevintalk with dissolve

    k 'Eh... Jangan lupa nanti ya! Sehabis pulang sekolah buat rapat untuk acara Ulang Tahun sekolah kita.'

    hide kevintalk
    show idlekevintalk

    p 'Okay... Pasti aku datang kok.'
    p 'Aku kan anak rajin.'

    hide idlekevintalk
    show kevinhappy at short_shake, center

    k 'Heleh ahahahaha.'

    hide kevin
    scene bg hallway with dissolve
    python:
        renpy.notify("Lorong Sekolah")


    "Aku menuju ke ruang kelasku."
    "Saat di pertengahan perjalanan aku dan Kevin bertemu Yeri lalu menyapanya."

    show idleyerinormal with dissolve

    p 'Hai Yeri. Bagaimana kabarmu?'
 
    hide idleyerinormal
    show yerihappy at short_shake, center

    y 'Hai [name], baik kok. Bagaimana denganmu?'

    hide yerihappy
    show idleyerihappy

    p 'Baik kok.'
    p "Aku dan Kevin ke kelas duluan dulu ya!"
    
    hide idleyerihappy
    show yerihappy
    
    y 'Okei!'

    hide yerihappy with dissolve

    scene bg aclass with dissolve
    python:
        renpy.notify("Kelas 2-A")

    "Sesampainya dikelas, aku langsung menuju ke tempat dudukku."
    "Saat aku sedang melamun. Tiba-tiba Zaky datang untuk menyapaku."
    
    show zakyhappy at long_shake, center

    z "[name]. Kamu kenapa melamun saja?" 
    z "Apa ada masalah dengan dirimu?"

    hide zakyhappy
    show idlezakyhappy

    p 'Tidak ada, aku cuma berpikir bernapas itu menyenangkan ya..'

    hide idlezakyhappy
    show zakyworry at short_shake, center

    z "Eh... "
    z "Iyadeh yang penting jangan lupa untuk ikut rapat nanti sepulang sekolah ya!"

    hide zakyworry
    show idlezakyworry

    p 'Iya... Santai aja. Aku inget kok.'

    hide idlezakyworry with dissolve

    "Tidak lama kemudian guru pun masuk kedalam ruangan untuk memulai pelajaran di pagi yang cerah ini."


    scene bg hallway with dissolve
    python:
        renpy.notify("Lorong Sekolah")

    "Bel istirahat pun berbunyi."
    "Lalu beberapa saat kemudian Yeri menghampiriku didepan kelasku."
    "Aku, Zaky, dan Kevin langsung keluar dari ruang kelas dan menghampiri posisi Yeri."

    show idlekevintalk with dissolve:
        xalign 0.0
        yalign 1.0

    show idleyerismile with dissolve:
        xalign 0.5
        yalign 1.0

    show idlezakyhappy with dissolve:
        xalign 1.0
        yalign 1.0

    hide idleyerismile
    show yerismile:
        xalign 0.5
        yalign 1.0

    y 'Hei [name], Kevin, Zaky yuk ke kantin. Mau ga?' 

    hide idlekevintalk
    show kevintalk:
        xalign 0.0
        yalign 1.0

    hide yerismile
    show idleyerismile:
        xalign 0.5
        yalign 1.0
    k "Kalau aku serah sih."
    hide kevintalk
    show idlekevintalk:
        xalign 0.0
        yalign 1.0
    hide idlezakyhappy
    show zakyhappy:
        xalign 1.0
        yalign 1.0
    z 'Aku oke aja.'
    z "Kalau [name] mau ga?"

    hide zakyhappy
    show idlezakyhappy:
        xalign 1.0
        yalign 1.0
    
    p 'Boleh saja sih... Tapi...'

    hide idlekevintalk
    show kevintalk at short_shake:
        xalign 0.0
        yalign 1.0

    k 'Ga usah pake tapi-tapian. Ayo gas berangkat.'

    hide kevintalk
    show idlekevinserious:
        xalign 0.0
        yalign 1.0

    p 'Tapi aku tu males banget coy...'

    hide idlezakyhappy
    show zakytalk:
        xalign 1.0
        yalign 1.0
    
    z 'Sudahlah ikut saja...'

    hide zakytalk
    show idlezakytalk:
        xalign 1.0
        yalign 1.0

    menu:
        "Aku akan ikut.":
            jump kantin_yes

        "Aku tidak ingin ikut.":
            jump kantin_no

#--------------------
#CANTEEN ROUTE
#-------------------
    label kantin_yes:

        $ menu_flag = True

        p 'Iya deh aku ikut. Yuk ke kantin.'
        
        hide idlekevinserious
        show kevincheerful at short_shake:
            xalign 0.0
            yalign 1.0

        k 'Nah gitu donk... Lama bet mikirnya dah ni anak.' 

        hide kevincheerful
        show idlekevinsmile:
            xalign 0.0
            yalign 1.0

        hide idleyerismile
        show yericheerful at short_shake, center

        y "Hahaha"
        y 'Yaudah yokkk berangkat!' 

        # 3 chara hilang bersamaan
        hide idlekevinsmile
        hide yericheerful
        hide idlezakytalk
        with dissolve

        "Kami berempat pergi menuju kantin bersama."
        "Dalam perjalanan menuju kantin, mereka bertiga membicarakan tentang rapat OSIS yang akan diadakan sore ini."
        "Aku terdiam sejenak, dan berpikir." 
        "Sejujurnya..." 
        
        menu:

            "Aku sangat antusias dengan rapat nanti.":
                jump choice2_yes
       
            "Aku kurang tertarik dengan rapat kali ini.":
                jump choice2_no

                label choice2_yes:

                    $ menu_flag = True

                    "Tiba-tiba Kevin memanggilku dengan keras dan itu membuatku terkejut." 
                    "Ternyata aku tertinggal jauh dari mereka. Lalu, aku menyusul mereka dengan cepat." 

                    scene bg canteen with dissolve
                    python:
                        renpy.notify("Kantin")

                    "Kami berempat telah tiba dikantin."
                    "Kevin dan Zaky lalu menuju tempat makanan, sedangkan aku dan Yeri mencari tempat duduk." 
                    "Kami berdua berhasil mendapatkan tempat duduk." 
                    "Lalu kami mendudukinya untuk menunggu Kevin dan Zaky." 
                    

                    show yerinormal with dissolve
                    
                    y 'Kamu tadi mengapa melamun?' 
                    y 'Apa yang sedang kamu pikirkan?' 

                    hide yerinormal
                    show idleyerinormal

                    p 'Ga ada apa-apa sih.' 

                    hide idleyerinormal
                    show yerinormal

                    y 'Ah boong kamu.'
                    p 'Beneran kok.'

                    hide yerinormal
                    show idleyerinormal

                    "Yeri menatapku dengan tatapan serius dicampur kesal."
                    "Akhirnya aku pun menyerah dan memberitahunya apa alasanku melamun tadi."

                    p "Aku cuma terlalu antusias aja untuk ikut rapat nanti."
                    
                    hide idleyerinormal
                    show yerismile
                
                    y 'Ya ampun kukira kamu mikirin apaan.' 
                    y 'Ternyata mikirin hal kayak gitu aja.' 

                    hide yerismile
                    show idleyerismile

                    p 'Ahahaha... Maaf ya...' 
                    
                    hide idleyerismile
                    show yericheerful at short_shake, center
                    
                    y 'Ga apa-apa.' 
                    y 'Kamu harus ikut rapat itu walaupun suka atau engga.'
                    
                    hide yericheerful
                    show yerismile

                    y 'Karena rapat itu untuk membahas perayaan ulang tahun sekolah kita.' 

                    hide yerismile
                    show idleyerismile

                    p 'Iya aku tau kok.' 

                    hide idleyerismile with dissolve

                    jump choice2_done

                label choice2_no:

                    $ menu_flag = False

                    "Tiba-tiba Kevin memanggilku dengan keras dan itu membuatku terkejut." 
                    "Ternyata aku tertinggal jauh dari mereka. Lalu, aku menyusul mereka dengan cepat." 

                    scene bg canteen with dissolve
                    python:
                        renpy.notify("Kantin")

                    "Kami berempat telah tiba dikantin."
                    "Kevin dan Zaky lalu menuju tempat makanan, sedangkan aku dan Yeri mencari tempat duduk." 
                    "Kami berdua berhasil mendapatkan tempat duduk." 
                    "Lalu kami mendudukinya untuk menunggu Kevin dan Zaky." 
                    

                    show yerinormal with dissolve
                    
                    y 'Kamu tadi mengapa melamun?' 
                    y 'Apa yang sedang kamu pikirkan?' 

                    hide yerinormal
                    show idleyerinormal

                    p 'Ga ada apa-apa sih.' 

                    hide idleyerinormal
                    show yerinormal

                    y 'Ah boong kamu.'
                    p 'Beneran kok.'

                    hide yerinormal
                    show idleyerinormal

                    "Yeri menatapku dengan tatapan serius dicampur kesal."
                    "Akhirnya aku pun menyerah dan memberitahunya apa alasanku melamun tadi."

                    p "Bukan masalah besar si, hanya saja aku kurang tertarik dengan rapat nanti."
                    
                    hide idleyerinormal
                    show yerismile
                
                    y 'Ya ampun kukira kamu mikirin apaan.' 
                    y 'Ternyata mikirin hal kayak gitu aja.' 

                    hide yerismile
                    show idleyerismile

                    p 'Ahahaha... Maaf ya...' 
                    
                    hide idleyerismile
                    show yericheerful at short_shake, center
                    
                    y 'Ga apa-apa.' 
                    y 'Kamu harus ikut rapat itu walaupun suka atau engga.'
                    
                    hide yericheerful
                    show yerismile

                    y 'Karena rapat itu untuk membahas perayaan ulang tahun sekolah kita.' 

                    hide yerismile
                    show idleyerismile

                    p 'Iya aku tau kok.' 

                    hide idleyerismile with dissolve

                    jump choice2_done
                
        label choice2_done:
         
            "Tak lama kemudian Kevin datang ke tempat dudukku dengan Citra." 

            show kevincheerful with dissolve

            k 'Kalian lagi membahas apa nih?' 

            show kevincheerful with move:
                xalign 0.3
                yalign 1.0 
            
            hide kevincheerful
            show idlekevincheerful:
                xalign 0.3
                yalign 1.0

            show yericheerful at right with dissolve:
                xalign 0.8
                yalign 1.0

            y "Ga ada apa-apa sih."

            hide yericheerful
            show idleyericheerful:
                xalign 0.8
                yalign 1.0

            p "Iya, ga ada apa-apa."

            hide idlekevincheerful
            show kevincheerful:
                xalign 0.3
                yalign 1.0

            k "Yang bener?"

            hide kevincheerful
            show idlekevincheerful:
                xalign 0.3
                yalign 1.0
            
            hide idleyericheerful
            show yeriangry2 at short_shake, right:
                xalign 0.8
                yalign 1.0

            y "Ga ada Kevin..."
            hide yeriangry2
            hide idlekevincheerful
            show kevinhappy at short_shake:
                xalign 0.3
                yalign 1.0

            show idleyeriangry2:
                xalign 0.8
                yalign 1.0
            k "Iya deh iya."

            hide idleyeriangry2
            hide kevinhappy
            with dissolve

            "Kevin mulai duduk di kursi meja kantin yang aku duduki."
            "Saat Kevin telah duduk."
            "Datanglah Citra dan Zaky."

            show citra with dissolve:
                xalign 0.3
                yalign 1.0 
            show zakyhappy at right with dissolve:
                xalign 0.8
                yalign 1.0
            
            c "Nyahaloo..."
            z "Halo halo"

            hide citra
            hide zakyhappy
            with dissolve

            show yerismile with dissolve

            y "Haii, Bagaimana kabarmu Cit?"

            show yerismile with move:
                xalign 0.3
                yalign 1.0 

            hide yerismile
            show idleyerismile:
                xalign 0.3
                yalign 1.0

            show citra at right with dissolve:
                xalign 0.8
                yalign 1.0

            c "Baik kok!"

            hide idleyerismile
            show yericheerful at short_shake:
                xalign 0.3
                yalign 1.0 

            y "Sini dong, kalian berdua ikut duduk!"
            c "Okeiiii!"

            hide yericheerful
            hide citra
            with dissolve

            "Citra dan Zaky mulai duduk di kursi meja kantin yang kutempati."
            "Saat mereka berempat sedang berbincang."
            

            jump kantin_done

#---------------
#LIBRARY ROUTE
#--------------

    label kantin_no:

        $ menu_flag = False
        p 'Ga dulu deh. Aku mau ke kamar mandi aja.' 

        hide kevinserious
        show kevintalk at short_shake, left

        k 'Yah ga asik lu!' 
        hide kevintalk
        
        hide idleyerismile
        show yeriangry2 at short_shake, center

        y 'Iya nih... Ga asik.' 
        hide yeriangry2
        show idleyeriangry2
        p 'Aku bilang ngga ya ngga anjir!'
        hide idlezakytalk
        show zakytalk:
            xalign 1.0
            yalign 1.0
        z 'Sudah deh biarin aja dia...' 
        hide zakytalk
        show idlezakynormal:
            xalign 1.0
            yalign 1.0
        hide idlekevinserious
        show kevintalk:
            xalign 0.0
            yalign 1.0
        k 'Yaudah deh... Yuk Yeri Zaky, Kita ke kantin.' 

        hide kevintalk
        hide idleyeriangry2 
        hide idlezakynormal 
        with dissolve

        "Mereka bertiga mulai berjalan menjauhiku." 
        "Sejujurnya aku tidak ingin pergi kekamar mandi." 
        "Tetapi, aku ingin ke Perpustakaan untuk menenangkan diri sebelum menghadapi rapat nanti." 
        "Karena perpustakaan adalah tempat yang tenang dan sunyi." 
        "Karena hal itulah aku ingin pergi ke perpustakaan." 

        scene bg library with dissolve
        python:
            renpy.notify("Perpustakaan")

        "Sesampainya di perpustakaan."
        "Hawa ketenangan mulai dirasakan oleh benakku."
        "Aku berpikir ini merupakan pilihan terbaik daripada pergi kekantin yang tempatnya sangat ramai."
        "Aku ingin mengambil salah satu buku di rak buku." 
        "Saat aku ingin mengambil buku tersebut. Tiba-tiba ada seseorang yang menepuk pundakku dan menyapaku." 

        u '"Halo..."'

        show citra with dissolve

        "Ternyata itu Citra." 

        p 'Ahhh Citra. Ada apa?' 
        c 'Aku boleh minta tolong ga?' 
        p 'Minta tolong apa?'
        c 'Tolong ambilin buku itu donk.' 

        "Citra menunjuk buku diatas pojok kanan."

        menu:
            "Oke deh!":
                jump choice5_a
            "Engga ah.":
                jump choice5_b
        label choice5_a:
        p "Oke deh!"
        p "Bentar ya."
        c "Iya!"
        jump choice5_done  
        label choice5_b:
        p "Engga ah."
        c 'Ya ampun... Itu tinggi banget. Ambilin donk.' 
        p 'Iya deh iya.'
        jump choice5_done
        label choice5_done:

        hide citra with dissolve

        "Aku mengambilkan buku tersebut."
        "Ternyata buku itu adalah buku novel romance yang akhir-akhir ini terkenal dikalangan remaja."
        "Saat aku memberikan buku tersebut kepada Citra."
        "Dirinya agak malu-malu."

        show citra with dissolve

        c 'Makasih ya!' 
        p 'Iya okay...'
        c 'Btw... kamu ikut rapat nanti sore ngga?'
        p 'Mungkin iya sih... Kan itu wajib untuk anggota OSIS.'
        p 'Emang kamu ga mau ikut?'
        c 'Bukan begitu.'

        c 'Aku hanya bertanya saja.'
        p 'Baiklah... Btw buku yang kamu baca itu lumayan terkenal ya.'
        c 'Iya sih bener... Aku mau baca dulu ya...'
        p 'Oke deh...'

        hide citra with dissolve
        
        "Citra pergi meninggalkanku untuk mencari tempat duduk yang nyaman."
        "Aku mulai mencari buku untuk dibaca."
        "Aku telah menemukan buku yang ingin kubaca."
        "Buku tersebut ialah novel misteri yang judulnya cukup menarik perhatianku."
        "Dan juga cover buku itu cukup menarik bila diperhatikan."
        "Saat aku ingin mengambil buku tersebut."
        "Ada satu buku aneh yang terjatuh."
        "Buakkkk!!!!"
        "Buku aneh tersebut terjatuh dilantai."
        "Buku itu terjatuh dalam keadaan terbuka dan di dalamnya terdapat secarik kertas."

        python:
            renpy.notify("Mendapatkan Diary 1")
            inventory.add(diary01)

        "Aku mengambil kertas itu."
        "Dan tiba-tiba ada yang memanggil ku."

        u 'Hei...[name].'

        show citra with dissolve

        "Ah... ternyata itu Citra."
        p 'Ada apa Cit?'
        c 'Kamu mau ikut ke kantin ga?'
        p 'Eh...'

        hide citra with dissolve

        "Ternyata Citra mengajak diriku ke kantin."
        "Aku bingung ingin ikut atau tidak."
        "Padahal beberapa waktu lalu aku menolak ajakan Kevin, Zaky, dan Yeri."
        
        show citra with dissolve
        c 'Gimana? Mau ikut?'

        menu:
            "Aduh gimana yah...":
                jump choice6_done
            "Bentar kupikir dulu...":
                jump choice6_done
                

                label choice6_done:

       
        c 'Ayo donk ikut... Jangan lama-lama mikirnya.'
        p 'Tapi tuh, beberapa waktu yang lalu aku diajak ke kantin sama Kevin, Zaky, dan Yeri.'
        p 'Tapi aku menolaknya.' 
        c 'Kok gitu? Kenapa kamu menolaknya?'
        p 'Ya... karena aku males buat ikut.'
        c 'Nah... Yok ikut sekalian.'
        c 'Nanti sekalian juga untuk membahas masalah rapat nanti sore.' 

        hide citra with dissolve

        "Aku kebingungan ingin mengikutinya atau tidak."
        "Ya... mungkin ikut bukan sesuatu yang buruk."

        show citra with dissolve

        c 'Gimana?'
        p 'Iya deh iya...'
        c 'Nah gitu donk...'

        hide citra with dissolve

        "Aku mengembalikan buku yang kuambil dari ke rak buku."
        "Citra mulai meninggalkan ruangan perpustakaan."
        "Lalu, aku ikut meninggalkan ruangan perpustakaan dan mengikuti Citra."

        #kantin
        scene bg canteen with dissolve
        python:
            renpy.notify("Kantin")

        "Sesampainya disana Citra langsung menuju ke tempat pembelian."
        "Disana aku melihat Yeri sedang sendirian."
        "Aku menghampirinya dan menyapanya."

        show idleyerinormal with dissolve

        p "Hai Yeri... Kamu lagi ngapain?"

        hide idleyerinormal
        show yerisurprised at short_shake, center

        y "Eh [name]... Kenapa kamu kesini?"

        hide yerisurprised
        show yerismile at short_shake, center

        y "Katanya ngga mau ikut ke kantin?"
        hide yerismile
        show idleyerismile
        p "Aku ikut Citra tadi." 
        p "Dipaksa sih."
        
        hide idleyerismile 
        show yericheerful at short_shake, center
        
        y "Hahahaha... Dipaksa yaa."
        hide yericheerful
        show idleyericheerful
        p "Ya mau gimana lagi."
        
        hide idleyericheerful with dissolve
        
        "Saat kita berdua sedang mengobrol datang Kevin, Zaky, dan Citra."
        show kevincheerful at left with dissolve:
            xalign 0.0
            yalign 1.0
        show citra at center with dissolve:
             
        show idlezakynormal at right with dissolve:
            xalign 0.9
            yalign 1.0
        
        k "Hai..."

        hide kevincheerful
        show kevinhappy at short_shake:
            xalign 0.0
            yalign 1.0

        k "Eh... Ada [name], katanya kamu ga mau ikut ke kantin sama kita."
        hide kevinhappy
        show idlekevinhappy at left:
            xalign 0.0
            yalign 1.0
        show zakytalk at right:
            xalign 0.9
            yalign 1.0
        z "Iya... Kenapa tadi ga mau ikut?"
        hide zakytalk
        show idlezakynormal at right:
            xalign 0.9
            yalign 1.0
        c "Tadi [name] bareng sama aku dari perpustakaan."
        hide idlezakynormal
        show zakytalk at right:
            xalign 0.9
            yalign 1.0
        z "Jadi gitu ya."
        hide zakytalk
        show zakyworry at right:
            xalign 0.9
            yalign 1.0
        z "Katanya tadi kamu mau ke kamar mandi."
        hide zakyworry
        show idlezakynormal at right:
            xalign 0.9
            yalign 1.0
        p "Iya tadi aku ke kamar mandi sih."
        p "(Sebenarnya diriku berbohong.)"
        hide idlekevinhappy
        show kevinhappy at left:
            xalign 0.0
            yalign 1.0
        k "Begitu ya..."

        hide kevinhappy
        hide citra 
        hide idlezakynormal
        with dissolve
        
        "Kevin, Citra, dan Zaky mulai duduk di kursi meja kantin yang aku duduki."

        jump kantin_done

#---------------
#END OF PROLOGUE
#---------------
    label kantin_done:

        "Aku mulai ingat rapat pada sore nanti."

        jump chapter1_start

#---------------
#CHAPTER 1 
#---------------
label chapter1_start:

    show kevintalk at short_shake, center

    k "Oiya, aku ingetin lagi ya."
    k "Jangan lupa rapat sore nanti."

    hide kevintalk
    show idlekevintalk

    p "Memangnya kita mau membahas apa saja di rapat nanti?"

    hide idlekevintalk
    show kevintalk

    k "Rencananya nanti sore pas sepulang sekolah mau ngumpulin semua anggota pengurus OSIS."

    k "Jadi-"

    hide kevintalk
    show yeriangry2 at long_shake, center

    y_shout "AH ANJIRLAH..."
    y "sebenarnya aku males banget buat ikut rapat."

    hide yeriangry2 with dissolve
    show citra with dissolve

    c "Hahaha, sabar Yeri.."
    c "Emang resikonya ikut organisasi tu ya gini."
    c "Pulangnya telat mulu."

    hide citra with dissolve
    show yeritalk at short_shake, center

    y "Iyadeh iya, Silahkan kalau mau dilanjut Vin.."

    hide yeritalk 
    with dissolve

    show kevintalk at short_shake, center

    k "Jadi rapat kali ini itu mau membahas tentang acara ulang tahun sekolah kita."

    k "Ini kujelasin sedikit."

    hide kevintalk with dissolve

    "Lalu Kevin menjelaskan sedikit tentang rapat nanti."

    

    p "Lalu kenapa di jadwal itu lama sekali rapatnya?"

    show yerinormal with dissolve:
        xalign 0.2
        yalign 1.0
    show citra with dissolve:
        xalign 0.8
        yalign 1.0

    y "Itulah kenapa aku malas ikut rapatnya."
    hide yerinormal
    show idleyerinormal:
        xalign 0.2
        yalign 1.0
    c "Iya nih, dari jam 4 sore sampai jam 8 malam itu lama banget."

    hide citra
    hide idleyerinormal 
    with dissolve

    show zakyhappy with dissolve

    z "Gini, karena waktunya sudah mepet, maka rapat diadakan selama 4 jam."
    z "Jadi rencana Kevin tu mau rapat sekali jalan aja."

    show zakyhappy with move:
        xalign 0.2
        yalign 1.0

    hide zakyhappy

    show idlezakyhappy:
        xalign 0.2
        yalign 1.0

    show kevintalk at long_shake:
        xalign 0.7
        yalign 1.0

    k "Yep betul."
    k "Lagian kita dapat dana dari sekolah juga baru kemaren malam."
    k "Jujur aku juga agak jengkel sama guru Kesiswaannya karena dia nganggep acara ini sepele."

    hide kevintalk
    show idlekevintalk:
        xalign 0.7
        yalign 1.0

    hide idlezakyhappy
    show zakytalk:
        xalign 0.2
        yalign 1.0

    z "Tapi mau gimana lagi, daripada ngeluh terus mending fokus sama event besar ini."

    hide idlekevintalk
    hide zakytalk 
    with dissolve

    "Tiba tiba Yeri tertawa dengan sangat keras."
   
    show yeriangry2 at long_shake, center

    y "Hahaha..."
    y "Apa yang kamu harapkan dari sekolah ini."
    y "Memang sih, dari fasilitas dan muridnya itu sangat bergengsi."
    y "Tapi guru guru disini beberapa ada yang tidak niat untuk menjadi guru dan hanya ingin gajinya saja."

    hide yeriangry2 with dissolve

    show citra with dissolve

    c "Hey Yeri..." 
    c "Jangan keras keras nanti kedengeran guru lain gimana?"
    show citra with move:
        xalign 0.3
        yalign 1.0
    
    show zakytalk:
        xalign 0.7
        yalign 1.0
    z "Iya nih..." 
    z "Yeri kalo ngomong kadang ga dipikir dulu dua kali."

    hide citra
    hide zakytalk
    with dissolve

    show yericheerful at long_shake, center

    y "Halah gapapa, gaada guru disini."

    hide yericheerful
    show yeritalk

    y "Toh kalau memang ada guru yang dengar biar dia tersinggung aja."

    show yeritalk with move: 
        xalign 0.2
        yalign 1.0

    hide yeritalk
    show idleyeritalk:
        xalign 0.2
        yalign 1.0

    show kevinhappy with dissolve:
        xalign 0.8
        yalign 1.0

    k "Ckckck."
    k "Yaa beginilah Yeri, emang dari dulu sudah begini."

    hide kevinhappy
    show idlekevinhappy:
        xalign 0.8
        yalign 1.0

    hide idleyeritalk
    show yericheerful at long_shake:
        xalign 0.2
        yalign 1.0

    y "Lagipula kita disini cukup ramai juga gaada yang dengar sama pembicaraan kita."
    y "Kecuali hantu yang bergentayangan disini hahaha..."

    hide yericheerful
    hide idlekevinhappy
    with dissolve

    show zakyhappy with dissolve

    z "Eh kamu jangan bilang gitu di sekolah ini..."
    z "Nanti kamu didatengin hantu beneran lo."

    show zakyhappy with move:
        xalign 0.8
        yalign 1.0

    hide zakyhappy
    show idlezakyhappy:
        xalign 0.8
        yalign 1.0

    show yeriangry2 at short_shake:
        xalign 0.2
        yalign 1.0

    y "Dih... mana ada hantu di sekolah ini..." 
    y "lagipula aku ga percaya sama hal hal begituan."

    hide idlezakyhappy
    show zakytalk:
        xalign 0.8
        yalign 1.0

    hide yeriangry2
    show idleyeriangry2:
        xalign 0.2
        yalign 1.0

    z "Kamu belum pernah dengar rumor ada hantu di sekolah ini?"

    hide idleyeriangry2
    show yeritalk at short_shake:
        xalign 0.2
        yalign 1.0

    hide zakytalk
    show idlezakytalk:
        xalign 0.8
        yalign 1.0

    y "Heee..."
    y "Gimana tuh rumorya??"
    y "Paling paling cuma pohon keramat atau kamar mandi terkutuk kan..."
    hide yeritalk
    hide idlezakytalk
    with dissolve
    "Pembicaraan ini semakin menjauh dari pembahasan rapat."
    "Justru malah membahas tentang hal-hal yang diluar rapat."


    show zakyworry at long_shake:
        xalign 0.5
        yalign 1.0

    z "Bukan..."
    z "Jadi katanya sekolah ini sangat menyeramkan kalau di malam hari."

    hide zakyworry
    show kevinhappy at long_shake:
        xalign 0.5
        yalign 1.0

    k "Hahaha..."
    k "Bukannya semua sekolah itu memang kesannya menyeramkan kalau di malam hari?"

    show kevinhappy with move:
        xalign 0.2
        yalign 1.0

    hide kevinhappy
    show idlekevinhappy:
        xalign 0.2
        yalign 1.0

    show zakyhappy with dissolve:
        xalign 0.8
        yalign 1.0

    z "Gini, aku pernah dengar kalau kita itu gaboleh di sekolah sampai malam hari..."
    z "Katanya sih jika kita berada di sini hingga malam hari nanti akan menghilang dan tidak pernah ditemukan kembali..."
    z "Makanya jika sekolah ada kegiatan kemah biasanya diadakan diluar sekolah."

    hide idlekevinhappy
    show kevintalk at long_shake:
        xalign 0.2
        yalign 1.0

    hide zakyhappy
    show idlezakyhappy:
        xalign 0.8
        yalign 1.0

    k "Yang kamu katakan masuk akal sih..."
    k "Tapi, apa ada kasus murid menghilang disini?"

    hide kevintalk
    show idlekevintalk:
        xalign 0.2
        yalign 1.0

    hide idlezakyhappy
    show zakytalk:
        xalign 0.8
        yalign 1.0

    z "Belum tau sih, tapi aku denger denger ada orang yang sempat hilang lalu ditemukan kembali..."

    hide idlekevintalk
    hide zakytalk 
    with dissolve

    "Tiba-tiba Yeri tertawa dengan keras lagi."

    show yericheerful at long_shake, center

    y_shout "HAHAHAHAHAHA"

    y "Mana ada murid yang menghilang dan bisa kembali lagi disini..."
    y "itu ma, cuma gosip."

    hide yericheerful
    show zakyhappy 

    z "Iya denger denger sih begitu..."
    z "Kalau beneran ada apa ngga ya aku gatau."
    
    menu:
        "Aku masi ga percaya...":
            jump zaky_story

        "Kamu dengar rumor itu darimana?":
            jump zaky_story

        "...":
            jump zaky_story

    label zaky_story:

        z "Jadi kemarin jam 6 sore, aku baru keluar sekolah karena tugas piket dan sekalian nyelesaiin tugas."
        z "Lalu saat di gerbang aku gak sengaja denger dua satpam sedang membicarakan tentang sekolah ini saat malam hari."
        z "Jadi kata salah satu satpam itu..."
        #ganti scene
        z "Kalau bisa jangan masuk di sekolah ini pada malam hari."
        z "Dan jika masi ngeyel kamu bakal menyesal."

        hide zakyhappy with dissolve

        "Setelah mendengar itu, aku merasa rumor yang di ceritakan Zaky sangat tidak masuk akal."
        "Dan sepertinya bukan hanya aku yang merasakan itu."

        show kevincheerful at long_shake, center

        k "Hahaha, mana mungkin..."

        hide kevincheerful
        show zakyhappy

        z "Iya beneran, aku denger dari telinga ku sendiri, rill no fek."

        hide zakyhappy
        show yericheerful at short_shake, center

        y "Halah, mungkin itu satpamnya yang penakut."

        show yericheerful with move:
            xalign 0.2
            yalign 1.0
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0

        show kevinserious with dissolve:
            xalign 0.8
            yalign 1.0

        k "Mana mungkin..."
        k "Satpam kan sudah dilatih buat berani."
        hide kevinserious
        show idlekevinserious:
            xalign 0.8
            yalign 1.0
        hide idleyericheerful
        show yerinormal:
            xalign 0.2
            yalign 1.0

        y "Iya bener si..."

        hide yerinormal
        hide idlekevinserious
        with dissolve

        show zakyhappy at short_shake, center

        z "Tapi karena kedua satpam itu membahasnya, aku jadi heran."

        hide zakyhappy
        show citra at long_shake, center

        c "Tapi memangnya kalau disekolah saat malam hari ada hantunya yah?"
        c "Kan hantu itu tidak nyata."

        hide citra with dissolve
        "Seperti biasa Citra memang tidak percaya dengan hantu."

        p "Jaman sekarang masi percaya hantu?"

        show yericheerful with dissolve

        y "Bener juga yak, hantu itu tidak nyata."

        hide yericheerful
        show yerihappy at long_shake, center

        y "Jadi buat apa takut sama hantu?"

        hide yerihappy with dissolve
        show zakyhappy with dissolve

        z "Kalian semua pemberani ya."
        z "Aku nonton film horror, 3 hari gabisa tidur dengan tenang."

        hide zakyhappy
        show citra at short_shake, center

        c "Kalo nonton begituan ma aku juga takut sebenarnya..."
        c "Tapi yang namanya film itu kan belum tentu nyata."
        c "Jadi aku masi tetep ga percaya yang namanya hantu.."

        hide citra with dissolve

        show yericheerful at long_shake, center

        y "Iyep.. betulll"
        y "Hantu itu tidak nyata, kayak husbuku aja."
        hide yericheerful
        show idleyericheerful
        p "Hahahaha"
        p "Bisa aja kamu, Teri."

        hide idleyericheerful
        show yerisurprised at long_shake, center

        y_shout "Teri??"
        y_shout "JA-"

        hide yerisurprised
        show yeritsundere2 at short_shake, center

        y_shout "JANGAN PANGGIL AKU TERI, DASAR BODOH!!!"

        p "kan cuma bercanda Yeri, hehe"

        hide yeritsundere2
        show yeriangry2 at short_shake, center

        y "Dih, bodolah."

        hide yeriangry2 with dissolve
        show citra with dissolve

        c "Udah, sabar Yeri."
        c "[name] kan cuma bercanda."

        hide citra with dissolve
        show zakyhappy at short_shake, center

        z "Hahaha, bercandanya."

        hide zakyhappy with dissolve
        show kevintalk with dissolve

        k "Btw..."
        k "Perasaan tadi kita lagi membahas rapat Osis dah."
        k "Kenapa pembahasannya jadi kemana-mana?"
        hide kevintalk
        show idlekevintalk
        p "Iya juga."
        p "Jadi gimana? Rapatnya jadi jam 4 sore nanti?"
        hide idlekevintalk
        show kevintalk
        k "Iya, jangan sampe lupa... apalagi cabut."
        hide kevintalk
        show idlekevintalk
        p "Gaakan cabut aku."
        p "Tah aku kan anaknya si paling rajin hehe."

        hide idlekevintalk
        show yerinormal at long_shake, center

        y "Iyadeh si paling rajin."

        show yerinormal with move:
            xalign 0.2
            yalign 1.0

        show citra with dissolve:
            xalign 0.7
            yalign 1.0
        
        hide yerinormal
        show idleyerinormal:
            xalign 0.2
            yalign 1.0

        c "Hahaha."
        c "Eh Yer, sebelum rapat nanti kita ketemuan dulu di depan perpus yaa"
        c "Aku ada urusan, jadi tolong temani aku."
        hide idleyerinormal
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0

        y "Oke gas."
        hide yericheerful
        show yerismile:
            xalign 0.2
            yalign 1.0
        y "Kebetulan aku juga mau meminjam beberapa buku buat ulangan besok."
        hide yerismile
        show idleyerismile:
            xalign 0.2
            yalign 1.0
        c "Eh mapel apa?"
        hide idleyerismile
        show yerismile:
            xalign 0.2
            yalign 1.0
        y "Bahasa Jepang."
        hide yerismile
        hide citra
        with dissolve
        "Aku teringat dengan ulangan Bahasa Jepang."
        "Beberapa hari yang lalu diriku telah mengerjakan ulangan Bahasa Jepang."
        "Bisa dibilang cukup sulit ulangan tersebut."
        "Nilaiku bisa dibilang cukup baik."
        "Dari yang kudengar kelasnya Citra telah mengerjakan ulangan Bahasa Jepang."
        
        show citra at center:
            
        c "Mapel yang cukup sulit ya."
        c "Kemarin aku sudah ulangannya."
        show citra with move:
            xalign 0.7
            yalign 1.0
        show yerisurprised at long_shake:
            xalign 0.2
            yalign 1.0
        y "Lo kamu sudah ulangan?"
        hide yerisurprised
        show idleyerisurprised:
            xalign 0.2
            yalign 1.0
        c "Iya, kemarin di jam ke tujuh."
        hide idleyerisurprised
        show yerisad at short_shake:
            xalign 0.2
            yalign 1.0
        
        y "Kok enak sih.. kelasku baru besok loh."
        hide yerisad
        show yerihappy:
            xalign 0.2
            yalign 1.0
        y "Oiya.. boleh kali."
        hide yerihappy
        show yericheerful:
            xalign 0.2
            yalign 1.0
        y "Bocoran soalnya."
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        c "Aduh maaf Yer."
        c "Karena ulangannya susah pas aku sudah selesai seketika langsung lupa semua..."
        hide idleyericheerful
        show yerisad at short_shake:
            xalign 0.2
            yalign 1.0
        y "Ah kamu ga asik."
        hide yerisad
        hide citra
        with dissolve
        show zakytalk
        z "Udah-udah daritadi ngerumpi sendiri."
        hide zakytalk
        show idlezakytalk
        p "Iyanih.. women."
        hide idlezakytalk with dissolve

        "Sesaat kemudian bel masuk kelas pun berbunyi."
        "Hal tersebut menandakan untuk segera masuk ke kelas masing-masing."
        #bel
        show kevintalk with dissolve
        k "Udah bel tuh, mending kita masuk kelas aja."
        k "Ayo [name] kita ke kelas."
        hide kevintalk
        show idlekevintalk
        p "Okeoke"
        hide idlekevintalk
        show zakytalk at long_shake, center
        z "Weh, tungguin napa.."
        z "Aku juga mau bareng ke kelasnya."
        hide zakytalk
        show idlezakytalk
        p "Halah, manja banget lu."
        hide idlezakytalk
        show zakytalk at short_shake, center
        z_shout "Bodoamat lah."
        hide zakytalk
        show idlezakytalk
        p "ehe"
        hide idlezakytalk with dissolve

        "Kami berlima pun kembali ke kelas masing-masing untuk pelajaran selanjutnya."
        "Sebenarnya aku masih penasaran dengan cerita yang diceritakan oleh Zaky."
        "Apakah cerita tersebut beneran nyata atau tidak."
        "Bagaimana jika cerita tersebut NYATA?"

    #ch1 selesai(?) (hore(?))

    #-----------------
    #CHAPTER 2 OPEN
    #-----------------

        scene inclass with dissolve
        python:
            renpy.notify("Kelas 2-A")
        "KRINGGGGGGGGGGGGGG"
        "Jam telah menunjukkan pukul 3 sore."
        "Pelajaran hari ini telah selesai."
        "Aku, Zaky, dan Kevin keluar menuju lorong depan kelas."
   
        scene bg hallway with dissolve

        python:
            renpy.notify("Lorong Sekolah")
        
        show zakytalk with dissolve
        z "*Huft* capek banget dah hari ini."
        hide zakytalk
        show idlezakytalk
        p "Iya nih, hari ini banyak banget materi prakteknya."
        hide idlezakytalk
        show zakysad at short_shake, center
        z "Bener banget!"
        z "Udah praktek membelah kodok, membuat es krim, sama berdialog pakai Bahasa Jepang."
        show zakysad with move:
            xalign 0.8
            yalign 1.0
        hide zakysad 
        show idlezakysad:
            xalign 0.8
            yalign 1.0
        show kevintalk with dissolve:
            xalign 0.2
            yalign 1.0
            
        k "Udah, gapapa."
        hide kevintalk
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        k "Lagipula pada bisa menjalaninya kan?"
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        hide idlezakysad
        show zakysad:
            xalign 0.8
            yalign 1.0
        z "Iya sih, tapi capek tau."
        hide zakysad
        show idlezakysad:
            xalign 0.8
            yalign 1.0
        p "Hahaha, daripada ngeluh terus."
    menu:
        "Mending kita ke kantin dulu bentar.":
            jump chap2kantin_yes
        "Mending kita menemui Citra sama Yeri.":
            jump chap2kantin_no

    label chap2kantin_yes:
        $ menu_flag = True
        hide idlezakysad
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Oh iya, gimana tuh Kevin?"
        hide zakytalk
        hide idlekevinsmile
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Ayok dah, kita ke kantin bentar."
        hide kevintalk
        hide idlekevintalk
        hide idlezakytalk
        with dissolve
        "Kita bertiga mulai pergi kekantin."
        scene canteen with dissolve
        python:
            renpy.notify("Kantin")
        show kevintalk with dissolve
        k "Kita ke kantin mau ngapain?"
        hide kevintalk with dissolve
        show zakytalk with dissolve
        z "Ya buat jajan, masak mau nginep disini."
        hide zakytalk with dissolve
        show kevintalk with dissolve
        k "Oh, yaudah."
        k "Agak cepetan ya!"
        hide kevintalk
        show idlekevintalk   
        p "Oke!"
        hide idlekevintalk with dissolve
        "Kami bertiga langsung menuju tempat penjaga kantin untuk membeli beberapa jajanan."
        "Tetapi..."
        "Entah kenapa suasana semakin sepi."
        "Mungkin ini sudah jam pulang."
        "Namun, biasanya walau ini sudah jam pulang."
        "Kantin tidak akan sampai sesepi ini."
        show zakyworry with dissolve
        z "Eh eh, ini perasaanku aja atau emang ini suasana kantin kayak sepi gini ya?"
        show zakyworry with move:
            xalign 0.8
            yalign 1.0
        hide zakyworry 
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        show kevintalk with dissolve:
            xalign 0.2
            yalign 1.0
        k "Emang iya?"
        k "Habisnya aku kalo jam segini ga pernah ke kantin."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Perasaanmu aja kali."
        p "Disini kan masih ada penjaga kantinnya."
        hide idlekevintalk
        hide idlezakyworry
        with dissolve
        #-------------
        p "Iya kan bu?"
        pk "..."
        show zakyworry with dissolve #SCENE WARUNG KANTIN
        z "Bu???"
        hide zakyworry with dissolve
        pk "..."
        #-------------
        "Penjaga kantin tidak menanggapinya."
        "Semakin lama semakin aneh dengan kejadian ini."
        "Zaky mendekatiku lalu membisiki sesuatu."

        show zakyworry with dissolve

        z_whisper "Eh... bener kan? Kayak semakin sepi disini"
        hide zakyworry
        show idlezakyworry
        p_whisper "Duh, bener nih."
        hide idlezakyworry
        show zakyworry
        z_whisper "Kok aku jadi takut begini ya."
        z_whisper "Mending kita cabut aja dari kantin."
        hide zakyworry
        show idlezakyworry
        p_whisper "Iya, ayo dah!"
        p_whisper "Tapi..."
        p_whisper "Dimana si Kevin?"
        hide idlezakyworry
        show zakyworry
        z "..."
        hide zakyworry with dissolve
        "Tiba-tiba ada seseorang yang ingin menghampiri dari belakang."
        u_shout "Hei!!!"
        #-------------
        #IMAGE KAGET ZAKY!!!!
        show zakyworry at long_shake, center
        zc_shout "KYAAAHHHHHHHH!!!"
        #----------
        hide zakyworry
        #------------
        #IMAGE KEVIN KAGET
        show kevinserious at long_shake, center
        k_shout "WAAAAAAAAAAAA"
        k "Hei, bikin kaget saja."
        k "Kenapa sih?"
        show kevinserious with move:
            xalign 0.2
            yalign 1.0
        show zakyworry at short_shake:
            xalign 0.8
            yalign 1.0
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
            
        z "Kamu yang bikin kaget sialan!"
        hide zakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        show kevintalk at short_shake:
            xalign 0.2
            yalign 1.0
        k "HAHAHAHAHA"
        k "Iya maaf deh."
        k "Aku tadi habis ke kamar mandi dekat sini."
        hide kevintalk
        hide idlezakyworry
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        show zakyworry:
            xalign 0.8
            yalign 1.0
        z "Kenapa kamu ga ngomong dulu sih."
        hide idlekevintalk
        hide zakyworry
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        k "Iya maaf."
        k "Habisnya tadi aku kebelet banget."
        hide kevinsmile
        hide idlezakyworry
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Iya yaudah."
        z "Yuk, cabut sekarang."
        hide idlekevinsmile
        hide zakytalk
        show kevinserious:
            xalign 0.2
            yalign 1.0
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        k "Emang kenapa buru-buru amat?"
        hide kevinserious
        hide idlezakytalk
        show zakyworry:
            xalign 0.8
            yalign 1.0
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        
        z "Disini serem ga ada orang."
        hide idlekevinserious
        hide zakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        show kevintalk at short_shake:
            xalign 0.2
            yalign 1.0
        k_shout "HAHAHAHA"
        k "Udah takut jam segini di kantin?"
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
    menu:
        "Iya aku udah takut.":
            jump takut1_yes
        "Engga juga kok.":
            jump takut1_no

    label takut1_yes:
        
        p "Iya aku udah takut."
        hide idlekevintalk
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        k "Emang ada apa sih?"
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        p "Entah kenapa disini sepi banget."
        p "Terus waktu aku panggil penjaga kantin kok dianya engga ada jawaban."

        jump takut1_done

    label takut1_no:
        hide idlekevintalk
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        p "Engga takut sih."
        p "Cuma aneh aneh aja kenapa kok disini sepi banget."
        hide idlezakyworry
        show zakyworry:
            xalign 0.8
            yalign 1.0
        z "Iya bener!"
        hide zakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        p "Dan juga tadi penjaga kantin udah aku panggil ga ada jawaban sama sekali."
        jump takut1_done
    label takut1_done:
        hide idlezakyworry
        hide idlekevintalk
        hide idlekevinsmile
        with dissolve

        "Entah kenapa suasana dikantin ini sangat sepi sekali."
        "Seharusnya jika masih jam segini masih ada beberapa murid yang berada di kantin."
        "Tetapi justru tidak ada seorang murid kecuali kita bertiga yang disini."
        "Ini seperti sesuatu yang TIDAK BIASA."

        
        show kevintalk at short_shake, center
        k "Hahaha, mestilah!"
        k "Emang ga ada jawaban dari penjaga kantin."
        k "Habisnya, penjaga kantinnya lagi di dekat kamar mandi tadi."
        
        show kevintalk with move:
            xalign 0.2
            yalign 1.0
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        show zakytalk:
            xalign 0.8
            yalign 1.0
        
        z "Owalah, ngapain dah disitu?"
        hide idlekevintalk
        hide zakytalk
        show idlezakynormal:
            xalign 0.8
            yalign 1.0
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Tadi aku saat mau kembali ke kantin."
        k "Ada ibu penjaga kantin itu lagi mengambil barang-barangnya."
        k "Jadi aku bantu mengambil barang-barangnya."
        hide kevintalk
        hide idlezakynormal
        show zakytalk:
            xalign 0.8
            yalign 1.0
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Ooohhh, jadi begitu ya."
        z "Pantas aja tadi [name] manggil kok ngga dijawab."
        z "Ternyata emang ga ada orangnya."
        hide zakytalk
        show zakytalk at short_shake:
            xalign 0.8
            yalign 1.0
        z "HAHAHAHAHA"
        hide idlekevintalk
        hide zakytalk
        show idlezakynormal:
            xalign 0.8
            yalign 1.0
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        k "Emang kalian pikir apaan?"
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
    menu:
        "Dedemit.":
            jump jokes1_a
        "Syaiton.":
            jump jokes1_b
        "Makhluk tak terlihat.":
            jump jokes1_c

    label jokes1_a:
        p "Dedemit."
        jump jokes1_done
    label jokes1_b:
        p "Syaiton."
        jump jokes1_done
    label jokes1_c:
        p "Makhluk tak terlihat."
        jump jokes1_done
    label jokes1_done:

        hide idlekevinsmile
        show kevintalk at short_shake:
            xalign 0.2
            yalign 1.0
        k "Hadeh."
        k "Mana ada yang kek gitu."
        k "Sudah-sudah, yok ke ruang OSIS."

        hide kevintalk
        hide idlezakynormal
        with dissolve

        "Kita bertiga beranjak meninggalkan kantin yang sunyi dan sepi itu."
        "Dan pergi menuju ke ruang OSIS."
        "Waktu di pertengahan jalan kita saling mengobrol."
        scene bg hallway with dissolve
        python:
            renpy.notify("Lorong Kelas")
        show kevintalk with dissolve
        k "Oiya, tadi Yeri chat aku."
        show kevintalk with move:
            xalign 0.2
            yalign 1.0
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        show zakyhappy:
            xalign 0.8
            yalign 1.0
        z "Chat apa?"
        z "Udah makan belum sayang?"
        z "Gitu?"
        hide zakyhappy
        hide idlekevintalk
        show kevinserious at short_shake:
            xalign 0.2
            yalign 1.0
        show idlezakyhappy:
            xalign 0.8
            yalign 1.0
        k "Mana ada, dia chat kalo dia sama Citra udah di ruang OSIS."
        hide idlezakyhappy
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        show zakyhappy2:
            xalign 0.8
            yalign 1.0
        z "Oh, kukira chat kayak gitu."
        hide zakyhappy2
        hide idlekevinserious
        show kevintalk at short_shake:
            xalign 0.2
            yalign 1.0
        show idlezakyhappy2:
            xalign 0.8
            yalign 1.0
        k "Ya enggalah!"
        k "Yakali aku pacaran ama Yeri."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Sudah-sudah, lebih baik kita langsung ke ruang OSIS aja."
        p "Kasihan mereka udah nungguin."
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya yaudah."
        hide kevintalk
        show kevintalk at short_shake:
            xalign 0.2
            yalign 1.0
        k "Btw..."
        k "Tadi waktu aku menolong ibu penjaga kantin."
        k "Beliau memberitahu sesuatu kepadaku."
        hide kevintalk
        hide idlezakyhappy2
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Bilang apaan?"
        hide idlekevintalk
        hide zakytalk
        show kevinserious:
            xalign 0.2
            yalign 1.0
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        k "Jadi gini."
        k "Intinya ibu itu memberi tahu sesuatu kalau kita tidak boleh malam-malam di sekolahan."
        hide kevinserious
        hide idlezakytalk
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        show zakyworry:
            xalign 0.8
            yalign 1.0
        z "Emang kenapa?"
        z "Lagipula kita udah izin sama orang tua kita."
        z "Harusnya kan tidak apa-apa."
        hide idlekevinserious
        hide zakytalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        k "Bukan gitu."
        k "Kata ibu penjaga katanya disekitar lorong ini kadang ada penampakan."
        hide kevintalk
        hide idlezakytalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        show zakyworry:
            xalign 0.8
            yalign 1.0
        z "Eh jangan nakut-nakutin ya."
        hide idlekevinserious
        hide zakyworry
        show kevintalk:
            xalign 0.2
            yalign 1.0
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        k "Aku engga nakut-nakutin, tapi emang mulai heran aja."
        k "Baru tau kalau ada penampakan begituan di sekolah."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Emang penampakan apa?"
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Jadi kata ibu penjaga."
        k "Katanya kalau jam segini nih mulai ada penampakan pelajar sekolah ini."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
    menu:
        "Paling itu emang beneran manusia.":
            jump ask1_a
        "Hah? Pelajar gimana?":
            jump ask1_b
        
    label ask1_a:
        p "Palingan itu cuma manusia."
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Tapi katanya tadi gitu sih."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Apa iya? Yang bener."
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya."
        jump ask1_done
    label ask1_b:
        p "Hah? Pelajar?"
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya pelajar, di sekitar sini."
        jump ask1_done
    label ask1_done:
        k "Jadi tuh ada penampakan kayak pelajar cewe disini."
        k "Rambutnya panjang dan wajahnya itu pucat."
        k "Ibu penjaga pernah mencoba buat manggil dia."
        k "Tetapi pelajar itu hanya berdiri dan diam aja disana."
        k "Lalu saat ingin pergi."
        k "Ibu penjaga melihat kebelakang lagi dan saat itu pelajarnya sudah tidak ada lagi."
        hide kevintalk
        hide idlezakyworry
        with dissolve
        "Kevin menceritakan panjang lebar apa yang sudah pernah dialami oleh ibu penjaga kantin."
        "Saat Kevin menceritakan tentang ciri-ciri pelajar perempuan yang dilihat ibu penjaga kantin itu."
        "Aku..."
    menu:
        "Mulai penasaran dengan apa yang dialami oleh ibu penjaga kantin.":
            jump imo1_a
        "Kurang percaya dengan kejadian yang dialami oleh ibu penjaga kantin.":
            jump imo1_b
        "Merinding dengan yang diceritakan Kevin.":
            jump imo1_c
    #--------------------------------------------------------------
    label imo1_a:
        "Aku mulai penasaran dengan apa yang dialami ibu penjaga kantin."
        "Itu sangat menarik apabila bisa diusut tuntas."
        "Tetapi BAGAIMANA JIKA CERITA TADI ADALAH NYATA?"

        show zakyworry with dissolve

        z "Kok serem yah."
        z "Cabut aja yok!"

        hide zakyworry with dissolve
        show kevinserious with dissolve

        k "Iya, makanya barang-barang bawaan ibu penjaga sempat terjatu karena terburu-buru."
        k "Tapi jujur saja, aku masih diantara percaya atau tidak percaya dengan kejadian itu."
        k "Mana ada yang namanya hantu disini."

        hide kevinserious with dissolve
        show zakyworry with dissolve

        z "Ada tuh, seperti yang kamu ceritain tadi."
        z "Ibu penjaga kantin lihat penampakan disini."
        hide zakyworry with dissolve
        show kevinserious with dissolve

        k "Iya bener, tapi aku kurang percaya."

        hide kevinserious 
        show idlekevinserious

    menu:
        "Aku bingung kenapa bisa ada kejadian seperti itu.":
            jump imo3_a
        "Aku malah penasaran.":
            jump imo3_b
    label imo3_a:
        p "Aku bingung kenapa bisa ada kejadian seperti itu."
        jump imo3_done
    label imo3_b:
        p "Aku malah penasaran."
        jump imo3_done
    label imo3_done:
        show kevinserious at short_shake, center
        k "Bener banget!"
        hide kevinserious
        show idlekevinserious
        p "Itu palingan ibu penjaganya masih kecapean."
        hide idlekevinserious
        show kevintalk at short_shake, center
        k "Nah, mungkin itu masuk akal."
        hide kevintalk with dissolve
        show zakyworry with dissolve
        z "Ni orang engga ada takutnya ya?"
        z "Mending cabut aja deh sekarang."
        hide zakyworry with dissolve
        show kevintalk with dissolve
        k "Iya, yaudah ayok!"
        hide kevintalk with dissolve
        jump imo1_done
    label imo1_b:
        "Aku kurang percaya dengan kejadian yang dialami oleh ibu penjaga kantin."
        "Kalau dipikir-pikir bisa saja pelajar cewe itu manusia asli."
        "Karena jam segitu masih masuk akal ada anak sekolah yang masih lalu lalang di sekitar sekolah."
        "Tetapi BAGAIMANA JIKA CERITA TADI ADALAH NYATA?"

        show zakyworry with dissolve

        z "Kok serem yah."
        z "Cabut aja yok!"

        hide zakyworry with dissolve
        show kevinserious with dissolve

        k "Iya, makanya barang-barang bawaan ibu penjaga sempat terjatu karena terburu-buru."
        k "Tapi jujur saja, aku masih diantara percaya atau tidak percaya dengan kejadian itu."
        k "Mana ada yang namanya hantu disini."

        hide kevinserious with dissolve
        show zakyworry with dissolve

        z "Ada tuh, seperti yang kamu ceritain tadi."
        z "Ibu penjaga kantin lihat penampakan disini."
        hide zakyworry with dissolve
        show kevinserious with dissolve

        k "Iya bener, tapi aku kurang percaya."

        hide kevinserious 
        show idlekevinserious

    menu:
        "Sama aku juga kurang percaya.":
            jump imo2_a
        "Tapi cerita tadi memang kurang menyakinkan sih.":
            jump imo2_b
    label imo2_a:
        p "Sama aku juga kurang percaya."
        jump imo2_done
    label imo2_b:
        p "Tapi cerita tadi memang kurang menyakinkan sih."
        jump imo2_done
    label imo2_done:
        show kevinserious at short_shake, center
        k "Nah kan."
        hide kevinserious
        show idlekevinserious
        p "Itu palingan ibu penjaganya masih kecapean."
        hide idlekevinserious
        show kevinserious at short_shake, center
        k "Nah, mungkin itu masuk akal."
        hide kevinserious with dissolve
        show zakyworry with dissolve
        z "Ni orang engga ada takutnya ya?"
        z "Mending cabut aja deh sekarang."
        hide zakyworry with dissolve
        show kevintalk with dissolve
        k "Iya, yaudah ayok!"
        hide kevintalk with dissolve
        jump imo1_done
    label imo1_c:
        "Aku merinding dengan yang diceritakan Kevin."
        "Hanya mendengarkan saja aku merasa merinding."
        "BAGAIMANA JIKA CERITA TADI BENAR-BENAR NYATA?"

        show zakyworry with dissolve

        z "Kok serem yah."
        z "Cabut aja yok!"

        hide zakyworry with dissolve
        show kevinserious with dissolve

        k "Iya, makanya barang-barang bawaan ibu penjaga sempat terjatu karena terburu-buru."
        k "Tapi jujur saja, aku masih diantara percaya atau tidak percaya dengan kejadian itu."
        k "Mana ada yang namanya hantu disini."

        hide kevinserious with dissolve
        show zakyworry with dissolve

        z "Ada tuh, seperti yang kamu ceritain tadi."
        z "Ibu penjaga kantin lihat penampakan disini."
        hide zakyworry with dissolve
        show kevinserious with dissolve

        k "Iya bener, tapi aku kurang percaya."

        hide kevinserious 
        show idlekevinserious

    menu:
        "Aku takut banget sama cerita tadi.":
            jump imo4_a
        "Aku merinding dengar cerita tadi.":
            jump imo4_b
    label imo4_a:
        p "Aku takut banget sama cerita tadi."
        jump imo4_done
    label imo4_b:
        p "Aku merinding denger cerita tadi."
        jump imo4_done
    label imo4_done:
        show kevinserious with dissolve
        k "Hadeh..."
        k "Masak gitu aja takut sih."
        hide kevinserious
        show idlekevinserious
        p "Tetapi kalau dipikir-pikir bisa saja ibunya lagi kecapean."
        p "Jadi lagi halu kayak gitu."
        hide idlekevinserious
        show kevintalk
        k "Nah, mungkin itu masuk akal."
        hide kevintalk with dissolve
        show zakyworry with dissolve
        z "Sudah cukup."
        z "Mending cabut aja deh sekarang."
        hide zakyworry with dissolve
        show kevintalk with dissolve
        k "Iya, yaudah ayok!"
        hide kevintalk with dissolve
        jump imo1_done
    label imo1_done:

        scene bg osisdepan with dissolve
        python:
            renpy.notify("Depan Ruang OSIS")
        "Akhirnya kita bertiga sampai ke didepan ruang OSIS."
        "Selama perjalanan tadi diriku selalu membayangkan apa yang diceritakan Kevin."
        "Disini diriku bertemu dengan Citra dan Yeri yang sedang berada didepan ruangan OSIS."

        show zakyhappy at long_shake, center
        z_shout "AKHIRNYAAAAAAAA"
        z "Sampai juga disini."
        hide zakyhappy
        show yerinormal with dissolve
        y "Kenapa dah?"
        hide yerinormal
        show zakynormal with dissolve
        z "Ceritanya panjang banget."
        hide zakynormal
        show yerinormal with dissolve
        y "Apa? Aku penasaran banget."
        show yerinormal with move:
            xalign 0.2
            yalign 1.0
        hide yerinormal
        show idleyerinormal:
            xalign 0.2
            yalign 1.0
        show citra with dissolve:
            xalign 0.8
            yalign 1.0
        c "Kok kalian seperti orang kebingungan gitu."
        c "Sama kalian keringetan gitu."
        hide idleyerinormal
        show yerinormal:
            xalign 0.2
            yalign 1.0
        y "Iya nih, cerita aja."
        hide yerinormal
        show yerismile:
            xalign 0.2
            yalign 1.0
        y "Tetap kudengerin kok meskipun panjang ceritanya."
        hide yerismile
        show idleyerismile:
            xalign 0.2
            yalign 1.0
    menu:
        "Tadi tuh Kevin cerita kejadian aneh sama ada kejadian aneh.":
            jump mcstroy1_a
        "Engga ada apa-apa sih.":
            jump mcstroy1_b
    label mcstroy1_a:
        p "Tadi tuh Kevin cerita kejadian aneh sama ada kejadian aneh."
        p "Nah Kevin cerita kalau Penjaga Kantin pernah melihat sesuatu yang tidak masuk akal."
        p "Lalu, tadi dikantin tuh an-"

        hide idleyerismile
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Apa? Cerita hantu kayak si Zaky tadi?"
        hide idleyericheerful
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHAHAHA"
        y "Zaky sama Kevin engga ada bedanya."
        y "Suka cerita yang aneh-aneh."
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        c "Memangnya gimana sih?"
        c "Kalian sampai buat kalian jadi orang kebingungan."
        hide idleyericheerful
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHAHAHA"
        y "Sudahlah aneh-aneh aja kalian bertiga ini."
        y "Yok masuk keruangan."
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        p "Tapi, tadi tuh dikantin an-"
        hide idleyericheerful
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHAHAHA"
        y "Sudah-sudah capek ketawa aku melihat kalian."
        y "Ayo, masuk keruangan."
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        c "Iya nih, udah ada beberapa anggota yang datang."
        c "Katanya mau diselesaiin hari ini."
        hide citra
        hide idleyericheerful
        with dissolve

        show kevinsmile with dissolve

        k "Ya sudah yuk."
        k "Engga usah dipikirin yang tadi ya."

        hide kevinsmile with dissolve
        show zakynormal with dissolve
        z "Tapi..."
        z "Ya udah deh, yok [name] masuk keruangan."
        hide zakynormal 
        show idlezakynormal
        p "Oke deh masuk aja lah."
        hide idlezakynormal with dissolve
        jump mcstroy1_done
    label mcstroy1_b:
        p "Engga ada apa-apa sih."
        p "Cuma tadi Kevin cerita sesuatu yang lumayan serem sama tadi kita mengalami kejadian yang cukup aneh."
        p "Tapi kejadian tadi cuma kebetulan saja kok."

        hide idleyerismile
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Kejadian apa sih?"
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        p "Tadi kan kita ke kantin suasananya tu sunyi dan sepi gitu."
        p "Jadi ya mungkin itu cuma kebetulan."
        hide idleyericheerful
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Cuma gitu aja."
        hide yericheerful
        show yerismile:
            xalign 0.2
            yalign 1.0
        y "Emang Kevin cerita apaan?"
        hide yerismile
        show idleyerismile:
            xalign 0.2
            yalign 1.0
        p "Katanya Penjaga Kantin pernah mengalami kejadian yang aneh gitu."
        hide idleyerismile
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Kevin mau jadi kayak Zaky kah?"
        y "Suka cerita aneh-aneh."
        hide citra
        hide yericheerful
        with dissolve
        show kevinsmile with dissolve
        k "Aku cuma menceritakan yang diceritain sama Penjaga Kantin kok."
        k "Sudah-sudah lupakan aja kejadian tadi."
        k "Ayo masuk ke ruangan."
        hide kevinsmile with dissolve
        show yerihappy with dissolve
        y "Ya sudah ayo masuk."
        hide yerihappy with dissolve
        show citra with dissolve
        c "Iya ayo, udah ada beberapa anggota kita yang udah dateng nih."
        c "Katanya mau diselesaikan hari ini juga."
        hide citra with dissolve
        show kevinsmile with dissolve
        k "Yo [name] sama Zaky masuk."
        hide kevinsmile with dissolve
        show zakysmile at short_shake, center

        zc "Ayo!"

        hide zaky smile with dissolve
        jump mcstroy1_done
    label mcstroy1_done:

        jump chap2kantin_done
#------------------------------------------------------
    label chap2kantin_no:
        $ menu_flag = False
        #hide idlekevinserious
        #hide zakyworry
        #show kevintalk:
            #xalign 0.2
            #yalign 1.0
        #show idlezakyworry:
            #xalign 0.8
            #yalign 1.0
        p "Mending kita temuin Citra sama Yeri."
        hide idlezakysad
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Kapan?"
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
    menu:
        "Tahun depan.":
            jump jokes2_a
        "Nunggu sampai kucing bertelur.":
            jump jokes2_b
        "Nanti nunggu pasangan karakter fiksiku jadi nyata.":
            jump jokes2_c
    label jokes2_a:
        p "Tahun depan."
        hide idlezakytalk
        show zakyhappy2:
            xalign 0.8
            yalign 1.0
        z "Lah lama banget."
        z "Mending sekarang langsung ngga sih?"
        hide zakyhappy2
        show idlezakyhappy2:
            xalign 0.8
            yalign 1.0
        p "Ya sekarang lah sialan!"
        p "Pertanyaanmu memang tidak perlu dijawab deh."
        hide idlekevinsmile
        show kevincheerful:
            xalign 0.2
            yalign 1.0
        k "Hahahaha"
        k "Sudah-sudah yuk berangkat sekarang."
        hide kevincheerful
        hide idlezakyhappy2
        with dissolve
        jump jokes2_done
    label jokes2_b:
        p "Nunggu kucing bertelur."
        hide idlezakytalk
        show zakyhappy2:
            xalign 0.8
            yalign 1.0
        z "Lah?."
        z "Kucing mana bisa bertelur?"
        z "Aneh banget [name]."
        hide zakyhappy2
        show idlezakyhappy2:
            xalign 0.8
            yalign 1.0
        p "Yang aneh kamu sialan!"
        p "Pertanyaanmu memang tidak perlu dijawab deh."
        hide idlekevinsmile
        show kevincheerful:
            xalign 0.2
            yalign 1.0
        k "Hahahaha"
        k "Sudah-sudah yuk berangkat sekarang."
        hide kevincheerful
        hide idlezakyhappy2
        with dissolve
        jump jokes2_done
    label jokes2_c:
        p "Nanti nunggu pasangan karakter fiksiku jadi nyata."
        hide idlezakytalk
        show zakyhappy2:
            xalign 0.8
            yalign 1.0
        z "Halu kamu dek."
        z "Semoga kamu cepat sadar yah."
        z "Semoga [name] segera menemukan pasangan yang nyata."
        hide zakyhappy2
        show idlezakyhappy2:
            xalign 0.8
            yalign 1.0
        p "Sialan! Hahahahaha..."
        p "Walaupun dia tidak nyata tetapi membuatku bahagia."
        hide idlekevinsmile
        show kevincheerful:
            xalign 0.2
            yalign 1.0
        k "Hahahaha"
        k "Sudah-sudah yuk berangkat sekarang."
        hide kevincheerful
        hide idlezakyhappy2
        with dissolve
        jump jokes2_done
    label jokes2_done:
        
        scene bg hallway2 with dissolve
        python:
            renpy.notify("Lorong Kelas")
        
        "Kita bertiga mulai berjalan menuju ke ruang OSIS."
        "Saat dalam perjalanan menuju ke ruang OSIS."
        "Kita saling mengobrol satu sama lain."

        show zakytalk with dissolve

        z "Jadi nanti kita pertama bahas apa dulu?"             
        show zakytalk with move:
            xalign 0.8
            yalign 1.0
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        show kevintalk with dissolve:
            xalign 0.2
            yalign 1.0
        k "Yang pertama kita bahas dulu dari urutan acara ultah sekolah ini."
        hide kevintalk
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Urutannya gimana nanti?"
        hide idlekevintalk
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Jadi pertama nanti itu sambutan."
        k "Sebelum sambutan kita kumpulin dulu semua murid di Aula."
        k "Setelah sambutan kita membuka opening ceremony."
        k "Lalu, ada beberapa pentas di panggung Aula."
        k "Lalu, sembari beberapa pertunjukkan sedang berlangsung nanti di lapangan akan dibuka bazar."
        k "Tapi, sebelum bazar dibuka bakalan ada sambutan singkat juga."
        k "Lalu-"
        hide kevintalk
        hide idlezakytalk
        show zakytalk at short_shake:
            xalign 0.8
            yalign 1.0
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Sudah cukup."
        hide zakytalk
        show zakynormal:
            xalign 0.8
            yalign 1.0
        z "Bahasnya waktu rapat saja."
        hide idlekevintalk
        hide zakynormal
        show idlezakynormal:
            xalign 0.8
            yalign 1.0
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Ya, habisnya kamu sendiri yang minta kan?"
        hide kevintalk
        hide idlezakynormal
        show zakysad:
            xalign 0.8
            yalign 1.0
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Well-"
        z "Iya sih."
        hide zakysad
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Tapi ga gitu juga kali."
        hide idlekevintalk
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Lah?"
        k "Katanya tadi kamu mau tau apa aja yang akan dibahas saat rapat."
        k "Ya, aku kasih tau lah."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        p "Lumayan banyak juga ya."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Apanya yang banyak?"
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
    menu:
        "Agendanya lah.":
            jump jokes3_a
        "Cintaku pada pasangan fiksiku.":
            jump jokes3_b
        "Orang yang korupsi di negara ini.":
            jump jokes3_c
    label jokes3_a:
        p "Agendanya lah, apalagi."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Justru itu, makanya kita rapatkan hari ini."
        k "Dan targetnya hari ini selesai."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        jump jokes3_done
    label jokes3_b:
        p "Cintaku pada pasangan fiksiku."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Halu kau dek."
        k "Cepet sadar ya."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        p "Engga, bercanda."
        p "Maksudku agenda hari ini banyak banget."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Justru itu, makanya kita rapatkan hari ini."
        k "Dan targetnya hari ini selesai."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        jump jokes3_done
    label jokes3_c:
        p "Orang yang korupsi di negara ini."
        hide idlekevinserious
        show kevinsmile at short_shake:
            xalign 0.2
            yalign 1.0
        k "Sialan! Bercandamu bahaya sekali."
        k "Aku engga ikut-ikut."
        k "Hahahahaha."
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        p "Hahahaha, engga."
        p "Aku tadi cuma bercanda."
        p "Maksudku agenda hari ini banyak banget."
        hide idlekevinsmile
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Justru itu, makanya kita rapatkan hari ini."
        k "Dan targetnya hari ini selesai."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        jump jokes3_done
    label jokes3_done:
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Wah, berat juga ya jadi Ketua OSIS."
        hide idlekevinserious
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya, pastinya berat."
        k "Tetapi, karena berat itulah jadi banyak maknanya."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Emang maknanya apa saja tuh?"
        p "Kok aku lihat-lihat kamu kayak kesusahan gitu?"
        p "Udah susah, ribet, sama sering dimarahin pembina."
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya, justru itu sisi yang menyenangkan."
        k "Dan karena itulah aku bisa belajar biar lebih mandiri."
        hide kevintalk
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Afa iyah deck?"
        hide idlekevintalk
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        show kevintalk at short_shake:
            xalign 0.2
            yalign 1.0
        k "Hahahaha."
        k "Beneran kok, coba aja deh jadi Ketua OSIS."
        hide kevintalk
        hide idlezakytalk
        show zakytalk at short_shake:
            xalign 0.8
            yalign 1.0
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Ya, ga maulah! Yakali."
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        p "Kalau engga mau ga usah bacot deck."
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Iya deh, aku diem."
        hide zakytalk
        hide idlekevintalk
        with dissolve
        
        "Kita asik bercanda dan mengobrol."
        "Sungguh sangat menyenangkan."
        "Tetapi..."
        "Entah kenapa aku mendengarkan sesuatu yang samar."
        #scene bg penampakan.
        u_whisper "Apa kamu melihatku???"
        p "Eh..."
        "Lalu tiba-tiba ada sesosok perempuan lewat di depan lorong."
        p "Itu apaan tadi?"
        show zakyworry at long_shake, center
        z "Eh eh apaan? Kamu kenapa?"
        hide zakyworry
        show zakyworry at short_shake, center
        z "Kamu lihat apa?"
        z "Penampakan?"
        hide zakyworry
        show idlezakyworry
        p "Eh..."
        p "Ngga kok."
        p "Engga ada apa-apa."
        hide idlezakyworry
        show zakyworry at short_shake, center
        z "Ah jangan bohong deh."
        z "Kelihatan banget dari mukamu."
        hide zakyworry
        show idlezakyworry
        p "Sebenarnya aku ngeliat sesuatu tadi."

        hide idlezakyworry
        show zakyworry

        z "Lihat apaan?"

        hide zakyworry 
        show idlezakyworry

        p "Kayak ada cewe pakai seragam sekolah kita."
        show idlezakyworry with move:
            xalign 0.8
            yalign 1.0
        hide idlezakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        show kevinserious with dissolve:
            xalign 0.2
            yalign 1.0
            
        k "Mungkin murid sini kali."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0

    menu:
        "Mungkin sih.":
            jump imo5_a
        "Bisa jadi sih.":
            jump imo5_b
    label imo5_a:
        p "Mungkin sih."
        p "Tetapi, aku ngerasa dia itu beda banget."
        jump imo5_done
    label imo5_b:
        p "Bisa jadi sih."
        p "Tetapi, aku ngerasa dia itu beda banget."
        jump imo5_done
    label imo5_done:
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Beda gimana? Coba jelasin."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
    
        p "Rambutnya panjang banget, terus seperti sedang menunduk."
        p "Dan dia sempat menatapku."
        p "Terus tersenyum kearahku."
        p "Lalu-"

    menu:   
        "Seperti ada sesuatu yang membisikiku dan mengatakan “Apa kamu melihatku?“.":
            jump info1_a
        "Em... gitu aja sih.":
            jump info1_b
    label info1_a:
        p "Seperti ada sesuatu yang membisikiku dan mengatakan “Apa kamu melihatku?“."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Wait... Ada sesuatu membisikimu dan mengatakan “Apa kamu melihatku?“."
        k "Apa kamu yakin dengan apa yang kamu dengarkan?"
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        p "Iya ga bohong aku."
        jump info1_done
    label info1_b:
        p "Em... gitu aja sih."
        jump info1_done
    label info1_done:

        hide idlezakyworry
        show zakyworry at long_shake:
            xalign 0.8
            yalign 1.0
        z "HEH!"
        z "JANGAN NAKUTIN GUE!!!"
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        hide zakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        k "Sudah-sudah cukup."
        k "Tadi yakin kamu melihatnya?"
        k "Aku tidak melihatnya loh."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        hide idlezakyworry
        show zakyworry:
            xalign 0.8
            yalign 1.0
        z "Iya aku juga engga melihatnya."
        hide zakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        p "Iya, aku melihatnya agak lama."
        p "Aku  ketakutan sampai ga sempat bilang ke kamu, dan fokus sama dia saja."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Hah? Agak lama?"
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        p "Iya agak lama, kok bisa kalian tidak lihat sama sekali?"
        hide idlezakyworry
        show zakyworry:
            xalign 0.8
            yalign 1.0
        z "Lah, memang engga lihat sama sekali kok."
        z "Tiba-tiba ngeliat kamu udah pucat begitu."
        hide zakyworry
        show idlezakyworry:
            xalign 0.8
            yalign 1.0
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Iya, padahal tadi kamu biasa-biasa aja."
        k "Saat melihat kamu lagi kok tiba-tiba wajahmu pucat begitu."
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        p "Kok bisa ya, heran sekali aku."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Iya, yaudah gini aja deh."
        k "Kamu mau ke UKS sebentar atau gimana?"
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        p "Sudah tidak apa-apa kok, sekarang sudah jauh lebih mendingan."
        hide idlekevinserious
        show kevinserious:
            xalign 0.2
            yalign 1.0
        k "Yakin sudah mendingan?"
        hide idlezakyworry
        show zakytalk:
            xalign 0.8
            yalign 1.0
        hide kevinserious
        show idlekevinserious:
            xalign 0.2
            yalign 1.0
        z "Tidak apa-apa kok kalau mau ke UKS, nanti aku temenin."
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        p "Sudah aku beneran tidak apa-apa kok."
        hide idlekevinserious
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Ya sudah, kalau kamu beneran mendingan."
        k "Tetapi, kalau kamu tiba-tiba pucat lagi waktu saat rapat nanti."
        k "Langsung pulang saja ya."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Iya deh."
        p "Tetapi, beneran seketika langsung mendingan."
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        z "Kalau aku saja yang pulang gimana vin?"
        z "Aku beneran takut disini."
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        hide idlekevintalk
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        k "Kalau kamu ngga boleh pulang sekarang."
        k "Karena kamu ada peran penting buat rapat dan tugasmu sangat penting."
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        z "Yah..."
        z "Nangis nih aku."
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        hide idlekevinsmile
        show kevincheerful:
            xalign 0.2
            yalign 1.0
        k "Iya, silahkan menangis aja disini yang keras."
        k "Siapa tau kamu bakal ketemu orang yang tidak diinginkan juga."
        hide idlezakytalk
        show zakyworry:
            xalign 0.8
            yalign 1.0
        hide kevincheerful
        show idlekevincheerful:
            xalign 0.2
            yalign 1.0
        z "Eh asli, lu mah bercandanya gaasik banget jadi orang."
        z "Engga lucu bercandanya."
        hide zakyworry
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        hide idlekevincheerful
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya, maaf deh."
        k "Aku engga bakal kayak gitu lagi."
        hide idlezakytalk
        show zakytalk:
            xalign 0.8
            yalign 1.0
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        z "Ya sudah, ayo cabut dari sini."
        z "Takut banget aku lama-lama disini."
        hide zakytalk
        show idlezakytalk:
            xalign 0.8
            yalign 1.0
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya sudah yok, kasihan juga [name]."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
    menu:
        "Oke deh.":
            jump imo6_a
        "Ya udah, yok pergi sekarang.":
            jump imo6_b
    label imo6_a:
        p "Oke deh."
        p "Yok pergi sekarang."
        jump imo6_done
    label imo6_b:
        p "Ya udah, yok pergi sekarang."
        jump imo6_done
    label imo6_done:
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Tapi, kamu bisa jalan sendiri kan?"
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Iya bisa lah, aku cuma pucat tadi."
        p "Bukan jatuh dari tangga terus kakinya terluka."
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Ya siapa taukan kamu ketakutan sampai engga bisa jalan."
        hide kevintalk
        show idlekevintalk:
            xalign 0.2
            yalign 1.0
        p "Bisa-bisa."
        p "Ayo dah, sudah engga apa-apa aku."
        hide idlekevintalk
        show kevintalk:
            xalign 0.2
            yalign 1.0
        k "Iya, okedeh kalau gitu."
        hide kevintalk
        hide idlezakytalk
        with dissolve

        "Setelah kejadian yang aku lihat tadi kita bertiga langsung bergegas untuk menuju ruang OSIS."
        "Kenapa hanya diriku yang melihat kejadian tadi."
        "Padahal tadi kelihatan jelas dan diriku melihatnya cukup lama."
        "Namun, kenapa Kevin dan Zaky tidak melihat kejadian tadi."
        "Dan juga, tadi ada sesuatu yang membisikiku."
        "“Apa kamu melihatku?“ Kata-kata tersebut masih terngiang dikepalaku."
        "Apa maksudnya semua ini?"
        "Padahal dihari biasa diriku tidak pernah merasakan hal-hal aneh seperti tadi."

        scene bg osisdepan with dissolve
        python:
            renpy.notify("Depan Ruang OSIS")
        "Akhirnya kita bertiga sampai ke didepan ruang OSIS."
        "Gegara mengalami kejadian seperti tadi kita dengan secepat kilat sampai sini."
        "Disini diriku bertemu dengan Citra dan Yeri yang sedang berada didepan ruangan OSIS."

        show zakyhappy at long_shake, center
        z_shout "AKHIRNYAAAAAAAA"
        z "Sampai juga disini."
        hide zakyhappy with dissolve
        show yerinormal with dissolve
        y "Kenapa dah?"
        hide yerinormal with dissolve
        show zakynormal with dissolve
        z "Ceritanya panjang banget."
        hide zakynormal with dissolve
        show yerinormal with dissolve
        y "Apa? Aku penasaran banget."
        show yerinormal with move:
            xalign 0.2
            yalign 1.0
        hide yerinormal
        show idleyerinormal:
            xalign 0.2
            yalign 1.0
        show citra with dissolve:
            xalign 0.8
            yalign 1.0
        c "Kok kalian seperti habis lari atau gimana gitu sih."
        c "Kayak keringetan gitu."
        hide idleyerinormal
        show yerinormal:
            xalign 0.2
            yalign 1.0
        y "Iya nih, cerita aja."
        hide yerinormal
        show yerismile:
            xalign 0.2
            yalign 1.0
        y "Tetap kudengerin kok meskipun panjang ceritanya."
        hide yerismile
        show idleyerismile:
            xalign 0.2
            yalign 1.0
    menu:
        "Sebenernya ada kajadian janggal sih.":
            jump mcstroy2_a
        "Engga ada apa-apa sih.":
            jump mcstroy2_b
    label mcstroy2_a:
        p "Sebenernya ada kejadian janggal sih."
        hide idleyerismile
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Kayak apa tuh? Hantu?"
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        p "Tadi tuh aku lihat cewe-"
        hide idleyericheerful
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Masih keinget perkataannya Zaky kah?"
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
    menu:
        "Bukan begitu.":
            jump mctell_a
        "Dengerin dulu.":
            jump mctell_b
    label mctell_a:
        p "Bukan begitu."
        p "Tadi tuh aku li-"
        jump mctell_done
    label mctell_b:
        p "Dengerin dulu."
        p "Tadi tuh aku li-"
        jump mctell_done
    label mctell_done:
        hide idleyericheerful
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Udah ah capek."
        y "Kalian ini ada-ada aja, mending langsung masuk aja ke ruangan."
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        c "Iya ayo, udah ada beberapa anggota kita yang udah datang."
        c "Katanya mau diselesaikan hari ini juga."
        hide idleyericheerful
        hide citra
        with dissolve
        show kevinsmile with dissolve
        k "Iya, ayo."
        k "[name], Zaky. Tidak usah dipikirin lagi ya kejadian tadi."
        k "Mungkin itu cuma kebetulan aja."
        hide kevinsmile with dissolve
        show zakysad with dissolve
        z "Tapi kan-"
        hide zakysad with dissolve
        show kevinsmile with dissolve
        k "Udah, gapapa oke?"
        hide kevinsmile
        show idlekevinsmile
        p "Iya oke deh."
        p "Zaky, kamu engga usah mikirin hal itu lagi."
        p "Semakin dipikir semakin takut kamu nanti."
        hide idlekevinsmile with dissolve
        show zakysad with dissolve
        z "Oke oke, trying my best."
        hide zakysad with dissolve
        show kevinsmile with dissolve
        k "Nah gitu dong, baguslah kalau begitu"
        k "Yok masuk."
        jump mcstroy2_done
    label mcstroy2_b:
        p "Engga ada apa-apa sih."
        hide idleyerismile
        show yericheerful:
            xalign 0.2
            yalign 1.0
        y "Beneran nih engga bohong?"
        hide yericheerful
        show idleyericheerful:
            xalign 0.2
            yalign 1.0
        c "Beneran nih?"
        c "Kalian tu kayak orang ketakutan."
        c "Jujur aja."

        p "Engga ada apa-apa kok."
        p "Kita cuma ada kejadian aneh aja tadi."
        p "Tapi itu cuma halusinasi."

        hide idleyericheerful
        show yerinormal:
            xalign 0.2
            yalign 1.0
        y "Kejadian apaan sih?"
        hide yerinormal
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Kalau kalian ketakutan gegara cerita Zaky tadi lucu sih."
        y "Aku bakalan ketawa banget."
        hide yerinormal
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0
        y_shout "HAHAHAHAHAHAHAHA"
        y "Wajah kalian kayak orang panik sama bingung."
        hide yerinormal
        show idleyerinormal:
            xalign 0.2
            yalign 1.0
        p "Sudah-sudah tadi cuma halusinasi palingan."
        p "Ayo, masuk sekarang!"
        
        c "Yaudah ayo, udah ada beberapa anggota yang udah datang."
        c "Katanya mau diselesaikan hari ini juga."

        hide citra 
        hide idleyerinormal
        with dissolve

        show kevinhappy with dissolve
        k "Ayo masuk."
        k "Ayo [name] sama Zaky."
        hide kevinhappy with dissolve
        show zakysmile with dissolve

        z "Ya udah deh."
        z "Ayo masuk [name]."
        jump mcstroy2_done
    label mcstroy2_done:
    label chap2kantin_done:
        scene bg club with dissolve
        python:
            renpy.notify("Ruang OSIS")
        "Rapat akhirnya dimulai."
        "Saat rapat membahas akan banyak hal."
        "Seperti apa saja yang dibutuhkan saat merayakan Ulang Tahun sekolah ini."
        "Rapat ini bisa dibilang berjalan cukup lama."
        "Karena harus selesai pada hari ini juga."
        "Maka dari itu, rapat baru selesai pukul 19.00."
        "Padahal ada yang pernah bilang bahwa jangan disekolah ini jika hari udah MULAI MALAM."
        show kevinsmile with dissolve

        k "Oke kerja bagus buat kalian semua."
        k "Berkat kalian semua rapat kali ini berjalan dengan sukses."

        hide kevinsmile with dissolve
        show citra with dissolve

        c "Terima kasih juga Kevin."
        c "Kamu bisa dengan mudah menjelaskan kepada semua anggotamu dengan baik."
        hide citra with dissolve
        show kevinsmile with dissolve

        k "Ehehehe, iya terima kasih ya Citra."
        k "Ini mah masih bisa berani bilang ke semua pengurus OSIS disini."
        hide kevinsmile
        show kevintalk
        k "Minggu depan besok saat aku membuka opening ceremony untuk ulang tahun sekolah itu aku agak kurang berani."
        hide kevintalk with dissolve
        show yerinormal with dissolve
        y "Emang kenapa? Takut?"
        hide yerinormal with dissolve
        show kevinsmile with dissolve
        k "Iya, dikit sih."
        k "Karena itu pertama kalinya aku bisa public speaking ke banyak orang."
        show kevinsmile with move:
            xalign 0.2
            yalign 1.0
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
        show zakysmile at short_shake:
            xalign 0.8
            yalign 1.0
        z "Wah, keren sih kalau kamu bisa public speaking dengan lancar minggu depan nanti."
        hide zakysmile
        show idlezakysmile:
            xalign 0.8
            yalign 1.0
        p "Iya nih, semoga bisa lancar ya ngomongnya."
        hide idlekevinsmile
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        k "Iya terima kasih ya [name] atas dukunganmu."
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.2
            yalign 1.0
    menu:
        "Iya sama-sama.":
            jump talking1_a
        "Iya oke!":
            jump talking1_b
    label talking1_a:
        p "Iya sama-sama."
        jump talking1_done
    label talking1_b:
        p "Iya oke."
        jump talking1_done
    label talking1_done:
        hide idlekevinsmile
        show kevinsmile:
            xalign 0.2
            yalign 1.0
        k "Kalau kamu dukung gini aku jadi semakin semangat."
        hide kevinsmile
        hide idlezakysmile
        with dissolve
        show yeritsundere1 at short_shake, center
        y "Ehem..."
        hide yeritsundere1
        show yerishy
        y "Engga makasih ke aku juga nih?"
        hide yerishy
        show yerismile
        y "Aku tadi membantu banyak banget lho saat rapat."
        show yerismile with move:
            xalign 0.2
            yalign 1.0
        hide yerismile
        show idleyerismile:
            xalign 0.2
            yalign 1.0
        show kevinsmile with dissolve:
            xalign 0.8
            yalign 1.0
        k "Iya, justru aku mau mengucapkan makasih kepada kalian semua."
        k "Karena kalian udah bisa bantu aku banget."
        k "Rapat kali ini sukses juga berkat kalian semua."
        k "Tanpa kalian semua, aku tidak bisa seberani ini."
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.8
            yalign 1.0
        hide idleyerismile
        show yerismile:
            xalign 0.2
            yalign 1.0
        y "Iya, sama-sama Kevin."
        y "Kan kita sudah solid dari kecil."
        y "Jadi saat salah satu dari kita butuh pertolongan."
        y "Kami semua siap membantu."
        hide yerismile
        show idleyerismile:
            xalign 0.2
            yalign 1.0
        hide idlekevinsmile
        show kevinsmile:
            xalign 0.8
            yalign 1.0
        k "Iya deh iya."
        k "Sekarang, ayo beresin lagi ruangan OSIS ini."
        k "Sehabis dipakai rapat jadi agak berantakan gini."
        k "Sama sekalian buat bersih-bersih ruang OSIS."
        k "Karena sebenarnya sudah cukup lama juga kita tidak bersihin ruangan ini."
        hide kevinsmile
        show idlekevinsmile:
            xalign 0.8
            yalign 1.0
        p "Oke deh!"
        hide idlekevinsmile
        hide idleyerismile
        with dissolve
        "Saat ini hanya tersisa kita berlima diruang OSIS ini."
        "Anggota-anggota lain sudah mulai untuk beranjak pulang karena jam sudah menunjukkan pukul 19.10."
        "Kita berlima mulai bersih-bersih ruangan OSIS ini seperti yang telah diperintahkan oleh Kevin."
        "Ruangan OSIS ini sudah cukup lama tidak dibersihkan."
        "Bisa dibilang sudah sekitar 3-4 bulan tidak dibersihkan."
        "Oleh karena itu, kita berlima membersihkan ruangan ini agar lebih enak untuk dipandang dan digunakan."
        "Setelah memakan waktu sekitar 20-30 menit."
        "Kita berlima telah selesai membersihkan ruangan OSIS."
        "Dan jam saat ini telah menunjukkkan pukul 19.38."

        show zakyhappy at short_shake, center
        z "Akhirnya selesai juga."
        z "Asli dah capek banget coy."
        hide zakyhappy with dissolve
        show citra at short_shake, center
        c "Iya bener nih!"
        c "Capek banget *hiks*."
        c "Kakiku sampai lemas begini."
        hide citra
        show citra at short_shake, center
        c "Ahahahahaha."
        hide citra 
        show yerisad with dissolve
        y "Kok aku malah ngantuk ya sekarang."
        hide yerisad
        show yerinormal
        y "Apa mungkin gegara ruangan ini sudah dibersihkan ya."   
        y "Jadi terasa nyaman banget."
        show yerinormal with move:
            xalign 0.2
            yalign 1.0
        hide yerinormal
        show idleyerinormal:
            xalign 0.2
            yalign 1.0
        show kevintalk with dissolve:
            xalign 0.8
            yalign 1.0
        k "Duh, jangan sampai nginep disini ya."   
        k "Nanti petugas satpam datang kesini dan memarahi kita."
        hide idleyerinormal
        hide kevintalk 
        with dissolve
        show zakytalk with dissolve
           
        z "Paling engga akan datang satpamnya."
        z "Kan dia engga berani datang ke sekolah jam segini."
        hide zakytalk
        show zakyworry
        z "..."
        z "Kesekolah..."
        z "Jam segini..."
        hide zakyworry
        show zakynormal at long_shake, center   
        z_shout "LAH IYA JUGA YAKKKKKKK!"
        hide zakynormal
        show zakysad at long_shake, center
        z_shout "PULANG AJA YUK SEKARANG."
        z "Tiba-tiba kok aku ketakutan ya."
        z "Rasanya kok aku ngantuk banget yak."
        hide zakysad with dissolve
        "Zaky tertidur."
    menu:
        "...":
            jump talking2_a
        "...":
            jump talking2_b
    label talking2_a:
        p "..."
        jump talking2_done
    label talking2_b:
        p "..."
        jump talking2_done
    label talking2_done:
        
        show kevinhappy at short_shake, center
        k "HAHAHAHAHA."
        k "Bisa gitu ya."
        hide kevinhappy with dissolve
        show yerihappy at short_shake, center
        y "HAHAHAHAHA."
        y "Lucu juga si Zaky ini."
        hide yerihappy with dissolve
        show kevinhappy with dissolve
        k "Ada-ada aja nih Zaky."
        hide kevinhappy
        show kevinserious
        k "Tapi kok bener juga yah."
        k "Rasanya ngantuk banget nih."
        k "Kok aneh yah..."
        k "Tiba-tiba... bisa ngantuk... begini..."
        hide kevinserious with dissolve
        "Kevin tertidur."
    menu:
        "...":
            jump talking3_a
        "Sepertinya ada yang aneh.":
            jump talking3_b
    label talking3_a:
        p "..."
        show yerinormal with dissolve
        y "Ni anak juga sama aja ya."
        hide yerinormal 
        show idleyerinormal
        p "Ini kok ada yang aneh ya."
        hide idleyerinormal
        show yerinormal
        y "Aneh kenapa? Mereka emang kecapean kali."
        hide yerinormal with dissolve
        jump talking3_done
    label talking3_b:
        p "Sepertinya ada yang aneh."
        show yerinormal with dissolve
        y "Aneh kenapa? Mereka emang kecapean kali."
        hide yerinormal with dissolve
        jump talking3_done
    label talking3_done:
        show citra with dissolve
        c "Kayaknya bukan karena mereka kecapean deh, Yer."
        hide citra with dissolve
        show yerinormal with dissolve
        y "Terus karena apa?"
        hide yerinormal with dissolve
        show citra with dissolve
        c "Kayaknya sih karena ada sesuatu diruangan ini."
        c "Yang bisa membuat orang ter-"
        hide citra with dissolve
        hide idleyerinormal
        with dissolve
        "Citra tertidur."
    menu:
        "...":
            jump talking4_a
        "INI SUDAH ANEH CEPAT LARI!":
            jump talking4_b
    label talking4_a:
        p "..."
        show yeriscared at short_shake, center
        y "..."
        hide yeriscared
        show idleyeriscared
        p "LARI!!!"
        hide idleyeriscared
        jump talking4_done
    label talking4_b:
        p "INI SUDAH ANEH CEPAT LARI!"
        show yeriscared at short_shake, center
        y "..."
        hide yeriscared
        show idleyeriscared
        p "LARI!!!"
        hide idleyeriscared
        jump talking4_done
    label talking4_done:
        show yeriscared at short_shake, center
        y "Aku ingin lari..."
        y "Tapi aku engga kuat..."
        y "Lagi..."
        hide yeriscared with dissolve
        "Yeri tertidur."
        p "Sialan, aku harus lari secepatnya."
        "Aku ingin membuka pintu ruangan OSIS."
        "Tiba-tiba aku mengantuk."
        scene bg black with dissolve
        p "..."
        p "..."
        p "..."
    menu:
        "Sial! Kenapa semua ini terjadi.":
            jump talking5_a
        "Aku harus tetap terbangun.":
            jump talking5_b
    label talking5_a:
        p  "Sial! Kenapa semua ini terjadi."
    menu:
        "Siapa yang melakukan semua ini?":
            jump talking7_a
        "Aku harus tetap terbangun.":
            jump talking7_b
    label talking7_a:
        p  "Siapa yang melakukan semua ini?"
        jump talking7_done
    label talking7_b:
        p "Aku harus tetap terbangun."
        p "Sial! Sulit sekali untuk terbangun dari kantuk ini."
        jump talking7_done
    label talking7_done:
        jump talking5_done
    label talking5_b:
        p "Aku harus tetap terbangun."
        p "Sial! Sulit sekali untuk terbangun dari kantuk ini."
    menu:
        "Sial! Kenapa semua ini terjadi.":
            jump talking6_a
        "Siapa yang melakukan semua ini?.":
            jump talking6_b
    label talking6_a:
        p  "Sial! Kenapa semua ini terjadi."
        jump talking6_done
    label talking6_b:
        p "Siapa yang melakukan semua ini?"
        jump talking6_done
    label talking6_done:
        jump talking5_done
    label talking5_done:
    
        p "Apa yang sudah terjadi aku tidak paham."
        p "Ah, sialan!"
        p "Apa jangan-jangan rumor itu?"
        p "Atau apa?"
        p "..."
    menu:
        "Tolong hentikan semua ini.":
            jump talking8_a
        "Kumohon sudah cukup.":
            jump talking8_b
    label talking8_a:
        p  "Tolong hentikan semua ini."
        jump talking8_done
    label talking8_b:
        p "Kumohon sudah cukup."
        jump talkin8_done
    label talking8_done:
        p "..."
        p "Selesai sudah semua ini."
    return

label variabels:
    $ Inventory[0] = Items("Diary", 1, 1, 0, 0)
    
    return 
