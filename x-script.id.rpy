define persistent.dialogueBoxOpacity = 1.0

label splashscreen:
    scene black with dissolve
    pause(0.2)
    $ renpy.sound.set_volume(0.5, channel='movie')
    $ renpy.movie_cutscene("gui/ntr_maniac.webm")

    scene warning with dissolve
    pause
    scene black with dissolve

    return

label start:
    scene black

    $ name = renpy.input("My name is", default ="Jake", length=15)
    $ persistent.name = name

    if name == "":
        $ mc = "Jake"
        $ mct = "Jake Tought"
        menu:
            "Are you sure about Jake?"
            "Yes":
                pause
            "No,Please.":

                pause



    $ fname = renpy.input("My wife's name is", default ="Emily", length=15)
    $ persistent.fname = fname

    if fname == "":
        $ em = "Emily"
        $ emt = "Emily Tought"

    if _in_replay:
        if persistent.name:
            $ mc = persistent.name
        if persistent.fname:
            $ em = persistent.fname


    scene st1 with fade

    pause

    scene st2 with dissolve

    pause

    scene st3 with dissolve

    pause

    scene st4 with dissolve

    pause

    em "Saya tidak akan pernah terbiasa dengan ini."

    scene st5 with dissolve

    $ persistent.mc_unlock = True

    mc "Aku tahu sayang, itu sangat rumit. Saya tidak percaya sudah hampir 1 tahun."

    scene st6 with dissolve

    mct "Kami bahagia tetapi setelah kejadian itu hidup kami menjadi berantakan.Ini adalah istri saya yang setia, __var_0__. Kami telah menikah selama 5 tahun. Kami sangat mencintai satu sama lain."

    mct "Saya tidak dapat memutuskan apakah saya beruntung atau tidak beruntung.Akhir 2026 virus terjadi. Setiap wanita lajang mati karena virus ini kecuali __var_0__ dan beberapa yang. Sekarang semua orang ingin bersama istri saya."

    mct "Tapi saya tahu satu hal yang selalu kita cintai satu sama lain apa pun yang terjadi."

    scene black with dissolve

    pause

    scene hm1 with fade

    mc "Sayang, apakah kamu ingin bicara?"

    scene hm2 with dissolve

    pause

    scene hm2 with dissolve

    mc "Saya pikir kita harus berbicara sekarang. Kami tidak dapat menunda konservasi ini lagi."

    scene hm4 with dissolve

    em "Saya tidak tahu harus berbuat apa."

    scene hm3 with dissolve

    mc "Kami mencoba setiap hari meskipun kami tahu faktanya saya tidak subur. Kemanusiaan mungkin berakhir karena kita dan saya merasa bersalah. Jika Anda mencoba dengan seseorang ..."

    scene hm4 with dissolve

    em "Sayang, aku tidak bisa. Aku mencintaimu."

    scene hm5 with dissolve

    pause

    scene hm5 with dissolve

    anc "Hanya 5 dari 15 wanita yang selamat setelah virus mampu melahirkan."

    scene hm6 with dissolve

    anc "Para ilmuwan memprediksi penurunan yang signifikan dalam populasi manusia, yang berpotensi menandakan akhir umat manusia."

    scene hm7 with Dissolve(1.0)

    anc "Berita baiknya adalah bahwa keempat wanita ini membuat banyak pengorbanan dan menjadi penyelamat kemanusiaan."

    scene hm8 with dissolve

    anc "Sayangnya, ini tidak cukup."

    scene hm9 with dissolve

    anc "Masih belum ada berita dari wanita yang tinggal di New-York City."

    scene hm10 with dissolve

    em "Sayang..."

    scene hm11 with dissolve

    em "Saya akan mencoba. Saya harus ..."

    scene hm12 with dissolve

    mc "Kita harus. Aku tidak akan pernah membiarkanmu sendirian. Aku akan selalu bersamamu."

    scene hm11 with dissolve

    em "Terima kasih, sayang. Aku tidak bisa melakukan ini tanpamu, apa yang akan kita lakukan sekarang?"

    scene hm12 with dissolve

    mc "Hanya satu orang yang muncul di pikiran saya."

    scene hm11 with dissolve

    em "Siapa?"

    scene hm13 with dissolve

    mc "Ermm ... yah ..."

    scene hm14 with dissolve

    em "Menumpahkan kacang."

    scene hm15 with dissolve

    mc "Dengan baik. Andrew?"

    scene hm16 with dissolve

    em "B-tapi dia adalah sahabatmu."

    scene hm15 with dissolve

    mc "Itu sebabnya saya menyarankannya, Andrew adalah homie saya yang bisa saya percayai."

    scene hm17 with dissolve

    em "Yah saya sangat menyukai Andrew tapi ini sesuatu yang berbeda. Saya tidak yakin .."

    scene hm18 with dissolve

    mc "Saya tahu ini sulit bagi kami berdua. Tapi kita harus. Jangan khawatir saya tidak mendorong Anda apa pun. Kami dapat bergerak langkah demi langkah sampai Anda merasa baik -baik saja."

    scene hm19 with dissolve

    em "Oke."

    scene hm19_5 with dissolve

    mc "Hei Andrew, aku membutuhkanmu. Bisakah kamu segera datang?"

    scene hm19_5 with dissolve

    mc "Ya ya, saya akan menjelaskan saat Anda tiba."

    scene hm20 with dissolve

    pause

    scene hm22 with dissolve

    mct "Ini Andrew, saudaraku. Kami sudah menjadi teman terbaik sejak kami berusia lima tahun."

    mct "Dia selalu mendukung saya, terutama ketika harus berurusan dengan pengganggu selama masa kecil saya. Kami telah berbagi ikatan yang kuat sejak itu."

    mct "Andrew dan __var_0__ juga rukun juga."

    scene hm21 with dissolve

    aw "Apa masalahnya? Mengapa saya harus segera datang?"

    $ persistent.aw_unlock = True

    scene hm22 with dissolve

    mc "Kamu harus membantu kami."

    scene hm21 with dissolve

    aw "Tentu, tentang apa?"

    scene hm23 with dissolve

    mc "Tidak ada cara mudah untuk mengatakan ini jadi saya hanya akan mengatakannya secara langsung. Dapatkan __var_0__ hamil."

    scene hm24 with dissolve

    aw "Apa fuuuck? Apakah kamu gila ??"

    scene hm25 with dissolve

    mc "Anda tahu kondisi kesehatan saya. Kita harus melakukan ini demi kemanusiaan."

    scene hm26 with dissolve

    aw "Dan apakah kamu baik -baik saja dengan itu?"

    scene hm27 with dissolve

    pause(0.5)

    scene hm28 with dissolve

    em "Ya."

    scene hm29 with dissolve

    aw "Bung, saya tidak yakin tentang itu. Maksud saya __var_0__ sangat sempurna. Saya sangat ingin FUC, Ermm, maksud saya membantu Anda dan __var_0__."

    aw "Apakah Anda yakin ini tidak akan membahayakan hubungan Anda?"

    scene hm30 with dissolve

    mc "Kami sudah membicarakan hal itu, tidak ada yang akan mempengaruhi pernikahan kami. Ini adalah tugas kita, begitulah adanya. Sayang benar?"

    scene hm31 with dissolve

    em "Ya, sayang."

    scene hm32 with dissolve

    mc "Jadi apa yang kamu katakan bung? Apakah Anda masuk atau keluar?"

    scene hm33 with dissolve

    aw "Im in."

    scene hm34 with dissolve

    em "Saya tidak ingin terburu -buru apa pun yang saya sudah merasa gugup."

    scene hm35 with dissolve

    mc "Jangan khawatir sayang, aku akan selalu bersamamu."

    jump hj1

label hj1:
    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"






    scene hm36 with dissolve

    $ persistent.a_scene1_unlocked = True

    aw "Jadi kapan kita melakukannya?"

    menu:
        "Push [fname] to sex":

            $ ntr_point += 1

            scene hm37 with dissolve

            mc "Sekarang ... tidak perlu menunggu. Tidak ada gunanya memperpanjangnya. Lakukan saja."

            scene hm38 with dissolve

            em "Apakah kamu serius sekarang? ASTAGA! Bukankah kita membicarakan hal ini?"

            scene hm39 with dissolve

            aw "Oke dinginkan teman -teman. Mengapa kita tidak meminumnya perlahan?"

            scene hm40 with dissolve

            aw "Mari kita mengenal tubuh satu sama lain untuk saat ini."

            scene hm41 with dissolve

            em "???"

            scene hm42 with dissolve

            em "Seberapa besar hal itu?!"

            scene hm43 with dissolve

            mct "Saya tidak bisa membayangkan __var_0__ mengambil semuanya."

            scene hm44 with dissolve

            mct "Mengapa jantungku berdetak lebih cepat? Mengapa saya menjadi bersemangat?"

            scene hm45 with dissolve

            pause(0.5)

            scene hm47 with dissolve

            pause(0.5)

            scene hm48 with dissolve

            pause

            scene hm49 with dissolve

            pause

            scene hm51 with dissolve

            em "Haruskah saya merasa bersalah karena menyukainya?"

            scene hm50 with dissolve

            em "Itu nyaris tidak cocok di tangan saya."

            scene hm52 with dissolve

            aw "Ah, benarkah? Anda adalah gadis pertama yang mengatakan itu. Hahahah!"

            scene hm53 with dissolve

            mct "Saya tidak percaya saya membiarkan ini tetapi kita harus bertahan."

            scene hm53_5 with dissolve

            mct "Saya bertanya -tanya bagaimana perasaan __var_0__ sekarang?"

            scene black with dissolve

            pause(0.01)

            scene hj1 with dissolve

            em "mmmm ..."

            aw "Oh-hhh! Tanganmu sangat kecil dan lembut."

            scene hj2 with dissolve

            em "hhh ..."

            aw "Terus berlanjut..."

            scene hm54 with dissolve

            pause

            scene hm55 with dissolve

            mct "Kotoran!"

            scene hm57 with dissolve

            em "Saya pikir kita harus berhenti untuk hari ini. Banyak yang harus diambil."

            scene hm58_b with dissolve

            aw "Ayo __var_0 __..."

            scene hm59_b with dissolve

            aw "Kami sudah dalam hal ini."

            scene hm60_b with dissolve

            aw "Kami tidak bisa berhenti begitu saja sekarang. Mungkin ini akan membuat Anda dalam mood."

            scene hm61_b with dissolve

            pause

            scene hm62_b with dissolve

            pause

            scene hm64_b with dissolve

            mct "Holly! Dia benar -benar meletakkan penisnya di antara kakinya. Bagaimana __var_0__ akan bereaksi terhadap ini?"

            mct "Sangat menyenangkan, saya merasa aneh dan benar -benar ingin melihat apa yang terjadi selanjutnya. Sepertinya benda basah besar itu ada di dalam __var_0__."

            scene hm63_b with dissolve

            emt "Dia memelukku dengan sangat erat. Aku tidak bisa menghentikannya memaksaku melawannya. Ada sesuatu yang besar di antara kedua kakiku."

            emt "Saya bisa merasakan kehangatan dan kekerasan seolah -olah saya tidak mengenakan celana pendek. Apa perasaan basah ini? Apakah saya basah?"

            emt "Saya harus menghentikannya.Oh tidak. Sangat memalukan bagi __var_0__ untuk melihat saya seperti ini. Saya tidak ingin pergi terlalu cepat."

            em "BERHENTI!!!"

            scene hm65_b with dissolve

            em "Andrew, tolong mengerti. Ini luar biasa bagi saya. Saya perlu waktu untuk memproses semuanya."

            scene hm66_b with dissolve

            aw "Tapi kami tidak mampu menunggu. Kami memiliki tanggung jawab di sini."

            scene hm67_b with dissolve

            em "Tidak, Andrew. Saya bilang tidak."

            scene hm68_b with dissolve

            mc "Namun kami akan melanjutkan __Var_0__."

            scene hm69_b with dissolve

            aw "Baik, lakukan dengan cara Anda. Tapi jangan lupa tujuannya di sini."

            aw "Saya pikir saya harus pergi sekarang. Saya akan memberi Anda ruang untuk memproses semua yang terjadi. Selamat tinggal."

            $ renpy.end_replay()
        "Encourage [fname]":


            $ nts_point += 1

            scene hm37 with dissolve

            mc "Saya tidak ingin __var_0__ terasa buruk."

            scene hm38_a with dissolve

            mc "Mari kita lanjutkan langkah demi langkah. Kita harus mulai dari suatu tempat. Apakah Anda baik -baik saja dengan Andrew telanjang?"

            scene hm40 with dissolve

            aw "Mengapa saya satu -satunya orang telanjang di ruangan itu, __var_0__ Anda juga harus telanjang."

            scene hm42_a with dissolve

            em "Saya belum merasa nyaman."

            scene hm41_a with dissolve

            aw "Oke, tapi akhirnya kamu akan telanjang ..."

            scene hm41 with dissolve

            em "???"

            scene hm42 with dissolve

            em "Seberapa besar hal itu?!"

            scene hm43 with dissolve

            mct "Saya tidak bisa membayangkan __var_0__ mengambil semuanya."

            scene hm44 with dissolve

            mct "Mengapa jantungku berdetak lebih cepat? Mengapa saya menjadi bersemangat?"

            scene hm45 with dissolve

            pause(0.5)

            scene hm47 with dissolve

            pause(0.5)

            scene hm48 with dissolve

            pause

            scene hm49 with dissolve

            pause

            scene hm51 with dissolve

            em "Haruskah saya merasa bersalah karena menyukainya?"

            scene hm50 with dissolve

            em "Itu nyaris tidak cocok di tangan saya."

            scene hm52 with dissolve

            aw "Ah, benarkah? Anda adalah gadis pertama yang mengatakan itu. Hahahah!"

            scene hm53 with dissolve

            mct "Saya tidak percaya saya membiarkan ini tetapi kita harus bertahan."

            scene hm53_5 with dissolve

            mct "Saya bertanya -tanya bagaimana perasaan __var_0__ sekarang?"

            scene black with dissolve

            pause(0.01)

            scene hj1 with dissolve

            em "mmmm ..."

            aw "Oh-hhh! Tanganmu sangat kecil dan lembut."

            scene hj2 with dissolve

            em "hhh ..."

            aw "Terus berlanjut..."

            scene hm54 with dissolve

            pause

            scene hm55 with dissolve

            mct "Kotoran!"

            scene hm57 with dissolve

            em "Saya pikir kita harus berhenti untuk hari ini. Banyak yang harus diambil."

            scene hm67 with dissolve

            aw "Ya, ini intens. Kami tidak perlu terburu -buru."

            scene hm68 with dissolve

            mc "Tentu saja, mari kita sambat -lambatnya. Kita semua bersama -sama, tidak perlu mendorong diri kita terlalu keras."

            scene hm67_b with dissolve

            em "Terima kasih. Saya hanya perlu waktu untuk memproses semuanya."

            scene hm69 with dissolve

            aw "Tentu saja, __var_0__. Kami akan pergi dengan kecepatan Anda."

            scene hm70 with dissolve

            mc "Ayo duduk dan bicara sebentar. Kita bisa mencari cara terbaik untuk menangani ini bergerak maju."

            scene hm71 with dissolve

            aw "Saya pikir yang terbaik jika saya pergi sekarang. Saya akan memberi Anda beberapa ruang untuk memproses apa yang terjadi. Anda harus duduk dan berbicara. Selamat tinggal."

            scene hm67_b with dissolve

            em "Tunggu sebelum Anda pergi…"

            scene hm73 with dissolve

            pause

            aw "Oh!"

            scene hm74 with dissolve

            pause

            scene hm75 with dissolve

            pause

            aw "Berengsek!!!"

            scene hm72 with dissolve

            em "Anda bisa mengucapkan terima kasih ciuman atau hadiah lain kali ... selamat tinggal."

            scene hm71 with dissolve

            aw "Oke ... saya- Saya kira sekarang karena saya punya hadiah, saya harus pergi."

            $ renpy.end_replay()


    scene hm76 with fade

    mc "Itu ... intens."

    scene hm77 with dissolve

    em "Ya, saya tidak percaya kami benar -benar melakukannya."

    scene hm76 with dissolve

    mc "Aku tahu. Itu sangat nyata. Saya merasa seperti kita berada dalam semacam mimpi buruk yang aneh."

    scene hm78 with dissolve

    em "Apakah Anda pikir kami melakukan hal yang benar?"

    scene hm76 with dissolve

    mc "Aku tidak tahu. Tapi pilihan apa yang kita miliki? Ini bukan hanya tentang kita lagi. Ini tentang kemanusiaan."

    scene hm79 with dissolve

    em "Saya mengerti, tapi ... masih terasa salah. Maksud saya, kami saling mencintai, dan sekarang kami melibatkan orang lain dalam sesuatu yang sangat pribadi."

    scene hm76 with dissolve

    mc "Saya merasakan hal yang sama. Ini memalukan, tapi ... kita harus mencoba, kan?"

    scene hm77 with dissolve

    em "Ya, saya kira begitu. Saya tidak pernah membayangkan hidup kita akan berubah seperti ini."

    scene hm76 with dissolve

    mc "Aku juga tidak. Tapi apa pun yang terjadi, kita akan menghadapinya bersama. Anda tidak sendirian dalam hal ini."

    scene hm80 with dissolve

    em "Terima kasih. Saya sangat membutuhkannya sekarang. Itu sangat luar biasa."

    scene hm81 with dissolve

    mc "Aku tahu, sayang. Kami akan melewati ini."

    scene hm80 with dissolve

    em "Anda benar. Kami akan melewati ini. Bersama."

    scene hm81 with dissolve

    mc "Bersama..."

    scene hm82 with dissolve

    mct "Ketika saya menahannya, aroma yang akrab menghantam saya. Air mani."

    mct "Sisa -sisa dari apa yang baru saja terjadi. Yang mengejutkan saya, itu membangkitkan saya."

    mct "Tubuh saya merespons terlepas dari kebingungan dan rasa bersalah pikiran saya."

    scene hm83 with dissolve

    mct "Oh tidak, tidak sekarang. Saya tidak bisa membiarkan dia memperhatikan."

    scene hm84 with dissolve

    em "Saya merasa sangat malu dan bersalah karena mengatakan ini, tapi ... saya benar -benar terangsang sekarang. Bisakah kita pergi ke kamar tidur kita?"

    scene hm85 with dissolve

    mc "Benar-benar? Maksud saya, saya - tentu, jika itu yang Anda inginkan."

    scene hm86 with dissolve

    mct "Jadi, __var_0__ dipengaruhi oleh apa yang baru saja terjadi. Lagi pula, dia seorang wanita."

    scene hm87 with dissolve

    mc "Kita bersama -sama, ingat?Hei, tidak apa -apa. Kita bisa pergi ke kamar tidur. Tidak ada yang perlu malu."

    scene hm84 with dissolve

    em "Terima kasih. Saya hanya perlu merasa dekat dengan Anda sekarang."

    scene hm85 with dissolve

    mc "Aku tahu sayang tapi bagaimana dengan ini? Ada bioskop erotis yang saya ingat dari masa lalu. Ini bisa menjadi gangguan yang menyenangkan dan membantu kami menghilangkan keanehan dari sebelumnya. Bagaimana menurutmu?"

    scene hm88 with dissolve

    em "Benar-benar? Kedengarannya ... menarik. Ayo lakukan!"

    scene hm89 with dissolve

    mc "Baiklah, mari kita cepat dan pergi sebelum bioskop ditutup."

    scene hm90 with dissolve

    pause

    scene cs1 with dissolve

    em "Saya sudah memikirkannya lagi. Apakah Anda yakin bioskopnya aman untuk saya? Saya sedikit khawatir."

    scene cs2 with dissolve

    mc "Jangan khawatir, sayang. Saya tahu pemiliknya dan kami memiliki sejarah yang baik. Kami dapat mempercayai dia untuk memberi kami tempat pribadi yang bagus."

    scene cs3 with dissolve

    mc "Selain itu kami memilikinya untuk melindungi kami."

    scene cs3_5 with dissolve

    pause

    scene cs4 with dissolve

    em "Terkadang saya lupa mereka ada di sekitar, tetapi saya tidak mempercayai mereka. Apakah Anda pikir mereka akan memperlakukan kami dengan cara yang sama ketika perjanjian pemerintah kami berakhir?"

    scene cs5 with dissolve

    mc "Bisakah Anda berhenti!"

    scene cs6 with dissolve

    mc "Maaf, __var_0__. Kami tidak perlu khawatir tentang itu sekarang. Mari kita bersenang -senang."

    scene cs7 with dissolve

    em "Benar. Tidak ada gunanya memikirkan hal ini sekarang. Kami di sini untuk bersantai, jadi mari kita masuk ke dalam."

    scene ch1 with fade

    $ persistent.jm_unlock = True

    jm "Hei, sobat. Selamat datang! Saya sudah mengharapkan Anda."

    scene ch2 with dissolve

    mc "Hai. Terima kasih telah menyiapkan ruangan untuk kami dengan sangat cepat. Maaf sudah menelepon pada menit terakhir."

    scene ch3 with dissolve

    jm "Jangan khawatir, kawan. Saya selalu punya kamar untuk Anda, kapan saja. Hubungi saya, dan saya akan memastikan tempat yang siap untuk Anda."

    jm "Jika perlu, saya bahkan akan menutup salah satu salon saya sehingga Anda berdua dapat memiliki privasi."

    scene ch4 with dissolve

    mct "Ini adalah James, pemilik Teater Dewasa. Bertahun -tahun yang lalu, Andrew dan saya dulu datang ke sini. Terkadang, dia mendirikan kamar pribadi hanya untuk kita dan pacar kita."

    mct "James telah memperhatikan kami lebih dari yang bisa saya hitung. Dia bahkan akan meminjamkan uang kepada kami saat kami pendek."

    mct "Namun seiring waktu, kami kehilangan kontak. Terakhir kali kami bertemu adalah ketika kami pergi untuk menyampaikan belasungkawa setelah dia kehilangan istrinya."

    scene ch5 with dissolve

    mc "Terima kasih, James."

    scene ch6 with dissolve

    jm "Suatu kehormatan untuk bertemu istri Anda. Saya harus mengatakan, Anda memiliki wanita yang sangat cantik dan elegan."

    scene ch7 with dissolve

    em "Terima kasih banyak, James. Senang bertemu dengan Anda juga."

    scene ch8 with dissolve

    jm "Kalau begitu, pergi ke dalam dan buat dirimu di rumah. Menikmati!"

    scene ch9 with dissolve

    mc "Terima kasih, James."

    em "Terima kasih"

    scene cs7_1 with fade

    pause

    scene cs7_2 with dissolve

    em "Wow. Tempat ini jauh lebih bersih dan ... lebih baik dari yang saya harapkan!"

    scene cs7_3 with dissolve

    mc "Kualitas premium."

    scene cs7_4 with dissolve

    mc "Mari kita duduk."

    scene cs7_5 with dissolve

    em "Saya ingin melepaskan ini."

    scene cs8 with dissolve

    pause

    scene cs8_5 with dissolve

    em "Mmm ..."

    scene cs9 with dissolve

    em "Hhh ..."

    scene cs10 with dissolve

    mct "Dia sangat basah, dan saya bahkan belum memulai. Saya tahu apa yang terjadi di rumah berbelok __var_0__ pada lebih banyak lagi, tapi aneh bahwa dia masih dalam mood."

    mct "Saya suka versi __var_0__ ini, tetapi saya tidak dapat bertanya -tanya apakah itu pengaruh Andrew."

    scene cs11 with dissolve

    em "Tenang, bocah terangsang."

    scene cs12 with dissolve

    em "Jika kita akan bergerak secepat ini, kita bisa tinggal di rumah."

    scene cs12_5 with dissolve

    mc "Saya tahu melakukannya di depan umum membuat Anda lebih banyak lagi."

    scene cs12_6 with dissolve

    mc "Kemarilah."

    scene cs13 with dissolve

    em "Seseorang tahu bagaimana menyenangkan istrinya. Anak yang baik."

    mc "Itu tugas saya dan tugasnya menelepon saya."

    scene cs13_1 with dissolve

    em "Berbohong."

    em "Turun."

    scene cs13_2 with dissolve

    mc "Ya, Bu."

    scene cs13_3 with dissolve

    pause

    jump cinema

label cinema:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"

    $ persistent.b_scene1_unlocked = True

    scene black with dissolve

    pause(0.01)

    scene rc1 with dissolve

    mc "Kamu sangat basah."

    em "Karena penismu, tampan."

    scene rc2 with dissolve

    mc "Anda semakin ketat ..."

    em "Ahhh ...."

    scene cs14 with dissolve

    jmt "Saya harus lebih dekat."

    scene cs15 with dissolve

    jmt "Lubang merah muda."

    jmt "Saya ingin menjilatnya."

    scene cs16_5 with dissolve

    jm "*Mencucup*"

    scene cs16 with dissolve

    jmt "Mari kita lihat apakah Anda bisa mengambil ujung jari saya."

    scene cs17 with dissolve

    pause

    scene cs18 with dissolve

    pause

    scene cs19 with dissolve

    em "Mmm .. ah !!"

    scene cs20 with dissolve

    em "Oh!! Sayang itu baru."

    mct "Saya tidak tahu apa yang dia bicarakan, tetapi saya tidak ingin merusak suasana hati dengan mengajukan pertanyaan."

    scene cs21 with dissolve

    jmt "Sekarang, mari kita lihat apakah kita bisa melebarkan lubang Anda sedikit."

    scene cs22 with dissolve

    em "Ahh, itu menyakitkan!"

    scene cs23 with dissolve

    em "Mmm, lebih keras!"

    scene cs23_5 with dissolve

    em "__Var_0__, lakukan lebih keras!"

    scene hm44 with eye_shut

    mct "Apa ini sekarang? Saya tidak ingin mengingat ini sekarang."

    scene hm48 with dissolve

    mct "Kotoran! Saya tidak bisa mengendalikan pikiran saya. Mengingat hal -hal ini terasa benar -benar…"

    mct "sangat berbeda ..."

    scene cs23 with eye_open

    em "Mmm ..."

    scene hm51 with eye_shut

    emt "Itu ..."

    emt "Sangat besar."

    emt "Rasanya seperti dari dunia lain."

    scene hm52 with dissolve

    emt "Jika ada di dalam diri saya sekarang, itu akan menghancurkan saya. Saya pikir saya hanya bisa mengambil ujungnya."

    emt "Ahhh… sial. Jangan memikirkan hal ini sekarang, jangan memikirkan hal ini sekarang, __var_0__!"

    scene cs24 with eye_open

    em "Hhh .."

    scene cs25 with dissolve

    "*Sniff*-*Sniff*"

    scene cs26 with dissolve

    jmt "Saya harus pergi sekarang."

    scene cs27 with dissolve

    jmt "Tapi segera, hal yang masuk akan ada lidahku."

    scene black with dissolve

    pause(0.01)

    scene rc2 with dissolve

    em "*Bernafas sangat*ahhh ...*bernapas berat*"

    mc "* Sangat bernafas* Saya akan cum. *Bernafas sangat*"

    em "* Bernafas sangat* cum di dalam diriku. *Bernafas sangat*"

    scene cs28 with dissolve

    em "*(Berteriak)*ahh !!"

    scene cs29 with dissolve

    mc "*Ohh-hhh !!!"

    scene cs30 with dissolve

    pause

    scene cs13_1 with dissolve

    em "__Var_0__. Ini sangat ... sangat bagus. Ahh… *bernafas sangat *"

    scene cs13_2 with dissolve

    mc "Saya suka vagina hangat dan ketat Anda. Ohh. *Bernafas sangat*"

    scene cs13_3 with dissolve

    pause

    scene cs13_5 with dissolve

    em "Saya sangat lelah, saya perlu mengisi ulang besok. Ayo pulang, sayang."

    scene cs13_2 with dissolve

    mc "Oke, sayang."

    $ renpy.end_replay()

    scene ch10 with fade

    jm "Halo, pasangan muda kami yang cantik!"

    scene ch11 with dissolve

    mc "Terima kasih untuk semuanya James."

    scene ch12 with dissolve

    jm "Tidak perlu berterima kasih kepada saya; Lagi pula, saya melayani kemanusiaan. Saya akan selalu ada di sini untuk kalian."

    jm "Minggu depan, film baru akan keluar. Dan tebak siapa bintangnya? Anda tidak akan pernah menebak."

    scene ch13 with dissolve

    jm "Sharlet Moansson!"

    scene ch14 with dissolve

    em "Apakah dia masih hidup ??"

    mc "Benar-benar?! Apakah dia masih hidup dan membintangi film -film dewasa?"

    scene ch15 with dissolve

    jm "Hahahah. Anda berharap. Maksudku, kita semua berharap."

    jm "Film ini dibuat dengan AI, maksud saya, hanya bagian -bagian dengannya yang dianimasikan. Semua orang itu nyata, kecuali dia."

    scene ch16 with dissolve

    em "__Var_0__! Kita harus pergi minggu depan. Saya sangat ingin melihat seperti apa penampilannya."

    scene ch17 with dissolve

    jm "Bahkan jika __var_0__ tidak dapat membuatnya, saya pasti akan menunggu Anda!"

    scene ch18 with dissolve

    mc "Jangan khawatir, saya juga akan ikut dengannya. Bagaimanapun, kita harus pergi sekarang. Sampai jumpa."

    em "Bye, James ..."

    scene ch19 with dissolve

    pause

    scene ch20 with dissolve

    jm "*Mencium*"

    scene ch21 with dissolve

    jm "Hmm..."

    scene ch22 with dissolve

    jm "Lezat."

    scene cs4 with fade

    em "Sayang, ada sesuatu yang mengganggu saya."

    scene cs4_5 with dissolve

    mc "Apakah sesuatu terjadi?"

    scene cs4_6 with dissolve

    em "Tidakkah menurut Anda sikap James berubah setelah film?"

    scene cs4_5 with dissolve

    mc "Apa maksudmu?"

    scene cs4_6 with dissolve

    em "Saya tidak tahu, itu seperti cara dia memandang saya berbeda. Seperti dia sedang menatapku."

    scene cs4_5 with dissolve

    mc "Ya, Anda mungkin benar. Anda satu -satunya wanita yang dia lihat dalam waktu yang lama, jadi dia mungkin telah bertindak sedikit aneh."

    mc "Tapi James adalah pria yang baik. Dan selain itu, saya di sini bersamamu."

    scene cs4_6 with dissolve

    em "Bahkan jika bukan itu masalahnya, saya telah memutuskan saya tidak ingin memikirkannya sekarang. Kami memiliki pekerjaan besok; Kita perlu bersiap -siap. Mari kita pulang, mandi, dan tidur."

    scene cs4_5 with fade

    mc "Saya sangat membutuhkannya juga."

    scene pass1 with dissolve

    pause

    scene hd1 with dissolve

    mc "Masih belum berpakaian?"

    scene hd2 with dissolve

    em "Saya sudah berpakaian."

    scene hd3 with dissolve

    mc "Bukankah Theo datang hari ini?"

    scene hd2 with dissolve

    em "Ya, dia."

    scene hd1_5 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    pause

    scene hd3 with dissolve

    mc "Bukankah pakaian Anda sedikit terbuka?"

    scene hd4 with dissolve

    em "Hahahahah."

    scene hd4_5 with dissolve

    em "Dia hanya anak -anak."

    scene hd5 with dissolve

    mc "Anak?! Dia berusia 18 tahun, dan Anda tahu seperti apa usia anak laki -laki itu."

    mc "Hormon mereka melalui atap, dan Anda satu -satunya wanita yang dilihatnya."

    scene hd7 with dissolve

    "KNOCK!KNOCK!KNOCK!"

    scene hd6 with dissolve

    em "Tolong bertindak normal."

    scene hd8 with dissolve

    pause

    scene hd9 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    pause

    scene hd10 with dissolve

    $ persistent.th_unlock = True

    em "Selamat datang Theo!"

    scene hd11 with dissolve

    th "Hei, __var_0__."

    scene hd12 with dissolve

    mc "Ada apa teman?"

    scene hd13 with dissolve

    th "Saya baik mr…"

    scene hd14 with dissolve

    mc "Panggil saja saya __var_0__."

    scene hd15 with dissolve

    th "Oke. Terima kasih __var_0__!"

    scene hd16 with dissolve

    em "Baiklah, cukup berbicara. Mari kita mulai."

    scene hd17 with dissolve

    em "Mari kita lihat apa yang sedang kita kerjakan hari ini!"

    scene hd18 with dissolve

    th "Turunan..."

    scene hd19 with dissolve

    em "Lagi?!"

    scene hd20 with dissolve

    th "Ya."

    scene hd21 with dissolve

    em "Oh sayang, maafkan aku. Kita bisa menanganinya. Jangan khawatir."

    scene hd21_5 with dissolve

    pause

    scene hd22 with dissolve

    mct "Anak ya?"



    menu:
        "Stop Theo":

            $ stp_th += 1

            $ nts_point += 1

            scene hd23_a with dissolve

            mc "Hei Theo!"

            scene hd24_a with dissolve

            th "Hhh-uhh?"

            scene hd25_a with dissolve

            mc "Saya tidak ingat pernah melihat Anda ini fokus."

            scene hd26_a with dissolve

            th "Well-y-yess ... saya harus lulus."

            scene hd27_a with dissolve

            mc "Saya terlambat bekerja. Saya harus pergi sekarang. Semoga berhasil dengan belajar Anda!"

            scene hd28_a with dissolve

            mc "Bye Honey, Bye theo."

            em "Sampai jumpa, sayang."

            th "Bye, __var_0__."

            scene pass2 with dissolve

            pause

            jump path_a
        "Let Him Enjoy The View":


            $ ntr_point += 1

            scene hd23_b with dissolve

            mct "Dia akan pingsan karena menatap."

            mct "Siapa yang tidak akan menatap jika mereka berada di tempatnya?"

            mct "Saya penasaran, akankah __var_0__ juga memperhatikan?"

            scene hd27_a with dissolve

            mc "Saya terlambat bekerja. Saya harus pergi sekarang. Semoga berhasil dengan belajar Anda!"

            scene hd28_a with dissolve

            mc "Bye Honey, Bye theo."

            em "Sampai jumpa, sayang."

            th "Bye, __var_0__."

            scene pass2 with dissolve

            pause

            jump path_b



label path_a:

    scene r1 with fade

    mc "Saya sangat lelah hari ini. Sangat menyenangkan akhirnya berada di rumah dengan Anda."

    mc "Bagaimana belajar Anda?"

    scene r2 with dissolve

    em "Itu bagus. Saya suka mengajar Theo."

    em "Itu mengingatkan saya pada hari -hari ketika saya adalah seorang guru, jadi saya merasa sangat bahagia ketika dia datang."

    scene r3 with dissolve

    mc "Aku suka melihatmu bahagia."

    scene r4 with dissolve

    em "Aww, kamu manis."

    em "Oh, apakah saya menyebutkan bahwa Theo akan datang lebih sering sekarang? Dia masih sedikit berjuang."

    scene r5_a with dissolve

    mc "Saya bisa menebak alasannya. Fokusnya jelas bukan pada studinya."

    scene r6_a with dissolve

    em "Apa maksudmu?"

    scene r7_a with dissolve

    mc "Sepertinya dia lebih tertarik pada payudara Anda daripada pelajaran."

    scene r8_a with dissolve

    em "Benar-benar?? Saya tidak menyadari."

    scene r9_a with dissolve

    mc "Yah, dia bukan anak kecil lagi. Dia masih muda dan sehat."

    mc "Jika dunia seperti dulu, dia bahkan bisa memiliki anak."

    scene r10_a with dissolve

    mc "Saya sedang berpikir--"

    scene r11_a with dissolve

    em "Ya?"

    scene r10_a with dissolve

    mc "Haruskah kita memiliki rencana cadangan selain Andrew?"

    scene r12_a with dissolve

    em "Dengan Theo?!"

    scene r13_a with dissolve

    mc "Dia masih muda, dan spermanya harus sehat. Peluang keberhasilan kami bisa tinggi."

    scene r14_a with dissolve

    em "Anda ada benarnya, tapi ... Saya tidak tahu sayang."

    em "Sebenarnya, itu membuat saya sedikit sedih bahwa dia tidak akan pernah bersama wanita. Mungkin seperti ini, saya juga bisa meringankan hati nurani saya."

    scene r15_a with dissolve

    mc "Saya juga tidak suka, tetapi begitu kami memiliki bayi, kami akan bebas."

    jump dream

label path_b:

    scene r1 with fade

    mc "Saya sangat lelah hari ini. Sangat menyenangkan akhirnya berada di rumah dengan Anda."

    mc "Bagaimana belajar Anda?"

    scene r2 with dissolve

    em "Itu bagus. Saya suka mengajar Theo."

    em "Itu mengingatkan saya pada hari -hari ketika saya adalah seorang guru, jadi saya merasa sangat bahagia ketika dia datang."

    scene r3 with dissolve

    mc "Aku suka melihatmu bahagia."

    scene r4 with dissolve

    em "Aww, kamu manis."

    em "Oh, apakah saya menyebutkan bahwa Theo akan datang lebih sering sekarang? Dia masih sedikit berjuang."

    scene r5_a with dissolve

    mc "Saya bisa menebak alasannya. Fokusnya jelas bukan pada studinya."

    scene r6_a with dissolve

    em "Saya kira itu karena saya. Kamu benar."

    scene r7_a with dissolve

    mc "Sudah kubilang dia bukan anak kecil."

    scene r8_b with dissolve

    mc "Anda seperti guru -guru nakal di porno dengan tema semacam itu."

    scene r8_b1 with dissolve

    em "Hahahahah"

    scene r8_a with dissolve

    em "Sebenarnya, ketika saya melihat Theo mengawasi saya hari ini, saya merasa kasihan padanya ..."

    em "dan terus memikirkannya sepanjang pelajaran."

    scene r9_a with dissolve

    mc "Apa yang Anda pikirkan?"

    scene r11_a with dissolve

    em "Tentang situasi bayi. Maksud saya..."

    em "Saya tahu kami akan mencoba dengan Andrew, tetapi memiliki rencana cadangan akan bagus."

    scene r8_a with dissolve

    mct "Mendengar ini dari __var_0__ mengejutkan saya."

    mct "Sepertinya dia menjadi semakin nyaman dengannya."

    mct "Saya tahu dia menyarankan ini untuk masa depan kita, tapi tetap saja ..."

    scene r12_a with dissolve

    em "Jadi .. apa yang Anda pikirkan tentang ini?"

    scene r13_a with dissolve

    mc "Selama Anda baik -baik saja dengan itu, saya tidak punya masalah."

    mc "Saya tahu Anda menyarankan ini untuk masa depan kami. Aku percaya padamu dan mencintaimu."

    scene r13_b with dissolve

    em "Aku juga sayang."

    scene r16_a with dissolve

    pause

    jump dream

label dream:

    $ persistent.d_scene1_unlock = True

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"


    scene dr1 with fade

    pause

    scene dr2 with dissolve

    unk "*(Erangan)*"

    scene dr3 with dissolve

    mct "Apa suara -suara itu?"

    scene dr4 with dissolve

    unk2 "Anda adalah guru terbaik di dunia. Saya tidak lagi memiliki masalah dengan turunan."

    unk "Mmm ... *Slurp * *-lurp * *rp *"

    unk "Saya siap melakukan apa pun yang Anda butuhkan untuk membantu Anda fokus."

    scene dr5 with dissolve

    mct "WTF ?? Saya harus salah paham."

    scene black with dissolve

    pause(0.01)

    scene bj1 with dissolve

    pause

    scene dr7 with dissolve

    em "Mmmmm ...."

    mc "Apa -apaan?!"

    scene dr8 with dissolve

    em "Jangan khawatir, sayang. Saya hanya membantunya dengan turunan."

    scene dr9 with fade

    th "Saya perlu masuk ke dalam diri Anda, saya tidak bisa menahan diri lagi."

    scene dr10 with dissolve

    em "Ayo, ambil turunan saya."

    menu:
        "Just Watch":

            $ nts_point += 1

            scene dr11 with dissolve

            mct "Itu akan terjadi cepat atau lambat. Saya mungkin juga menikmatinya."

            scene dr11_a with dissolve

            em "Mmm ... tolong masukkan perlahan, Theo."

            mct "Holly ..."
        "Try to Stop":


            $ ntr_point += 1

            scene dr11 with dissolve

            mct "Oke, itu akan terjadi cepat atau lambat, tetapi saya tidak ingin itu dilakukan di belakang saya seperti ini."

            scene dr11_b with dissolve

            mc "WTF?! __Var_0__! Hentikan ini!"


    scene black with dissolve

    "KNOCK!KNOCK!KNOCK!"

    scene dr12 with dissolve

    pause

    scene dr13 with dissolve

    mc "Astaga! Ini sangat nyata."

    $ renpy.end_replay()

    scene black with dissolve

    pause

    scene nm1 with dissolve

    unk2 "Hey __var_0 __... ops .. apakah saya datang lebih awal?"

    scene nm1 with dissolve

    em "Tidak, tidak, masuk. Saya baru saja kembali dari tenis dan melakukan beberapa latihan relaksasi. Beri aku 5 menit, oke?"

    scene nm1 with dissolve

    unk "Oke..."

    scene nm2 with dissolve

    mc "Siapa ini?"

    mc "Oh ... Theo seharusnya datang hari ini. Saya tidak punya pekerjaan, jadi saya bisa bergaul dengan mereka. Biarkan berpakaian dan pergi."

    scene nm3 with dissolve

    em "Kenapa kamu berdiri? Miliki duduk, sayang."

    scene nm4 with dissolve

    th "Saya baik, terima kasih."

    scene nm5 with dissolve

    em "Oh, kamu bangun, sayang. Apakah ada yang salah? Apakah Anda merasa sakit?"

    scene nm6 with dissolve

    mc "Hai! Ya, saya baik -baik saja. Saya bermimpi, dan saya pikir saya masih terpengaruh olehnya."

    scene nm7 with dissolve

    em "Apakah itu mimpi yang buruk?"

    menu:
        "Yes":


            $ ntr_point += 1

            scene nm8 with dissolve

            mc "Saya pikir itu ... apakah Anda sudah belajar hari ini?"

            jump theo_cm
        "No":


            $ nts_point += 1

            scene nm8 with dissolve

            mc "Sejujurnya, itu adalah mimpi yang menyenangkan. Apakah Anda sudah belajar hari ini?"

            jump theo_cm

label theo_cm:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"

    $ persistent.d_scene2_unlock = True

    scene nm9 with dissolve

    em "Ya, konyol, saya katakan itu kemarin. Apakah Anda lupa? Bagaimanapun, jangan mengalihkan perhatian saya; Saya perlu menyelesaikan latihan ini."

    scene nm10 with dissolve

    pause

    scene nm11 with dissolve

    pause

    scene nm12 with dissolve

    pause

    if stp_th == 1:

        scene nm12 with dissolve

        mct "Apakah saya melihat ini salah, atau __var_0__ dengan sengaja menggoda Theo? Tampaknya dia telah menerima apa yang saya sarankan kemarin."
    else:


        scene nm12 with dissolve

        mct "Apakah __var_0__ sudah menempatkan rencana yang dia sarankan kepada saya kemarin untuk beraksi? Saya terkejut dengan betapa bersemangatnya dia."

    scene nm13 with dissolve

    em "Saya tidak bisa cukup meregangkan. Saya butuh bantuan."

    menu:
        "Offer your help.":

            $ ofr_mc += 1

            $ ntr_point += 1

            scene nm14_a with dissolve

            mc "Biarkan saya membantu Anda, sayang."

            scene nm15_a with dissolve

            em "Saya tidak yakin Anda bisa melakukannya dengan benar."

            scene nm16_a with dissolve

            em "THEO! Anda menyukai olahraga, bukan? Bisakah Anda membantu saya?"

            mc "Saya tahu kami memiliki rencana dengan Theo, tetapi apakah dia benar -benar perlu mengatakan saya tidak bisa mengelolanya."

            scene nm15_b with dissolve

            th "Oh .. oke .. apakah kamu yakin?"

            scene nm16_b with dissolve

            em "Lagi pula, Anda telah bermain basket sejak Anda masih kecil. Anda harus tahu beberapa trik."

            scene nm17_b with dissolve

            mct "Saya pikir __var_0__ ingin membuat proses ini menyenangkan dan memasukkan saya ke dalam permainan. Saya semakin bersemangat ..."

            scene nm18_b with dissolve

            pause

            scene nm19_b with dissolve

            em "Ayo, Theo, bukankah Anda akan membantu?"

            th "O-oke. Aku-aku akan melakukannya ..."

            scene nm20_b with dissolve

            pause

            scene nm21 with dissolve

            tht "Oh! Kotoran. Saya punya kesalahan. Saya berharap __var_0__ tidak memperhatikan ini."

            scene nm22 with dissolve

            emt "Apa?"

            emt "Bagaimana dia sudah menjadi sulit? Saya bahkan belum melakukan apa pun!"

            scene nm23 with dissolve

            emt "Yah .. dia berhasil menggosoknya tepat di tempat."

            scene nm24 with dissolve

            mct "Tidak ada keraguan ini lebih dari sekedar membantu latihan peregangan."

            scene nm25 with dissolve

            em "Saya merasa jauh lebih baik sekarang! Terima kasih atas bantuannya. Mari kita hancurkan turunan ini."

            scene nm26 with dissolve

            th "O-Oke…"

            scene nm25 with dissolve

            mct "Yah, yah ... sepertinya seseorang memiliki kesalahan."

            $ renpy.end_replay()
        "Suggest Theo to help.":



            $ nts_point += 1

            $ sgt_th += 1

            scene nm14_b with dissolve

            mc "Theo, mengapa Anda tidak membantu?"

            scene nm15_b with dissolve

            th "Oh .. oke .. apakah kamu yakin?"

            scene nm16_b with dissolve

            em "Lagi pula, Anda telah bermain basket sejak Anda masih kecil. Anda harus tahu beberapa trik."

            scene nm17_b with dissolve

            mct "Saya pikir __var_0__ ingin membuat proses ini menyenangkan dan memasukkan saya ke dalam permainan. Saya semakin bersemangat ..."

            scene nm18_a with dissolve

            pause 

            scene nm19_b with dissolve

            em "Ayo, Theo, bukankah Anda akan membantu?"

            th "O-oke. Aku-aku akan melakukannya ..."

            scene nm20_b with dissolve

            pause

            scene nm21 with dissolve

            tht "Oh! Kotoran. Saya punya kesalahan. Saya berharap __var_0__ tidak memperhatikan ini."

            scene nm22 with dissolve

            emt "Apa?"

            emt "Bagaimana dia sudah menjadi sulit? Saya bahkan belum melakukan apa pun!"

            scene nm23 with dissolve

            emt "Yah .. dia berhasil menggosoknya tepat di tempat."

            scene nm24 with dissolve

            mct "Tidak ada keraguan ini lebih dari sekedar membantu latihan peregangan."

            scene nm25 with dissolve

            em "Saya merasa jauh lebih baik sekarang! Terima kasih atas bantuannya. Mari kita hancurkan turunan ini."

            scene nm26 with dissolve

            th "O-Oke…"

            scene nm25 with dissolve

            mct "Yah, yah ... sepertinya seseorang memiliki kesalahan."

            $ renpy.end_replay()

    scene nm27 with fade

    th "Saya selesai dengan tugas yang Anda berikan kepada saya kemarin!"

    scene nm28 with dissolve

    pause

    scene nm29 with dissolve

    em "Menurut saya…"

    scene nm30 with eye_open

    em "Saya akan memberi Anda hadiah untuk itu."

    scene nm31 with eye_shut

    pause (2.0)

    scene nm32 with eye_open

    th "Tha..tertanggungjawabkan. Anda tidak perlu memberi saya hadiah."

    scene nm33 with dissolve

    pause

    scene chl with dissolve

    pause



    if sgt_th == 1:

        scene a1 with dissolve

        mc "Anda tidak marah karena saya mengemukakan ide tentang Theo segera, bukan?"

        scene a2 with dissolve

        em "TIDAK! Sebenarnya, itu sangat menyenangkan. Saya merasa sangat panas menggodanya seperti itu."

        scene a3 with dissolve

        mc "Ha ha ha. Melihatmu seperti itu agak aneh, tapi ... kurasa aku menyukainya"

        scene a4 with dissolve

        em "Ini adalah sesuatu yang baru untuk hubungan kami ... Saya harus mengakui, saya juga menyukainya. Tapi aku masih merasa aneh, sayang."

        em "Ketika semua ini dimulai, saya pikir semuanya akan sangat sulit, tetapi dengan Anda, semuanya terasa lebih mudah. Aku mencintaimu, sayang."

        scene a6 with dissolve

        mc "Aku juga mencintaimu, lebih dari yang pernah kamu ketahui."

    if ofr_mc == 1:


        scene a2 with dissolve

        em "Saya harus mengakui, ini adalah pengalaman yang sangat berbeda. Saya merasa sangat panas menggodanya seperti itu."

        em "Theo mengalami ereksi tanpa saya melakukan apa pun. Saya menghibur saya untuk menempatkannya pada posisi yang canggung."

        scene a1 with dissolve

        mc "Melihat Anda seperti itu membuat saya bersemangat, tetapi Anda benar -benar tidak harus melakukan itu."

        scene a4 with dissolve

        em "Apa yang kamu bicarakan?"

        scene a1 with dissolve

        mc "Saya berbicara tentang Anda mengatakan saya tidak akan bisa melakukannya."

        scene a4 with dissolve

        em "Saya menempatkan rencana yang kami bicarakan kemarin beraksi. Kami membuat keputusan, dan saya baru saja melakukannya untuk memulai."

        em "Anda tahu saya mencintaimu, __var_0__. Saya pikir Anda menginginkan ini juga."

        scene a1 with dissolve

        mc "Saya ingin ..."

        mc "Aku hanya ..."

        mc "Saya kira Anda benar. Itu adalah keputusan bersama kami. Anda baru saja membuat saya lengah."

        scene a6 with dissolve

        mc "Dan aku juga mencintaimu, sayang."

    scene 5m with dissolve

    pause

    scene at1 with dissolve

    "*-RING!! RING!! RING!!-"

    scene at2 with dissolve

    pause

    scene at2 with dissolve

    mct "Oh. Itu Andrew."

    scene at3 with dissolve

    aw "Hei, bagaimana kabarmu? Kami belum berbicara sejak hari itu."

    aw "Saya tidak ingin membuat hal -hal canggung, tetapi saya harus bertanya - apakah Anda memutuskan untuk mundur?"

    scene at4 with dissolve

    mc "Apakah Anda turun untuk langkah lain selanjutnya?Tidak, kami belum mundur; Kami hanya memproses apa yang terjadi. Sebenarnya, saya akan menelepon Anda hari ini."

    scene at3 with dissolve

    aw "Saya sibuk sekarang, tapi ... oke, saya sedang dalam perjalanan!"

    scene at4 with dissolve

    mc "Oke, bung."

    scene at5 with dissolve

    mc "Dia akan datang."

    scene at6 with dissolve

    em "Memiliki beberapa hari berlalu baik. Saya merasa jauh lebih santai sekarang."

    scene at5 with dissolve

    mc "Saya dapat melihat bahwa Anda lebih santai sekarang, dan itu ..."

    menu:
        "Worries me":

            $ ntr_point += 1

            scene at6_a with dissolve

            mc "Saya tidak bisa tidak khawatir - bagaimana jika ini mempengaruhi hubungan kita? Bagaimana jika Anda mulai mengembangkan perasaan untuk Andrew?"

            scene at7_a with dissolve

            em "Jangan konyol! Aku mencintaimu. Semua ini tidak akan mengubah apa pun di antara kami"
        "Comforts me":


            $ nts_point += 1

            scene at6_b with dissolve

            mc "Saya tahu situasinya aneh, tetapi saya senang bahwa saya tidak melihat Anda stres lagi."

            scene at7_b with dissolve

            em "Saya percaya pada cinta kita. Tidak peduli apa yang terjadi, kami bersama -sama."

    scene at8 with dissolve

    em "Saya akan minum satu atau dua gelas anggur sebelum Andrew tiba di sini. Apakah Anda juga menginginkannya?"

    scene at9 with dissolve

    mc "Tidak, terima kasih sayang."

    scene at9_5 with dissolve

    pause

    scene oneh with dissolve

    pause

    scene rt1 with dissolve

    aw "Hei, kawan! Siap untuk ronde kedua?"

    scene rt2 with dissolve

    pause

    scene rt3 with dissolve

    aw "Hanya lelucon, kawan. Santai."

    scene rt4 with dissolve

    mc "Kami melakukan ini karena suatu alasan, ingat?"

    scene rt5 with dissolve

    aw "Oke, oke ... jangan simpan __var_0__ menunggu."

    scene rt6 with dissolve

    aw "Whoa, kamu terlihat luar biasa hari ini!"

    scene rt7 with dissolve

    em "Hei, Andrew!"

    scene rt8 with dissolve

    em "Baru hari ini?"

    scene rt9 with dissolve

    aw "Ha ha ha. Saya pikir Anda akan tegang seperti terakhir kali."

    scene rt10 with dissolve

    em "Saya sudah terbiasa."

    scene rt11 with dissolve

    aw "Jadi, apakah Anda siap untuk langkah selanjutnya?"

    mct "Saya pikir mungkin lebih baik jika saya tetap sedikit sunyi, dengan begitu suasana tidak akan begitu canggung."

    scene rt12 with dissolve

    em "Kukira..."

    mct "Ya, kami kira ..."

    scene rt13 with dissolve

    aw "Apakah Anda akan melepas pakaian Anda saat ini?"

    scene rt14 with dissolve

    em "Yah, tidak terlalu cepat. Aku bisa menyentuhmu seperti terakhir kali."

    scene rt15 with dissolve

    aw "Ya ampun ... oke, kalau begitu."

    scene rt16 with dissolve

    aw "Anda adalah bosnya."

    scene rt17 with dissolve

    mct "Saya bertanya -tanya apa yang dipikirkan __var_0__ sekarang."

    mct "Kali ini, saya akan mundur sedikit. Mari kita lihat bagaimana kemajuan."

    scene rt18 with dissolve

    pause

    scene rt19 with dissolve

    aw "Tunggu."

    scene rt20 with dissolve

    aw "Sekarang ... lebih baik. Mari kita lanjutkan __var_0__."

    scene rt21 with dissolve

    emt "Saya bilang saya sudah terbiasa, tetapi ketika saya melihat hal besar itu, saya berubah pikiran. Bagaimana mungkin wanita mana pun terbiasa dengan ini?"

    scene rt22 with dissolve

    emt "Saya bisa merasakan beratnya di tangan saya. Semakin sulit dan lebih sulit di tangan saya."

    scene black with dissolve

    pause(0.01)

    scene hj3_s with dissolve

    emt "Penis Andrew memiliki aroma yang berbeda. Itu aroma yang lebih kuat. Saya tidak bisa menggambarkannya, tetapi berbeda dari __var_0 __ 's."

    scene black with dissolve

    pause(0.01)

    scene hj3_f with dissolve

    pause

    scene rt23 with dissolve

    awt "Dia berbau seperti parfum dan anggur. Kali ini, saya tidak akan membiarkan Anda menyelesaikannya dengan cepat. Si kecil tidak hanya akan puas dengan tangan Anda kali ini."

    scene black with dissolve

    pause(0.01)

    scene hj_s with dissolve

    pause

    scene hj_f with dissolve

    emt "Apakah saya salah? Sepertinya dia tidak akan cum dalam waktu dekat."

    scene rt24 with dissolve

    em "Ugh. Saya lelah. Mengapa Anda belum bisa menyelesaikannya? Apakah Anda mengambil sesuatu atau apa?"

    scene rt25 with dissolve

    aw "Whaaa… apa? Saya tidak minum pil atau apapun. Beginilah saya. Tidak ada yang bisa membuat saya cum hanya dengan tangan mereka."

    scene rt26 with dissolve

    em "Benar-benar?! Jadi, apa yang perlu saya lakukan?"

    scene rt25 with dissolve

    aw "Saya pikir Anda siap untuk seks. Biarkan diri Anda pergi dengan saya. Saya berjanji Anda akan merasa baik."

    scene rt27 with dissolve

    em "Mustahil! Terlalu dini untuk itu!"

    scene rt28 with dissolve

    aw "Oh .. Oke, bos. Kemudian setidaknya biarkan saya menggunakan mulut Anda."

    scene rt29 with dissolve

    em "Dengan baik..."

    scene rt30 with dissolve

    pause 

    jump aw_scnd

label aw_scnd:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"

    $ persistent.b_scene1_unlocked = True


    $ persistent.a_scene2_unlocked = True

    scene rt31 with dissolve

    mct "Saya tidak tahu apakah saya ingin dia melakukan ini dengan orang lain karena dia menolaknya berkali -kali sebelumnya."

    mct "Saya tahu kita perlu bergerak maju. Saya tidak yakin apakah saya ingin dia melakukan sesuatu dengan orang lain yang tidak ingin dia lakukan dengan saya."

    menu:
        "Insist on sex":

            $ ntr_point += 2

            scene rt32 with dissolve

            mc "Sayang ... Anda akan berhubungan seks pada akhirnya. Saya pikir Anda siap untuk itu hari ini"

            scene rt33 with dissolve

            em "Benar-benar? Sudah kubilang aku belum siap! Saya tidak bisa mempercayai Anda. Saya akan pergi dengan saran Andrew."

            em "Andrew Bisakah Anda bergerak seperti ini?"

            scene rt34 with dissolve

            aw "Oke… saya akan berdiri di mana pun Anda menginginkan saya sekarang."

            scene rt35_a with dissolve

            mct "__Var_0__ sangat marah padaku. Saya merasa tidak memadai dan akhirnya mengabaikan perasaannya. Saya tidak yakin apakah dia menghukum saya atau jika dia tidak peduli."

            mct "Dia bertingkah seolah -olah saya bahkan tidak ada di dalam ruangan."
        "Support the blowjob idea":


            $ nts_point += 2

            scene rt32 with dissolve

            mc "Tidak apa -apa sayang. Saya tahu Anda belum siap untuk seks."

            scene rt29 with dissolve

            em "Saya kira saya harus melakukan itu. Saya belum siap untuk mengambil benda itu di ..."

            em "Anywways. Andrew, bisakah kamu pindah ke sana?"

            scene rt34 with dissolve

            aw "Oke… saya akan berdiri di mana pun Anda menginginkan saya sekarang."

            scene rt35 with dissolve

            mct "Apakah __var_0__ mencoba menggodaku? Jika demikian, itu pasti berfungsi."

            scene rt36 with dissolve

            mct "Dia terlihat sangat seksi sekarang. Rasanya seperti saya dan __var_0__ sedang bermain game - permainan nakal."

    scene rt37 with dissolve

    awt "Mulutnya sangat kecil dan kencang ... rasanya seperti saya di dalam __var_0__ vagina."

    em "Mmm ... mmm."

    scene rt38 with dissolve

    awt "Sepertinya ini bukan pertama kalinya dia."

    aw "Hhh… __var_0__ y-kamu ..."

    aw "Hhh .. kamu sangat sempurna."

    scene rt39 with dissolve

    em "Slurp..slurp… Slurp."

    aw "Rasanya menyenangkan."

    scene black with dissolve

    pause(0.01)

    scene bj2 with dissolve

    aw "__Var_0__, Anda harus berhenti! Saya akan .. cum !!"

    scene rt40 with dissolve

    aw "OH!!!"

    scene rt41 with dissolve

    em "Apa…"

    scene rt42 with dissolve

    mc "Tunggu..."

    scene rt43 with dissolve

    aw "Maaf __var_0__, itu adalah kecelakaan. Saya tidak tahan lagi."

    scene rt44 with dissolve

    mc "BUNG!"

    em "Apa dia ..."

    scene rt45 with dissolve

    aw "Oh, saya benar -benar lupa! Saya punya sesuatu untuk dilakukan. Saya harus pergi. Selamat tinggal!"

    scene rt46 with dissolve

    em "Apa itu ?? Ugh ... aku akan membersihkan."

    scene rt47 with dissolve

    mc "Oke..."

    $ renpy.end_replay()

    scene rt48 with dissolve

    pause

    scene rt49 with dissolve

    em "Saya pasti tidak mengharapkan hal itu terjadi."

    scene rt50 with dissolve

    mc "Sama di sini, itu sangat aneh."

    scene rt51 with dissolve

    mct "Dia berbau sangat kuat ... semen…"

    scene rt52 with dissolve

    em "Saya akan berteriak padanya."

    scene rt53 with dissolve

    em "Tetapi ketika saya melihatnya melarikan diri seperti itu, saya harus benar -benar menahan tawa saya."

    scene rt54 with dissolve

    em "Saya pikir kami menangani hari ini dengan cukup baik, selain dari bagian terakhir."

    scene rt51 with dissolve

    mc "Saya pikir begitu juga."

    mc "Jadi saya berpikir ..."

    scene rt55 with dissolve

    pause

    scene rt56 with dissolve

    em "Tidak terlalu mood untuk itu, sayang."

    scene rt57 with dissolve

    mc "Ohh. Oke. Maaf sayang."

    scene rt58 with dissolve

    mc "Oh! Ini telepon Andrew! Dia pasti menjatuhkannya. Saya harus membawanya kepadanya."

    scene rt59 with dissolve

    pause

    scene rt60 with dissolve

    em "Sekarang?"

    scene rt61 with dissolve

    mc "Ya, saya akan segera kembali."

    scene rt60 with dissolve

    em "Oke, sayang. Berkendara aman."

    scene rt62 with dissolve

    pause

    scene rt63 with dissolve

    mc "Hai! Sayang… Saya di rumah."

    scene rt64 with dissolve

    mct "Oh…"

    mct "Apakah itu pengontrol jarak jauh?"

    scene black with dissolve

    pause

    jump expose




label halloween_event_label:

    $ disable_saving = True

    scene inf with dissolve

    pause

    scene black

    $ name = renpy.input("My name is", default ="Jake", length=15)
    $ persistent.name = name

    if name == "":
        $ mc = "Jake"
        $ mct = "Jake Tought"
        menu:
            "Are you sure about Jake?"
            "Yes":
                pause
            "No,Please.":

                pause



    $ fname = renpy.input("My wife's name is", default ="Emily", length=15)
    $ persistent.fname = fname

    if fname == "":
        $ em = "Emily"
        $ emt = "Emily Tought"

    if _in_replay:
        if persistent.name:
            $ mc = persistent.name
        if persistent.fname:
            $ em = persistent.fname


    scene h0 with dissolve

    mct "Wanita ... dia bilang dia akan siap dalam 10 menit satu jam yang lalu, dan dia masih belum siap."

    scene h1 with dissolve

    mc "Apakah Anda masih belum siap, __var_0__?"

    scene h2 with dissolve

    em "Baiklah, baiklah! Lima menit lagi. Jangan terburu -buru."

    scene h1 with dissolve

    mc "Jadi ... itu berarti Anda akan siap dalam setengah jam?"

    scene h2 with dissolve

    em "Haha, kamu sangat imut. Percayalah, saya akan layak ditunggu."

    scene h2 with dissolve

    em "Oh, omong -omong, sayang, apakah Anda mendapatkan anggur yang saya minta?"

    scene h2_5 with dissolve

    mct "Oh, sial. Bagaimana saya melupakan itu? Jika saya memberi tahu __var_0__, dia akan membunuh saya."

    scene h2_5 with dissolve

    mc "Uh ... ya, tentu saja! Saya bahkan sudah menurunkannya di Andrew."

    scene h2_6 with dissolve

    em "Oh, kamu luar biasa!"

    scene h2_7 with dissolve

    mct "James adalah satu -satunya yang bisa menangani ini dengan cepat. SMS lebih baik sekarang."

    scene 30m with dissolve

    pause

    scene h2_8 with fade

    em "Saya siap."

    scene h3 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    mc "Wow!"

    scene h4 with dissolve

    em "Tak bisa bicara?"

    scene h4 with dissolve

    mc "Hmm… sayang?"

    menu:
        "Warn her about the dress showing too much":

            scene h4_1 with dissolve
            mc "Tidakkah Anda pikir bagian depan gaun Anda adalah ... yah, agak terlalu rendah?"

            scene h4_2 with dissolve
            em "Ah, benarkah? Anda pikir begitu?"

            scene h4_3 with dissolve
            mc "Maksud saya, jika Anda tidak berhati -hati, saya mungkin mengintip ... yah, Anda tahu."

            scene h4_4 with dissolve
            em "Kurasa aku lebih baik ekstra hati -hati."

            scene h4_4 with dissolve
            mc "Ha ha."

            $ persistent.warn_1 = False
        "Don't warn her":


            scene h4_1 with dissolve
            mc "Kecantikan Anda hanya membuat saya terdiam sebentar di sana."

            scene h4_1 with dissolve
            mc "Anda terlihat sangat menakjubkan."

            scene h4_2 with dissolve
            em "Ohh ... terima kasih, sayang."

            $ persistent.warn_1 = True

    scene h4_1 with dissolve

    mc "Ayo ...."

    scene h4_9 with dissolve

    em "Mwah!"

    scene h4_5 with fade

    mc "Wow! Untuk apa itu?"

    em "Ini hanya ciuman permintaan maaf karena membuat Anda menunggu. Ayo, kita terlambat - mari kita pergi!"

    scene 30m with dissolve

    pause

    scene h4_6 with dissolve

    mc "Wow! Andrew benar -benar masuk ke dalam semangat Halloween!"

    em "Ya, saya tidak berharap dia pergi ke semua masalah ini."

    em "Tunggu Tunggu Tunggu!"

    scene h4_7 with dissolve

    em "Apakah saya terlihat seram dan seksi?"

    mc "Anda selalu melakukannya, sayang."

    scene h4_8 with dissolve

    em "Hai?!"

    scene h4_8_2 with dissolve

    aw "Apa yang kalian lakukan di sini?"

    aw "Tidak berencana masuk?"

    scene h4_8_3 with dissolve

    aw "Ngomong -ngomong, sudahlah. Saya bekerja keras pada sambutan saya, jadi begini!"

    scene h5 with dissolve

    aw "Selamat datang di Pesta Halloween Legendaris Andrew!"

    mc "Kawan! Anda membuat saya takut!"

    em "Ahhhh! Astaga!"

    scene h5_5 with dissolve

    aw "Maaf! Saya pikir itu akan membuat 'sambutan' yang mengesankan."

    em "Anda membuat saya takut setengah mati dengan sambutan itu! Tapi karena ini Halloween, saya akan membiarkannya meluncur kali ini."

    mc "Ya, kawan…"

    scene h6 with dissolve

    aw "Hei, dari mana saja kalian? Saya mulai berpikir Anda telah menyerah pada datang."

    mc "Kami terlambat. Anda bisa menebak mengapa."

    scene h7 with dissolve

    aw "Biarkan saya menebak. Itu semua salahmu."

    mc "Ha ha ha."

    scene h8 with dissolve

    em "Hai! Berhenti mengacaukan saya."

    aw "Tentu…"

    mc "Tentu saja, sayang!"

    em "Ayo, mari kita pergi ke dalam."

    scene h9 with dissolve

    aw "Psst, hey man, bisakah kita bicara sebentar?"

    mc "Ya, ada apa, kawan? Apakah ada yang salah?"

    scene h10 with dissolve

    aw "Anak yang Anda undang muncul, tetapi apakah Anda yakin dia berusia 18 tahun?"

    mc "Ya, ya. Dia hanya terlihat sedikit lebih muda, tetapi tidak ada masalah."

    scene h11 with dissolve

    aw "Jika Anda berkata begitu ..."

    aw "Dia tampak agak ... aneh. Dan kostum itu ...?"

    mc "Ada apa dengan kostumnya?"

    aw "Anda akan melihat. Ayo, mari kita masuk ke dalam."

    scene h12 with fade

    pause

    scene h13 with Dissolve(3.5)

    unk2 "Aaaaargh ..."

    scene h14 with Dissolve(1.5)

    unk2 "Ha ha ha!"

    scene h15 with Dissolve(1.5)

    unk2 "Mari bersenang -senang."

    scene h12 with Dissolve(3.5)

    pause

    scene h16 with fade

    jm "Maukah Anda jika saya memeriksa kain gaun Anda, __var_0__?"

    em "Hah?"

    th "Ya, tolong, bisakah saya merasakannya juga?"

    scene h17 with dissolve

    jm "Hai! Selamat datang, __var_0__."

    mc "Terima kasih."

    th "Selamat datang, __var_0__."

    mc "Terima kasih, sobat."

    mc "Sejujurnya saya tidak berharap Anda melakukan banyak upaya dalam kostum ini. Itu terlihat sangat realistis."

    scene h18 with dissolve

    jm "Ya. Saya dan istri saya dulu pergi ke pesta kostum setiap tahun, dan ada ... berbagai fantas ... ahem. Pokoknya, terima kasih."

    scene h17 with dissolve

    th "Ya, sangat penting bagi saya. Ini pertama kalinya saya menghadiri pesta Halloween."

    mc "Itu bagus. Tapi Theo, sepertinya Anda lupa berpakaian, sobat. Ada apa dengan kostumnya?"

    scene h19 with dissolve

    th "Dia karakter yang solid.Ini kostum bonecrusher! Beginilah cara dia berpakaian. Sebenarnya, dia juga orang jahat, tapi dia menghancurkan orang jahat lainnya."

    scene h20 with dissolve

    emt "Wow. Saya kira sudah saatnya saya menerima bahwa Theo mulai tumbuh dewasa. Sepertinya dia mendorong sesuatu yang besar ke dalam pakaian dalamnya, dan pakaian dalamnya akan meledak."

    scene h19 with dissolve

    mc "Apakah saya melihat ini benar, atau __var_0__ melihat penis Theo?"

    mc "Apakah ukuran yang menarik perhatiannya? Bisakah dia menyukainya?"

    mc "Wanita yang saya cintai sedang melihat ayam besar pria muda lainnya. Kotoran. Saya bahkan tidak tahu bagaimana perasaannya."

    mc "Saya seharusnya tidak memikirkan hal ini sekarang, atau akhirnya saya akan menjadi sulit."

    scene h21 with dissolve

    jm "Baiklah, tenanglah. Biarkan saya membuat kalian minum. Anda perlu sedikit melonggarkan!"

    scene h22 with dissolve

    "Yeah!"

    scene h22_5 with dissolve

    jmt "Sekarang…"

    scene h23 with dissolve

    jmt "Mari kita tambahkan beberapa campuran khusus Paman James dan ..."

    scene h23_5 with dissolve

    jmt "Biarkan pesta menjadi lebih menarik."

    scene h24 with dissolve

    em "... Itu adalah pokok dari pesta kuliah kami ..."

    scene h25 with dissolve

    jm "Siapa yang mau anggur? Ini sangat bagus - yang berumur dengan sempurna."

    scene h26 with dissolve

    jmt "Wow! Sungguh pemandangan. Suatu hari, aku akan menggigit putingmu, __var_0__."

    scene h27 with dissolve

    em "Apakah Anda bercanda? Saya sudah menunggu ini sepanjang minggu!"

    scene h27 with dissolve

    mc "Sama di sini."

    th "Saya menginginkannya juga!"

    aw "Hitung aku! Saya tidak kehilangan itu."

    scene h28 with dissolve

    em "Jadi, Andrew, apakah ini pesta Halloween yang terkenal yang telah Anda hipati?"

    aw "Oh, kamu bertaruh! Kemudian malam ini, saya telah mengatur agar hantu horny Mary berdarah muncul. Dia akan membawa pesta ke tingkat berikutnya!"

    th "Mengapa mereka memanggilnya * Horny * Mary?"

    em "Percayalah, Theo. Anda tidak ingin tahu."

    mc "Ayo, jangan memenuhi kepalanya dengan omong kosong ini."

    jm "Hehehe ..."

    scene h28 with dissolve

    aw "Bloody Horny Mary adalah legenda. Mereka mengatakan dia muncul di cermin, mengambil alih tubuh wanita, dan memberi pria waktu hidup mereka ..."

    aw "Sampai dia mengeringkan penis mereka kering dari setiap tetes darah terakhir. Dia tidak berhenti sampai sama sekali tidak ada yang tersisa!"

    th "Whoa."

    em "Ha ha..."

    scene h29 with dissolve

    mct "Apakah bajingan tua ini menatap payudara __var_0 __?"

    if persistent.warn_1 == True:

        scene h29 with dissolve

        mct "Dia bahkan belum bergabung dengan percakapan atau menggerakkan kepalanya sama sekali."

        mct "Sulit untuk mengatakan dengan tepat di mana dia melihat dengan topeng itu. Topeng itu menutupi matanya."

        scene h31 with dissolve

        mct "WTF? Apakah dia ... membelai dirinya sendiri?"

        mct "Saya harus memperingatkan __var_0__. Dia masturbasi tepat di depan saya sambil menatap payudaranya."

        scene h30 with dissolve

        mct "Dia sangat dekat. Hanya sedikit lagi, dan dia bisa menggosok bahunya. Atau bahkan di wajahnya."

        mct "Kotoran. Berpikir tentang ini membuatku sulit. Pikiran James tua menggosok penisnya di wajah istri saya yang cantik sangat membangkitkan gairah. Apakah alkoholnya?"

        mct "Bagaimanapun, dia tidak terlalu menyakiti siapa pun. Tetap tenang, __var_0__. Nikmati saja momennya."
    else:


        scene h30_5 with dissolve

        mct "Haha ... sepertinya __var_0__ juga diperhatikan. Dia pasti ingat peringatan yang saya berikan di rumah."

        scene h31_5 with dissolve

        jm "Grrr ..."

        mct "Kemudian, lama James, tetapi saya harus menyerahkannya kepada Anda untuk upaya ini."


    scene h33 with dissolve

    em "Sayang, di mana kamu menemukan anggur ini? Vino Rouge d'Argent ... Sudah bertahun -tahun sejak saya terakhir memiliki beberapa."

    scene h32 with dissolve

    mc "Seorang pesulap tidak pernah mengungkapkan rahasianya."

    jm "Ha ha ha!"

    scene h33 with dissolve

    em "Mungkin pesulap yang menemukan anggur ini layak mendapatkan hadiah. Di penghujung malam ..."

    scene h32 with dissolve

    jm "Hmm..."

    mct "Kotoran."

    mc "Ya, sayang. Anda pasti harus menghadiahinya."

    scene h33 with dissolve

    em "Haha ... Saya berharap Anda bisa melihat raut wajah Anda. Anda tersipu, bukan? Imut-imut sekali."

    mct "Jika Anda tahu saya baru saja mendengar Anda mengatakan ingin memberi hadiah kepada James di tempat tidur, Anda akan mengerti mengapa wajah saya terlihat seperti ini."

    scene h34 with Dissolve(3.5)

    unk2 "Ah, kelompok yang hidup."

    scene h35 with Dissolve(2.0)

    unk2 "Biarkan aku…"

    scene h36 with Dissolve(2.0)

    unk2 "Aduk sedikit."

    scene h37 with Dissolve(2.0)

    unk2 "Kecantikan seperti itu ... layak untuk dihargai oleh semua orang."

    scene h38 with Dissolve(2.0)

    unk2 "Apakah kita juga sedikit bermain dengan puting? Maka itu sempurna. Bersenang -senang, kecantikan ..."

    scene h39 with Dissolve(3.5)

    em "Pokoknya ... terima kasih telah menemukan anggur ini, sayang."

    scene h40 with dissolve

    em "Itu ... sangat aneh. Saya merasakan dingin sejenak di sana."

    em "Mengapa semua orang menatapku seperti itu?"

    mc "Uh ... __var_0 __..."

    scene h41 with dissolve

    th "Saya ... saya pikir gaun Anda ..."

    aw "Membuka. Itu ... terbuka."

    em "Apa?"

    scene h42 with dissolve

    em "Astaga!"

    em "Bagaimana ini bisa terjadi?!"

    scene h43 with dissolve

    mc "Sayang, kamu baik -baik saja?"

    em "Tidak, saya tidak baik -baik saja! Ini memalukan!"

    em "Mereka melihat segalanya!"

    scene h44 with dissolve

    jm "Hei, eh, mungkin anggurnya? Sudah malam yang aneh ..."

    th "Ya, ya dan tidak ada yang melihat apapun! Aku bersumpah!"

    aw "Theo, kita semua melihat segalanya."

    em "Andrew! Tidak membantu!"

    scene h45 with dissolve

    mc "__Var_0__, mari kita melangkah keluar sebentar. Berhati -hatilah, oke?"

    em "...Bagus. Hanya ... Beri aku waktu sejenak."

    em "Saya pikir saya harus sendirian sebentar ... di mana kamar mandi?"

    aw "Di lantai atas, di sebelah kanan."

    scene h46 with dissolve

    jm "Yah ... itu ... tidak terduga."

    aw "Jadi, eh, siapa yang mau lebih banyak anggur?"

    scene h47 with fade

    em "Ya Tuhan ... mereka semua melihat saya."

    em "Andrew, James, bahkan Theo! Mereka semua menatapku seperti—"

    em "Bagaimana mungkin saya tidak memperhatikan gaun saya? Tuhan, itu sangat memalukan ..."

    em "Mereka menatapku seolah -olah mereka ingin melahapku ... dan aku berdiri di sana, menunjukkan semuanya dengan __var_0__ tepat di sebelahku."

    scene h48 with dissolve

    em "Mereka menatapku seolah -olah mereka ingin melahapku ... dan aku berdiri di sana, menunjukkan semuanya dengan __var_0__ tepat di sebelahku."

    scene h48 with dissolve

    em "Memikirkan mereka saat mereka menatap, dengan __var_0__ di sisiku ... rasanya begitu…"

    scene h49 with dissolve

    unk2 "Sungguh pemandangan yang indah ... semua mata mereka tertuju pada Anda, minum setiap inci."

    scene h49 with dissolve

    unk2 "Gaun itu ... memelukmu dengan sangat sempurna. Dan kemudian, cara membuka, mengungkapkan rahasia Anda. Godaan seperti itu ... bahkan jika Anda tidak bermaksud demikian."

    scene h50 with dissolve

    unk2 "Saya bisa merasakan keinginan mereka mengisi ruangan, sama seperti mereka ingin mengisi Anda. Tidak bisakah kamu?"

    scene h50 with dissolve

    unk2 "Tubuh ini ... sangat hangat, sangat lembut. Itu milikku sekarang."

    scene h50 with dissolve

    unk2 "Izinkan saya menunjukkan kepada Anda apa yang mereka bayangkan. Biarkan saya membantu Anda merangkul kesenangan ini yang telah Anda tetap terkubur."

    scene h50 with dissolve

    unk2 "Mmm ... ya. Inilah yang pantas Anda dapatkan ... untuk merasa dipuja, disembah, diinginkan."

    scene h51 with dissolve

    pause

    scene h52 with dissolve

    pause

    scene h53 with dissolve

    unk2 "Hmm…"

    scene h54 with dissolve

    jm "Baiklah, teman -teman, saya secara resmi pada batas saya. Saya terlalu tua untuk anggur sebanyak ini. Panggilan alam, dan ini sangat mendesak!"

    scene h54 with dissolve

    jm "Apakah ada kamar mandi lain di sekitar sini? Sepertinya __var_0 __ menggunakan satu di lantai atas."

    scene h55 with dissolve

    aw "Ya, ada satu lagi di kamar saya. Kepala ke atas, dan itu adalah pintu ke kiri."

    scene h56 with dissolve

    jm "Punya, terima kasih."

    scene h56_5 with dissolve

    pause

    scene h57 with dissolve

    jmt "Tunggu ... apakah __var_0__?"

    scene h57_5 with dissolve

    jmt "Suci - apa dia ...?"

    scene h58 with fade:
        subpixel True
        yalign 1.0
        pause 1.5
        linear 7.0 yalign 0.0

    jmt "Apa ini? Apakah dia ... apakah ini semacam lelucon?"

    jmt "Apakah dia membiarkan pintu terbuka dengan sengaja? Mungkin __var_0__ dan __var_1__ menjadi sesuatu yang keriting, dan saya baru saja menemukannya ..."

    scene h59 with dissolve

    em "James ... Saya tahu Anda di sana. Mendekati."

    scene h59 with dissolve

    jm "__Var_0__, apakah ini ... apakah ini lelucon? Apakah Anda dan __var_1__ menguji saya atau sesuatu?"

    scene h60 with dissolve

    em "Apakah ini terlihat seperti lelucon bagi Anda?"

    scene h60 with dissolve

    jmt "Sialan ... ini tidak bisa nyata. Apakah dia benar -benar ... mengundang saya?"

    scene h60 with dissolve

    jm "__Var_0__, saya ... lihat, jika Anda serius tentang ini, saya bukan orang yang mengatakan tidak, tetapi ini harus ada di antara kami. Anda tahu __var_1__ tidak dapat mengetahuinya."

    scene h60 with dissolve

    em "__Var_0__? Oh, James ... lupakan dia. Saat ini, hanya Anda dan saya."

    scene h60 with dissolve

    em "Sekarang, James ... mengapa Anda tidak menunjukkan apa yang telah Anda pikirkan sepanjang malam?"

    scene h61 with dissolve

    jm "Jangan pedulikan jika saya melakukannya, sayang."

    scene h62 with dissolve

    em "Jadi, katakan padaku, James ..."

    scene h62 with dissolve

    em "Apa yang akan Anda lakukan dengan tubuh ini? Maksudku ... apa yang akan kamu lakukan padaku?"

    scene h62 with dissolve

    jm "Ermm ... aku ingin mencium bau vaginamu. Dan kemudian cicipi itu."

    scene h62 with dissolve

    em "Anda akan mencium bau dan merasakan vagina seorang wanita yang suaminya berada di lantai bawah menikmati pesta? Suamiku bahkan belum mencium bau vaginaku."

    scene h62 with dissolve

    jm "Kemudian biarkan saya berhasil di mana suami Anda gagal. Biarkan lidah saya menjelajahi di dalam."

    scene h63 with dissolve

    jmt "Ahh…"

    scene h63 with dissolve

    jmt "Mmm ..."

    scene h63 with dissolve

    jmt "Bau itu. Seperti bunga liar yang basah kuyup dalam dosa. Begitu mentah, sangat kotor ... Tuhan, itu membuat saya gila."

    scene h64 with dissolve

    em "Apakah Anda menyukainya?"

    scene h64 with dissolve

    jm "Kulit muda dan halus seperti itu ... untuk pria seusia saya, ini di luar mimpi."

    scene h64 with dissolve

    em "Ahh ..."

    scene h64 with dissolve

    jm "Saya tidak percaya suami Anda berada di lantai bawah saat Anda membiarkan saya mengendus vagina Anda di sini."

    scene h64 with dissolve

    em "Saya hanya berharap dia bisa menonton apa yang akan Anda lakukan pada saya. Anda dapat melakukan apa pun yang Anda inginkan untuk vagina saya James."

    scene h65 with dissolve

    jm "Kemudian berbaring di sana."

    scene h65 with dissolve

    em "Tapi aku harus memperingatkanmu. Anda tidak punya banyak waktu. Anda hanya dapat memenuhi satu keinginan untuk saat ini."

    scene h65 with dissolve

    jm "Satu -satunya keinginan saya adalah mencicipi pot madu Anda."

    scene h66 with dissolve

    em "Hmm..."

    scene h66 with dissolve

    em "Kemudian?"

    scene h67 with dissolve

    jm "Ha ha."

    scene h68 with dissolve

    pause

    scene h69 with dissolve

    pause

    scene h70 with dissolve

    pause

    scene h71 with dissolve

    pause

    scene h72 with dissolve

    em "Ahh…"

    scene h72 with dissolve

    em "Jalankan lidah Anda di dalam diri saya."

    scene h73 with dissolve

    jm "*Mencucup*"

    scene h73 with dissolve

    em "Ahhh… ah…"

    scene h73 with dissolve

    jm "Mmmm…"

    scene h73 with dissolve

    em "Saya cumming."

    scene h74 with dissolve

    em "Itu terasa sangat enak. Saya yakin Anda benar -benar mengonsumsi __var_0__ saat menikmati esensinya."

    scene h74 with dissolve

    jm "__Var_0__, apa maksudmu?"

    scene h74 with dissolve

    em "Tidak peduli, itu bukan urusan Anda, bajingan tua."

    scene h74 with dissolve

    jm "O-o-okay ... Anda tiba-tiba menjadi sedikit keras."

    scene h74 with dissolve

    em "Untuk seseorang yang menjilati vagina wanita yang sudah menikah, Anda secara mengejutkan sopan. Hah! Sekarang, sudah kembali ke bawah."

    scene h75 with dissolve

    em "Tapi tunggu ... sebelum Anda pergi, izinkan saya memberi Anda sedikit hadiah."

    scene h76 with dissolve

    em "Ambil ini. Itu semua milikmu. Saya tidak akan membutuhkannya lagi malam ini."

    scene h76 with dissolve

    jm "Apa kamu yakin?"

    scene h76 with dissolve

    em "Ya. Ambil saja."

    scene h76 with dissolve

    jm "Sampai jumpa di lantai bawah."

    scene h76 with dissolve

    em "Selamat tinggal…"

    scene h77 with dissolve

    em "Baiklah, __var_0__."

    scene h77 with dissolve

    em "Saya membiarkan Anda pergi sekarang. Turun dan mari bersenang -senang bersama."

    scene h78 with dissolve

    pause

    scene h47 with dissolve

    pause

    scene h79 with dissolve

    em "…aneh. Hah? Apa?"

    scene h79 with dissolve

    em "Rasanya seperti dingin lagi. Itu membuat menggigil di tulang belakang saya."

    scene h79 with dissolve

    em "Apa? Benar -benar ada dingin. Saya bisa merasakannya di bawah rok saya."

    scene h80 with dissolve

    em "Orang udik? Apa ... apa ini?!"

    scene h81 with dissolve

    em "Ya Tuhan, dimana celana dalamku?! Apa yang telah terjadi?!"

    scene h81 with dissolve

    em "Apakah saya ... tidak pernah memakainya? Saya ingat mengenakannya ketika saya meninggalkan rumah."

    scene h81 with dissolve

    em "Sial, sial, sial. Apakah saya kehilangan akal?"

    scene h80 with dissolve

    em "Apa basah ini?"

    scene h80 with dissolve

    em "Aku bersumpah aku tidak merasa seperti ini beberapa saat yang lalu."

    scene h80 with dissolve

    em "Ini sangat menakutkan. Saya tidak ingin sendirian lagi."

    scene h82 with fade

    emt "Jika saya tidak hati -hati, mereka mungkin melihat sesuatu yang seharusnya tidak mereka lakukan."

    scene h82 with dissolve

    emt "Saya perlu memberi tahu __var_0__ tentang hal aneh yang terjadi, tetapi tanpa terlalu menarik perhatian."

    scene h83 with dissolve

    em "Sayang"

    scene h83 with dissolve

    em "Apakah Anda bercanda?! Hei, bangun. Ayo, jangan tertidur di sini."

    scene h83 with dissolve

    aw "Semoga berhasil dengan itu, __var_0__. Dia kedinginan. Tebak anggur itu memukulnya lebih keras dari yang dia pikirkan."

    scene h84 with dissolve

    em "Tidak sekarang…."

    scene h85 with fade

    unk2 "Wakey, wakey, sayang ..."

    scene h86 with dissolve

    mc "Hah? Siapa—?"

    scene h88 with dissolve

    unk2 "Shh ... jangan berjuang. Anda belum bangun dari ini, belum."

    scene h89 with dissolve

    mc "Apa ...? Dimana saya? Siapa kamu?"

    scene h89 with dissolve

    mc "Beberapa saat yang lalu saya ... apa yang terjadi?"

    scene h89 with dissolve

    mc "Dimana __var_0__?"

    scene h88 with dissolve

    unk2 "Anda akan segera mengetahuinya. Katakan saja ... Saya di sini untuk bermain. Dan __var_0__ oh, dia bagian dari permainan sekarang."

    scene h90 with dissolve

    mc "Apa yang kamu?!"

    scene h90 with dissolve

    mc "Tinggalkan dia dari ini!"

    scene h88 with dissolve

    unk2 "Tapi di mana kesenangannya? Anda akan menjawab pertanyaan saya, sayang. Buatlah mereka dengan benar, dan mungkin - mungkin saja - saya akan menghindarinya."

    scene h88 with dissolve

    unk2 "Tapi setiap jawaban yang salah ... yah, katakan saja, __var_0__ tidak akan menikmatinya sebanyak yang saya mau."

    scene h91 with dissolve

    unk2 "Oh, mungkin dia juga akan ..."

    scene h91 with dissolve

    unk2 "Kalau begitu, mari kita mulai dengan pertanyaan pertama ... pertanyaan-pertanyaan pengujian hubungan ... mari kita lihat apakah Anda benar-benar suami yang baik."

    scene h91 with dissolve

    unk2 "Ini yang pertama. Apa anggur favorit __var_0 __?"

    menu:
        "Vino Rouge D’or":

            scene h92 with dissolve

            mc "VI-Vino Rouge d'Or?"

            scene h93 with dissolve

            unk2 "Ha ha ha. Anda berbohong kepada __var_0__, berpura -pura Anda adalah orang yang mendapatkan anggur, namun Anda bahkan tidak dapat mengingat namanya dengan benar."

            scene h93 with dissolve

            unk2 "Anda benar -benar suami yang mengerikan, dan untuk itu, kita harus menghukum __var_0__ tepat di depan mata Anda."

            scene h90 with dissolve

            mc "Kotoran. Apa yang akan kamu lakukan padanya?"

            scene h93 with dissolve

            unk2 "Saya tidak akan melakukan apapun. Duduk saja dan perhatikan."

            scene h94_5 with dissolve

            unk2 "Permainan di mana keadaan menjadi sedikit ... rumit.Ah, __var_0 __... Sepertinya Anda telah bergabung dengan pesta juga. Anda harus bingung, ya? Baiklah, izinkan saya mengisi Anda - ini semua adalah bagian dari permainan."

            scene h95 with dissolve

            pause 0.5

            scene h96 with dissolve

            em "Apa yang terjadi? Mengapa Anda di sini ... dan mengapa ini terjadi pada saya?"

            scene h94_5 with dissolve

            unk2 "Oh, __var_0 __... Anda telah menjadi bagian dari game ini sejak saat Anda memasuki rumah Andrew. Ini sedikit ujian, sedikit tantangan bagi suami Anda. Yang saya inginkan hanyalah melihat seberapa jauh dia akan melangkah, dan apakah dia akan lewat atau gagal."

            scene h97 with dissolve

            em "Game? Apa maksudmu? Game apa yang kamu bicarakan? Ini tidak menyenangkan, ini tidak benar—"

            scene h94_5 with dissolve

            unk2 "Oh, itu semua bagian yang menyenangkan, sayangku. Aturannya sederhana: suami Anda menjawab pertanyaan saya, dan setiap jawaban yang salah mengarah pada sesuatu ..."

            scene h94_5 with dissolve

            unk2 "tidak menyenangkan untukmu. Dan, tentu saja, setiap jawaban yang benar membuat Anda tetap aman ... tetapi tidak selalu."

            scene h98 with dissolve

            mc "Jangan khawatir, sayang. Saya akan mengeluarkan Anda dari ini. Aku akan menghentikannya, aku bersumpah."

            scene h99 with dissolve

            em "W-apa? Anda akan menghentikannya? Tapi bagaimana caranya? Kami terjebak di sini ..."

            scene h94_5 with dissolve

            unk2 "Dia mungkin mencoba menyelamatkan Anda, tetapi ingat, setiap kesalahan yang dia buat akan dikenakan biaya. Mari kita lihat apakah dia cukup kuat untuk menangani apa yang akan terjadi."

            scene h100 with dissolve

            unk2 "Ayo, __var_0 __... Mari kita bawa hukuman di sini."

            scene h101 with dissolve

            em "Apa yang terjadi. __Var_0__ Apa itu?"

            mc "Hentikan!"

            scene h102 with dissolve

            unk2 "Mari kita basah lebih dulu, kan? Melompat lurus mungkin bukan ide terbaik."

            scene black with dissolve

            pause(0.01)

            scene td with dissolve

            em "Saya tidak bisa menggerakkan tubuh saya. Ahh ..."

            em "Punggungnya menyakiti saya, dan sangat dingin."

            unk2 "Jangan khawatir. Anda akan menghangatkannya dengan panci madu Anda sedikit."

            unk2 "Jadi ... bagaimana pandangannya dari sana, __var_0__?"

            scene h90 with dissolve

            mc "Pergi ke neraka!"

            scene black with dissolve

            pause(0.01)

            scene td2 with dissolve

            unk2 "Ha ha ha. Saya sudah datang dari sana."

            unk2 "Karena Anda cukup basah, Anda siap mengambilnya."

            em "Ahhh…. Hhhh…."

            em "Berhenti!"

            unk2 "Saya tidak bisa membantu tetapi membuat Anda membayar hukuman Anda, maaf."

            mc "Kotoran!"

            em "Itu terlalu besar ... itu h ... sakit ..."

            scene h103 with dissolve

            unk2 "Saya pikir kita bisa beralih ke pertanyaan berikutnya sekarang…"

            scene h104 with dissolve

            unk2 "Mari kita pindahkan dia seperti ini sehingga Anda dapat melihat mainan seks kami lebih jelas."

            em "Hhhh…"

            mct "Dia benar -benar memegang __var_0__ seperti mainan seks plastik yang tak bernyawa."

            unk2 "Saya kira Anda menikmati pemandangan."

            unk2 "Maaf menarik Anda menjauh darinya, tetapi kami harus melanjutkan."
        "Vino Rouge D’Argent":


            scene h90 with dissolve

            mc "Tentu saja saya tahu ini. Vino Rouge D'Argent."

            scene h93 with dissolve

            unk2 "Yah ... Anda terlalu malas untuk membeli anggur favorit istri Anda, tetapi Anda masih tahu yang mana."

            unk2 "Meskipun Anda mendapatkan jawabannya dengan benar, karena penipuan kecil Anda, Anda masih layak mendapatkan hukuman kecil."

            scene h90 with dissolve

            mc "TIDAK! Saya melakukannya dengan benar. Tetap berpegang pada kata Anda."

            scene h94 with dissolve

            unk2 "Diam! Dan cobalah untuk tidak membuatku marah."

            scene h95 with dissolve

            unk2 "Permainan di mana keadaan menjadi sedikit ... rumit.Ah, __var_0 __... Sepertinya Anda telah bergabung dengan pesta juga. Anda harus bingung, ya? Baiklah, izinkan saya mengisi Anda - ini semua adalah bagian dari permainan."

            scene h96 with dissolve

            em "Apa yang terjadi? Mengapa Anda di sini ... dan mengapa ini terjadi pada saya?"

            scene h94_5 with dissolve

            unk2 "__Var_0 __... Anda telah menjadi bagian dari game ini sejak saat Anda memasuki rumah Andrew. Ini sedikit ujian, sedikit tantangan bagi suami Anda."

            unk2 "Yang saya inginkan hanyalah melihat seberapa jauh dia akan melangkah, dan apakah dia akan lewat atau gagal."

            scene h97 with dissolve

            em "Game? Apa maksudmu? Game apa yang kamu bicarakan? Ini tidak menyenangkan, ini tidak benar—"

            scene h94_5 with dissolve

            unk2 "Oh, itu semua bagian yang menyenangkan, sayangku. Aturannya sederhana: suami Anda menjawab pertanyaan saya, dan setiap jawaban yang salah mengarah pada sesuatu ..."

            unk2 "tidak menyenangkan untukmu. Dan, tentu saja, setiap jawaban yang benar membuat Anda tetap aman ... tetapi tidak selalu."

            scene h98 with dissolve

            mc "Jangan khawatir, sayang. Saya akan mengeluarkan Anda dari ini. Aku akan menghentikannya, aku bersumpah."

            scene h99 with dissolve

            em "W-apa? Anda akan menghentikannya? Tapi bagaimana caranya? Kami terjebak di sini ..."

            scene h94_5 with dissolve

            unk2 "Dia mungkin mencoba menyelamatkan Anda, tetapi ingat, setiap kesalahan yang dia buat akan dikenakan biaya. Mari kita lihat apakah dia cukup kuat untuk menangani apa yang akan terjadi."

            scene h93 with dissolve

            unk2 "Ayo, __var_0 __... Mari kita bawa pesulap yang menemukan anggur kita."

            scene h105 with dissolve

            unk2 "Ayo bawa James ke sini. Sebagai hasil dari jawaban yang baru saja Anda berikan, kami dapat mengatakan bahwa Anda mencegah masuknya sesuatu yang lebih tebal, tetapi tetap saja jari -jari James yang kotor dan tua harus mencicipi vagina istri Anda. Ayo James ..."

            mc "James! Membantu!"

            scene h106 with dissolve

            unk2 "Jangan repot -repot berjuang. James berada di bawah kendali saya sekarang - sama seperti yang lainnya di sini ... Anda semua adalah boneka kecil saya!"

            scene h107 with dissolve

            em "Itu tidak bisa!…"

            unk2 "Ah ... ya, Anda baik untuk mengingatkan saya pada kehadiran Anda."

            scene h108 with dissolve

            unk "Mari kita masuk ke posisi yang bagus dan nyaman. Apa yang kamu katakan?"

            scene h109 with dissolve

            em "Saya tidak bisa menggerakkan tubuh saya. __Var_0__ BANTUAN!"

            mc "Sialan! Saya juga tidak bisa bergerak."

            unk2 "Ayo, pesulap, mari kita lihat pertunjukan Anda."

            scene h110 with dissolve

            jm "Grrr…."

            em "__Var_0__, dia menyentuhku."

            mc "Saya tidak bisa melakukan apa pun! Kotoran!"

            mc "Seluruh tubuh saya lumpuh, kecuali satu bagian. Kenapa pemikiran tentang hal mengerikan ini menyentuh __var_0 __ bagian pribadi membuat saya hidup?"

            mc "Jauh di lubuk hati, saya tahu saya menikmati membayangkan __var_0__ dengan orang lain, tapi ... ini ..-"

            scene h111 with dissolve

            em "__Var_0__! Dia semakin dekat!"

            em "HHH ... James, bangun!"

            unk2 "Ha ha ha. Percayalah, Anda tidak ingin dia bangun sekarang. Jika Anda tahu hal -hal yang ingin dia lakukan untuk Anda, Anda tidak akan pernah mendekatinya lagi."

            em "__Var_0__, dia menyentuh ..."

            scene h112 with dissolve

            jm "Hmm..."

            em "Dapatkan tangan kotormu dari aku… ahhh!"

            scene h113 with dissolve

            mc "Wanita yang saya cintai ... dia akan diraba, dan saya tidak bisa melakukan apa -apa tentang itu!"

            scene h114 with dissolve

            em "Dia ... dia bergerak ..-"

            scene h113 with dissolve

            em "Jarinya di dalam vaginaku!"

            scene h114 with dissolve

            mc "Selesaikan hukuman ini! Silakan!"

            unk2 "Kami baru saja punya beberapa hal lagi yang harus dilakukan dengan James."

            scene h115 with dissolve

            jm "Ha ha ha…"

            scene h116 with dissolve

            em "*Orang udik*!!"

            scene h117 with dissolve

            em "Hhh ..."

            scene h118 with dissolve

            em "Ahh!"

            scene h120 with dissolve

            em "Dia mendorongnya ..."

            scene h119 with dissolve

            em "Sangat dalam ..!"

            scene h89 with dissolve

            mc "Apakah ini mimpi buruk?"

            scene h119 with dissolve

            em "Mmm…"

            scene h120 with dissolve

            pause

            scene h119 with dissolve

            em "Jika dia terus berjalan seperti ini…"

            scene h120 with dissolve

            em "Mmm ... saya tidak bisa bertahan."

            scene h119 with dissolve

            em "Mmm…"

            scene h120 with dissolve

            pause

            scene h119 with dissolve

            em "Hhhh…"

            scene h120 with dissolve

            em "Ahh ..."

            scene h94_5 with dissolve

            unk2 "Saya pikir kita bisa beralih ke pertanyaan berikutnya."

            unk2 "Nah ... hukuman Anda sudah cukup."

            scene h108 with dissolve

            unk2 "Anda bebas sekarang, James ... Anda bisa pergi."

    scene h91 with dissolve

    unk2 "Sekarang, mari kita beralih ke pertanyaan kedua dan terakhir."

    unk2 "Saya sarankan Anda menjawab ini dengan bijak. Kali ini jawaban yang salah yang Anda berikan mungkin tidak memiliki obat."



    menu:
        unk2 "Apakah pikiran seseorang mengacaukan istri Anda?"
        "Yes":

            scene h90 with dissolve

            mc "Ya! Sialan, ya. Saya menyukainya. Saya mengatakan yang sebenarnya, sekarang tinggalkan dia sendiri!"

            scene h121 with dissolve

            em "Sayang ... apakah kamu yakin?"

            scene h125 with dissolve

            mc "__Var_0__? Tapi kamu ... kamu bisa pindah ..."

            scene h122 with dissolve

            em "Ya. Saya bisa selama ini."

            scene h125 with dissolve

            mc "Maksudmu ... apakah semua yang baru saja terjadi pilihanmu sendiri? Apakah Anda Bertindak?"

            scene h123 with dissolve

            mc "Bagaimana ini mungkin? Matamu ... itu tidak bisa nyata."

            scene h122 with dissolve

            em "Bagaimana jika kita fokus untuk mewujudkan keinginan Anda?"

            scene h126 with dissolve

            mc "Saya ... Saya tidak yakin."

            scene h122 with dissolve

            em "Kami akan meluangkan waktu dan memastikan Anda menikmatinya, tetapi pada akhirnya, saya akan kacau oleh seseorang. Bersiaplah untuk itu."

            scene h127 with dissolve

            mc "O-Oke, cintaku."

            scene h124 with dissolve

            em "Apakah tidak apa -apa jika saya menginginkan Andrew?"

            mc "Oke..."

            scene h128 with dissolve

            aw "Hai sobat. Saya pikir seseorang membutuhkan saya."

            scene h129 with dissolve

            em "Selamat datang. Ya, saya benar -benar membutuhkan Anda, tetapi saya hanya akan melakukan ini sehingga keinginan __var_0 __ terpenuhi. Tahu ini."

            aw "Oke. Seperti yang Anda katakan ..."

            aw "Jadi, bisakah saya menggunakan kalian semua?"

            em "Saya tidak tahu, kita perlu mendapatkan izin __var_0 __."



            menu:
                em "Apa yang kamu katakan, sayang?"
                "Use Her Pussy":

                    scene h129 with dissolve

                    mc "Anda bisa menggunakan vaginanya."

                    scene h130 with dissolve

                    em "Apakah kamu yakin sayang?"

                    em "Sekarang?"

                    mc "Ya, saya tidak ingin menunggu lagi."

                    scene h134 with dissolve

                    em "Oh.."

                    mc "Apa yang telah terjadi?"

                    scene h132 with dissolve

                    em "Tidak ada yang hanya saya…"

                    scene h133 with dissolve

                    aw "Ya sobat… tidak ada yang terjadi…"

                    scene h132 with dissolve

                    em "*Berbisik*Bagaimana bisa sebesar ini? Rasanya seperti cabang pohon besar yang meluncur di antara pipiku.*Bisikan*"

                    scene h135 with dissolve

                    mc "Apa yang kamu katakan sayang?"

                    scene h132 with dissolve

                    pause

                    scene h133 with dissolve

                    pause

                    scene h136 with dissolve

                    em "Hhh… tidak ada sayang…"

                    scene h145 with dissolve

                    aw "Bung, saya harus berterima kasih karena telah berbagi istri Anda yang berharga dengan saya."

                    scene h132 with dissolve

                    pause

                    scene h133 with dissolve

                    pause

                    scene h145 with dissolve

                    em "Mmm…"

                    scene h146 with dissolve

                    mc "Apa yang kamu lakukan padanya?"

                    scene h146 with dissolve

                    aw "Aku..? Tidak ada ... hanya berkeliaran."

                    scene h146 with dissolve

                    aw "Ayo lakukan sesuatu dengan benar?"

                    scene h148 with dissolve

                    em "Apa? Sayang?"

                    scene h149 with fade:
                        subpixel True
                        yalign 0.0
                        pause 1.5
                        linear 7.0 yalign 1.0

                    mc "Apa? Apa? __Var_0__?"

                    scene h147 with dissolve

                    mc "Motherf…"

                    scene h147 with dissolve

                    aw "Bukankah saya berjanji kepada kalian itu akan menjadi pesta yang mengesankan?"

                    scene h147 with dissolve

                    em "Saya tidak bisa mengatakan saya tidak terkesan."

                    scene black with dissolve

                    pause(0.01)

                    scene hrub with dissolve

                    aw "Lalu mari kita geser sedikit di atasnya."

                    em "Ahhh ... sangat dekat dengan lubang."

                    em "__Var_0__, hampir masuk."

                    em "Sangat licin. Saya pikir itu akan meluncur."

                    aw "Bukankah sudah waktunya untuk memasukkannya?"

                    aw "Mari kita peregangan Anda sedikit."

                    scene h150 with dissolve

                    aw "Ini dia…"

                    scene h125 with dissolve

                    mc "Tidak, belum berhenti!"

                    mc "NOOOOOO!"

                    scene h154 with fade

                    mc "TOOO!"

                    scene h155 with dissolve

                    mc "Oh. Itu pasti mimpi buruk."

                    em "Apa yang terjadi, sayang? Anda membangunkan saya."

                    mc "Tidak ada apa-apa. Ini hanya mimpi buruk."

                    em "Oke. Selamat malam, sayang."

                    mc "Selamat malam, babygirl saya."

                    scene h156 with dissolve

                    em "HHH ... Sayang?"

                    mc "Ya."

                    em "Bagaimana kita pulang? Saya tidak ingat."

                    em "Dan saya merasakan sakit di antara kaki saya."

                    scene h154 with dissolve

                    mc "Kamu bilang apa!?"

                    scene h94 with fade

                    pause

                    scene inf2 with dissolve

                    pause
                "Use Her Mouth":


                    scene h129 with dissolve

                    mc "Anda bisa menggunakan mulutnya"

                    scene h131 with dissolve

                    em "Saya tidak tahu bagaimana itu akan pas di mulut saya, tetapi saya akan mencobanya, hanya untuk Anda."

                    aw "Jangan khawatir, saya yakin Anda bisa mengambil semuanya."

                    em "Kemudian…"

                    scene h137 with dissolve

                    em "Mmm…"

                    scene h138 with dissolve

                    em "* Muck* mmmm… tidak bisakah aku menciumnya?"

                    em "__Var_0__, sayang ... itu nyaris tidak cocok di tangan saya ... bagaimana saya bisa memasukkannya ke dalam mulut saya?"

                    mc "Wow __var_0__, tolong ... Saya ingin melihat Anda mencoba."

                    scene h139 with dissolve

                    em "Mmm ... muck"

                    em "Karena itulah yang Anda inginkan ..."

                    scene h142 with dissolve

                    em "Mmm…"

                    scene h141 with dissolve

                    em "** Gag ** Gag **"

                    scene h143 with dissolve

                    em "Sangat besar…"

                    em "__Var_0__, ini hampir dua kali ukuran Anda."

                    mct "Saya sudah sulit untuk sementara waktu sekarang. Saya akan merobek celanaku."

                    scene black with dissolve

                    pause(0.01)

                    scene hbj with dissolve

                    em "Mmmm… mmm…"

                    em "*Mencucup*"

                    mc "Sangat besar! Bagaimana dia bisa mengambil semuanya? Itu pasti di tenggorokannya."

                    aw "Mulut yang sangat ketat."

                    aw "Ambillah sepanjang jalan."

                    aw "Terima kasih telah mengizinkan saya menggunakan mulut istri Anda, __var_0__."

                    mc "Sayang, Anda bisa berhenti kapan saja Anda mau."

                    em "Mmm… mmm…"

                    mct "Cara dia melihat ke mata saya membuat saya begitu banyak."

                    aw "Saya pikir saya cumming!"

                    scene h151 with dissolve

                    em "Mmm ..."

                    aw "OPSS ..."

                    scene h152 with dissolve

                    em "Mmmwa…"

                    aw "Anda perlu menelan."

                    em "Hhh ... cwame ... di ... my ... mwouth ..."

                    scene h153 with dissolve

                    em "*Meneguk*"

                    em "Maaf, Sayang. Saya tidak sengaja menelan saat mencoba berbicara."

                    mc "Tapi ... tapi ... Anda belum pernah menelan milik saya sebelumnya."

                    em "Maaf, Sayang."

                    scene h89 with dissolve

                    mc "NOOOOOO!"

                    scene h154 with fade

                    mc "TOOO!"

                    scene h155 with dissolve

                    mc "Oh. Itu pasti mimpi buruk."

                    em "Apa yang terjadi, sayang? Anda membangunkan saya."

                    mc "Tidak ada apa-apa. Ini hanya mimpi buruk."

                    em "Oke. Selamat malam, sayang."

                    mc "Selamat malam, babygirl saya."

                    scene h156 with dissolve

                    em "HHH ... Sayang?"

                    mc "Ya."

                    em "Bagaimana kita pulang? Saya tidak ingat."

                    em "Dan saya merasakan sakit di antara kaki saya."

                    scene h154 with dissolve

                    mc "Kamu bilang apa!?"

                    scene h94 with fade

                    pause

                    scene inf2 with dissolve

                    pause
                "Use Both":


                    scene h129 with dissolve

                    mc "Anda dapat menggunakan bagian apa pun dari dirinya yang Anda inginkan."

                    scene h130 with dissolve

                    em "Apakah kamu yakin, sayang?"

                    em "Apakah dia memiliki izin untuk menggunakan semuanya?"

                    mc "Ya. Saya memberikan izin."

                    em "Sekarang?"

                    mc "Ya, saya tidak ingin menunggu lagi."

                    em "Saya tidak bisa menerimanya sekarang, jadi saya harus membasahi terlebih dahulu."

                    mc "Hmm..."

                    aw "Saya menyukai ide itu."

                    scene h137 with fade

                    em "Mmm…"

                    scene h138 with dissolve

                    em "* Muck* mmmm… tidak bisakah aku menciumnya?"

                    em "__Var_0__, sayang ... itu nyaris tidak cocok di tangan saya ... bagaimana saya bisa memasukkannya ke dalam mulut saya?"

                    mc "Wow __var_0__, tolong ... Saya ingin melihat Anda mencoba."

                    scene h139 with dissolve

                    em "Mmm ... muck"

                    em "Karena itulah yang Anda inginkan ..."

                    scene h142 with dissolve

                    em "Mmm…"

                    scene h141 with dissolve

                    em "** Gag ** Gag **"

                    scene h143 with dissolve

                    em "Sangat besar…"

                    em "__Var_0__, ini hampir dua kali ukuran Anda."

                    mct "Saya sudah sulit untuk sementara waktu sekarang. Saya akan merobek celanaku."

                    scene black with dissolve

                    pause(0.01)

                    scene hbj with dissolve

                    em "Mmmm… mmm…"

                    em "*Mencucup*"

                    mc "Sangat besar! Bagaimana dia bisa mengambil semuanya? Itu pasti di tenggorokannya."

                    aw "Mulut yang sangat ketat."

                    aw "Ambillah sepanjang jalan."

                    aw "Terima kasih telah mengizinkan saya menggunakan mulut istri Anda, __var_0__."

                    mc "Sayang, Anda bisa berhenti kapan saja Anda mau."

                    em "Mmm… mmm…"

                    mct "Cara dia melihat ke mata saya membuat saya begitu banyak."

                    scene h143 with dissolve

                    em "Cukup licin sekarang."

                    scene h134 with dissolve

                    em "Oh.."

                    scene h132 with dissolve

                    em "Aku hanya…"

                    scene h133 with dissolve

                    aw "Apakah Anda merasa __var_0__?"

                    scene h132 with dissolve

                    em "*Berbisik*Bagaimana bisa sebesar ini? Rasanya seperti cabang pohon besar yang meluncur di antara pipiku.*Bisikan*"

                    scene h135 with dissolve

                    mc "Apa yang kamu katakan, sayang?"

                    scene h136 with dissolve

                    em "Hhh… tidak ada, sayang…"

                    scene h145 with dissolve

                    aw "Bung, saya harus berterima kasih karena telah berbagi istri Anda yang berharga dengan saya."

                    scene h132 with dissolve

                    pause

                    scene h133 with dissolve

                    pause

                    scene h145 with dissolve

                    em "Mmm… sayang, aku ingin ..."

                    scene h146 with dissolve

                    em "Andrew menggosok pinggulku, dan aku ..."

                    mc "Apakah kamu menyukainya?"

                    scene h146 with dissolve

                    aw "Ya, dia menyukainya."

                    scene h146 with dissolve

                    aw "Jadi ... mari kita lakukan sesuatu, kan?"

                    scene h148 with dissolve

                    em "Apa? Sayang?"

                    scene h149 with fade:
                        subpixel True
                        yalign 0.0
                        pause 1.5
                        linear 7.0 yalign 1.0

                    mc "Apa? Apa? __Var_0__?"

                    scene h147 with dissolve

                    mc "Motherf…"

                    scene h147 with dissolve

                    aw "Bukankah saya berjanji kepada kalian itu akan menjadi pesta yang mengesankan?"

                    scene h147 with dissolve

                    em "Saya tidak bisa mengatakan saya tidak terkesan."

                    scene black with dissolve

                    pause(0.01)

                    scene hrub with dissolve

                    aw "Lalu mari kita geser sedikit di atasnya."

                    em "Ahhh ... sangat dekat dengan lubang."

                    em "__Var_0__, hampir masuk."

                    em "Sangat licin. Saya pikir itu akan meluncur."

                    aw "Bukankah sudah waktunya untuk memasukkannya?"

                    aw "Mari kita peregangan Anda sedikit."

                    scene h150 with dissolve

                    aw "Ini dia…"

                    scene h125 with dissolve

                    mc "Tidak, saya belum siap untuk melakukan ini, berhenti!"

                    scene h154 with fade

                    mc "TOOO!"

                    scene h155 with dissolve

                    mc "Oh. Itu pasti mimpi buruk."

                    em "Apa yang terjadi, sayang? Anda membangunkan saya."

                    mc "Tidak ada apa-apa. Ini hanya mimpi buruk."

                    em "Oke. Selamat malam, sayang."

                    mc "Selamat malam, babygirl saya."

                    scene h156 with dissolve

                    em "HHH ... Sayang?"

                    mc "Ya."

                    em "Bagaimana kita pulang? Saya tidak ingat."

                    em "Dan saya merasakan sakit di antara kaki saya."

                    scene h154 with dissolve

                    mc "Kamu bilang apa!?"

                    scene h94 with fade

                    pause

                    scene inf2 with dissolve

                    pause
        "No":




            scene h157 with fade

            mc "TOOO!"

            scene h158 with dissolve

            mc "Oh. Itu pasti mimpi buruk."

            scene h159 with dissolve

            mc "Hai. Dimana __var_0__?"

            scene h91 with fade

            unk2 "Sekarang, mari kita beralih ke pertanyaan kedua dan terakhir."

            unk2 "Saya sarankan Anda menjawab ini dengan bijak. Kali ini jawaban yang salah yang Anda berikan mungkin tidak memiliki obat."

            scene h157 with dissolve

            mc "TOOO!"

            scene h94 with fade

            pause

            scene inf2 with dissolve

            pause



    jump return_main_menu

label return_main_menu:

    $ disable_saving = False

    return

label expose:

    scene vt1 with dissolve

    em "Mmm ..."

    mct "Dia sangat menyukainya, dia bahkan tidak mendengar saya masuk. Dia terlihat sangat terangsang."

    scene vt2 with dissolve

    mct "Haruskah saya meninggalkannya sendirian, atau haruskah saya bergabung?"

    scene vt3 with dissolve

    mct "Saya bahkan tidak tahu harus berpikir apa."

    menu:
        "Keep Watching":

            scene vt4 with dissolve

            mct "Saya seharusnya tidak menonton ini ... tapi saya tidak bisa mengalihkan pandangan darinya."

            mct "Dia terlihat sangat cantik seperti ini ... sangat rentan, begitu tersesat dalam dirinya."

            scene vt3 with dissolve

            mct "Apa artinya ini bagi kita? Untuk saya? Ya Tuhan, aku seharusnya tidak merasakan hal ini dihidupkan, haruskah aku?"

            scene vt11 with dissolve

            mct "Saya diam -diam mengawasi istri saya dan menyentuh diri saya sendiri."

            scene vt13_5 with dissolve

            mct "Bagaimana kita sampai pada titik ini?"

            mct "Apakah saya benar -benar kehilangan nafsu?"

            scene vt12 with dissolve

            pause 

            scene vt13 with dissolve

            em "Hah?"

            scene vt17 with dissolve

            em "Astaga! Apa yang kamu lakukan?!"

            scene vt18 with dissolve

            mc "__Var_0__, i - uh—"

            scene vt19 with dissolve

            em "Apakah Anda hanya berdiri di sana ... mengawasi saya?!"

            em "Dan apa itu? Apakah Anda ... menyentuh diri sendiri?!"

            scene vt20 with dissolve

            mc "__Var_0__, saya— Saya tidak bisa menahannya ... Anda hanya ..."

            scene vt21 with dissolve

            em "Astaga! Ada apa denganmu?!"

            scene vt22 with dissolve

            emt "Saya tidak percaya ini sedang terjadi! Tapi ... mungkin alasan saya sangat marah bukan hanya karena dia mengawasi saya ... itu karena Andrew. Apa yang kami lakukan…"

            emt "Itu membuat saya merasa sangat bersalah dan begitu ... dinyalakan pada saat yang sama. Ya Tuhan, apa yang salah denganku? Mungkin berteriak padanya adalah satu -satunya cara saya bisa mengatasi rasa malu ini."

            scene vt23 with dissolve

            mct "Saya tahu saya seharusnya tidak menonton ... tetapi melihatnya seperti itu, saya tidak bisa berhenti. Ya Tuhan, aku telah mengacaukan banyak waktu."

            mc "Sayang, __var_0__ ... Maaf. Saya seharusnya tidak ... melakukan itu. Itu salah, dan saya melewati batas. Saya tidak berpikir."

            scene vt24 with dissolve

            em "Anda benar, Anda melewati garis!"

            scene vt25 with dissolve

            emt "Saya berteriak padanya, tapi ... apakah benar -benar dia marah? Atau apakah itu saya? Semuanya terasa di luar kendali sejak Andrew. Dan sekarang ini ... tapi mungkin saya melangkah terlalu jauh."

            scene vt26 with dissolve

            em "Saya ... maaf juga. Saya seharusnya tidak berteriak seperti itu. Semua ini hanya ... sangat luar biasa."

            scene vt27 with dissolve

            mc "Tidak, Anda benar untuk marah. Saya menginvasi privasi Anda, dan saya seharusnya tidak melakukannya. Itu salahku."

            em "Mungkin ... tapi saya juga tidak bersalah di sini. Ada begitu banyak rasa bersalah yang saya bawa akhir -akhir ini, dan itu hanya ... sulit untuk ditangani."

            scene vt28 with dissolve

            mc "Mungkin kita bisa ... membicarakannya? Bersama? Aku benci melihatmu seperti ini, dan aku tidak ingin memperburuk keadaan."

            scene vt29 with dissolve

            em "Ya ... mungkin kita harus melakukannya. Kami tidak bisa terus seperti ini. Itu tidak baik untuk kita berdua."

            scene vt28 with dissolve

            mc "Saya hanya ingin kita mencari tahu ini, __var_0__. Aku mencintaimu, apa pun yang terjadi."

            scene vt30 with dissolve

            em "Aku pun mencintaimu. Bahkan jika Anda kadang -kadang idiot."

            scene vt31 with dissolve

            mc "Anda tahu ... mungkin sudah saatnya kita berbicara dengan seseorang tentang semua ini. Saya tidak ingin terus mendorong semuanya."

            mc "Kami telah melalui banyak hal, dan mungkin kami bisa menggunakan bantuan untuk memahaminya."

            scene vt32 with dissolve

            em "Seorang terapis? Apakah kamu serius?"

            scene vt33 with dissolve

            mc "Saya tidak tahu ... Saya pikir itu bisa membantu kami. Maksud saya, semua yang kami hadapi - saya, Anda, Andrew ... ada begitu banyak hal yang terjadi."

            mc "Mungkin kita membutuhkan seseorang untuk membimbing kita melalui ini."

            scene vt34 with dissolve

            em "Saya kira ... tidak ada salahnya. Saya merasa sangat tersesat akhir -akhir ini. Tapi ... bagaimana jika itu membuat semuanya lebih buruk? Dan saya tidak tahu, saya merasa seperti saya berubah. Saya bahkan tidak mengenali diri saya lagi."

            scene vt33 with dissolve

            mc "Saya mengerti. Tapi itulah sebabnya kami membutuhkan bantuan. Kami tidak dapat melakukan ini sendirian, dan kami tidak perlu melakukannya."

            scene vt35 with dissolve

            em "Ya, saya sudah lama menahan semua ini, dan saya hanya ... Saya tidak tahu siapa saya. Ini menakutkan."

            scene vt36 with dissolve

            mc "Saya di sini untuk Anda.Saya mengerti, __var_0__. Tapi apa pun yang terjadi, kita akan melewatinya bersama. Kami akan mengetahuinya."

            scene vt35 with dissolve

            em "Oke… Aku percaya padamu. Ayo coba. Mari kita bicara dengan seseorang."

            scene vt36 with dissolve

            mc "Kemudian saya akan memesan janji dengan terapis yang telah diatur pemerintah untuk Anda sesegera mungkin."

            scene vt37 with dissolve

            em "Oke."
        "Interrupt Her":


            scene vt4 with dissolve

            mc "__Var_0__?"

            scene vt5 with dissolve

            pause

            scene vt6 with dissolve

            mc "Apa yang sedang kamu lakukan?"

            scene vt17 with dissolve

            em "Astaga! Saya tidak berpikir Anda akan segera kembali!"

            scene vt18 with dissolve

            mc "Ya, saya baru saja menurunkan telepon Andrew dan langsung pulang. Tapi ... um, saya kira saya mengganggu sesuatu."

            scene vt20_b with dissolve

            em "TIDAK! Maksudku ... ya ... Maksudku ... Ya Tuhan, ini sangat memalukan!"

            scene vt21_b with dissolve

            mc "Hei, hei, tidak apa -apa. Benar-benar. Kita semua memiliki kebutuhan, Anda tahu? Tidak ada yang perlu malu."

            scene vt20 with dissolve

            em "Tapi ini ... ini terasa berbeda. Rasanya ... entah bagaimana salah. Setelah Andrew, saya ... saya seharusnya tidak merasa seperti ini."

            scene vt25 with dissolve

            mc "Lihat, __var_0__, mungkin kita perlu membicarakan hal ini. Perasaan yang Anda alami ini, rasa bersalah ini ... memakan Anda, dan saya benci melihatnya."

            scene vt26 with dissolve

            em "Apakah saya ... apakah saya beralih ke orang lain atau ... ya ampun! Saya orang yang mengerikan. Kenapa kamu begitu baik padaku?"

            scene vt28 with dissolve

            mc "Tidak, tidak, jangan berpikir seperti itu. Anda tidak mengerikan. Sesuatu terjadi dengan kami, dan mungkin ... mungkin kami membutuhkan seseorang untuk membantu kami mengetahuinya. Bersama."

            scene vt29 with dissolve

            em "Apakah Anda mengatakan ... seorang terapis?"

            scene vt28 with dissolve

            mc "Ya. Merasa bersalah itu alami, tetapi kita tidak boleh membiarkannya mengambil alih. Dan jujur saja ... Saya mencoba mencari tahu perasaan saya sendiri juga. Situasi ini ... itu memengaruhi saya dengan cara yang tidak saya harapkan."

            scene vt29 with dissolve

            em "Apa maksudmu? Apakah Anda mengatakan bahwa apa yang terjadi dengan Andrew dan saya tidak ... mengganggu Anda?"

            scene vt29_b with dissolve

            mct "Permainan kecil yang dia mainkan dengan Theo, cara dia membawa Andrew ke mulutnya - hanya memikirkannya membuat saya keras."

            mct "Saya tidak bisa mengakuinya sekarang, tetapi mungkin seorang terapis dapat membantu saya mengetahui mengapa ini membuat saya begitu banyak."

            scene vt28 with dissolve

            mc "Saya tidak akan mengatakan itu tidak mengganggu saya. Tetapi pada saat yang sama ... sepertinya memengaruhi saya dengan cara yang berbeda. Hampir seperti ... Saya tidak tahu, seperti saya baik -baik saja dengan itu. Mungkin bahkan ... saya tidak tahu ..."

            scene vt32 with dissolve

            em "Apakah kamu serius?"

            scene vt33 with dissolve

            mc "Kami berdua.Ya, saya pikir begitu. Tapi itu sesuatu yang perlu saya pikirkan juga. Itu sebabnya saya pikir melihat seseorang dapat membantu kami."

            scene vt29 with dissolve

            em "Oke. Mungkin Anda benar. Layak dicoba."

            scene vt28 with dissolve

            mc "Kami akan melewati ini. Bersama. Saya berjanji."

            scene vt30 with dissolve

            em "Oke sayang, aku percaya padamu."

            scene vt31 with dissolve

            mc "Kemudian saya akan memesan janji dengan terapis yang telah diatur pemerintah untuk Anda sesegera mungkin."

            scene vt30 with dissolve

            em "Oke."

    scene vt38 with dissolve

    em "Saya tidak tahu mengapa, tetapi tiba -tiba saya sangat gugup."

    scene vt39 with dissolve

    mc "Benar-benar? Anda tampak baik -baik saja di sini."

    scene vt40 with dissolve

    em "Saya, tapi sekarang ... gagasan duduk di sana, membuka diri kepada beberapa pria yang bahkan tidak saya ketahui, rasanya begitu ... mengintimidasi."

    scene vt41 with dissolve

    mc "Hei, dia bukan hanya ‘seorang pria.’ Dia seorang profesional, __var_0__. Ini adalah keseluruhannya - membantu orang merasa lebih baik."

    scene vt42 with dissolve

    em "Saya tahu, tapi ... lebih dari itu. Terkadang saya merasa seperti saya bahkan tidak perlu membutuhkan ini. Seperti, dari semua orang, saya harus bisa menanganinya."

    em "Maksud saya, saya salah satu dari sedikit wanita yang tersisa di dunia yang tidak terpengaruh oleh virus itu. Dan alih -alih merasa ... spesial atau bersyukur, saya merasa tersesat. Seperti saya gagal."

    scene vt43 with dissolve

    mc "__Var_0__, Anda tidak gagal. Tidak ada yang mengharapkan Anda membawa beban dunia hanya karena ini. Anda manusia, dan tidak apa -apa membutuhkan bantuan."

    scene vt44 with dissolve

    em "Sulit untuk dijelaskan. Saya merasa seperti saya tidak hanya mengecewakan diri saya tetapi juga ... semua orang juga."

    scene vt45 with dissolve

    mc "Anda tidak mengecewakan siapa pun. Anda di sini, Anda mencoba, dan itu lebih dari yang akan dilakukan kebanyakan orang. Anda diizinkan mengalami hari -hari yang buruk."

    mc "Itu tidak membuat Anda lemah, __var_0__. Itu membuatmu manusia."

    scene vt44 with dissolve

    em "Saya kira itu sebabnya saya di sini, kan? Untuk mencari tahu semua ini."

    scene vt45 with dissolve

    mc "Tepat. Dan lihat, Anda tidak sendirian dalam hal ini. Saya akan berada di sini, setiap langkah."

    scene vt44 with dissolve

    em "Anda benar -benar pandai dalam hal pembicaraan ini, Anda tahu itu?"

    scene vt45 with dissolve

    mc "Itu hadiah. Sekarang, mari kita masuk ke sana sebelum Anda memutuskan untuk mengikat. Kami mendapatkan ini."

    scene vt46 with dissolve

    em "Baiklah. Tetapi jika ini berjalan mengerikan, Anda berutang makan malam kepada saya ... hidangan penutup .... pijat punggung…. dan membersihkan rumah dan…"

    scene vt47 with dissolve

    mc "Wow, Anda benar -benar menaikkan taruhannya di sini. Apa selanjutnya? Mencuci mobil Anda juga?"

    scene vt48 with dissolve

    em "Sebenarnya, itu bukan ide yang buruk."

    scene vt49 with dissolve

    mc "Jangan mendorongnya."

    scene vt50 with dissolve

    em "Hei, saya hanya mengatakan, motivasi itu penting."

    scene vt51 with dissolve

    mc "Baik, tetapi hanya jika Anda selamat dari sesi tanpa kehabisan pintu berteriak."

    scene vt52 with dissolve

    em "Kesepakatan adalah kesepakatan. Tapi jangan berpikir saya tidak akan menahan Anda untuk semua itu."

    scene vt53 with dissolve

    mc "Dicatat. Sekarang, mari kita pergi sebelum daftar ini menjadi lebih lama."

    scene vt54 with fade

    psy "Selamat datang, tolong, duduklah. Saya senang Anda berdua bisa membuatnya hari ini."

    psy "Mari kita mulai dengan perkenalan. Saya Dr. Matt Wise, dan saya di sini untuk membantu dengan tantangan apa pun yang mungkin Anda hadapi."

    psy "Saya harus mengatakan, tidak setiap hari saya bisa bertemu seseorang seperti Anda, __var_0__. Anda benar -benar salah satu yang langka. Suatu kehormatan untuk memiliki Anda di sini."

    scene vt55 with dissolve

    psy "Ini adalah ruang yang aman, jadi jangan ragu untuk mengekspresikan apa pun yang ada di pikiran Anda."

    scene vt56 with dissolve

    mc "Kami telah melalui beberapa hal akhir -akhir ini ... sulit untuk dijelaskan, tetapi itu ... itu memengaruhi hubungan kami."

    scene vt57 with dissolve

    psy "Tidak apa -apa. Hubungan bisa menjadi rumit. Jenis tantangan apa yang Anda hadapi?"

    scene vt58 with dissolve

    em "Ya, itu ... Saya merasa banyak kesalahan dan kebingungan, terutama dengan semua yang terjadi."

    em "Sepertinya saya terpecah antara apa yang saya rasakan dan apa yang diharapkan dari saya."

    em "Dan saya kira, kami di sini karena kami tidak tahu bagaimana menghadapi semua ini. Itu ... itu mengacaukan kedua kepala kita."

    scene vt59 with dissolve

    mc "Ya, maksud saya, itu hanya ... Saya juga mencoba memahami perasaan saya sendiri. Ini banyak tekanan, dan saya tidak ingin hal -hal menjadi lebih buruk di antara kami."

    mc "Kami datang karena ... Saya pikir kami perlu bantuan menavigasi ini, Anda tahu?"

    scene vt57 with dissolve

    psy "Ada baiknya Anda berdua di sini bersama. Hubungan bisa melalui tempat -tempat sulit,"

    psy "Tetapi dengan alat dan pemahaman yang tepat, banyak hal dapat dilakukan. Saya di sini untuk membimbing Anda melalui itu."

    psy "Sebelum kita melanjutkan, saya perlu menjalankan tes cepat dengan __var_0__ untuk lebih memahami kebingungan yang Anda berdua hadapi."

    scene vt60 with dissolve

    mc "Tunggu, apa? Saya? Anda melakukan tes pada saya? Saya pikir kami ada di sini __var_0 __..."

    scene vt61 with dissolve

    psy "Ya, tentu saja. Tetapi untuk memahami semuanya sepenuhnya, penting untuk memulai dengan berfokus pada Anda."

    psy "Ini adalah bagian dari proses untuk melihat bagaimana perasaan Anda berdua secara individual."

    scene vt62 with dissolve

    mc "Baiklah, oke ... kurasa itu masuk akal."

    scene vt63 with dissolve

    psy "Kami akan sampai pada Anda berdua, jangan khawatir. Tapi pertama -tama, memahami dari mana Anda berasal, sangat penting. Kami akan mengambil satu langkah pada satu waktu."

    scene vt64 with dissolve

    em "Sepertinya dia mulai denganmu, sayang."

    scene vt63 with dissolve


    menu:
        psy "Katakanlah Anda seorang petani, dan benih tahun ini tidak menghasilkan hasil yang Anda harapkan. Bagaimana Anda mendekati situasi ini?"
        "Look better seeds":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Saya akan mencari biji berkualitas lebih baik dan mencoba lagi."
        "Leave the field empty":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "Saya akan meninggalkan musim kosong dan menunggu yang lebih beruntung tahun depan."

    scene vt66 with dissolve

    psy "Hmm..."

    scene vt63 with dissolve


    menu:
        psy "Anda akan melakukan perjalanan dengan seseorang di sisi Anda, dan tiba -tiba, orang lain bergabung dengan Anda. Bagaimana perasaan Anda pada saat itu?"
        "Feel excited":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Saya merasa bersemangat, seperti awal yang baru dengan teman baru."
        "Feel uneasy":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "Saya merasa tidak nyaman, karena kehadiran orang lain mengganggu keseimbangan."

    scene vt66 with dissolve

    psy "Jadi begitu..."

    scene vt63 with dissolve


    menu:
        psy "Di taman, dua bunga tumbuh berdampingan. Ketika Anda melihat bahwa yang satu sedikit lebih besar dan lebih menarik perhatian daripada yang lain, bagaimana perasaan Anda?"
        "It feels balanced":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Rasanya seperti keseimbangan alami, dan saya merasakan bahwa mereka saling melengkapi."
        "My focus shifts":


            $ ntr_point += 1

            mc "Fokus saya terganggu, dan saya merasa tidak nyaman."

    scene vt66 with dissolve

    psy "Menarik ... Anda hampir menyelesaikan tes, hanya beberapa pertanyaan lagi."

    scene vt63 with dissolve

    psy "Ketika Anda masih kecil, apakah Anda pernah berharap saudara kandung?"

    scene vt65 with dissolve

    mc "Apa hubungannya ini dengan sesuatu? Saya tidak mendapatkan koneksi."

    scene vt67 with dissolve

    psy "Tolong, jawab saja sejujur mungkin. Ini adalah bidang profesional saya, dan saya tidak akan mengomentari interpretasi hasil dulu."

    scene vt60 with dissolve

    mc "Maaf, Anda benar. Mari kita lanjutkan."

    scene vt63 with dissolve


    menu:
        psy "Bukan masalah! Lalu ... ketika Anda masih kecil, apakah Anda pernah berharap Anda memiliki saudara kandung?"
        "Yes":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Saya selalu menginginkan saudara kandung."
        "No":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "Tidak, saya selalu ingin menjadi anak tunggal."

    scene vt66 with dissolve

    psy "Hmm..."

    scene vt63 with dissolve


    menu:
        psy "Apakah Anda orang kucing atau anjing?"
        "Dog":

            $ nts_point += 1

            scene vt65 with dissolve

            mc "Saya orang anjing. Saya suka kesetiaan dan persahabatan."
        "Cat":


            $ ntr_point += 1

            scene vt65 with dissolve

            mc "Saya orang kucing. Saya menikmati kemerdekaan dan misteri."

    scene vt66 with dissolve

    psy "Hmm ... mencatat."

    psy "Pertanyaan dilakukan."

    scene vt63 with dissolve

    psy "Terima kasih telah menjawab. Sekarang, kami akan terus sendirian dengan __var_0__ sebentar. Anda bisa menunggu di luar."

    scene vt68 with dissolve

    mc "Terima kasih, Dok. Aku akan menunggumu tepat di luar pintu, sayang."

    scene vt64 with dissolve

    em "Oke, sayang."

    scene vt63 with dissolve

    psy "Ya ... Sekarang kita sendirian ... apa yang membawamu ke sini hari ini __var_0__? Tolong beritahu saya perasaan dan pikiran Anda, dalam semua ketelanjangannya."

    scene vt70 with dissolve

    em "Dimana saya harus memulai?"

    em "Pertama, izinkan saya memberi tahu Anda tentang apa yang telah kami lalui sejauh ini."

    scene vt71 with dissolve

    pause (1.0)

    scene vt72 with dissolve

    pause (1.0)

    scene vt73 with dissolve

    pause (0.5)

    scene vt75 with dissolve

    pause 

    scene vt76 with dissolve

    pause 

    scene vt75_5 with dissolve

    pause

    scene vt77 with dissolve

    pause

    scene vt75 with dissolve

    pause

    scene vt76 with dissolve

    pause

    scene vt74 with dissolve

    em "Juga, Andrew benar -benar lebih tebal dan lebih panjang dari lengan saya."

    em "Saya bahkan tidak tahu bagaimana itu cocok di mulut saya. Saya bisa merasakannya mengisi tenggorokan saya dan ini tidak membuat saya jijik sama sekali."

    scene vt70 with dissolve

    em "Biasanya, saya tidak akan melakukan ini dengan __var_0__. Saya akan jijik, tetapi pada saat itu, membawa Andrew di mulut saya benar -benar membangkitkan saya."

    em "Saya merasakan emosi yang begitu campur aduk. Jika saya membiarkan diri saya pergi, rasanya seperti orang yang mengerikan akan keluar. Saya tidak ingin __var_0__ menjadi kesal, tetapi apa yang saya alami menggairahkan saya."

    em "Di sisi lain, saya suka __var_0__, dan entah bagaimana hal -hal ini tidak terasa benar. Saya tidak tahu bagaimana menjelaskannya. Sulit dikatakan."

    em "Saya tahu saya sangat mencintainya ... Saya khawatir itu akan membahayakan hubungan kita."

    scene vt73 with dissolve

    em "Maaf, saya pikir saya berbicara sedikit terlalu terbuka."

    scene vt76 with dissolve

    psy "Tidak, tidak. Yang saya inginkan di sini adalah persis ini - menjadi transparan dengan saya. Jika Anda bisa transparan dengan saya, Anda mungkin juga mendengar suara yang Anda coba hening di dalam."

    psy "Saya mengerti bahwa Anda saat ini terjebak antara ID dan superego Anda."

    psy "Sederhananya, kepribadian Anda terdiri dari tiga bagian: ID, ego, dan superego."

    psy "Saat ini, Anda berfungsi melalui ego Anda, tetapi superego Anda menekan ID Anda, khususnya keinginan seksual Anda."

    psy "Ini menciptakan perasaan macet. Semakin Anda menekan, semakin kuat kesalahan Anda. Ini bisa menjadi alasan untuk ledakan Anda."

    psy "Anda perlu membiarkan diri Anda kebebasan - terhubung dengan ID Anda lagi. Hancurkan tabu. Dengan melakukannya, Anda akan menemukan keseimbangan."

    scene vt72 with dissolve

    em "Itu masuk akal ... tapi itu sulit. Saya selalu diajarkan untuk menjaga semuanya tetap terkendali."

    em "Rasanya jika saya melepaskannya, segalanya bisa lepas kendali. Saya tidak tahu apakah saya bisa mempercayai diri sendiri untuk melepaskannya."

    scene vt76 with dissolve

    psy "Dapat dimengerti bahwa Anda ragu -ragu. Proses membebaskan diri dari apa yang telah diajarkan kepada Anda bisa luar biasa, tetapi ini merupakan langkah yang diperlukan untuk menemukan kedamaian pribadi."

    psy "Ini bukan tentang meninggalkan kontrol, tetapi tentang menemukan keseimbangan yang lebih sehat. Apakah Anda pikir Anda mungkin siap untuk menjelajahi ini?"

    scene vt70 with dissolve

    em "Saya akan mencoba."

    scene vt77 with dissolve

    psy "Sesi kami hampir berakhir, tetapi sebelum Anda pergi, mari kita berlatih cepat."

    scene vt70 with dissolve

    em "Oke."

    scene vt76 with dissolve

    psy "Sekarang, dengan teknik ini, mari kita keluarkan energi psikis Anda."

    scene vt75 with dissolve

    em "Apa yang perlu saya lakukan?"

    scene vt76 with dissolve

    psy "Sekarang bangun, pergi ke belakang sofa, peluk diri Anda seperti ini dengan tangan Anda, dan tutup mata Anda."

    scene vt78 with dissolve

    em "Seperti ini? Haruskah saya memeluk diri saya seperti ini?"

    scene vt77 with dissolve

    psy "Tidak, tidak seperti itu. Biarkan saya membantu Anda sampai Anda terbiasa."

    scene vt79 with dissolve

    psy "Angkat lengan Anda, dan saya akan membimbing Anda - pikirkan saya sebagai lengan Anda untuk saat ini."

    em "Oke, dokter bijaksana."

    psy "Di sana, begitu saja. Santai, ambil napas dalam -dalam, dan ..."

    scene vt79_5 with dissolve

    psy "Rasakan pergeseran energi di dalam diri Anda. Lepaskan ketegangan apa pun - trust prosesnya."

    scene vt80 with dissolve

    em "Uh ... apakah kamu yakin begitulah seharusnya dilakukan?"

    scene vt81 with dissolve

    psy "Sangat. Percayalah kepadaku. Teknik ini sangat efektif jika dilakukan dengan benar. Fokus saja pada pernapasan Anda dan biarkan diri Anda merasakan rilis."

    scene vt82 with dissolve

    em "Saya ... Saya tidak tahu apakah ini terasa benar. Apakah Anda yakin ini adalah bagian dari teknik ini?"

    scene vt83 with dissolve

    psy "Anda datang ke sini untuk bantuan saya, dan ini adalah teknik yang dirancang untuk melepaskan energi dalam jiwa Anda."

    psy "Jika saya tidak terlalu terampil dalam pekerjaan saya, negara bagian tidak akan mempercayakan saya bekerja dengan seseorang seperti Anda."

    psy "Tolong, ambil napas dalam -dalam dan bayangkan energi Anda mengalir keluar dari tubuh Anda saat saya membimbingnya dengan sentuhan saya."

    em "Hhh…"

    scene vt84 with dissolve

    psy "Aku bisa merasakan keringat di dada dan jantungmu berdetak lebih cepat. Apakah teknik saya membuat Anda bersemangat?"

    em "Apa? Menyenangkan saya? Tidak, itu hanya ... rasanya ruangan menjadi sedikit lebih hangat, itu saja."

    scene vt83 with dissolve

    psy "Oh, begitu. Nah, sesi kami hampir berakhir. Sekarang, untuk latihan terakhir ..."

    psy "Saya ingin Anda menutup mata lagi dan membayangkan ini: semua hal menahan Anda, merantai Anda ..."

    psy "Dan membuat Anda terkendali tersedot melalui puting Anda dan mengalir ke luar."

    emt "Apakah itu berbisik di telingaku? I-i fe -..."

    scene vt79 with dissolve

    psy "Bagus. Sekarang, ambil napas dalam -dalam dan rasakan energi di dalam diri Anda. Lepaskan ketegangan. Percayalah pada dirimu sendiri."

    em "Ini ... aneh. Saya merasa ... lebih tenang, tetapi juga sedikit terbuka."

    psy "Itu benar -benar normal. Ini adalah proses. Teknik ini membantu melepaskan stres dan kecemasan yang dibangun, memungkinkan Anda untuk terhubung kembali dengan diri batin Anda."

    scene vt85 with dissolve

    em "Saya pikir saya bisa merasakannya. Ini ... tidak nyaman, tetapi dengan cara yang baik, saya kira."

    scene vt86 with dissolve

    psy "Itu kemajuan. Ingat, Anda tidak harus memiliki semua jawaban sekarang. Tidak apa -apa untuk tidak pasti."

    psy "Teknik ini cukup kuat. Saya mengembangkannya menggambar inspirasi dari karya Freud. Ini membantu melepaskan ketegangan built-up dan menghasilkan katarsis, yang merupakan langkah pertama dalam proses yang lebih dalam."

    psy "Saat kami melanjutkan, kami akan melewati tahap berikutnya."

    psy "Itu cukup untuk hari ini. Mari kita bawa pasangan Anda juga."

    if ntr_point >= nts_point:

        scene vt87_5 with fade

        mc "Hei, apakah sesimu sudah berakhir?"

        scene vt88_5 with dissolve

        psy "Ya, kita bisa membungkus semuanya hari ini."

        scene vt89_5 with dissolve

        mc "Jadi, bagaimana hasilnya tanpaku? Apakah Anda bisa mengeluarkan semuanya?"

        scene vt90_5 with dissolve

        em "Erm ... haha ... Saya baru saja berbicara tentang semua yang telah kami lalui akhir -akhir ini, sayang."

        scene vt91_5 with dissolve

        psy "__Var_0__ sangat terbuka selama sesi kami."

        scene vt92_5 with dissolve

        psy "Itu selalu menyegarkan ketika seseorang benar -benar bisa telanjang sendiri - secara emosional, tentu saja. Ini memungkinkan kita untuk menjelajahi kedalaman tersembunyi itu secara lebih efektif."

        scene vt93_5 with dissolve

        em "Ya. Saya merasa saya hancur bebas dari rantai saya. Saya pikir beberapa kebingungan saya telah diselesaikan."

        scene vt94_5 with dissolve

        mc "Rantai apa? Wow, bahkan satu sesi tampaknya memiliki dampak besar pada Anda. Anda terlihat lebih percaya diri."

        scene vt95_5 with dissolve

        em "Saya kira Dr. Wise sangat pandai dalam apa yang dia lakukan."

        scene vt96_5 with dissolve

        psy "Ha ha ha. Terima kasih, tapi saya tidak melakukan apa -apa. Segala sesuatu yang dicapai di sini adalah berkat upaya dan kemauan klien saya."

        scene vt98_5 with dissolve

        psy "Sesi saya berikutnya akan dimulai. Saya akan mengharapkan Anda lagi minggu depan. Sampai jumpa."

        scene vt99_5 with dissolve

        em "Selamat tinggal, Dr. Wise."

        scene vt100_5 with dissolve

        mc "Terima kasih, Dr. Wise."

        jump first_ntr
    else:


        scene vt87 with fade

        mc "Hei, apakah sesimu sudah berakhir?"

        scene vt88 with dissolve

        psy "Ya, kita bisa membungkus semuanya hari ini."

        scene vt89 with dissolve

        mc "Jadi, bagaimana hasilnya tanpaku? Apakah Anda bisa mengeluarkan semuanya?"

        scene vt90 with dissolve

        em "Erm ... haha ... Saya baru saja berbicara tentang semua yang telah kami lalui akhir -akhir ini, sayang."

        scene vt91 with dissolve

        psy "__Var_0__ sangat terbuka selama sesi kami."

        scene vt92 with dissolve

        psy "Itu selalu menyegarkan ketika seseorang benar -benar bisa telanjang sendiri - secara emosional, tentu saja. Ini memungkinkan kita untuk menjelajahi kedalaman tersembunyi itu secara lebih efektif."

        scene vt93 with dissolve

        em "Uh ... ya, itu ... berwawasan luas."

        scene vt94 with dissolve

        mc "__Var_0__, apakah semuanya baik -baik saja? Pipi Anda semuanya merah, dan Anda sepertinya bernapas sedikit lebih cepat ... apakah Anda baik -baik saja?"

        scene vt95 with dissolve

        em "Apa? Tidak, tidak, tidak ada yang terjadi! Maksudku, semuanya baik -baik saja! Itu hanya ... Anda tahu, berbicara. Itu saja."

        scene vt96 with dissolve

        psy "Adalah normal untuk merasa sedikit lepas setelah sesi yang jujur. Tapi jangan khawatir, __var_0__, Anda menanganinya dengan sangat baik."

        scene vt97 with dissolve

        em "Ya, sungguh! Tidak ada yang perlu dikhawatirkan ... kan?"

        scene vt98 with dissolve

        psy "Kalau begitu, sampai jumpa lagi minggu depan. Hati-hati di jalan."

        scene vt99 with dissolve

        em "Selamat tinggal, Dr. Wise."

        scene vt100 with dissolve

        mc "Terima kasih, Dr. Wise."

        jump first_nts

label first_ntr:

    scene vt101 with fade

    mc "Ayo ... hanya satu gigitan. Anda tidak akan mati karena berbagi."

    scene vt102 with dissolve

    em "Tidak. Tidak terjadi ... Saya mendapatkan Ice Cream Fair dan persegi ini."

    scene vt101 with dissolve

    mc "Tapi saya sangat menginginkannya sekarang."

    scene vt103 with dissolve

    em "Nah, Anda seharusnya mendapatkan milik Anda. Ketika saya bertanya, Anda mengatakan Anda tidak ingin."

    scene vt104 with dissolve

    mc "Saat itu! Hal -hal berubah, terutama ketika saya melihat Anda sangat menikmatinya."

    scene vt105 with dissolve

    em "Sayang sekali. Burung awal mendapatkan cacing - atau dalam hal ini, es krim."

    scene vt106 with dissolve

    mc "Ayo, hanya satu gigitan. Anda tidak akan mati ... meskipun jika itu Andrew, Anda mungkin akan membiarkannya menjilat es krim, ya?"

    scene vt107 with dissolve

    em "Andrew? Darimana dia berasal?"

    scene vt108 with dissolve

    em "Oh ... maksudmu hal blowjob."

    scene vt108_5 with dissolve

    em "Anda bercanda, bukan? Anda sepertinya tidak terlalu terganggu dengan apa yang Anda lihat."

    scene vt106_5 with dissolve

    mc "Terakhir kali, Anda memberinya blowjob. Saya pikir Anda tidak menyukai hal semacam itu. Sejujurnya, saya tidak terlalu terganggu dengan apa yang saya lihat."

    scene vt109 with dissolve

    em "Apa maksudmu? Jika saya pergi ke pria itu sekarang dan memberinya blowjob, bukankah itu mengganggu Anda?"

    scene vt110 with dissolve

    mc "Aku tidak tahu..."

    scene vt111 with dissolve

    em "Setelah berbicara dengan terapis, saya merasa sedikit berbeda. Saya pikir beberapa batasan perlu didorong jika kita akan menyelamatkan dunia."

    scene vt112 with dissolve

    mc "Batas macam apa, misalnya?"

    scene vt113 with dissolve

    em "Ketika saya bertanya apakah Anda akan terganggu jika saya mengambil pria itu di mulut saya, Anda mengatakan Anda tidak tahu. Saya kira ada cara untuk mengetahuinya."

    scene vt114 with dissolve

    em "Bisakah Anda memegang es krim saya? Jika Anda mau, Anda bisa menggigit, sayang."

    mc "Hey __var_0__!"

    scene vt115 with dissolve

    mc "Apakah kamu serius?"

    scene vt116 with dissolve

    em "Hai! Saya perhatikan Anda telah melihat saya menjilat es krim sejak saya tiba di sini."

    scene vt117 with dissolve

    em "Anda menatap saya seperti Anda ingin memakan saya. Apakah Anda ingin saya menjilat es krim Anda?"

    scene vt118 with dissolve

    unk "S-SURE ..."

    scene vt119 with dissolve

    unk "WTF? Apakah saya mati atau sesuatu? Apakah saya di surga?"

    em "Wow ... mengapa semua orang begitu besar?"

    scene vt120 with dissolve

    unk "Ha ha ha."

    scene vt121 with dissolve

    unk "Bukankah itu suamimu di sana? Apa yang terjadi di antara kalian berdua?"

    em "Anda benar -benar ingin berbicara tentang suami saya sekarang?"

    scene vt122 with dissolve

    unk "Oke ... oke ... terus berjalan."

    scene vt123 with dissolve

    mct "Saya tidak percaya __var_0__ berubah sebanyak ini setelah hanya satu sesi. Apakah mereka berbicara tentang saya?"

    scene vt124 with dissolve

    mct "Apakah begitulah hidup saya dari sekarang?"

    mct "Dia biasa mengatakan dia tidak suka mengambil milikku di mulutnya."

    mct "Sekarang, dia mengambil orang tua tanpa ragu -ragu, bahkan berjalan sepanjang jalan. Seperti halnya saya benci mengakuinya, melihat __var_0__ seperti ini membuat saya bersemangat."

    scene black with dissolve

    pause (0.01)

    scene p_bj with dissolve

    pause

    scene vt126 with dissolve

    mct "Sial ... kurasa sudah berakhir sekarang."

    scene vt127 with dissolve

    mc "Sayang. Mulutmu…"

    scene vt128 with dissolve

    em "Terima kasih, sayang. Saya merasa lelah, bisakah kita pulang?"

    scene vt129 with dissolve

    em "Saya pikir ada beberapa hal yang perlu kita bicarakan sesudahnya."

    scene vt130 with dissolve

    mc "O-Oke ... Tentu, Sayang."

    scene black with dissolve

    pause

    jump ntr_path_cont

label first_nts:

    scene vt101 with fade

    mc "Ayo ... hanya satu gigitan. Anda tidak akan mati karena berbagi."

    scene vt102 with dissolve

    em "Tidak. Tidak terjadi ... Saya mendapatkan Ice Cream Fair dan persegi ini."

    scene vt101 with dissolve

    mc "Tapi saya sangat menginginkannya sekarang."

    scene vt103 with dissolve

    em "Nah, Anda seharusnya mendapatkan milik Anda. Ketika saya bertanya, Anda mengatakan Anda tidak ingin."

    scene vt104 with dissolve

    mc "Saat itu! Hal -hal berubah, terutama ketika saya melihat Anda sangat menikmatinya."

    scene vt105 with dissolve

    em "Sayang sekali. Burung awal mendapatkan cacing - atau dalam hal ini, es krim."

    scene vt106 with dissolve

    mc "Ayo, hanya satu gigitan. Anda tidak akan mati ... meskipun jika itu Andrew, Anda mungkin akan membiarkannya menjilat es krim, ya?"

    scene vt107 with dissolve

    em "Andrew? Darimana dia berasal?"

    scene vt108 with dissolve

    em "Oh ... maksudmu hal blowjob."

    scene vt108_5 with dissolve

    em "Anda bercanda, bukan? Anda sepertinya tidak terlalu terganggu dengan apa yang Anda lihat."

    scene vt106_5 with dissolve

    mc "Terakhir kali, Anda memberinya blowjob. Saya pikir Anda tidak menyukai hal semacam itu. Sejujurnya, saya tidak terlalu terganggu dengan apa yang saya lihat."

    scene vt111 with dissolve

    em "Apakah Anda benar -benar baik -baik saja dengan semuanya? Dengan bagaimana keadaan akhir -akhir ini?"

    scene vt112 with dissolve

    mc "Saya baik-baik saja. Itu hanya ... berbeda, tapi itu tidak berbeda. Saya kira saya sudah menerimanya."

    scene vt131 with dissolve

    em "Senang mendengarnya. Sayang, bisakah kita duduk dan berbicara sebentar?"

    scene vt132 with dissolve

    em "Saya sudah banyak memikirkan apa yang dikatakan terapis. Mungkin kita terlalu menahan banyak hal. Ada hal -hal yang bisa kami coba buat menjadi lebih baik."

    scene vt133 with dissolve

    mc "Jenis apa?"

    scene vt132 with dissolve

    em "Nah, ini tentang mendorong batasan. Tidak dengan cara yang buruk, hanya ... batas pengujian. Mencari tahu apa yang berhasil bagi kami berdua."

    scene vt133 with dissolve

    mc "Batas, ya? Saya kira tidak ada salahnya mengeksplorasi, selama kita berdua nyaman."

    scene vt134 with dissolve

    em "Tepat. Ini tentang komunikasi, kepercayaan ... dan Anda tahu, mungkin bersenang -senang saat kami melakukannya."

    scene vt135 with dissolve

    em "Kami bahkan bisa mengubah ini menjadi permainan, jika Anda siap untuk itu. Tantangan. Untuk melihat seberapa jauh kami bersedia untuk saling pergi."

    scene vt136 with dissolve

    mc "Tantangan, ya? Saya tertarik. Game seperti apa yang kita bicarakan?"

    scene vt137 with dissolve

    em "Nah, Anda melihat pria itu berdiri di sana?"

    em "Dia telah menatapku sejak aku duduk. Saya bisa merasakan matanya pada saya. Ini semacam ... menarik."

    scene vt138 with dissolve

    mc "Benar-benar? Apa kamu yakin?"

    scene vt139 with dissolve

    em "Oh, saya yakin. Saya perhatikan cara dia menatap saya. Hampir seperti dia membayangkan melakukan sesuatu kepada saya. Tapi, saya bertanya -tanya ... apa pendapat Anda tentang itu?"

    scene vt138 with dissolve

    mc "Saya kira saya tidak bisa menyalahkannya. Anda terlihat bagus hari ini."

    scene vt140 with dissolve

    em "Mari kita lihat seberapa jauh kita bisa mengambil ini.Hmm, mungkin. Tapi saya pikir ada lebih dari itu. Bagaimana jika kita membuat permainan ini?"

    mc "Game, ya? Apa gunanya?"

    scene vt141 with dissolve

    em "Intinya adalah untuk melihat seberapa nyaman kita bisa mendapatkan hal -hal yang biasanya tidak kita coba. Mari kita lihat apakah Anda bisa menanganinya."

    em "Jika saya memberi tahu dia bahwa saya menyadarinya menonton, maukah Anda cemburu, atau Anda akan menikmati menonton saya bermain bersama?"

    scene vt142 with dissolve

    mc "Anda tidak serius, bukan? Anda ingin menggoda dia, di depan saya?"

    scene vt143 with dissolve

    em "Jangan menyebutnya godaan dengan tepat, tapi mungkin kita membiarkannya menonton dari kejauhan, bagaimana menurut Anda?"

    scene vt144 with dissolve

    em "Anda mengatakan Anda baik -baik saja dengan mengeksplorasi hal -hal ... mari kita lihat apakah Anda benar -benar bersungguh -sungguh."

    scene vt145 with dissolve

    em "Terlihat madu…."

    scene vt146 with dissolve

    mc "Wow… bisakah aku payah?"

    em "Haha ... tidak sekarang. Kami hanya bermain game sekarang."

    scene vt147 with dissolve

    mc "Sepertinya seseorang agak terlalu bersemangat untuk bergabung dengan permainan."

    em "Anda menjadi terlalu bersemangat, bukan?"

    scene vt146 with dissolve

    mc "Bisakah Anda menyalahkan saya? Anda menggodaku seperti orang gila sekarang."

    scene vt148 with dissolve

    em "Hmm, mungkin saya harus berbalik dan membiarkannya melihat semuanya?"

    scene vt149 with dissolve

    mc "Saya tidak tahu apakah saya bisa menangani lebih banyak, tetapi saya jelas tidak mengatakan tidak."

    scene vt148 with dissolve

    em "Baiklah, mari kita naikkan taruhannya sedikit."

    scene vt149 with dissolve

    em "Di sana. Bagaimana itu untuk sedikit sensasi?"

    scene vt148 with dissolve

    mc "Anda benar -benar bermain dengan api di sini ... tapi saya menyukainya."

    scene vt149 with dissolve

    em "Bagus. Sekarang, bagaimana jika saya membiarkan dia melihat sedikit lagi?"

    scene vt150 with dissolve

    mc "Anda serius? Anda akan melakukannya?"

    em "Mengapa tidak? Itu hanya permainan, bukan? Mari kita lihat betapa berani kita dapatkan."

    scene vt148 with dissolve

    em "Bagus. Mari kita terus berjalan sebentar lagi. Tapi ingat, ini adalah permainan kami. Kami mengontrol seberapa jauh kelanjutannya."

    scene vt149 with dissolve

    mc "Sangat."

    scene vt147 with dissolve

    em "Mungkin aku harus membiarkan dia menyentuhku? Atau mungkin saya harus menunjukkannya lebih banyak lagi? Bagaimana menurutmu?"

    mc "Ohh…"

    scene vt151 with dissolve

    em "Saya pikir sudah waktunya bagi saya untuk berbalik."

    em "Dia tampak terdiam. Haruskah saya pergi dan membiarkannya mencium payudaraku sekali?"

    mc "O-oke."

    scene vt152 with dissolve

    em "Ha ha ha. Sepertinya Anda juga benar -benar masuk ke dalam permainan."

    em "Selain itu, jika kita membuka kunci semua pencapaian sekaligus, bukankah permainan menjadi membosankan?"

    mc "Haha, kamu benar, itu akan terjadi."

    scene vt153 with dissolve

    em "Oh tidak…"

    scene vt154 with dissolve

    em "Saya pikir dia ingin mengambil semuanya lebih jauh."

    mc "Oh sial!"

    scene vt155 with dissolve

    em "Ayo ... Saya sangat dihidupkan, kita harus pulang dan berhubungan seks sekarang."

    scene vt156 with dissolve

    mc "O-Oke ... Tentu, Sayang."

    jump second_nts

label ntr_path_cont:

    scene int1 with fade

    mct "__Var_0__ telah berubah. Itu dimulai dengan rambutnya - dia berada di salon hampir setiap hari. Lalu datanglah Makeover Lemari Lemari."

    mct "Setiap pakaian baru yang dia pilih tampaknya dirancang untuk memamerkan kepercayaan dirinya, daya pikatnya. Dan saya harus mengakui ... dia terlihat luar biasa."

    mct "Tapi itu bukan hanya penampilannya. Cara dia bertindak di sekitar saya ... itu juga berubah."

    scene int4 with dissolve

    mct "Aku masih bisa merasakan cintanya, tapi tatapannya ... sekarang berbeda. Ada sesuatu di matanya, sesuatu yang tidak bisa saya pikirkan. Dan kemudian ada hari itu di taman ..."

    mct "Saya tidak bisa mengguncangnya. Mengawasinya dengan orang asing itu, lelaki tua itu ... Aku tidak tahu harus berpikir apa. Itu mendebarkan, tentu saja, tetapi pada saat yang sama, sangat meresahkan."

    scene int1 with dissolve

    mct "Apakah dia masih __var_0__ yang sama saya tahu?Sejak hari itu, ada saat -saat ketika dia menghilang begitu saja - perjalanan yang cepat, teleponnya, benar -benar tidak terjangkau. Saya tidak bisa membantu tetapi khawatir. Apakah dia aman?"

    scene int3 with dissolve

    mct "Pilihan yang saya buat baru -baru ini telah membawa kami ke sini. Saya tidak bisa membantu tetapi bertanya -tanya ... apa yang harus saya lakukan secara berbeda?"

    scene hm48_2 with fade

    mct "Mungkin saya mendorongnya terlalu cepat."

    scene hm52_2 with dissolve

    mct "Tuhan ... pertama kali dia menyentuh ayam besar Andrew ... Aku tidak bisa mengeluarkannya dari kepalaku. Itu bahkan tidak muat di tangannya."

    scene hd20_2 with dissolve

    mct "Saya ingat cara dia memandang __var_0__ ... dan cara dia bertemu tatapannya, tanpa henti. Saat itu, saya tidak sepenuhnya menangkapnya. Tapi sekarang? Sekarang, semuanya jernih."

    scene nm8_2 with dissolve

    mct "Tuhan ... hatiku berdebar kencang. Saya tahu persis ke mana arahnya, namun ... Saya tidak menghentikannya. Karena jauh di lubuk hati ... saya ingin ini."

    scene nm20_b_2 with dissolve

    mct "Saya tidak bisa memalingkan muka ... __var_0 __ pinggul menekan tonjolan Theo ... dan pada saat itu ..."

    scene rt32_2 with dissolve

    mct "Tampilan itu di mata __var_0 __ ... terbakar, intens, benar -benar tidak dijaga. Itu bukan hanya keinginan - itu adalah izin."

    mct "Undangan diam -diam. Dan alih -alih menolak ... saya mendapati diri saya ingin melihat seberapa jauh dia pergi."

    scene rt42_2 with dissolve

    mct "Tuhan ... untuk pertama kalinya, orang lain datang di wajah __var_0 __. Saya telah berfantasi tentang hal itu sebelumnya, membayangkan skenario dalam pikiran saya."

    mct "Tapi menontonnya terungkap, melihatnya menerimanya ... itu menghantam berbeda."

    mct "Atau ... haruskah saya merangkulnya?Itu terjadi begitu tiba -tiba ... bahkan sekarang, saya tidak tahu apa yang seharusnya saya rasakan. Haruskah saya marah? Haruskah saya menghentikan ini?"

    scene vt115_2 with dissolve

    mct "__Var_0__ memberi saya es krimnya, tidak ada kata -kata, hanya senyum yang lembut dan tahu sebelum dia berbalik dan berjalan pergi. Dan pada saat itu, sesuatu yang jauh di dalam diriku bergerak."

    scene vt118_2 with dissolve

    mct "Saya melihatnya mendekati seorang pria tua yang duduk di bangku. Dadaku menegang, denyut nadi saya berduri. Apa yang dia lakukan?"

    mct "Saya tidak perlu mendengar percakapan mereka - saya sudah tahu. Tuhan ... itu terjadi. Di sana, tepat di depanku. Sebuah fantasi yang telah saya mainkan di kepala saya berkali -kali ... tapi sekarang itu nyata."

    scene vt123_2 with dissolve

    mct "Seolah -olah ... seolah -olah dia telah menunggu ini.Ketika lelaki tua itu membuka ritsleting celananya, saya menangkap raut wajah __var_0 __. Tidak ada satu pun jejak ragu -ragu. Tidak ada pikiran kedua."

    scene vt124_2 with dissolve

    mct "Bibir yang saya cium setiap hari sekarang melilit ayam lelaki tua."

    mct "Apakah ini mimpi? Atau apakah saya akhirnya menghidupkan fantasi saya? Rasanya nyata, hampir mustahil ... namun, sensasi yang mengalir melalui saya tidak dapat dipungkiri."

    scene int4 with fade

    mct "Pikiran itu menggerogoti saya.Saya bertanya -tanya apakah membawanya ke psikolog itu adalah kesalahan. Apakah saya memulai sesuatu yang tidak bisa saya kendalikan? Apakah saya kehilangan dia?"

    scene int1 with dissolve

    mct "Saya tidak bisa menyangkal betapa bahagianya dia sekarang. Dan saya tidak bisa menjauhkan diri untuk mengambilnya darinya. Jika jalan baru ini menggairahkannya, maka saya akan menemukan cara untuk beradaptasi."

    scene int4 with dissolve

    mct "Karena terlepas dari segalanya ... aku masih mencintainya.Saya akan memberinya ruang, mendukungnya - apa pun ini. Saya tidak ingin kehilangan dia. Jika inilah yang membuatnya tetap di sisi saya, maka saya akan menanggungnya."

    scene black with dissolve

    pause (0.5)

    jump home_nmorning

label home_nmorning:

    scene nm1 with dissolve

    mct "Saya mendengar suara datang dari dalam lagi. Tapi ... suaranya tidak akrab."

    scene nm2 with dissolve

    mc "Ahh ... aku harus bergegas dan berpakaian. Saya sudah terlambat bekerja."

    scene nr1 with fade

    mct "Siapa orang ini? Dan bagaimana mereka begitu terjebak dalam percakapan mereka sehingga mereka bahkan tidak memperhatikan saya di sini?"

    scene nr2 with dissolve

    mc "Apa yang terjadi di sini?"

    scene nr3 with dissolve

    em "Jadi, ini dia.Oh, selamat pagi! Ini adalah Taylor - siswa yang saya ceritakan, yang saya temui di toko. Kami harus berbicara, dan dia bertanya apakah saya bisa mengajarinya."

    $ persistent.ty_unlock = True

    scene nr4 with dissolve

    ty "Yo, ada apa, kawan? Hanya mengambil kopi. __Var_0 __ akan membantu saya dengan angka."

    scene nr5 with dissolve

    mc "Matematika, ya? Dan Anda hanya ... di sini?"

    scene nr6 with dissolve

    em "Ya, seperti yang saya katakan, saya mengajarinya. Pikir akan baik untuk mengobrol sedikit terlebih dahulu, mengenalnya lebih baik sebelum melompat ke matematika."

    scene nr5 with dissolve

    mc "Begitu ... tapi, __var_0__, Anda tidak pernah menyebutkan mengajari orang lain selain Theo."

    scene nr6 with dissolve

    em "Saya tidak berpikir itu layak disebutkan. Taylor membutuhkan bantuan, jadi saya menawarkan. Ini benar -benar bukan masalah besar."

    scene nr4 with dissolve

    ty "Ya, kawan, tryna cukup lakukan nomor saya dengan benar. __Var_0 __ sangat sabar sabar dengan saya."

    scene nr5 with dissolve

    mc "Benar ... tidak mengharapkan ini. Uh, Taylor, hanya ... pastikan Anda tidak memberi __var_0__ waktu yang sulit, oke? Anda harus bersyukur dia bahkan membantu Anda."

    scene nr7 with dissolve

    ty "__Var_0 __ Got Keterampilan, dan saya hanya di sini untuk belajar.Dingin, kawan, aku mengerti. Kami hanya Vibin - matematika dan kopi, tidak ada drama. Saya menghargainya, nyata."

    scene nr8 with dissolve

    em "Oh, tolong, Anda membuatnya terdengar seperti saya mengajari Anda rahasia alam semesta. Itu hanya matematika."

    scene nr9 with dissolve

    mc "Ya, terserah. Saya punya pekerjaan, jadi saya akan meninggalkan kalian berdua. Just ... jaga agar semuanya tetap dingin, oke?"

    mc "Kami akan berbicara nanti."

    scene nr10 with dissolve

    ty "Pasti, kawan. Kami baik -baik saja. Tidak perlu stres. Dan hei, jaga dirimu, orang tua. Kami akan menahan benteng di sini."

    scene nr11 with dissolve

    mct "Sejujurnya, saya tidak merasa nyaman meninggalkan __var_0__ sendirian bersamanya di rumah."

    scene nr12 with dissolve

    em "Sayang, jangan lupa - kita akan pergi ke bioskop malam ini. Anda ingat, kan?"

    scene nr13 with dissolve

    mc "Tentu saja, saya akan berada di sana. Saya berbicara dengan bos saya, dan saya akan meninggalkan pekerjaan satu jam lebih awal untuk menemui Anda di teater."

    scene nr12 with dissolve

    em "Baiklah, saya akan menunggu Anda di sana. Jangan membuat saya terlalu lama menunggu."

    scene nr14 with dissolve

    mc "Mengerti, sayang. Sampai jumpa lagi."

    em "Sampai jumpa."

    ty "Bye-bye, Daddy-O!"

    scene nr15 with dissolve

    mct "Pria yang menjengkelkan."

    scene nr16 with fade

    ty "Baiklah, __var_0__, sekarang __var_1 __ dari gambar, kita bisa kembali ke obrolan kita."

    scene nr17 with dissolve

    em "Ya, dimana kita?"

    scene nr18 with dissolve

    ty "Oh ya - jadi apa masalahnya dengan Anda dan matematika? Anda selalu menjadi angka dan semua itu?"

    scene nr19 with dissolve

    em "Itu selalu menjadi gairah. Saya suka logika dan struktur. Ini seperti memecahkan teka -teki."

    scene nr18 with dissolve

    ty "Seperti, saya sudah bisa tahu - Anda mendapatkan kesabaran gila.Man, teka -teki? Saya sampah pada itu. Tapi hei, saya mendapat bakat untuk mencari tahu orang."

    scene nr20 with dissolve

    em "Nah, kesabaran itu penting, terutama saat mengajar."

    scene nr21 with dissolve

    ty "Ya, Anda seperti ratu dingin. Aku yakin tidak ada yang bisa terjadi padamu."

    scene nr22 with dissolve

    em "Saya mencoba untuk tetap tenang. Itu membuat pengajaran lebih mudah."

    scene nr23 with dissolve

    ty "Yo, sungguh, jika saya adalah seorang guru, saya akan kehilangan akal. Anak -anak hari ini liar."

    scene nr22 with dissolve

    em "Ini bisa menantang, tetapi juga bermanfaat. Melihat seseorang akhirnya memahami sesuatu adalah perasaan yang hebat."

    scene nr24 with dissolve

    ty "Anda mendapatkan getaran keren itu.Itu dalam. Anda pernah berpikir untuk melakukan sesuatu yang lain? Seperti, saya tidak tahu, rap atau semacamnya?"

    scene nr25 with dissolve

    em "Rapping?"

    scene nr26 with dissolve

    em "Ha ha ha."

    scene nr20 with dissolve

    em "Itu ... ide yang menarik. Saya tidak berpikir saya memiliki bakat untuk itu."

    scene nr27 with dissolve

    ty "Nah, Anda akan membunuhnya. Anda mendapat kehadirannya. Dan, mari kita menjadi nyata, Anda akan terlihat bersemangat dalam video musik."

    scene nr28 with dissolve

    em "Yah, terima kasih atas dorongan kepercayaan diri, tapi saya pikir saya akan tetap mengajar."

    scene nr29 with dissolve

    ty "Cukup adil. Tetapi jika Anda ingin mencoba, saya adalah pria hype Anda."

    scene nr30 with dissolve

    em "Saya akan mengingatnya."

    scene nr31 with dissolve

    ty "Jadi, apa yang Anda lakukan untuk bersenang -senang? Anda sepertinya memiliki beberapa hobi tersembunyi."

    scene nr32 with dissolve

    em "Hmm..."

    scene nr33 with dissolve

    em "Saya menikmati membaca, yoga, dan terkadang melukis."

    scene nr34 with dissolve

    ty "Yo, lukisan? Itu obat bius. Saya yakin Anda pandai dalam hal itu. Anda mendapatkan energi kreatif itu."

    scene nr35 with dissolve

    em "Itu hanya hobi. Sesuatu untuk bersantai."

    scene nr36 with dissolve

    ty "Sobat, Anda seperti paket total. Cerdas, kreatif, dan dingin. Anda seperti guru impian."

    scene nr37 with dissolve

    pause

    scene nr37_5 with dissolve

    em "Anda menyanjung saya, Taylor."

    scene nr38 with dissolve

    ty "Nah, saya hanya membuatnya nyata, mengajar. Bicaralah fakta."

    scene nr37 with dissolve

    emt "Dia berbicara banyak omong kosong, tapi entah bagaimana, itu menghibur. Dan, saya harus mengakui ... fisiknya mengesankan. Jika dunia tidak berantakan, saya ragu dia akan kesulitan menjauhkan gadis -gadis itu."

    scene nr38_5 with dissolve

    ty "Hai! Ada apa? Tiba -tiba Anda sangat sunyi. Apa yang ada di pikiran Anda?"

    scene nr39 with dissolve

    em "Oh, tidak ada. Hanya memikirkan apa yang Anda katakan."

    scene nr40 with dissolve

    ty "Haha, jadi aku punya kamu berpikir ', ya? Mungkin saya lebih mengesankan dari yang saya kira."

    scene nr39 with dissolve

    em "Keyakinan tidak selalu merupakan hal yang buruk."

    scene nr34 with dissolve

    ty "Tepat. Anda tidak bisa pergi ke mana pun tanpa itu, bukan?"

    scene nr41 with dissolve

    em "Benar, tetapi terlalu banyak kepercayaan diri terkadang bisa membuat Anda mendapat masalah."

    scene nr38 with dissolve

    ty "Hei, saya suka mengambil risiko. Di situlah kesenangan dimulai."

    scene nr46 with dissolve

    em "Mengambil risiko, ya? Anda yang menarik."

    scene nr40 with dissolve

    ty "Terima kasih, ajarkan. Dan Anda lebih menyenangkan dari yang saya harapkan."

    scene nr48 with dissolve

    em "Sepertinya kami saling mengejutkan."

    scene nr49 with dissolve

    ty "Ya? Yah, saya suka kejutan."

    ty "Membuat sesuatu ... lebih menarik."

    scene nr50 with dissolve

    em "Hati -hati sekarang, Taylor. Beberapa kejutan datang dengan konsekuensi."

    scene nr49 with dissolve

    ty "Oh, saya bisa menangani sedikit masalah. Pertanyaannya adalah ... bisakah kamu?"

    scene nr52 with dissolve

    em "Hmm ... berbicara tentang masalah, saya pikir 'pelajaran matematika' Anda sudah berakhir untuk hari ini."

    scene nr49 with dissolve

    ty "Sial, tepat saat itu menjadi 'baik. Kira saya harus menunggu kelas berikutnya."

    scene nr51 with dissolve

    em "Kesabaran, Taylor. Mungkin lain kali, Anda akan benar -benar mempelajari sesuatu."

    scene nr49 with dissolve

    ty "Oh, saya sudah belajar banyak, mengajar. Anda belum mengetahuinya."

    ty "Sial, kira aku harus bangkit. Tapi jangan khawatir, ajarkan - saya akan kembali. Anda tahu saya bukan tipe untuk melewatkan kelas."

    scene nr48 with dissolve

    em "Itu adalah obrolan yang bagus, Taylor. Tidak terduga, tapi ... menarik."

    jump ty_hug

label ty_hug:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"







    $ persistent.ty_scene1_unlocked = True

    scene nr34 with dissolve

    ty "Ya? Lalu bagaimana ‘tentang selamat tinggal yang tepat? Tidak ada jabat tangan yang agak - saya berbicara sangat hangat, sangat dekat. Pelukan perpisahan kecil, mengajar?"

    scene nr53 with dissolve

    em "Tentu saja, datang ke sini."

    scene nr54 with dissolve

    ty "Mmm, sekarang itulah yang saya sebut selamat tinggal. Anda berbau harum, mengajar. Berengsek."

    scene nr55 with dissolve

    em "Wow ... itu sedikit lebih hangat dari yang saya harapkan. Yang lebih ketat, dan saya mungkin mulai berpikir Anda tidak ingin pergi."

    ty "Kotoran! Saya bisa tinggal jika Anda memintaku."

    scene nr56 with dissolve

    em "Itu lelucon, Taylor."

    scene nr57 with dissolve

    ty "Aight, Aight. Tapi Anda bermain dengan api, mengajar. Anda beruntung saya mendapat kontrol diri."

    scene nr58 with dissolve

    emt "Apakah dia ... mencoba mencium dadaku? Apa?"

    scene nr59 with dissolve

    tyt "Sial, payudaranya berbau harum sekali. Seperti vanilla hangat atau sesuatu. Jika saya mendorong wajah saya hanya sedikit lebih dekat ... Saya bersumpah saya akan menciumnya puting."

    tyt "Sobat, orang bodoh ini __var_0__ bahkan tidak tahu betapa beruntungnya dia. Membuat saya merasa cemburu. Lurus ke atas diberkati, bung itu."

    emt "Jika saya tidak menghentikannya sekarang, dia akan mulai menginginkan lebih ..."

    scene nr60 with dissolve

    em "Hmm, kita akan melihat tentang itu lain kali. Saya berharap Anda tepat waktu untuk sesi kami berikutnya. Dan saya berjanji ... percakapan kami akan lebih menarik."

    scene nr61 with dissolve

    ty "Oh, sekarang kamu benar -benar membuatku hyped. Anda mengatakan saya mendapat pelajaran lain?"

    scene nr62 with dissolve

    em "Katakan saja ... Saya akan memberi Anda beberapa pelajaran lagi tentang apa artinya menjadi seorang pria."

    scene nr65 with dissolve

    ty "Sial, Anda sudah menjadi guru favorit saya."

    scene nr64 with dissolve

    em "Sampai jumpa minggu depan, Taylor."

    scene nr65 with dissolve

    ty "Ya, ya. Tapi jangan membuatku menunggu terlalu lama, mengajar. Seorang pria harus tetap tajam."

    $ renpy.end_replay()

    scene cm1 with fade

    em "Ahh ... mengapa Anda tidak menjawab telepon Anda?"

    scene cm2 with dissolve

    em "Saya telah terjebak di sini di malam hari, bahkan tidak yakin apakah saya harus masuk atau tidak."

    scene cm3 with dissolve

    em "Anda sangat mati, __var_0__!"

    scene cm4 with dissolve

    em "Hah."

    scene cm5 with dissolve

    em "Akhirnya!"

    em "Kemana saja kamu? Saya sudah menunggu di luar selama setengah jam!"

    scene cm6 with dissolve

    mc "Saya bahkan mungkin kehilangan pekerjaan.Maaf, sayang. Pertemuan darurat muncul. Perusahaan dalam krisis, mereka pada dasarnya menyatakan keadaan darurat."

    scene cm7 with dissolve

    em "Tunggu, apa?!"

    scene cm8 with dissolve

    em "Oh tidak ... maafkan aku, sayang."

    scene cm9 with dissolve

    mc "Tidak, tidak. Saya harus meminta maaf. Aku seharusnya tidak meninggalkanmu menunggu di luar selama ini. Mari kita hubungi saja saat ini. Anda harus pulang."

    scene cm10 with dissolve

    em "Dengan serius? Saya menunggu selama ini, saya mungkin juga baru saja masuk dan menonton film sialan itu."

    scene cm11 with dissolve

    mc "Dan apa yang akan Anda lakukan di film tanpa saya?"

    scene cm12 with dissolve

    em "Jangan terlalu memikirkannya. Lagipula aku sebagian besar di sini untuk Scarlett Johansson."

    scene cm13 with dissolve

    mc "Tentu saja Anda."

    scene cm14 with dissolve

    em "Selain itu, tidak bisakah Anda meminta James untuk membuat pemutaran film pribadi untuk saya? Tolong, tolong, tolong ..."

    scene cm15 with dissolve

    mc "...Bagus. Saya akan menelepon James. Sudah masuk ke dalam, jangan lebih menonjol di sini. Saya akan datang menjemput Anda setelah film."

    scene cm16 with dissolve

    em "Ya! Kesepakatan. Anda yang terbaik. Terima kasih, sayang. Aku mencintaimu!"

    scene cm17 with dissolve

    mc "Mencintaimu juga."

    scene cm18 with dissolve

    pause (0.2)

    scene cm19 with dissolve

    pause (0.2)

    scene cm20 with fade

    jm "__Var_0__! Sungguh kejutan yang menyenangkan melihat Anda di sini malam ini. Selalu senang menyambut pelanggan favorit saya."

    scene cm21 with dissolve

    em "Hai, James. Terima kasih telah menyiapkan pemutaran pribadi untuk saya. __Var_0__ tidak bisa berhasil, tetapi saya tidak ingin melewatkan ini. Anda tahu betapa penasarannya saya tentang film ini."

    scene cm22 with dissolve

    jm "Ah, __var_0 __— Selalu dimakamkan dalam pekerjaan. Malu dia tidak bisa bergabung dengan Anda, tapi hei, di situlah saya masuk. Saya sudah menyiapkan semuanya untuk Anda, jangan khawatir."

    scene cm23 with dissolve

    em "Saya menghargai itu. Tidak setiap hari Anda bisa melihat sesuatu seperti ini, dan saya menginginkan pengalaman penuh."

    scene cm24 with dissolve

    jm "Dan Anda akan mendapatkannya. Kamar pribadi sudah siap - tidak ada gangguan, suara sempurna, kursi terbaik di rumah. Anda akan memiliki tempat untuk diri sendiri."

    scene cm25 with dissolve

    jmt "Sial, lihat saja kaki -kaki itu ... halus, kencang, hanya mohon untuk dicicipi. Jika saya memiliki jalan, saya akan menjalankan lidah saya setiap inci, lambat dan dalam, sampai dia menggigil."

    jmt "Saya bertanya -tanya ... karena __var_0__ tidak ada, mungkin dia membiarkan saya memukulnya dari belakang hanya sekali?"

    scene cm23 with dissolve

    emt "Itu terlihat sama lagi ... jika James pernah mendapatkan saya, saya bahkan tidak ingin membayangkan apa yang akan dia lakukan."

    em "Membuat saya penasaran.Kedengarannya sempurna. __Var_0__ benar -benar hiped ini untukku. Dia terus melakukan betapa mengesankan Sharlet Moansson, mengatakan saya bahkan tidak akan bisa membedakan dengan AI."

    scene cm26 with dissolve

    jm "Hampir meresahkan betapa nyata dia.Oh, Anda siap untuk mengobati. Sharlet adalah ... yah, katakan saja dia tidak seperti orang lain. Bahkan jika itu bukan jenis film Anda yang biasa, Anda akan menghargai seni."

    scene cm23 with dissolve

    em "Saya telah melihat beberapa klip di sana -sini. Sangat menarik apa yang dapat dilakukan teknologi sekarang. Bagi saya, ini lebih tentang rasa ingin tahu daripada apa pun."

    scene cm26 with dissolve

    jm "Anda akan merasa seperti melangkah ke dunia lain.Saya mengerti. Ini bukan hanya film - ini adalah pengalaman. Teater yang ditingkatkan AI menghidupkan segalanya dengan cara yang sulit dijelaskan."

    jm "Anda tahu ... dunia bukan tempat yang dulu. Kebanyakan orang yang datang ke sini hanya ingin mengingat bagaimana rasanya - berada di sekitar wanita sejati. Sejak bencana, bisnis telah booming."

    scene cm25 with dissolve

    jm "Terkadang saya bertanya -tanya ... apa yang saya berikan hanya untuk mengingat seperti apa rasanya. Merasakan sesuatu yang nyata lagi."

    jmt "Sobat, saya akan memberikan apa saja hanya untuk satu perjalanan dengan Anda."

    scene cm27 with dissolve

    em "Wow. Itu ... banyak yang harus dibongkar."

    scene cm8 with dissolve

    em "Mengesampingkan bagian tragis dari apa yang baru saja Anda katakan ... film ini terdengar mengesankan. Saya sangat menantikannya."

    scene cm26 with dissolve

    jm "Ya ... dan jika Anda membutuhkan sesuatu - nada, minuman, atau bahkan hanya sebuah perusahaan kecil - Anda tahu di mana menemukan saya."

    scene cm23 with dissolve

    em "Terima kasih, James, tapi saya pikir saya akan mengelola. Hanya film dan sedikit waktu yang sepi adalah yang saya butuhkan malam ini."

    scene cm26 with dissolve

    jm "Dan jangan menjadi orang asing - Anda tahu di mana menemukan saya.Sesuai dengan diri Anda. Tapi hei, tawaran itu berdiri. Nikmati pertunjukannya, __var_0__."

    scene cm23 with dissolve

    em "Terima kasih, James. Saya akan memberi tahu Anda bagaimana kelanjutannya."

    emt "Ya, saya yakin dia akan melakukan apa saja untuk membawa saya sendirian di sana bersamanya."

    scene cm29 with dissolve

    jm "Oh, saya yakin Anda akan melakukannya."

    scene ca1 with fade

    em "Wow ... ini terasa sangat nyata. Detailnya, suasana ... sepertinya saya benar -benar ada di sana. __Var_0__ tidak bercanda tentang seberapa mendalam ini."

    scene ca2 with dissolve

    emt "Oke ... ini jelas bukan film untuk ditonton sendirian. Mengapa saya pikir ini ide yang bagus?"

    scene ca3 with dissolve

    em "Saya harus menyeret __var_0__ di sini dengan saya. Dia mungkin menyukai ini ... mungkin bahkan lebih dari saya."

    scene ca4 with fade

    em "Ya Tuhan, ini intens. Sepertinya menarik saya sepenuhnya ..."

    scene ca5 with dissolve

    em "Bagaimana jika seseorang masuk?"

    jump cnm_prv

label cnm_prv:

    $ name = persistent.name

    $ fname = persistent.fname

    if not name:
        $ name = "Jake"
    if not fname:
        $ fname = "Emily"






    $ persistent.cnm_scene1_unlocked = True

    scene ca6 with dissolve

    em "Tidak ... itu pribadi, bukan? James berjanji. Saya aman…"

    scene ca7 with dissolve

    em "Ini gila. Saya tidak pernah merasakan hal ini - bukan hanya karena filmnya, tetapi karena risiko yang saya ambil. Garam itu ... itu benar -benar membuat saya bersemangat"

    emt "Haruskah saya ... mungkin melepas sesuatu? Tidak ada yang masuk, dan bahkan jika mereka melakukannya ... jadi apa?"

    emt "Saya lebih terbuka untuk pengalaman baru sekarang. Sama seperti sensasi yang saya rasakan ketika saya meniup lelaki tua itu di taman ..."

    scene ca8 with dissolve

    emt "Ini terasa sama."

    scene ca9 with dissolve

    emt "Pikiran orang lain selain __var_0__ melihat payudaraku ... itu membuat saya bersemangat."

    scene ca10 with dissolve

    emt "Tapi bagaimana jika ... itu tidak berhenti hanya di payudaraku?"

    scene ca11 with dissolve

    emt "Bagaimana jika saya ingin lebih-jika saya ingin merasakan udara di semua kulit saya?"

    emt "Pakaian saya adalah satu bagian ... jika saya melepasnya, saya akan benar -benar terbuka."

    scene ca12 with dissolve

    emt "Itu terlalu berisiko."

    scene ca13 with dissolve

    emt "Tapi ide itu ... itu hanya membuatku lebih panas .."

    scene ca14 with dissolve

    emt "__Var_0__ tidak ada di sini, dan orang lain bisa melihat sekilas bagian saya yang paling intim."

    scene ca15 with dissolve

    emt "Bagaimana jika mereka tidak melihat saja? Menyentuh saya? Jari saya…?"

    scene ca16 with dissolve

    emt "Mmm ... hanya memikirkannya ... Tuhan, apa yang terjadi pada saya?"

    scene ca15 with dissolve

    emt "Aku bahkan tidak memakai celana dalam ... Aku bisa merasakan betapa basahnya aku."

    scene ca16 with dissolve

    emt "Mungkin ... mungkin aku harus melepas semuanya."

    scene ca17 with fade

    emt "Tidak ada hambatan ... tidak ada apa -apa di jalan ... hanya saya, benar -benar terbuka."

    scene ca18 with dissolve

    emt "Bagaimana jika seseorang masuk? Tidak ... James bilang itu kamar pribadi saya. Tidak apa -apa ..."

    scene ca19 with dissolve

    emt "Ini terasa sangat berisiko. Tapi itu juga menyenangkan."

    scene ca20 with dissolve

    emt "Berapa banyak orang yang duduk di sini? Melakukan hal -hal di sini?"

    scene ca19 with dissolve

    emt "Bagaimana jika ada ... seseorang ... meninggalkan sesuatu? Seperti ... di kursi?"

    scene ca20 with dissolve

    emt "Bagaimana jika ... bagaimana jika ada ... sesuatu di kursi? Dan sekarang ada pada saya?"

    scene ca21 with dissolve

    emt "Bagaimana jika itu ... menyentuh kulit saya? Bagaimana jika itu ... di celana saya sekarang? Atau bahkan ..."

    scene ca22 with dissolve

    emt "Tidak mungkin ... apakah itu ...?"

    scene ca23 with dissolve

    emt "Dia. Ya Tuhan… seseorang sebenarnya…"

    emt "Itu ada di sana, mengering ke kursi ... bukti kesenangan orang lain, pembebasan orang lain."

    emt "Berapa banyak orang di sini, tersesat dalam panas yang sama seperti yang saya rasakan sekarang?"

    scene ca24 with dissolve

    emt "Ini gila. Saya seharusnya tidak memikirkan hal ini. Itu menjijikkan ... bukan?"

    emt "Tapi kemudian ... mengapa tubuh saya terasa lebih panas?"

    scene ca25 with dissolve

    emt "Bagaimana jika saya hanya ... bersandar sedikit lebih dekat? Hanya untuk melihat ... pasti?"

    scene ca26 with dissolve

    emt "Itu nyata. Seseorang ... beberapa pria, seperti __var_0__, duduk di sini, tidak dapat menahan diri. Di sini, di tempat ini."

    emt "Bagaimana jika saya ... bagaimana jika saya duduk di sini juga? Jika saya membiarkan diri saya merasakan apa yang mereka rasakan?"

    scene ca27 with dissolve

    emt "Tidak. Saya tidak bisa. Itu gila. Bisa jadi siapa saja. Saya bahkan tidak tahu siapa—"

    emt "Tapi itulah yang membuatnya begitu terlarang ... atau mungkin bahkan lebih menarik."

    emt "Saya seharusnya tidak menginginkan ini. Saya seharusnya tidak memikirkan hal ini."

    scene ca28 with dissolve

    emt "Tubuh saya bereaksi sendiri. Ia tahu sesuatu yang ditolak pikiran saya untuk mengakui."

    scene ca27 with dissolve

    emt "Tidak ada hambatan ... tidak ada lapisan di antara ... hanya aku ... menekannya."

    emt "Ini bukan __var_0 __ ... tapi mungkin itu sebabnya saya lebih menginginkannya."

    scene ca26 with dissolve

    emt "Saya ingin merasakannya - menekankan diri saya terhadapnya, menggosoknya"

    emt "Apakah rasanya berbeda? Apakah itu akan membuat saya kehilangan diri saya sepenuhnya?"

    scene ca27 with dissolve

    emt "Saya seharusnya tidak melakukan ini. Saya seharusnya tidak ... tapi ..."

    emt "Tuhan… Saya ingin."

    scene ca29 with dissolve

    emt "Itu menyentuh bibir saya sekarang ... pria lain ... bukan suamiku ... mmm."

    scene ca30 with dissolve

    emt "Saya telah ... dinodai oleh orang lain."

    emt "Bagaimana jika itu ... bagaimana jika itu merembes ke dalam diri saya?"

    scene ca31 with dissolve

    emt "Bagaimana jika itu bukan hanya di bibirku?"

    emt "Bagaimana jika itu lebih dalam ... merendam saya?"

    scene ca32 with dissolve

    emt "Apakah saya ... diklaim oleh seseorang yang bahkan tidak saya kenal?"

    emt "Sangat kotor ... sangat salah ... tapi saya tidak bisa berhenti memikirkannya."

    scene ca33 with dissolve

    emt "Tubuh saya gemetar - bukan karena ketakutan."

    emt "Saya harus menarik diri ... Saya harus bangun dan pergi."

    scene ca30 with dissolve

    emt "Tapi sebaliknya ... Saya ingin menekan lebih keras."

    scene black with dissolve

    pause(0.01)

    scene m_sld1 with dissolve

    em "Ini ... ini gila. Saya tidak bisa berhenti ..."

    scene ca34 with dissolve

    em "Mmmm…"

    scene ca35 with dissolve

    "***Fap Fap Fap***"

    scene ca36_5 with dissolve

    emt "Apakah ada seseorang di belakangku, atau hanya imajinasi saya?"

    emt "Ya, seseorang ada di sana. Dan ... dan apakah suara -suara itu saya dengar?"

    emt "Astaga. Sudah berapa lama dia di sana?"

    emt "Mungkinkah __var_0__? Tidak ... itu tidak mungkin. Kenapa dia menyelinap padaku?"

    scene ca36 with dissolve

    emt "Bagaimana saya tidak mendengarnya masuk? Aku bahkan tidak bisa berbalik sekarang ... dia melihat segalanya."

    emt "Saya kira hal yang paling cerdas untuk dilakukan adalah membiarkannya selesai dan pergi. Kalau tidak, ini bisa menjadi lebih rumit. Saya hanya akan bertindak seolah dia tidak ada di sana."

    scene ca37 with dissolve

    emt "Diawasi…"

    scene ca38 with dissolve

    emt "Itu membuat saya menyala."

    scene ca39 with dissolve

    emt "Apa-apaan?"

    emt "Terlalu dekat, terlalu dekat, terlalu dekat."

    scene ca40 with dissolve

    emt "Ahh ... jantungku berdebar kencang."

    scene ca41 with dissolve

    emt "Jika saya menoleh ... rasanya seperti itu bisa berakhir di mulut saya."

    scene ca42 with dissolve

    emt "Mengabaikannya pasti membuatnya lebih berani."

    scene ca43 with dissolve

    emt "Ahhh ... Aku sangat hidup sekarang."

    emt "Aroma itu ... sangat kuat, luar biasa."

    scene ca44 with dissolve

    emt "Sangat kuat, luar biasa. Saya bahkan tidak bisa menjelaskan. Itu maskulin, mentah, memabukkan"

    scene ca45 with dissolve

    emt "Mmm, aku benar -benar perlu bercinta."

    scene black with dissolve

    pause(0.01)

    scene m_cnm1 with dissolve

    emt "Mmm."

    scene ca46 with flash

    pause

    scene ca47 with flash

    pause

    scene ca48 with flash

    emt "Dia datang ke seluruh tubuhku. Apa yang akan saya lakukan sekarang? Saya berantakan ... __var_0__ akan segera menjemput saya."

    scene ca49 with dissolve

    emt "Saya tidak punya apa -apa untuk Clea. Saya tidak punya pilihan selain mengenakan pakaian saya kembali, semua kotor seperti ini."

    scene ca50 with dissolve

    emt "Saya tidak punya pilihan ... Saya harus mengenakan pakaian saya kembali, seperti ini. Lengket, berantakan ... ternoda."

    emt "Saya merasa sangat kotor. Kehangatannya masih melekat pada kulit saya ... merendam saya."

    emt "Saya hanya berharap __var_0__ tidak mencoba memeluk saya ketika dia menjemput saya. Saya tidak tahu apakah saya bisa mengatasinya sekarang."

    emt "Dan bagian terburuk? Saya masih merasa sangat terangsang."

    emt "Saya harus merasa malu. Saya harus jijik. Tetapi sebaliknya, saya masih bisa merasakan tubuh saya sakit untuk lebih."

    emt "Bahkan sekarang ... kakiku terasa lemah, napasku goyah."

    scene ca51 with dissolve

    emt "Segera setelah saya pulang ... Saya perlu berhubungan seks dengan __var_0__."

    em "Saya harus berpakaian ... Saya benar -benar melewati batas hari ini."

    $ renpy.end_replay()

    scene ca52 with dissolve

    em "Selesai."

    scene ca53 with dissolve

    em "Oh, dia di sini."

    em "Hei, kamu di sini?"

    em "Tidak, tidak, jangan keluar dari mobil madu. Saya mendatangi Anda."

    scene black with fade

    "End of the version 0.5. You can save here."


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
