import json
dict_ref = {
    "Wayo" : "වායො",
    "Current" : "වත්මන්",
    "Calypso" : "කැලිප්සෝ",
    "Songs" : "ගීත",
    "Harsha" : "හර්ෂ",
    "Jayamanne" : "ජයමාන්න",
    "Senaka" : "සේනක",
    "Batagoda" : "බටගොඩ",
    "Request" : "ඉල්ලීම්",
    "request" : "ඉල්ලීම්",
    "Group" : "කණ්ඩායම්",
    "Movie" : "චිත්‍රපට",
    "Kasun" : "කසුන්",
    "Kalhara" : "කල්හාර",
    "Sunil" : "සුනිල්",
    "Ariyarathna"   : "ආරියරත්න",
    "Dayasiri" : "දයාසිරි",
    "Jayasekara" : "ජයසේකර",
    "Daddy" : "ඩැඩී",
    "Nandasiri" : "නන්දසිරි",
    "Nanda" : "නන්දා",
    "Malani" : "මාලනී",
    "Somadasa" : "සෝමදාස",
    "Elvitigala" : "එල්විටිගල",
    "Gunadas" : "ගුණදාස",
    "Kapuge" : "කපුගේ",
    "Sanath" : "සනත්",
    "Edirisinghe" : "එදිරිසිංහ",
    "Baddaga" : "බැද්දගේ",
    "Baddage" : "බැද්දගේ",
    "Sekara" : "සේකර",
    "Bandara" : "බණ්ඩාර",
    "Ahaliyagoda" : "ඇහැලියගොඩ",
    "Dhanawalawithana" : "දනවල්විතාන",
    "Achala" : "ආචලා",
    "Solamans" : "සොලමන්ස්",
    "Pop" : "පොප්",
    "Golden" : "රන්වන්",
    "Old" : "පැරණි",
    "Oldies" : "පැරණි",
    "Classic" : "ශාස්ත්‍ර්‍රීය",
    "Movie" : "චිත්‍රපට",
    "Duets" : "යුගල",
    "duet" : "යුගල",
    "Duet":"යුගල",
    "Inspirational" : "උද්වේගකර",
    "Alwis" : "අල්විස්",
    "Victor" : "වික්ටර්",
    "Rathnayaka" : "රත්නායක",
    # "W" : "ඩබ්ලිව්",
    # "D" : "ඩී",
    "Amaradewa" : "අමරදේව",
    "Lahiru" : "ළහිරු",
    "Perera" :"පෙරේරා",
    "Cyril" : "සිරිල්",
    "Premakeerthi" : "ප්‍රේමකීර්ති",
    "Jothipala" : "ජෝතිපාල",
    "Priyadarshani" : "ප්‍රියදර්ශනී",
    "Deepika" : "දීපිකා",
    "Rohana" : "රෝහණ",
    "Weerasingha" : "වීරසිංහ",
    "Pradeep" : "ප්‍රදීප්",
    "Rangana" : "රංගන",
    "Angelin" : "ඇන්ජලීන්",
    "Gunathilaka" : "ගුණතිලක",
    "Karunarathna" : "කරුණාරත්න",
    "Karunaratna" : "කරුණාරත්න",
    "Abeysekara" : "අබේසේකර",
    "Divulgane" : "දිවුල්ගනේ",
    "Fernando" : "ප්‍රානන්දු",
    "Milton" : "මිල්ටන්",
    "Roksami" : "රොක්සාමි",
    "De": "ද",
    "Wijewardena": "විජේවර්ධන",
    "Clarence" : "ක්ලැරන්ස්",
    "Bulathsinhala" : "බුලත්සිංහල",
    "Premasiri" : "ප්‍ර්‍රේමසිරි",
    "Khemadasa" : "කේමදාස",
    "Gamage" : "ගමගේ",
    "Walpola" : "වල්පොල",
    "Latha" : "ලතා",
    "Gunawardhana" : "ගුණවර්ධන",
    "Attanayaka" : "අත්තනායක",
    "Sujatha" : "සුජාතා",
    "Kumarathunga" : "කුමාරතුංග",
    "Vijaya" : "විජය",
    "Silva" : "සිල්වා",
    "Unknown" : "නොදනී",
    "Rathna" : "රත්න",
    "Wijesinge" : "විජේසිංහ",
    "Jayamaha" : "ජයමහ",
    "Sri" : "ශ්‍රී",
    "Somathilaka" : "සෝමතිලක",
    "Mallawarachchi" : " මල්ලව ආරච්චි",
    "Dasanayaka" : "දසනායක",
    "Sarath" : "සරත්",
    "Lushan" : "ලූෂන්",
    "Somapala" : "සෝමපාල",
    "Mervin" : "මර්වින්",
    "Pandith" : "පණ්ඩිත්",
    "Edward" : "එඩ්වඩ්",
    "Jayakody" : "ජයකොඩි",
    "Sisira" : "සිසිර",
    "Senarathna" : "සෙනාරත්න",
    "Rookantha" : "රූකාන්ත",
    "Chandana"  : "චන්දන",
    "Liyanarachchi" : "ලියනාරච්චි",
    "Pieris" : "පීරිස්",
    "Stanley" : "ස්ටැන්ලි",
    "Muththusami" : "මුත්තුසාමි",
    "Ranasinghe" : "රණසිංහ",
    "Dharmawardhana" : "ධර්මවර්ධන",
    "Annesley" : "ඇනෙස්ලි",
    "Malawana" :"මල්වාන",
    "Dayarathna" : "දයාරත්න",
    "Saman" : "සමන්",
    "Gamhewa" : "ගම්හේවා",
    "Nihal" : "නිහාල්",
    "Kularathna" : "කුලරත්න",
    "Ariyawansa" : "ආරියවංස",
    "Soyza" : "සොයිසා",
    "Punsiri" : "පුන්සිරි",
    "Kumara" : "කුමාර",
    "Jayawardhana" : "ජයවර්ධන",
    "Weerasinghe" : "වීරසිංහ",
    "Blue" : "බ්ලූ",
    "Shadows" :"ෂැඩෝස්"
}


new_list =[ 
            "Dharmarathna Perera",
            "Saman Palitha Gamage",
            "Amitha Wedisinghe",
            "Somadasa Elvitigala",
            "Victor Dalugama",
            "Kamal",
            "Athma Liyanage",
            "Shantha Jayalath Thisera",
            "Siri Nihal Jayasingha",
            "S Dakshinamurthi",
            "R.B.Jayasingha",
            "Siha Shakthi",
            "Chandrarathna Manawasingha",
            "Yamuna Malani Perera",
            "Lakshman Wijesekara",
            "Wasantha B Dissanayaka",
            "Buddhadasa Galappaththi",
            "Anuradha Abeysinghe",
            "Malkanthi Nandasiri",
            "Dayarathna Ranatunga",
            "Ranil Jayasena",
            "Leelananda Gunawardhana",
            "Korin Almeda",
            "K.A.W.Perera",
            "Shirley Waijayantha",
            "Maya Damayanthi",
            "Sanuka Wickramasinghe",
            "Hurbet M Senevirathna",
            "Dayasiri Jayasekara",
            "Madhawa Hewawasam",
            "Kasun Kalhara",
            "Soorya Shankar Molligoda",
            "Ananda Samarakoon",
            "Saman Guna Herath",
            "A.J.Kareem",
            "Somadasa Elvitigala",
            "Uresha Ravihari",
            "Navarathna Gamage",
            "Ashoka Kowilage",
            "Ajith Bandara",
            "Vernon Perera",
            "Rev Lenus Mendis",
            "Athma Liyanage",
            "Channa Jayanath",
            "Ruwan Hettiarchchi",
            "Nathasha Perera",
            "Sandya Bulathsinhala",
            "Hudson Samarasinghe",
            "Janaka Wickramasinghe"
            ]

tr_list=[
"ධර්මරත්න පෙරේරා",
"සමන් පාලිත ගමගේ",
"අමිත වැදිසිංහ",
"සෝමදාස ඇල්විටිගල",
"වික්ටර් දලුගම",
"කමල්",
"ආත්මා ලියනගේ",
"ශාන්ත ජයලත් තිසේරා",
"සිරි නිහාල් ජයසිංහ",
"එස්.දක්ෂිණ්මූර්ති",
"ආර්.බී.ජයසිංහ",
"සිහ ශක්ති",
"චන්ද්‍රරත්න මානවසිංහ",
"යමුනා මාලනී පෙරේරා",
"ලක්ෂ්මන් විජේසේකර",
"වසන්ත බී.දිසානායක",
"බුද්ධධාස ගලප්පත්ති", 
"අනුරාධ අබේසිංහ",
"මල්කාන්ති නන්දසිරි",
"දයාරත්න රනතුංග",
"රනිල් ජයසේන",
"ලීලනන්ද ගුණවර්ධන",
"කොරින් අල්මේදා",
"කේ.ඒ.ඩබ්.පෙරේරා",
"ෂර්ලි වයිජයන්ත",
"මායා දමයන්ති ",
"සනුක වික්‍රමසිංහ ",
"හර්බට්  එම්.සෙනෙවිරත්න", 
"දයාසිරි ජයසේකර",
"මාධව හේවාවසම්",
"කසුන් කල්හාර",
"සූර්‍යා ශන්කර් මොල්ලිගොඩ",
"ආනන්ද සමරකෝන්",
"සමන් ගුණහේරත්",
"ඒ.ජේ.කරීම්",
"සෝමදාස ඇල්විටිගල",
"උරේශා රවිහාරි",
"නවරත්න ගමගේ",
"අශෝක කෝවිලගේ",
"අජිත් බන්ඩාර",
"වනෝන් පෙරේරා",
"ලේනුස් මෙන්ඩිස්",
"ආත්මා ලියනගේ",
"චන්න ජයනාත්",
"රුවන් හෙට්ටිආරච්චි", 
"නතාශා පෙරේරා", 
"සන්ද්‍යා බුලත්සිංහල", 
"හඩ්සන් සමරසිංහ",
"ජනක වික්‍රමසිංහ"]

dict_keys = dict_ref.keys()
refactored_list =[]
with open('lyrics.json' , encoding='utf-8') as infile:
  object_list = json.load(infile)

for object in object_list:
    for key,value in object.items():
        if(key in ['artist','writer','music','genre']):
            # for i in range(0,len(new_list)):
             object[key] = object[key].replace("කෂාරා කල්හාරා","කසුන් කල්හාර")
         
    refactored_list.append(object)

with open('lyrics.json','w',encoding='utf-8') as outfile:
  json.dump(refactored_list,outfile,indent=4,ensure_ascii=False)