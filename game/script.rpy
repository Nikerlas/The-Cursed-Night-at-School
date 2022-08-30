#inventory

    

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
image bg aclass = "images/bg/inclass.jpg"
image bg library = "images/bg/perpus.png"
image bg canteen = "images/bg/canteen.jpg"
#END BG

#IMG CHARA
#ZAKY
#--------> talk
image zakyhappy = "images/zaky/talk/ZakyHappy.png"
image zakyhappy2 = "images/zaky/talk/ZakyHappy2.png"
image zakynormal = "images/zaky/talk/ZakyNormal.png"
image zakysad = "images/zaky/talk/ZakySad.png"
image zakySmile = "images/zaky/talk/ZakySmile.png"
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
image citra = "images/citra/Citra.png"

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
define p = Character('[name]')
define c_shout = Character("[name]", what_size=50)
define c_whisper = Character("[name]", what_size=18)
#Mix
define kyc = Character("Kevin, Yeri, dan [name]")

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
    "Saat di pertengahan perjalanan aku bertemu Yeri lalu menyapanya."

    show idleyerinormal with dissolve

    p 'Hai Yeri. Bagaimana kabarmu?'
 
    hide idleyerinormal
    show yerihappy at short_shake, center

    y 'Hai [name], baik kok. Bagaimana denganmu?'

    hide yerihappy
    show idleyerihappy

    p 'Baik kok. Aku ke kelas duluan dulu ya!'
    
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

    hide idlezakytalk with dissolve

    "Tidak lama kemudian guru pun masuk kedalam ruangan untuk memulai pelajaran di pagi yang cerah ini."

    scene bg hallway with dissolve
    python:
        renpy.notify("Lorong Sekolah")

    "Bel istirahat pun berbunyi."
    "Lalu beberapa saat kemudian Zaky, Yeri, dan Kevin menghampiriku didepan kelasku."

    show kevintalk with dissolve:
        xalign 0.0
        yalign 1.0

    show idleyerismile with dissolve:
        xalign 0.5
        yalign 1.0

    show idlezakyhappy with dissolve:
        xalign 1.0
        yalign 1.0

    z 'Hei [name], yuk ke kantin. Mau ga?' 

    hide kevintalk
    show idlekevintalk:
        xalign 0.0
        yalign 1.0

    hide idleyerismile
    show yerismile at short_shake:
        xalign 0.5
        yalign 1.0

    y 'Iya nih... mau ga?'

    hide yerismile
    show idleyerismile:
        xalign 0.5
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

            hide idlekevincheerful
            show kevinhappy at short_shake:
                xalign 0.3
                yalign 1.0


            k "Iya deh iya."

            hide yeriangry2
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

        hide yerihappy
        show yeriangry2 at short_shake, center

        y 'Iya nih... Ga asik.' 
        p 'Aku bilang ngga ya ngga anjir!' 
        z 'Sudah deh biarin aja dia...' 
        k 'Yaudah deh... Yuk Yeri Zaky. Kita ke kantin.' 

        hide kevintalk
        hide yeriangry2 
        hide zaky with dissolve

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
            "Kan kamu bisa ambil sendiri.":
                jump choice5_done
            "Engga ah.":
                jump choice5_done
                
                label choice5_done:

        c 'Ya ampun... Itu tinggi banget. Ambilin donk.' 
        p 'Iya deh iya.'

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
        "Saat aku ingin mengambil buku tersebut."
        "Ada satu buku yang terjatuh karena aku mengambil buku tersebut."
        "Buakkkk!!!!"
        "Buku tersebut terjatuh dilantai."
        "Buku itu terjatuh dalam keadaan terbuka dan di dalamnya terdapat secarik kertas"

        python:
            renpy.notify("Mendapatkan Diary 1")
            inventory.add(diary01)

        "Aku mengambil kertas itu"
        "Dan tiba-tiba ada yang memanggil ku"

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

        show yerinormal with dissolve

        p "Hai Yeri... Kamu lagi ngapain?"

        hide yerinormal
        show yerisurprised at short_shake, center

        y "Eh [name]... Kenapa kamu kesini?"

        hide yerisurprised
        show yerismile at short_shake, center

        y "Katanya ngga mau ikut ke kantin?"
        p "Aku ikut Citra tadi." 
        p "Dipaksa sih."
        
        hide yerismile 
        show yericheerful at short_shake, center
        
        y "Hahahaha... Dipaksa yaa."
        p "Ya mau gimana lagi."
        
        hide yericheerful with dissolve
        
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

    show citra with dissolve:
        xalign 1.0
        yalign 1.0

    hide yeriangry2
    show idleyeriangry2

    c "Hahaha, sabar Yeri.."
    c "Emang resikonya ikut organisasi tu ya gini."
    c "Pulangnya telat mulu."

    hide idleyeriangry2
    show yeritalk at short_shake, center

    y "Iyadeh iya, Silahkan kalau mau dilanjut Vin.."

    hide yeritalk
    hide citra 
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

    show citra:
        xalign 0.3
        yalign 1.0

    show zakyhappy:
        xalign 0.7
        yalign 1.0

    with dissolve

    c "Hey Yeri..." 
    c "Jangan keras keras nanti kedengeran guru lain gimana?"
    z "Iya nih..." 
    z "Yeri kalo ngomong kadang ga dipikir dulu dua kali."

    hide citra
    hide zakyhappy
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
   
    "Pembicaraan ini semakin menjauh dari pembahasan rapat."

    hide yeritalk
    hide idlezakytalk

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
    k "bukannya semua sekolah itu memang kesannya menyeramkan kalau di malam hari?"

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

    "Tiba-tiba Yeri tertawa dengan keras lagi..."

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

        show kevinserious with dissolve:
            xalign 0.8
            yalign 1.0

        k "Mana mungkin..."
        k "Satpam kan sudah dilatih buat berani."

        hide yericheerful
        show yerinormal:
            xalign 0.2
            yalign 1.0

        y "Iya bener si..."

        hide yerinormal
        hide kevinserious
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

        y "Bener juga yak, hantu itu tidak nyata..."

        hide yericheerful
        show yerihappy at long_shake, center

        y "Jadi buat apa takut sama hantu?"

        hide yerihappy with dissolve
        show zakyhappy with dissolve

        z "Kalian semua pemberani ya..."
        z "Aku nonton film horror, 3 hari gabisa tidur dengan tenang."

        hide zakyhappy
        show citra at short_shake, center

        c "Kalo nonton begituan ma aku juga takut sebenarnya..."
        c "Tapi yang namanya film itu kan belum tentu nyata."
        c "Jadi aku masi tetep ga percaya yang namanya hantu.."

        hide citra with dissolve

        show yericheerful at long_shake, center

        y "Iyep.. betulll"
        y "Hantu itu tidak nyata, kayak husbuku aja..."
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

        c "Udah, sabar Yeri..."
        c "[name] kan cuma bercanda."

        hide citra with dissolve
        show zakyhappy at short_shake, center

        z "Hahaha, bercandanya."

        hide zakyhappy with dissolve
        show kevintalk with dissolve

        k "Btw..."
        k "Perasaan tadi kita lagi membahas rapat Osis dah..."
        k "Kenapa pembahasannya jadi kemana-mana?"
        hide kevintalk
        show idlekevintalk
        p "Iya juga..."
        p "Jadi gimana? Rapatnya jadi jam 4 sore nanti?"
        hide idlekevintalk
        show kevintalk
        k "Iya, jangan sampe lupa... apalagi cabut."
        hide kevintalk
        show idlekevintalk
        p "Gaakan cabut aku..."
        p "Tah aku kan anaknya si paling rajin hehe"

        hide idlekevintalk
        show yerinormal at long_shake, center

        y "Iyadeh si paling rajin..."

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
        c "Aku ada urusan, jadi tolong temani aku.."
        hide idleyerinormal
        show yericheerful at long_shake:
            xalign 0.2
            yalign 1.0

        y "Oke gas..."
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
            
        c "Mapel yang cukup sulit yaa"
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
        c "Aduh maaf Yer..."
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
        k "Udah bel tuh, mending kita masuk kelas aja.."
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
        z_shout "Bodoamat lah..."
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

        scene inclass
        "KRINGGGGGGGGGGGGGG"
        "Jam telah menunjukkan pukul 3 sore."
        "Pelajaran hari ini telah selesai."
        "Aku, Zaky, dan Kevin keluar menuju lorong depan kelas."

        scene corridor

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
        scene canteen
        show kevintalk with dissolve
        k "Kita ke kantin mau ngapain?"
        hide kevintalk with dissolve
        show zakytalk with dissolve
        z "Ya buat jajan, masak mau nginep disini."
        hide zakytalk with dissolve
        show kevintalk with dissolve
        k "Oh, yaudah."
        k "Agak cepetan ya!"
        hide kevintalk with dissolve    
        p "Oke!"
        hide idlekevintalk with dissolve
        "Kami bertiga langsung menuju tempat penjaga kantin untuk membeli beberapa jajanan."
        "Tetapi..."
        "Entah kenapa suasana semakin sepi."
        

        

        jump chap2kantin_done

    label chap2kantin_no:
        $ menu_flag = False
        "INI KETEMU"
        "YERI DAN CITRA"
        jump chap2kantin_done

            








    
    return

label variabels:
    $ Inventory[0] = Items("Diary", 1, 1, 0, 0)
    
    return 
 
