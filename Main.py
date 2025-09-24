# _____________________________________________IMPORT & SETUP_____________________________________________
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from tensorflow.keras.models import load_model
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import re
import easyocr
import difflib
import pytesseract 
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Carica immagine 
lingueOCR = easyocr.Reader(['en','fr','de','it','es','pl'])

# _____________________________________________CONFIG PATH_____________________________________________
MODELLO_MACRO = r"C:\Users\Calfi\Desktop\Python BitCamp\Python\Progetto Alfio - Riconoscimento Carte\dataset\bestmacro.keras"
MODELLO_BRISCOLA = r"C:\Users\Calfi\Desktop\Python BitCamp\Python\Progetto Alfio - Riconoscimento Carte\dataset\bestbriscola.keras"

# _____________________________________________CARICO I MODELLI_____________________________________________
modello_macro = load_model(MODELLO_MACRO)
modello_briscola = load_model(MODELLO_BRISCOLA)
# _____________________________________________ARTISTI CHECK_____________________________________________
artisti_one = [
"Dai-XT",
"Shosuke",
"Sunohara",
"Kankurou",
"Yosuke Adachi",
"Phima",
"Nihihayashi",
"Nijima Arc",
"BISAI",
"Akira Egawa",
"Rina Usui",
"BerryVerrine",
"Ryuda",
"Kano Akirara",
"Koushi Rokushiro",
"Misa Matoki",
"Hatori Kyouka",
"Makitoshi",
"Anderson",
"Hashimoto Q.",
"Hagane Tsurugi",
"Hisashi Hujiwara",
"Nekobayashi",
"K Akagisi",
"Tapioca",
"Studio Vigor co. ltd",
"Touge369",
"Akihiro Miyano",
"Moopic",
"Suemi Jun",
"Hayaken-sarena",
"Mutsumi Sasaki",
"Suzume Muraichi",
"Kaito Shibano",
"Misa Tsutsui",
"Yuu Shimotsuki",
"Yamada Rokkaku",
"Tatsuya"
]

artisti_digi = [
"61",
"As'Maria",
"Aurola",
"Banira",
"BIRU YAMAGUCHI",
"Capitan Artiglio",
"DAI-XT.",
"E Volution",
"Funbolt",
"Gamazo",
"Gosha",
"GOSSAN",
"GS",
"Hisashi Fujiwara",
"Hokuyuu",
"Hokyyuu",
"Iori Sunakura",
"Irasa",
"Ishibashi Yosuke",
"Itohiro",
"IWAO",
"K.Dra",
"Kagemaru Himeno",
"Kanchi Fukunari",
"Kariki Hakime",
"Kayo Horaguchi",
"Kaz",
"Kazumasa Yasukuni",
"Keita Amemiya",
"Kenji Watanabe",
"Kirita",
"KISUKE",
"Koidetaku",
"Koki",
"Kuromori maya",
"MATSUMOTO EIGHT",
"Media.Vision Inc.",
"MINAMINAMI Take",
"Minato Sashima",
"Mojuke",
"Moyasi",
"Murakami Hisashi",
"NAKAMURA 8",
"Nakano Haito",
"NAKASHIMA YUUKI",
"Naochika Morishita",
"NAOKI AKAMINE",
"Naru",
"NIJIMAARC",
"Okada Anmitsu",
"P!k@ru",
"PLEX Fumiya Kobayashi",
"Poroze",
"Qacoro",
"Robomisutya",
"Ryodan",
"Ryuda",
"Sanosuke Sakuma",
"Sasasi",
"Satsuki may",
"SENNSU",
"Shigeo Niwa",
"Shin Sasaki",
"Shosuke",
"Shoyama Seihou",
"Soh Moriyama",
"Souichirou Gunjima",
"Spareribs",
"Sunohara",
"Suzuhito Yasuda",
"Takase",
"Takeuchi Moto",
"Takumi Kousaka",
"TANIMESO",
"TENYA YABUNO",
"Teppei Tadokoro",
"Tessy",
"Tomotake Kinoshita",
"Tonamikanji",
"Toriyufu",
"TSCR",
"Tsunemi Aosa",
"Tyuga",
"UnnoDaisuke",
"YAMURETSU",
"Yuki Mukai",
"Yuuki."
]

artisti_magic = [
"Aaron Boyd",
"Aaron Miller",
"Adam Paquette",
"Adam Rex",
"Adi Granov",
"Adrian Majkrzak",
"Adrian Smith",
"Ai Desheng",
"Al Davidson",
"Alan Pollack",
"Alan Rabinowitz",
"Alayna Danner",
"Alejandro Mirabal",
"Aleksi Briclot",
"Alex Brock",
"Alex Horley-Orlandelli",
"Alex Konstad",
"Alexander Forssberg",
"Alisa Lee",
"Allen Williams",
"Allison Carl",
"Alton Lawson",
"Amy Weber",
"Anastasia Ovchinnikova",
"Andi Rusu",
"Andrea Radeck",
"Andreas Rocha",
"Andrew Goldhawk",
"Andrew Murray",
"Andrew Robinson",
"Andrey Kuzinskiy",
"Anna Podedworna",
"Anna Steinbauer",
"Anson Maddocks",
"Anthony Francisco",
"Anthony Jones",
"Anthony Palumbo",
"Anthony S. Waters",
"Antonio José Manzanedo",
"April Lee",
"Ariel Olivetti",
"Arnie Swekel",
"Ash Wood",
"Austin Hsu",
"Babyson Chen & Uzhen Lin",
"Bartłomiej Gaweł",
"Bastien L. Deharme",
"Bayard Wu",
"BD",
"Ben Maier",
"Ben Thompson",
"Ben Wootten",
"Berry",
"Bill Sienkiewicz",
"Billy Christian",
"Blackie del Rio",
"Bob Eggleton",
"Bob Petillo",
"Brad Rigney",
"Bradley Williams",
"Bram Sels",
"Brandon Dorman",
"Brandon Kitkouski",
"Brian Despain",
"Brian Durfee",
"Brian Horton",
"Brian Snøddy",
"Samuel Perin",
"Christina Kraus",
"Winona Nelson",
"Irina Nordsol",
"Anato Finnstark",
"Kev Walker",
"Thanh Thuan",
"Victor Harmatiuk",
"Raymond Swanland",
"Brian Valeza",
"Borja Pindado",
"Bruno Biazotto",
"Brom",
"Bryan Sola",
"Bryan Talbot",
"Brynn Metheney",
"Bryon Wackwitz",
"Bud Cook",
"Cai Tingting",
"Caio Monteiro",
"Campbell White",
"Cara Mitten",
"Carl Critchlow",
"Carl Frank",
"Carol Heyer",
"Catherine Buck",
"Cecil Fernando",
"Charles Gillespie",
"Chase Stone",
"Chen Weidong",
"Chengo McFlingers",
"Chippy",
"Chris Appelhans",
"Chris Dien",
"Chris Rahn",
"Chris Rallis",
"Christine Choi",
"Christopher Burdett",
"Christopher Moeller",
"Christopher Rush",
"Chuck Lukacs",
"Ciruelo Cabral",
"Cliff Childs",
"Cliff Nielsen",
"Clint Cearley",
"Clint Langley",
"Clyde Caldwell",
"Cole Eastburn",
"Colin MacNeil",
"Corey D. Macourek",
"Cornelius Brudi",
"Craig Hooper",
"Craig J. Spearing",
"Craig Mullins",
"Cris Dornaus",
"Cynthia Sheppard",
"Cyril van der Haegen",
"D. Alexander Gregory",
"D. J. Cleland-Hura",
"Daarken",
"Dameon Willich",
"Dan Dos Santos",
"Dan Frazier",
"Dan Scott",
"Dan Seagrave",
"Dana Knutson",
"Daniel Gelon",
"Daniel Ljunggren",
"Daniel R. Horne",
"Darbury Stenderu",
"Darek Zabrocki",
"Daren Bader",
"Darrell Riche",
"Dave Allsop",
"Dave DeVries",
"Dave Dorman",
"Dave Kendall",
"Dave Seeley",
"David A. Cherry",
"David Day",
"David Gaillet",
"David Ho",
"David Horne",
"David Hudnut",
"David Martin",
"David Monette",
"David O'Connor",
"David Palumbo",
"David Rapoza",
"David Robert Hovey",
"David Seguin",
"Dennis Detwiller",
"Dermot Power",
"Deruchenko Alexander",
"Diana Vick",
"Ding Songjian",
"Dom!",
"Dominick Domingo",
"Don Hazeltine",
"Donato Giancola",
"Doug Chaffee",
"Douglas Shuler",
"Drew Tucker",
"Dylan Martens",
"E. M. Gist", 
"Edward P. Beard Jr.", 
"Efflam Mercier",
"Efrem Palacios",
"Eric David Anderson",
"Eric Fortune",
"Eric Peterson",
"Eric Polak",
"Eric Velhagen",
"Erica Yang",
"Esad Ribic",
"Evan Shipard",
"Eytan Zana",
"Fang Yue",
"Fay Jones",
"Filip Burburan",
"Florian de Gesincourt",
"Francis Tsai",
"Frank Kelly Freas",
"Franz Vohwinkel", 
"Fred Fields", 
"Fred Harper", 
"Fred Rahmqvist", 
"Gabor Szikszai", 
"Gao Jianzhang", 
"Gao Yan", 
"Garry Leach", 
"Gary Ruddell", 
"Geofrey Darrow", 
"George Pratt", 
"Gerry Grace", 
"Glen Angus", 
"Glenn Fabry", 
"Goran Josic", 
"Greg Bobrowski", 
"Greg Hildebrandt", 
"Greg Opalinski", 
"Greg Simanson", 
"Greg Staples", 
"Grzegorz Rutkowski",
"Hannibal King", 
"Harold McNeill", 
"He Jiancheng", 
"Erica Gassalasca-Jape", 
"Heather Hudson", 
"Henry G. Higgenbotham", 
"Henry van der Linde", 
"Hideaki Takamura", 
"Hiro Izawa", 
"Hong Yan", 
"Howard Lyon", 
"Huang Qishi", 
"Hugh Jamieson", 
"I. Rabarot", 
"Iain McCaig", 
"Ian Miller", 
"Igor Kieryluk",
"Ilse Gort", 
"Isis Sangaré", 
"Ittoku", 
"Izzy", 
"Medrano", 
"Jack Wang", 
"Jack Wei", 
"Jacques Bredy", 
"Jaime Jones", 
"Jakub Kasper", 
"Jama Jurabaev", 
"James Ernest", 
"James Kei", 
"James Paick", 
"James Ryman", 
"James Zapata", 
"Janet Aulisio", 
"Janine Johnston",
"Jarreau Wimberly", 
"Jason A. Engle", 
"Jason Alexander Behnke", 
"Jason Chan", 
"Jason Felix", 
"Jason Kang", 
"Jason Rainville", 
"Jasper Sandner", 
"Jean-Sébastien Rossbach", 
"Jeff A. Menges", 
"Jeff Easley", 
"Jeff Laubenstein", 
"Jeff Miracola", 
"Jeff Nentrup", 
"Jeff Reitz", 
"Jeff Remmer", 
"Jeff Simpson", 
"Jeffrey R. Busch", 
"Jehan Choo", 
"Jen Page", 
"Jennifer Law", 
"Jeremy Enecio", 
"Jeremy Jarvis", 
"Jerry Tiritilli", 
"Jesper Ejsing", 
"Jesper Myrfors", 
"Ji Yong", 
"Jiaming", 
"Jiang Zhuqing", 
"Jim Murray", 
"Jim Nelson", 
"Jim Pavelec", 
"Mark JOCK Simpson", 
"Joel Biske", 
"Joel Thomas", 
"Johann Bodin", 
"Johannes Voss", 
"John Avon", 
"John Bolton", 
"John Coulthart",
"John Donahue", 
"John Gallagher", 
"John Howe", 
"John Malloy", 
"John Matson", 
"John Severin Brassell",
"John Stanko", 
"John Zeleznik", 
"Jon Foster", 
"Jon J. Muth", 
"Jonas De Ro", 
"Jonathan Kuo", 
"Jose Cabrera", 
"Joseph Meehan", 
"Josh Hass", 
"Joshua Hagler",
"Julie Baroh", 
"Jung Park", 
"Junich Inoue", 
"Junior Tomlin", 
"Junko Taguchi", 
"Justin Hampton", 
"Justin Murray", 
"Justin Sweet", 
"Kaja Foglio", 
"Kang Yu", 
"Kari Johnson", 
"Karl Kopinski", 
"Karla Ortiz", 
"Kathryn Rathke", 
"Keith Garletts", 
"Keith Parkinson", 
"Ken Meyer Jr", 
"Kensuke Okabayashi", 
"Kerstin Kaman", 
"Kev Brockschmidt", 
"Kevin 'Kev' Walker", 
"Kevin Dobler", 
"Kevin Murphy", 
"Khang Le", 
"Kieran Yanner", 
"Kipling West", 
"Kirsten Zirngibl", 
"Koji", 
"Kristen Bishop",
"Ku Xueming", 
"Kuang Sheng", 
"L. A. Williams", 
"LHQ", 
"Lake Hurwitz", 
"Larry Elmore", 
"Larry MacDougall", 
"Lars Grant-West", 
"Lawrence Snelly", 
"Li Tie", 
"Li Wang", 
"Li Xiaohua", 
"Li Youliang", 
"Li Yousong", 
"Lie Tiu", 
"Lin Yan", 
"Lindsey Look", 
"Liu Jianjian", 
"Liu Shangying", 
"Lius Lasahido", 
"Livia Prima", 
"Liz Danforth", 
"Lou Harrison", 
"Lubov", 
"Luca Zontini", 
"Lucas Graciano", 
"Lucio Parrillo", 
"M. W. Kaluta", 
"Magali Villeneuve", 
"Marc Fishman", 
"Marc Simonetti", 
"Marcelo Vignali", 
"Marco Nelor", 
"Margaret Organ-Kean", 
"Mark Brill", 
"Mark Harrison", 
"Mark A. Nelson", 
"Mark Poole", 
"Mark Romanoski", 
"Mark Rosewater", 
"Mark Tedin", 
"Mark Winters", 
"Mark Zug", 
"Martin McKenna", 
"Massimilano Frezzato",
"Mathias Kollros", 
"Matt Cavotta", 
"Matt Stawicki", 
"Matt Stewart", 
"Matt Thompson", 
"Matthew D. Wilson", 
"Matthew Mitchell", 
"Melissa A. Benson", 
"Miao Aili", 
"Michael Bruinsma", 
"Michael Danza", 
"Michael Koelsch", 
"Michael Komarck", 
"Michael Phillippi",
"Matteo Bassini", 
"Michael Ryan", 
"Michael Sutfin", 
"Michael Weaver", 
"Michael Whelan", 
"Mike Bierek", 
"Mike Dringenberg", 
"Mike Kerr", 
"Mike Kimble", 
"Mike Ploog", 
"Mike Raabe", 
"Mike Sass", 
"Min Yum", 
"Miranda Meeks",
"Mitch Cotie",
"Mitsuaki Sagiri",
"Monte Michael Moore", 
"Naomi Baker", 
"Nathalie Hertz", 
"Nelson DeCastro", 
"Nene Thomas", 
"Nick Percival", 
"Nicola Leonard", 
"Nils Hamm", 
"Noah Bradley", 
"Nottsuo", 
"Omaha Pérez", 
"Omar Rayyan", 
"Paolo Parente", 
"Pat Lee", 
"Pat Morrissey",
"Patrick Beel", 
"Patrick Ho", 
"Patrick Kochakji", 
"Paul Bonner", 
"Paul Chadwick", 
"Paul Lee", 
"Pete Venters", 
"Peter Bollinger", 
"Peter Mohrbacher", 
"Phil Foglio", 
"Philip Mosness", 
"Philip Straub", 
"Philip Tan", 
"Phill Simmer", 
"Piotr Dura", 
"Puddnhead", 
"Qi Baocheng", 
"Qiao Dafu", 
"Qin Jun", 
"Qu Xin", 
"Quan Xuejun",
"Quinton Hoover", 
"Raf Sarmento", 
"Ralph Horsley", 
"Randy Asplund-Faith", 
"Randy Elliott", 
"Randy Gallegos", 
"Randy rk Post", 
"Randy Vargas", 
"Raoul Vitale", 
"Ray Lago", 
"Raymond Swanland",
"Rebecca Guay", 
"Rebekah Lynn", 
"Richard Kane Ferguson", 
"Richard Sardinha", 
"Richard Thomas", 
"Richard Whitters", 
"Richard Wright", 
"Rick Berry", 
"Rick Emond", 
"Rick Farrell", 
"Rob Alexander", 
"Robert Bliss", 
"Robh Ruppel", 
"Roger Raupp", 
"Rogério Vilela", 
"Romas Kukalis", 
"Ron Brown", 
"Ron Chironna", 
"Ron Spencer", 
"Ron Walotsky", 
"Ruth Thompson", 
"Ryan Alexander Lee", 
"Ryan Barger", 
"Ryan Pancoast", 
"Ryan Yee", 
"Sal Villagran", 
"Sam Guay", 
"Sam Wood", 
"Sandra Everingham", 
"Sara Winters", 
"Scott Altmann", 
"Scott Bailey", 
"Scott M. Fischer", 
"Scott Hampton", 
"Scott Kirschner", 
"Scott Murphy", 
"Sean McConnell", 
"Sean Murray", 
"Sean Sevestre", 
"Seb McKinnon", 
"Shang Huitong", 
"Shelly Wan", 
"Shishizaru",
"Shikee", 
"Sidharth Chaturvedi", 
"Slawomir Maniak", 
"Solomon Au Yeung", 
"Song Shikai", 
"Stephanie Pui-Mun Law", 
"Stephen Daniele", 
"Stephen L. Walsh",
"Steve Argyle", 
"Steve Ellis", 
"Steve Firchow", 
"Steve Luke", 
"Steve Prescott", 
"Steve White", 
"Steven Belledin", 
"Stuart Griffin", 
"Sue Ellen Brown", 
"Sun Nan", 
"Sung Choi", 
"Susan Van Camp",
"Svetlin Velinov", 
"Tang Xiaogu", 
"Ted Naifeh", 
"Terese Nielsen",
"Terry Springer",
"Thomas M. Baxa", 
"Thomas Denmark", 
"Thomas Gianni", 
"Tianhua Xu", 
"Tim Hildebrandt",
"Titus Lunter",
"Todd Lockwood",
"Tom Babbey",
"Tom Fleming",
"Tom Kyffin", 
"Tom Wänerstrand", 
"Tomas Giorello", 
"Tomasz Jedruszek", 
"Tommy Arnold", 
"Tony DiTerlizzi",
"Tony Foti", 
"Tony Roberts", 
"Tony Szczudlo", 
"Torstein Nordstrand", 
"Trevor Claxton", 
"Trevor Hairsine", 
"Tsutomu Kawade", 
"Tyler Jacobson", 
"Una Fricker", 
"Vance Kovacs", 
"Véronique Meignaud", 
"Véronique Paquereau", 
"Véronique Petit", 
"Victor Adame Minguez", 
"Victor Maury", 
"Victor Nizov", 
"Vincent Proce", 
"Viktor Titov", 
"Wang Wei", 
"Wang Xin", 
"Wayne England", 
"Wayne Reynolds", 
"Wei Wang", 
"Wenhua Guo", 
"William O'Connor", 
"Willy Engel", 
"Wlop", 
"Wojciech Kwiatkowski", 
"Xiao Li", 
"Xin Rui", 
"Xuefeng Yang", 
"Yongjae Choi", 
"Yongqing Liu", 
"Yongxuan Li",
"Yoshitaka Amano", 
"Yu Yang", 
"Yuefeng Liu", 
"Yun Long", 
"Zack Stella", 
"Zhang Yin", 
"Zhao Ling", 
"Zhu Dawei", 
"Zoltan Boros"
]
artisti_poke = [
"0313",
"5ban Graphics",
"2017 Pikachu Project",
"2019 Pikachu Project",
"Acorviart",
"Aimi Tomita",
"Akagi",
"Akino Fujuki",
"Akira Komayama",
"Aky CG Works",
"AKIRA EGAWA",
"Amelicart",
"Anae Dynamic",
"Arai Kiriko",
"Asako Ito",
"Atsuko Nishida",
"Atsuko Ujiie",
"Atsushi Furusawa",
"Avec Yoko",
"ashy",
"ashley",
"Benimaru Itoh",
"BERUBURI",
"'Big Mama' Tagawa",
"Bun Toujo",
"chibi",
"Cona Nitanda",
"ConceptLab",
"Craig Turvey",
"CR CG gangs",
"DOM",
"D.A.G Inc.",
"Daisuke Ito",
"Daisuke Iwamoto",
"DemizuPosuka",
"Dsuke",
"Emi Ando",
"Emi Miwa",
"Emi Yoshida",
"En Morikura",
"Eske Yoshinob",
"Gapao",
"Gabi",
"Gemi",
"GIDORA",
"GOSSAN",
"Haru Akasaka",
"Hataya",
"Hazuki Misono",
"Hikaru Koike",
"Hiroaki Ito",
"Hiroki Asanuma",
"Hiroki Fuchino",
"Hiroyuki Yamamoto",
"Hitoshi Ariga",
"Huang Tzu En",
"hncl",
"hyogonOSUKE",
"Jiro Sasumo",
"Jerky",
"Julie Hang",
"Junsei Kuninobu",
"K. Hoshiba",
"K. Utsunomiya",
"kai Ishikawa",
"kantaro",
"Kasumi Matsuda",
"Kazuaki Aihara",
"Kazuma Koda",
"Kazuo Yazawa",
"Keita Komatsuya",
"Keiko Fukuyama",
"Keiko Moritsugu",
"Keisin",
"Kent Kanetsuna",
"Kimiya Masago",
"kinu Nishimura",
"kirisAki",
"Kodama",
"Kouichi Ooyama",
"Kouji Tajima",
"Kouki Saitou",
"Kurata So",
"Kuroimori",
"Kyoko Koizumi",
"Kyoko Umemoto",
"Lee HyunJung",
"Ligton",
"M. Akiyama",
"Makoto Imai",
"Mana Ibe",
"Mark Kraus",
"Masaako Tomii",
"Masakazu Fukuda",
"Masako Yamashita",
"matazo",
"Megumi Higuchi",
"Megumi Mizutani",
"Mikiko Takeda",
"Mikio Menjo",
"Mina Nakai",
"Misa Tsutsui",
"Mousho",
"MPC Film",
"MUGENUP",
"Motofumi Fujiwara",
"Mt. TBT",
"N-DESIGN Inc.",
"Naoki Saito",
"Nabana Kensaku",
"Nakaoka",
"Natsumi Yoshida",
"NELNAL",
"Nisota Niso",
"Nobuyuki Fujimoto",
"Nobuhiro Imagawa",
"Noriko Hotta",
"Noriko Takaya",
"Noriko Uono",
"Nurikabe",
"NC Empire",
"OKACHEKE",
"OKUBO",
"Oku",
"ORBITALLINK Inc.",
"oswaldo KATO",
"Pani Kobayashi",
"Po-Suzuki",
"Pokémon Rumble",
"PLANETA",
"PLANETA Hiiragi",
"PLANETA Igarashi",
"PLANETA Mochizuki",
"PLANETA Otani",
"PLANETA Tsuji",
"PLANETA Yamashita",
"Reiko Tanoue",
"REN D",
"Rhivern",
"Ryo Ueda",
"Ryota Murayama",
"Ryota Saito",
"Ryuta Fuse",
"Ryuta Kusumi",
"Sachiko Adachi",
"Sachiko Eba",
"Sadaji",
"Sai no Misaki",
"satoma",
"Sanosuke Sakuma",
"Satoshi Ohta",
"Satoshi Shirai",
"Sawamura Yuichi",
"Scav",
"Sekio",
"Shiburingaru",
"Shibuzoh.",
"Shin Nagasawa",
"Shin-ichi Yoshida",
"Shin-ichi Yoshikawa",
"Shinji Kanda",
"Shinji Higuchi",
"Shigenori Negishi",
"Shin-ichi Yoshida",
"Souichirou Gunjima",
"sowsow",
"Studio Bora Inc.",
"Sylvia Forrest",
"Taiga Kayama",
"Taiga Kasai",
"takuyoa",
"Takeshi Nakamura",
"Taira Akitsu",
"Takao Unno",
"Takabon",
"Takumi Akabane",
"Takumi Wada",
"Tatsuya Honda",
"Teeziro",
"Tetsu Kayama",
"Tomokazu Komiya",
"Tomomi Kaneko",
"Tomomi Ozaki",
"Tomoko Wakai",
"Tonji Matsuno",
"TOKIYA",
"Toriyufu",
"Tsuji",
"UsGMEN",
"Uta",
"Yano Keiji",
"Yasuki Watanabe",
"Yoriyuki Ikegami",
"Yoshinobu Saito",
"Yoshioka",
"Yosuke Da Silva",
"Yousuke Hirata",
"Yuka Morii",
"Yuichi Sawayama",
"Yuya Oka",
"Yuu",
"zig",
"Zu-Ka"
]


# _____________________________________________DIZIONARI INDICE_____________________________________________
nomi_macro = {
    0: "Briscola",
    1: "Digimon",
    2: "Dragon Ball",
    3: "Francesi",
    4: "Magic: The Gathering",
    5: "One Piece",
    6: "Pokémon",
    7: "Salisburgo",
    8: "Union Arena",
    9: "Yu-Gi-Oh",
}

nomi_briscola = {
    0: "Bergamasche",
    1: "Bolognesi",
    2: "Bresciane",
    3: "Genovesi",
    4: "Milanesi",
    5: "Milanesi 800",
    6: "Napoletane",
    7: "Piacentine",
    8: "Romagnole",
    9: "Romane",
    10: "Sarde",
    11: "Siciliane",
    12: "Toscane",
    13: "Trentine",
    14: "Trevigiane",
    15: "Triestine",
}
# _____________________________________________STORIE DELLE CARTE_____________________________________________
storie_macro = {
    "Briscola": "Origini: Italia, primi riferimenti 1828; derivata dai giochi francesi “brusquembille” e “bazzica”. \nVarianti:\nBriscola Chiamata (Piemonte), Briscola Scoperta (Sicilia), Briscola a quattro.\nOgni regione ha le proprie tradizioni e stili artistici.\nCarte notevoli: nei mazzi storici, figure artistiche come quelle di Enrico Sacchetti (anni ’40-’50) sono ricercate dai collezionisti; i semi italiani spesso rappresentano figure locali.\nChicca da collezione: mazzi vintage con illustrazioni di folklore o celebri personaggi storici italiani (alcuni pezzi da museo) possono arrivare a centinaia di euro se in ottime condizioni.",
    "Digimon": "Origini: 1997, Bandai,Akiyoshi Hongo, virtual pet derivato dai Tamagotchi; anime 1999. \nCarte iconiche:\nWarGreymon (1a edizione, 1999) – alta richiesta tra i collezionisti.\nMetalGarurumon – artwork originale di Kenji Watanabe.\nArtisti e collaborazioni:\nKenji Watanabe, anche character designer per Pokémon, supervisionava gli artwork. Alcuni set speciali hanno artwork unici da eventi giapponesi (feste dei fan, convention).\nChicche: carte rare promo distribuite solo in eventi giapponesi possono superare i 200€ cadauna in collezione.\nLo sapevi? Akiyoshi Hongo è lo pseudonimo del trio che ha dato vita a Digimon (Che è l'abbreviazione di Digital Monster), ovvero Aki Maita (Uno dei creatori dei Tamagotchi), Hiroshi Izawa(Autore del primo fumetto di Digimon) e Takeichi Hongo(Diretto Marketing di bandain nel 1997)",
    "Dragon Ball": "Origini: manga 1984, anime 1986, Akira Toriyama. Ad Oggi lo Shonen(tipologia di riferimento, in questo caso : per ragazzi)più famoso al mondo e che ha cambiato il modo di disegnare e scrivere queste storie (prima di lui solo Tezuka).\nCarte da collezione:\nDragon Ball Z Carddass Serie 1 (1990) – “Super Saiyan Goku” e “Vegeta 1a forma” sono iconiche.\nAlcune carte holo e limited edition, come le “Daizenshuu Promo”, sono pezzi da collezione che raggiungono centinaia di euro.\nArtisti e chicche: Toriyama supervisionava i disegni principali; i card designer giapponesi spesso riprendevano storyboard dell’anime per rendere le pose dinamiche.\nCuriosità: alcune carte Carddass originali venivano vendute in bustine con mini-poster di Toriyama; oggi pezzi introvabili.",
    "Francesi": "Nate nel 16° secolo, generalmente attribuite a Pierre Maréchal, realizzate nel 1567 a Rouen, uno dei maggiori centri di produzione cartaria dell'epoca. Secondo il modello parigino, ciascura figura rappresenta un personaggio storico, biblico e mitologico.\nRe di Picche: David (re d’Israele)\n Re di Cuori: Carlo Magno\nRe di Quadri: Giulio Cesare\nRe di Fiori: Alessandro Magno\nRegina di Picche: Pallade, la dea della strategia in battaglia\nRegina di Cuori: Giuditta, un personaggio della Bibbia protagonista di un aneddoto ambientato all’epoca del re babilonese Nabucodonosor\nRegina di Quadri: Rachele, la consorte prediletta di Giacobbe\nRegina di Fiori: Argine; probabilmente un semplice anagramma di “regina” ma, secondo un’altra ipotesi, un riferimento ad Argea, madre di Argo e moglie di Polibio\nFante di Picche: Ogier il Danese, protagonista di una chanson de geste medievale\nFante di Cuori: Étienne de Vignolles, detto “La Hire”, condottiero francese protagonista della Guerra dei Cento Anni\nFante di Quadri: Ettore, l’eroe omerico\nFante di Fiori: Lancillotto",
    "Magic: The Gathering": "Origini: 1993, Richard Garfield, Wizards of the Coast. Definito IL GIOCO di carte per eccellenza..\nCarte iconiche e rare:\nBlack Lotus (Alpha/Beta) – fino a 500.000€ per copia mint.\nMox Sapphire, Mox Jet, Mox Ruby, Mox Pearl, Mox Emerald – le “Power Nine”, fondamentali per i collezionisti.\nAncestral Recall, Time Walk – leggendarie, prime edizioni rarissime.\nArtisti: Terese Nielsen, Rebecca Guay, Amy Weber, Dan Frazier.\nChicche: collaborazioni con Dungeons & Dragons, promo Secret Lair con artisti contemporanei famosi, carte foil limited, carte errori di stampa ricercatissime dai collezionisti.",
    "One Piece": "Origini: 22 luglio 1997, Eiichirō Oda, col sogno di rivisitare la pirateria! Raccontandola come storia di libertà, sogni, speranza personale e dei popoli oppressi..\nCarte iconiche: \nBandai TCG set iniziale (2002-2005) – “Monkey D. Luffy Gear Second”, “Gol D. Roger” limited edition.\nArtisti e chicche: artwork creati dai collaboratori di Oda, alcune carte promozionali in Giappone hanno illustrazioni uniche mai stampate nel resto del mondo.\nCuriosità: le prime promo distribuite nei Jump Festa sono pezzi da collezione, alcune con numeri seriali limitati! Tra cui una carte disegnata e firmata in oro da Oda stesso.",
    "Pokémon": "Origini: 1996, Satoshi Tajiri, che aveva una visione molto diversa da ciò che è diventato ora il brand Pokemon.\nCarte iconiche:\nCharizard Base Set (1999) – carta più ricercata.\nPikachu Illustrator (1998) – unica al mondo, valore oltre 200.000€.\nFirst Edition Base Set – holo cards come Blastoise e Venusaur molto ricercate.\nArtisti:\nKen Sugimori(Il numero 1, creatore indiscusso del brand),\nMitsuhiro Arita (numero 11, due volte numero 1, artwork magnifici e stile UNICO! A lui si devono tra le carte più belle), Ryo Ueda e altri.\nChicche: le prime carte giapponesi avevano piccole differenze di colore, errori di stampa diventati leggenda. In italia furono distribuite con forti errori di Holografia e alterazioni. Agli albori fu Wizard of the Coast (Magic the Gathering) a distruibirle nel mondo.",
    "Salisburgo": "Origini: metà Ottocento, derivazione da mazzi bavaresi e tirolesi.\nCarte iconiche: figure allegoriche, scene di caccia, personaggi storici tirolesi.\nChicca da collezione: i mazzi intatti, con incisioni originali, sono ricercatissimi dai collezionisti europei, specialmente pezzi firmati o numerati.",
    "Union Arena": "Origini: TCG Bandai, moderno, connette anime e giocatori. Nato col puro scopo di unire questi due mondi e accontentare i fan.\nCarte iconiche: carte promo rare con personaggi principali delle serie Bandai.\nArtisti: studi giapponesi partner di Bandai, spesso collaborazioni dirette con i designer degli anime.\nChicca: alcune carte hanno artwork digitali unici integrati nelle app Bandai, pezzi unici per collezionisti digitali e fisici.",
    "Yu-Gi-Oh": "Origini: TCG Konami, 30 settembre 1996, Kazuki Takahashi (Creatore del fumetto).\nCarte iconiche:\nBlue-Eyes White Dragon (1999) – prima edizione giapponese e internazionale, molto ricercata.\nDark Magician – artwork originale Takahashi, prima edizione rarissima.\nExodia the Forbidden One – pezzo leggendario per collezionisti.\nArtisti e chicche:\nTakahashi supervisionava gli artwork originali, alcune promo distribuite solo in Giappone durante eventi, fino a 10.000€ per pezzi in mint condition.\nCuriosità: carte errori di stampa (stampa doppia, colori invertiti) sono tra le più ricercate al mondo dai collezionisti hardcore.\n Konami per un veto non ha mai esposto i nomi dei propri artisti nelle carte, lasciando così un alone di mistero su chi ha creato quelle magnifiche creature."
}

storie_briscola = {
    "Romagnole": "Le carte romagnole affondano le loro radici nel XIV secolo, quando il gioco delle carte iniziò a diffondersi in Italia. La Romagna, una regione con una ricca storia culturale, adottò uno stile rustico e tradizionale per disegnare le sue carte, caratterizzato da disegni e simboli unici, che riflettono la tradizione e la vita quotidiana appartenente all’epoca.Durante i secoli XV e XVII, le carte romagnole continuarono a evolversi. Il design divenne più raffinato, con l’introduzione di nuovi simboli e figure. Questo periodo vide anche la standardizzazione dei semi (Coppe, Denari, Spade e Bastoni), che sono ancora in uso oggi. I mazzi erano spesso realizzati a mano da artigiani locali e riflettevano l’estetica dell’epoca.Nel XX secolo, le carte romagnole subirono ulteriori cambiamenti con l’introduzione della stampa offset e di nuovi materiali, come la plastica. Questo rese le carte più durevoli e accessibili a un pubblico più ampio. Il design delle carte fu ulteriormente standardizzato, ma mantenne gli elementi tradizionali che le distinguono dagli altri mazzi di carte italiane.",
    "Napoletane": "Le carte napoletane affondano le loro radici nel XV secolo, quando i mazzi di carte si diffusero in tutta Europa, portati da mercanti e viaggiatori. Il Regno di Napoli, all’epoca sotto dominio aragonese, subì una forte influenza spagnola, evidente nella struttura e nello stile grafico delle carte. Il mazzo napoletano infatti ricalca il modello “latino”, simile a quello spagnolo, con semi come coppe, denari, bastoni e spade.Nel corso dei secoli, le carte si radicarono profondamente nella cultura meridionale, assumendo tratti specifici a seconda delle zone. A differenza di altri mazzi regionali, come le carte piacentine o siciliane, quelle napoletane si contraddistinguono per le figure stilizzate, i colori vivaci e le scene evocative.Furono spesso utilizzate non solo per giocare, ma anche per comunicare messaggi simbolici, divenendo un elemento distintivo della cultura popolare partenopea.",
    "Piacentine": "Le carte da gioco piacentine rappresentano un affascinante esempio di arte figurativa che affonda le radici nella storia e nella cultura dell’Europa. Queste carte, originarie della città di Piacenza nell’Emilia-Romagna, sono un tesoro artistico che unisce tradizione, maestria artigianale e simbolismo e sono caratterizzate da un insieme di simboli, figure e motivi ornamentali che le rendono uniche nel loro genere. I quattro semi principali – coppe, denari, spade e bastoni – sono decorati con dettagli elaborati che riflettono la ricchezza e l’estetica dell’epoca in cui sono state create. Oltre ai semi, le carte piacentine presentano una serie di figure iconiche, conosciute come “carte di corte”. Queste figure si ispirano a personaggi storici e mitologici come Alessandro Magno, Caracalla, Giuditta, Rachele e molti altri che conferiscono un elemento narrativo e mitico alle carte e ci trasportano in un mondo di leggende e storie, arricchendo la loro iconografia.Le immagini e i simboli di queste carte gioco piacentine sono stati oggetto di ispirazione per molti artisti nel corso dei secoli. La loro bellezza e l’artigianalità con cui sono stati disegnati hanno trovato espressione in dipinti, sculture e opere d’arte, testimoniando la loro influenza nell’ambito artistico e culturale. ",
    "Siciliane": "Le carte siciliane presentano numerose analogie con quelle arabe, ed in particolare con le carte che i Mamelucchi Egiziani introdussero in Spagna già nel 1300.Ritroviamo l’influsso arabo nella figura del cavaliere, raffigurato a dorso di un cavallo grigio, riferimento sia alla tradizione cristiana (l’ingresso di Cristo a Gerusalemme) che a quella islamica (gli sceicchi entravano nelle città dominate cavalcando un asino).Inoltre in dialetto sicialiano la carta viene definita Sceccu o Sciccareddu, termine che ha la stessa origine della parola “sceicco”. Parlando di “volti noti”, forse non sai che nei primi mazzi di carte siciliane veniva raffigurato Giuseppe Garibaldi, patriota e generale italiano dell’’800, in sella al cavallo di spade o bastoni. Uno dei quattro re veniva invece raffigurato con le sembianze di Re Vittorio Emanuele II, il primo Re del Regno d’Italia.Questo dimostra come le carte siciliane, attraverso i loro semi e le loro figure, hanno sempre trasmesso un significato simbolico, capace di riflettersi nella vita quotidiana.",
    "Bergamasche": "La storia della Masenghini ha inizio più di un secolo fa, nel 1876 con Pietro Masenghini, all’interno di una piccola bottega di città. Una modesta fabbrica di carte, che nel 1918 è stata acquistata da Romolo Lombardini, che purtroppo lasciò molto presto la sua famiglia. I figli Adriano e Scipione, “il signore delle carte” scomparso da qualche anno all’età di 93 anni, riuscirono a realizzare quella che divenne poi la grande azienda che diede il marchio caratteristico alle nostre carte da gioco bergamaschNonostante la fabbrica sia stata creata nel 1876, le carte hanno origini più antiche: si pensa infatti che derivino dai tarocchi lombardi del XIV e XV secolo, ovvero fra il 1300 ed il 1500. Ai giorni nostri, un mazzo è composto da 40 carte – sono quindi di stile “italiano”, differenziandosi da quelle “francesi” a 52 carte – con figure a due teste, di misura 50 x 94 mm. Impiegate, come detto in precedenza, nel gioco della briscola, del “cotècc” e della scopa, assomigliano molto alle carte piacentine poiché presentano le figure del fante, del cavallo e del re tagliate in due e specchiate.Fra spade, bastoni, coppe e ori dai toni rossi, blu e gialli si nascondono diverse curiosità: ad esempio, i denari sono chiamati “ori” e sono di colore rosso e nero. Tutti gli assi presentano delle figure particolari, come quello di ori che è raffigurato come un grande cerchio giallo ed arancione. Sull’asso di bastoni si può trovare invece il motto “VINCERAI” su nastro rosso: un’espressione odiata da molti, poiché si dice porti sfortuna.L’asso di spade sfoggia una corona circondata da fiori rossi, che crescono rampicanti dall’elsa della spada, mentre in quello di coppe, analogalmente alle carte trentine e bresciane, è presente una forma a fontana che si ispira all’emblema araldico della famosa famiglia Sforza del XIV secolo, su cui poggia un putto bendato che sta per scoccare una freccia dalla sua balestra.Osservando invece il quattro di spade, si noterà che al suo interno emerge la piccola figura di una donna detta in dialetto “la Margì”, a cui è dedicato un omonimo gioco tipicamente bergamasco. Di notevole importanza poi, per gli amanti della scopa, il settebello, l’utilissima e fortunata carta che permette al giocatore di ottenere un punto. Infine, nel mazzo sono spesso presenti 4 carte supplementari, delle quali 2 portano stampati i numeri dall’1 all’8 e due dall’1 al 10, utilizzate come segnapunti.",
    "Bolognesi": "Il mazzo della Primiera Bolognese, così chiamato per distinguerlo dal “Tarocchino bolognese”, ha origini piuttosto antiche, risalenti probabilmente al XV° secolo. All’epoca, infatti, il gioco della primiera era già molto noto nell’Italia centro-settentrionale, tant’è che già all’inizio del Cinquecento, il numero di carte che componeva il mazzo originario fu ridotto da 52 a 40. Nello stesso periodo, il “Tarocchino – probabilmente derivato da mazzi importati da Milano o dalla vicina Ferrara – subì la stessa sorte, passando da 78 a 62 carte. A riprova del fatto che a Bologna si utilizzasse questo tipo di mazzo già nel corso del XVI° secolo, almeno, vi è l’autorizzazione papale alla riscossione dei tributi sulle carte da gioco, concessa nel 1588 ad Achille Pinamonti. Il documento stabiliva una tassa di 10 soldi per i mazzi di tarocchi e 5 per quelli da primiera. A partire dal Seicento, nella zona del bolognese si diffusero le carte piacentine (a seme spagnolo) mentre a est divennero sempre più popolari quelle che oggi chiamiamo romagnole. Le carte bolognesi, stampate con le figure speculari a partire dal 1770 circa, rimasero in uso principalmente nelle zone rurali della parte nord-occidentale della provincia di Bologna. A dicembre 2020 è stato stampato un mazzo ‘bolognese’ in cui i semi tradizionali sono stati sostituiti con i simboli della tradizione culinaria del capoluogo emiliano, ovvero vino, tortellini, coltellina per tagliatelle e mattarello.",
    "Bresciane": "Le carte bresciane hanno origini molto antiche; la struttura e il disegno dei semi presenta numerose analogie con alcuni mazzi di origine araba (i ‘naibbi’) risalenti al XII° secolo, oggi conservati al Museo Topkap di Istambul. È probabile che le carte da gioco orientali siano arrivate nel Bresciano a seguito della conquista da parte di Venezia (1426); non a caso, come quelle bergamasche, anche le carte bresciane derivano dal mazzo trevisano (o “veneto”) in uso già nel Cinquecento nei territori sottoposti al dominio della Serenissima. Una delle testimonianze dell’antica tradizione cartaria in area bresciana è un’ordinanza cittadina risalente al 23 gennaio del 1698 che sanciva l’apposizione del bollo rosso sul re di bastoni e il re di spade; fuori città, invece, il bollo (di colore verde), veniva apposto sul tre di coppe e il tre di denari. La produzione di carte da gioco a Brescia si consolidò notevolmente, tant’è che a metà Ottocento in città operavano due fabbricanti: la Ditta Francesco Mutinelli e la più nota Accurata Fabbrica Cassini&Salvotti che all’Esposizione Bresciana del 1904 vantava una produzione di duecentomila mazzi, non solo bresciani ma di altri tipi regionali italiani. I mazzi fabbricati da Cassini, oggi piuttosto rari, venivano venduti in astucci decorati con la Vittoria Alata; la ditta produceva anche “cartine” in formato ridotto per i bambini, uscite di produzione dopo il 1972, a causa dell’abolizione del bollo. Agli anni Settanta risale anche un tentativo di ‘variazione sul tema’ da parte della Italcards: l’azienda produsse un mazzo bresciano da 40 carte (con disegno leggermente diverso) che non ebbe particolare successo.",
    "Genovesi": "L’attuale iconografia delle carte genovesi deriva direttamente dal cosiddetto “mazzo belga”, detto anche “mazzo di Parigi”, stampato per la prima volta nel 1853. A metà Ottocento, infatti, il fabbricante Baptiste-Paul Grimaud decise di creare delle carte da gioco simili a quelle francesi da destinare all’esportazione; l’incarico fu affidato a Louis Badoureau, che disegnò il mazzo – praticamente identico a quello in uso ancora oggi anche in Belgio – verso il 1860. Dopo essere stato utilizzato dapprima nei casinò, il mazzo si arrivò anche in Liguria e in altre zone dell’area mediterranea. Naturalmente, la diffusione delle carte da gioco a Genova e in Liguria è di molto antecedente al XIX° secolo. Già alla fine del Seicento, infatti, un editto (datato 1698), rendeva obbligatorio l’utilizzo delle carte del Dauphiné (l’antica provincia francese del Delfinato) nei territori del Ducato di Savoia e, probabilmente, tale obbligo era esteso anche all’attuale Liguria. Le tracce di questo provvedimento sono rimaste in alcuni mazzi in cui la donna di picche ha un simbolo del Delfinato sulla spalla. Risale, invece, al 1799 una testimonianza più evidente della grande diffusione delle carte da gioco a Genova: una legge, approvata dai Serenissimi Collegi, dal Minor Consiglio e dal Gran Consiglio tra aprile e giugno, elenca tutti i ventisei giochi di carte allora permessi in città.",
    "Milanesi": "La diffusione delle carte da gioco in Italia si colloca tra il Duecento e il Trecento e si deve, con tutta probabilità, agli spagnoli; questi introdussero i ‘naibi’, ossia le carte importate in Spagna dagli Arabi Mamelucchi, nelle quali già si ritrovano i semi delle carte di tipo ‘spagnolo’. Per quanto riguarda Milano e, più in generale, la Lombardia, si sa con certezza che le carte da gioco fossero diffuse già alla fine del 14° secolo, alla corte di Gian Galeazzo Visconti (1351 – 1402). Sua figlia, Valentina, sposò Luigi di Turenna nel 1389, portando in dote un mazzo di “carte di Lombardia” mentre suo figlio minore, Filippo Maria, si appassionò fin da piccolo ai giochi di carte, tanto da commissionare al suo precettore, Marziano da Tortona, un “mazzo degli dèi”, composto da 36 (o 40) carte numerali alle quali si aggiungevano 16 carte, divise in quattro semi: Aquile, Falconi, Cani e Colombe.Nel corso di tutto il Quattrocento, vennero realizzati diversi mazzi di carte alla corte dei Visconti: il celebre mazzo “di Modrone” è attribuito da molti studiosi a Galeazzo Maria Sforza e Bona di Savoia (1468 circa). Dalla corte viscontea proviene anche il “mazzo Colleoni”, noto anche come “Tarocchi dei Visconti”, commissionato da Filippo Maria Visconti o da sua figlia, Bianca Maria. Questo mazzo è particolarmente importante perché, di fatti, divenne il modello per tutti gli altri mazzi lombardi; la produzione venne affidata al pittore e miniatore Bonifacio Bembo, attivo a Cremona a metà del Quattrocento, come dimostrato dalle fonti storiche che attestano alcune commesse alla bottega dei Bembo tra il 1451 e il 1452. Le carte milanesi attuali si standardizzano nel corso dell’Ottocento. Una versione ‘arcaica’, derivata dalle varianti veneziane e romagnole del mazzo Lyon II, presenta le figure intere e il bollo austriaco sul re di cuori, raffigurato mentre regge un falco con la mano sinistra. Il disegno definitivo, ad opera probabilmente di Teodoro Dotti, risale al 1860 circa epresenta le figure speculari divise a metà.",
    "Milanesi 800": "La diffusione delle carte da gioco in Italia si colloca tra il Duecento e il Trecento e si deve, con tutta probabilità, agli spagnoli; questi introdussero i ‘naibi’, ossia le carte importate in Spagna dagli Arabi Mamelucchi, nelle quali già si ritrovano i semi delle carte di tipo ‘spagnolo’. Per quanto riguarda Milano e, più in generale, la Lombardia, si sa con certezza che le carte da gioco fossero diffuse già alla fine del 14° secolo, alla corte di Gian Galeazzo Visconti (1351 – 1402). Sua figlia, Valentina, sposò Luigi di Turenna nel 1389, portando in dote un mazzo di “carte di Lombardia” mentre suo figlio minore, Filippo Maria, si appassionò fin da piccolo ai giochi di carte, tanto da commissionare al suo precettore, Marziano da Tortona, un “mazzo degli dèi”, composto da 36 (o 40) carte numerali alle quali si aggiungevano 16 carte, divise in quattro semi: Aquile, Falconi, Cani e Colombe.Nel corso di tutto il Quattrocento, vennero realizzati diversi mazzi di carte alla corte dei Visconti: il celebre mazzo “di Modrone” è attribuito da molti studiosi a Galeazzo Maria Sforza e Bona di Savoia (1468 circa). Dalla corte viscontea proviene anche il “mazzo Colleoni”, noto anche come “Tarocchi dei Visconti”, commissionato da Filippo Maria Visconti o da sua figlia, Bianca Maria. Questo mazzo è particolarmente importante perché, di fatti, divenne il modello per tutti gli altri mazzi lombardi; la produzione venne affidata al pittore e miniatore Bonifacio Bembo, attivo a Cremona a metà del Quattrocento, come dimostrato dalle fonti storiche che attestano alcune commesse alla bottega dei Bembo tra il 1451 e il 1452. Le carte milanesi attuali si standardizzano nel corso dell’Ottocento. Una versione ‘arcaica’, derivata dalle varianti veneziane e romagnole del mazzo Lyon II, presenta le figure intere e il bollo austriaco sul re di cuori, raffigurato mentre regge un falco con la mano sinistra. Il disegno definitivo, ad opera probabilmente di Teodoro Dotti, risale al 1860 circa epresenta le figure speculari divise a metà.",
    "Romane": "Prevalentemente diffuse nell’Italia centrale, le carte romane sono caratterizzate da semi italiani, come le più famose carte napoletane, piacentine o trevigiane. Sebbene durante il Cinque-Seicento la produzione e il consumo di queste carte fossero notevoli, tra i più rilevanti a livello internazionale, oggi non sono più diffuse e ne rimangono pochissimi esemplari. Uno di questi, un foglio con dodici carte, è conservato all‘Archivio di Stato di Roma nella rilegatura di un volume del 1585. Nel passato, le carte romane svolgevano un ruolo significativo nei salotti dell’alta società e nei circoli sociali del Lazio. Per i romani, giocare a carte non era solo un passatempo, ma un’importante attività sociale, che facilitava interazioni e connessioni tra le persone. Durante le festività locali e le celebrazioni, le carte capitoline erano spesso protagoniste di tornei e competizioni, portando allegria e divertimento alle comunità. ",
    "Sarde": "Il disegno delle carte sarde risale agli inizi dell’Ottocento; in particolare, deriva da quello del mazzo spagnolo inciso da José Martínez de Castro e prodotto da Clemente de Roxas nel 1810. Stampato fino alla fine del secolo, questo mazzo contava 48 carte e si differenziava dai precedenti per il disegno ricco e dettagliato che prevedeva una raffigurazione accurata degli sfondi alle spalle delle figure. Le carte prodotte da de Roxas vennero copiate – in maniera non troppo precisa – da diversi stampatori spagnoli, inclusi alcuni fabbricanti di Barcellona, dove il mazzo si diffuse attorno alla metà del secolo (1850 circa). Fu probabilmente dalla città catalana che le carte spagnole, seppur con un disegno molto semplificato, giunsero fino in Sardegna.",
    "Toscane": "Le prime tracce della presenza di carte da gioco nella città di Firenze risalgono al 14° secolo. In particolare, un’ordinanza datata 1377vietava l’utilizzo dei ‘naibi’ (o ‘naibbe’), il nome di origine araba (da na’ib, ossia “rappresentante del re”) con il quale venivano indicate all’epoca le carte da gioco. Quasi sessant’anni più tardi, il Catasto della città di Firenze testimonia la presenza di un “cartaro”, tale Antonio di Giovanni di Ser Francesco; questi produceva le matrici in legno necessarie a stampare le carte da gioco. In un documento catastale datato 1446, inoltre, viene menzionato un altro artigiano, Jacopo di Poggino; ciò fa presupporre che in città ve ne fossero diversi ma non ancora identificati. Per buona parte del 15° secolo, i giochi di carte furono proibiti a Firenze; i primi ad essere concessi, a partire dal 1477, furono il ‘pilucchino’ e il ‘gioco delle minchiate’, per il quale veniva usato un mazzo di carte simile ai tarocchi. Nel corso del tempo, le carte fiorentine– diffuse solo a Firenze e nelle zone limitrofe – si distinsero leggermente da quelle toscane, utilizzate in tutta la regione. Le prime, infatti, erano un po’ più grandi (67×101 mm) e presentavano figure in pose differenti e dal disegno più accurato. A partire dagli anni Sessanta del Novecento, la pubblicazione delle carte fiorentine divenne sempre più sporadica, fin quando non furono completamente sostituite da quelle toscane; queste ultime vennero prodotte in due formati, uno grande (67×101 mm) e uno leggermente più piccolo (88×58 mm). Le prime sono state commercializzate con la denominazione “toscane vecchie” per distinguerle da quelle originarie.",
    "Trentine": "Prodotte fin dal 16° secolo, le carte trentine derivano da quelle trevisane, in uso in tutto il Veneto. Un esemplare di mazzo trentino risalente al Cinquecento è custodito a Oxford, presso la Bodleian Library; esso rappresenta probabilmente il mazzo di carte regionali italiane più antiche stampate con il disegno originario. Da allora, l’iconografia e lo stile delle carte trentine ha subito alcune variazioni, mantenendo anche alcune peculiarità legate alle vicende storiche della zona; rispetto agli altri mazzi regionali, infatti, quello trentino non aveva il bollo sull’asso di denari dopo il 1862 in quanto, all’epoca, il Trentino faceva ancora parte dell’Impero austriaco. Quando le province di Trento e Bolzano vennero annesse al Regno d’Italia nel 1918, il bollo conservò la propria posizione originaria; in realtà, alcuni mazzi stampati alla fine dell’Ottocento, è posto sull’asso di denari mentre il marchio dello stampatore figura sulla carta del re di denari. Su quest’ultima, fino al 1972, veniva apposto il bollo italiano assieme al nome dello stampatore. Per quanto riguarda l’iconografia e il disegno, le variazioni più significative si registrano dopo il 1940: non ci sono più le decorazioni sulle numerali, le coppe sono chiuse in alto (mentre prima contenevano delle decorazioni floreali), i bastoni sono più spessi e le spade non hanno più la punta. Nel corso del Novecento, alcuni stampatori come Murari e Masenghini producevano anche un mazzo da 52 carte, utilizzato per il gioco del Dobellone.",
    "Trevigiane": "La tradizione delle carte da gioco nel Nord-Est ha origini molto antiche; la genesi di questo mazzo, come gli altri diffusi nel resto d’Italia, risale al periodo a cavallo tra il 13° e il 14° secolo, come testimoniato dall’affinità con i più antichi mazzi di carte arabe sopravvissuti fino ai giorni nostri. Nel corso dei secoli, ovviamente, il disegno ha subito notevoli variazioni; in un mazzo risalente al 1462 e oggi conservato in Spagna, presso il museo H. Fournier a Vitoria-Gasteiz, tutti i numerali di spade presentano una corona. Uno molto più recente, databile attorno alla metà dell’Ottocento, si caratterizza per la presenza del Leone di Venezia su alcune carte di denari (l’asso e il 4) e lo stemma di Marsiglia sul re di bastoni e il 2 di denari. Il disegno utilizzato ancora oggi si è consolidato verso l’inizio del 19° secolo; un mazzo stampato a Venezia da Luchini (1807 – 1814) con la tecnica della silografia mostra le figure intere e il dorso rivoltinato con motivo geometrico; a partire dal 1830, le figure verranno stampate divise in due in maniera speculare. Fino al 1862, il bollo trova posto sul re di bastoni; dopo tale data, viene apposto sull’asso di denari mentre lo spazio rimasto vacante sulla carta della figura viene colmato con lo stemma della città dello stampatore o quello dei Savoia. Quest’ultimo viene raffigurato anche sul 4 di denari nei mazzi antecedenti al 1945; su alcuni esemplari di epoca fascista, lo scudo sabaudo è affiancato dai fasci littori. L’ultima evoluzione significativa del mazzo risale al 1960, ultimo anno in cui la Dal Negro ha prodotto letrevisane “rivoltinate”(ossia con la figura sulla carta inserita in un motivo a cornice) da 52, con il bollo fiscale apposto sull’asso di denari.",
    "Triestine": "Le carte triestine derivano direttamente dalle trevisane, diffuse in Veneto e Friuli, come si evince dalle numerose affinità grafiche. Treviso vanta una tradizione molto antica in materia di carte da gioco, testimoniata da un mazzo quattrocentesco molto simile a quelli importati dagli arabi nei secoli precedenti. Nel corso della prima metà dell’Ottocento, mentre le carte trevigiane assumono progressivamente un disegno definitivo (molto simile a quello attuale), si registra l’avvio della produzione del mazzo triestino, probabilmente per iniziativa del fabbricante di carte Giovanni Battista Marcovich (o Marcovicii) che, nel 1837, acquista la fabbrica che Bartolomeo Mengotti, dopo un apprendistato in Veneto, aveva aperta a Trieste nel 1813. La produzione di carte da gioco in città ricevette nuovo slancio nel Secondo dopoguerra quando una famosa azienda di Trieste, che all’epoca fabbricava cartine per sigarette, cominciò a dedicarsi alle carte regionali, dal momento che le sigarette preconfezionate importate dagli americani avevano fatto calare la richiesta di cartine."
}# _____________________________________________PULIZIE STRAORDINARIE_____________________________________________
def formato_nome(nome: str) -> str:
    return " ".join([p.capitalize() for p in nome.split()])

def duplicati(testo): #Rimozione forzata di doppioni
    parole = testo.split()
    risultato = []
    for p in parole:
        if not risultato or risultato[-1].lower() != p.lower():
            risultato.append(p)
    testopulito = " ".join(risultato)
    parti = testopulito.split()
    n = len(parti)
    if n % 2 == 0:
        metà = n // 2
        prima = " ".join(parti[:metà])
        seconda = " ".join(parti[metà:])
        if prima.lower() == seconda.lower():
            testopulito = prima
    return testopulito

def pulizia(testo): #Metodo spartano e veloce per pulire l'OCR
    testo = re.sub(r"[^A-Za-z\s]", " ", testo)
    parole = testo.split()
    parole = [p for p in parole if len(p) > 1]
    return " ".join(parole).strip()
# _____________________________________________DEFINIZIONI TESSERACT MAGIC_____________________________________________
def artista_mtg(img):
    h, w = img.shape[:2]
    x1, y1 = 0, int(h*0.90)
    x2, y2 = int(w*0.80), h

    roi = img[y1:y2, x1:x2]
    roi_clean = roi[:, int(roi.shape[1]*0.10):]
    roi_zoom = cv2.resize(roi_clean, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(roi_zoom, cv2.COLOR_BGR2GRAY)
    roi_inverted = cv2.bitwise_not(gray)

 
    nickname_tess = pytesseract.image_to_string(roi_inverted, lang='eng+fra+jpn')
    nickname_tess = pulizia(nickname_tess)

    if not nickname_tess:
        results_easy = lingueOCR.readtext(roi_inverted, detail=0) 
        nickname_easy = " ".join(results_easy) 
        nickname_tess = pulizia(nickname_easy)
    nickname_tess = re.sub(r"\b(Otj|Ana|Ere|Ob Sig Ri|Coat|Renee|Cen|Vb|Manuel Castanon|Jho|Tee|Ls|Ffxiii|Op|Wizarasof|Tae|Coust|Fth|Artist|Illustrated by|XF|Lair|Play|Wizardsionbs|BS|rs|Nazetds|ofiehie|VS|Masterpiece|hr|IEDXEN|Mf|dhe|Iac|IFzans|vthe|AWaghs|reserves|SAN|DOI|wic|otthe|eal|ERENCESls|BY|pi|ete|LC|STOR|OSSANDON|LEAL|izards|it|Lair|Gen|Con|END|Con|END|LP|TORU|TERADA|TMA|ELC|FFVIII|RM|AD|lilus|Lunar|New|Yea|Year|oastehne|NG|aad|je|TT|Wizarasofthe|Sy|PACS|Buy|Box|NiAN|STA|ZO|ISIN|Fag|FFXVI|CA|Wivzards|Coasi|aD|vend|Nat|Shae|NEARER|BAR|and|dhe|QD|Wiara|Wa|intro|Pack|ki|TKXEN|RTS|Pr|release|OEehe Caast|Ilius|eBBC|VW|Ubisoft|CR|agp|Wicrds|Ccasc|Iac|FFVI|fs|LIC|FFIX|FPO|PLOT|CAE|INU|EME|LOE|ALIVIL|Jllus|Cv|Qs|og|oast|Ree|Vi|Ofahe|Coass|PLOT|CAE|INU|EME|LOE|dhe|Ipc|ofthc|sil|riebts|resersed|Cyast|AllrightS|uhe|Csast|Jns|scher|Wvzands|ofahc|righs|reserve|WPN|Premium|RMXEN|CRIME|Lert|Gilt|Bos|rwrevww|ws|roy|Yew|Nue|STA|SOI|CHEN|oh|attested|etd|PAIE|RISHXXY|OO|REP|Umi|Ye|ru|Nes|St|JOC|Buy|Box|CET|DM|Iizards|Coass|Iac|ast|reser|ed|RAR|OC|Fa|MESA|rx|OC|Pack|Wwzards|battlefield abandon this scheme DSC |ONS eB nw tI ete Lack Stella SSR|AC Tl fa DN |RS tis EVA ESE gi GT OG GS|Store|Championship|CH|NNN BBN NSN JOT|SENS GRADE ALI gg ASS uPFFIX|eit|Wizerds|Riley|tne|Ba|Inesu|nscryed|righes|fn|astunc|Ww|vzards|FPO|Kee|Fa|VA|WI|izards|PR|menu|rot|PR|DANSE|GRADE|LAS|CRE|OC|CORES|BOTT|AEDS|RULER|RPR|RR|PPR|CD|dt|Imagine|Critters|Css|LCQL|Sd|mme|Wiza|lie|st|Far|vast|eon|tt|WD|IMR|DOS|Imagine|Critters|LC|TMS|Gs|WMeseks|Cost|ner|izards|IAT|MRC|SEC|Ing|Qp|RCI|OR|IX|WS|di|Sol|RRS|See|SY|mg|eserveg|ZZ|IOM|Ww|Ince|AUUS|AVIATK|Led|PER|TNT|OOT|opthe|KR|DC|SSNS|nights|Wicardl|asc|Iic|rs|SNL|ARN|age|cae|Mi|CIRE|NAS|tlie|Coatt|EEA|SEER|SING|AB|RENNES|DANS|NEES|NOS|PO|MOEN|Swanland|GAS|RG|ASE|SN|JL|AACA|ANS|BL|Seok|fans|Weaitse|Heroes|JP|Wvzards|ofte|ah|ds|SC|LLOTBHSS|CES|ECS|ays|TA|PS|ate|ECS|NF|Cer|Ul|UULFE|BL|CAP|SC|KS|TO|NAN|Goss|LG|Viacom|INF|ea|othe|Par|obese|LA|UMPZECPT|IKEDA|CPT|zards|OK|ec|R|WIZSr|ii|Wvzards|wicicds|oFdic|Cos|LEC|TK|Day|Game|BD|IP|Ar|sr|SEEN|gq|ORNE|FC|EO|Wizaras|MH|Special|Guest|PG|Cer|OIE|PPAUBWWizards|che|Goase|TO|NR|IKM|fe|AMIG|wee|MKM|Special|Guest|PG|Wiards|ofdhe|Coasie|TR|MEE|BL|sic|PAR|Yi|Ce|tte|SPAY|PEERS|Cay|Np|Rie|MS|ETS|Nt|RO|OKUMURA|vz|rdsofmhe|Goast|Inco|IF|CSC|XS|Coase|Ro|PRS|RA|HO|BBC|OU|ie|INR|mn|HB|EO|CLP|Hovey|Scorr|OKUMURA|Wycards|astrInc|cee|MAX|Sead|Hasbrc|VN|wie|BP|FT|HO|Wvzaras|fche|ghus|NC|Ku|TK|IC|Cl|FFXIll|Prerelease|IKMXEN|sco|BP|PM|WY|Wvvards ofte|MARVEL|PM|Ty|BBC|onthe|Goarst|Incl|Ofche|BAP|MM|LO|NI|obthe|DPM|OK|CI|FFXI|TX|Promo|IP|TCSGIE|WiZaxdSiGRIthGICoaSt|Wizaras|Ivzards|Ofdhe|Prerclease|TK|OU|mn|Ol|Wit|mm|mn|IEO|Wizaras|ricbts|rese|ved|EO|Coasg|thc|SPP|Leu|Bh|EO|IC|Wvzards|ofue|KH|ez|em|FZ|SoO|BAP|Wvzards|ofche|dr|HOO|NO|SKRSGRKGetGNNEEC|Wvards|otahe|Yvzaras|Goasishnc|TRaRPPD|ol|Jneaz|EAP|Wzaras|hc|tor|Wiaras|th|Ine|Fo|Li|aWicnrds|cte|Coas|JneazTr|Tj|pls|Ih|Tj|Gw|Ew|Ow|eel|lt|ox|tie|goat|liEap|joe|Cars|jac|rightsgeserved|H|nod|Rp|tc|Iilus|Ko|Ies|tj|Tc|So|dre|rn|Ey|R|Mr|s|ma|Ct|Sk|Rf|Mu|Mp|Ld|Ln|At|0|O|Ve|vv|Fae|ewe|fw|ev|were|ywhitvy|XPH|oe|way|INGS|Ge|sui|mt|o|CP|OANA|Vin|US|OLS|DMX|XEN|the|RB|GONE|VIIA|k|EXP|SP|wily|T|CN|vo|LLG|SAS|YY|Tuc|rightseserved|llus|Gu|lus|f|Wivards|NA|R|aN|fr|O|x|oe|ILLUSTRATION|aA|Y|rds|Wir|EP|Geaswliic|e|ON|UE|Gcast|HIS|Tu|OLS|c|reserv|S|M|Sat|FFVII|FNM|Pp|KSY|AU|Wizar|qe|SECRET|Wizarc|OM|Coa|NN|Const|RNY|TWizards|OS|ET|reserved|mghts|Spotlight|ir|Story|Ne|bte|Hairsine|revor|AL|LB|ap|arr|NOIR|ANR|TRE|TRS|LR|As|Sa|vou|jj|LL|PL|FFXIV|XK|TS|rim|VRP|ay|ia|al|FFO|FFVII|WEN|NM|OLS|reserv|y|Ugin|ENIX|SQUARE|FFC|FFX|Ns|Cc|ooo|I|Le|CS|pe|es|RES|PA|ot|fac|rightsieserved|s|the|of|de|eee|Seah|RK|We|UCLLE|HU|CSU|wh|he|ny|TM|L|Fate|Ugins|Fm|IN|ke|Illus|D|MC|ofithe|Coast|Inc|Inc|All|rights|reserv|EE|ER|MX|OLS|SHR|Ultima|R|w|e|c|qq|re|ofthe|Co|LEO|EN|be|xe|FF|R|ME|Wizards of the Coast|Wizards|Wizard|FFI|si|N|A|ISTRATION|Llc|Se|Ae|C|U|P|Tad|Te|Im|Ss)\b", "", nickname_tess, flags=re.IGNORECASE) 
    nickname_tess = re.sub(r"[^A-Za-z\s]", "", nickname_tess) 
    nickname_tess = re.sub(r"\breserv(ed)?\b", "", nickname_tess, flags=re.IGNORECASE) 
    nickname_tess = pulizia(nickname_tess)
    nickname_tess = duplicati(nickname_tess) 
    nickname_tess = " ".join([w.capitalize() for w in nickname_tess.split()]) 
    nickname_tess = "".join(c for c in nickname_tess if c.isalpha() or c.isspace()).strip() 
    
    miglior_match = difflib.get_close_matches(nickname_tess, artisti_magic, n=1, cutoff=0.75) 
    if miglior_match: 
        return miglior_match[0]
    else:
        return nickname_tess
# _____________________________________________DEFINIZIONI TESSERACT Digimon_____________________________________________
def artista_digimon(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


    x1 = int(img_rotated.shape[1] * 0.75)  
    y1 = int(img_rotated.shape[0] * 0.95)  
    x2 = img_rotated.shape[1]              
    y2 = img_rotated.shape[0]              

    x2 = int(img_rotated.shape[1] * 0.93)  

    roi = img_rotated[y1:y2, x1:x2]


    scale_factor = 3
    roi_zoom = cv2.resize(roi, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)


    nickname_tess = pytesseract.image_to_string(roi_zoom, lang='eng+fra+jpn')
    nickname_tess = pulizia(nickname_tess)
    
    if not nickname_tess: 
        results_easy = lingueOCR.readtext(roi_zoom, detail=0) 
        nickname_easy = " ".join(results_easy) 
        nickname_tess = pulizia(nickname_easy) 
    nickname_tess = re.sub(r"\b(Nee|cereal|SSS|eee|ee|rN|..lid|tlle|or|v|i|CM|CU|ES|dr|CE|Li|GE|CB|EM|CH|GM|CCE|OM|)\b", "", nickname_tess, flags=re.IGNORECASE)
    nickname_tess = re.sub(r"[^A-Za-z\s]", "", nickname_tess) 
    nickname_tess = re.sub(r"\breserv(ed)?\b", "", nickname_tess, flags=re.IGNORECASE) 
    nickname_tess = pulizia(nickname_tess) 
    nickname_tess = duplicati(nickname_tess) 
    nickname_tess = " ".join([w.capitalize() for w in nickname_tess.split()]) 
    nickname_tess = "".join(c for c in nickname_tess if c.isalpha() or c.isspace()).strip() 
    
    miglior_match = difflib.get_close_matches(nickname_tess, artisti_digi, n=1, cutoff=0.75) 
    if miglior_match: 
        return miglior_match[0]
    else:
        return nickname_tess
# _____________________________________________DEFINIZIONI One Piece_____________________________________________
def artista_onepiece(img):
    img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)


    x1 = int(img_rotated.shape[1] * 0.75)  
    y1 = int(img_rotated.shape[0] * 0.95)  
    x2 = img_rotated.shape[1]              
    y2 = img_rotated.shape[0]              

    x2 = int(img_rotated.shape[1] * 0.93)  

    roi = img_rotated[y1:y2, x1:x2]

    scale_factor = 3
    roi_zoom = cv2.resize(roi, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)

    nickname_tess = pytesseract.image_to_string(roi_zoom, lang='eng+fra+jpn')
    nickname_tess = pulizia(nickname_tess)
    
    if not nickname_tess:
        results_easy = lingueOCR.readtext(roi_zoom, detail=0) 
        nickname_easy = " ".join(results_easy) 
        nickname_tess = pulizia(nickname_easy) 
    nickname_tess = re.sub(r"\b(lee|Lee|Nee|cereal|SSS|eee|ee|rN||tlle|or|v|i|CM|CU|ES|dr|CE|Li|GE|CB|EM|CH|GM|CCE|OM|)\b", "", nickname_tess, flags=re.IGNORECASE)
    nickname_tess = re.sub(r"[^A-Za-z\s]", "", nickname_tess) 
    nickname_tess = re.sub(r"\breserv(ed)?\b", "", nickname_tess, flags=re.IGNORECASE) 
    nickname_tess = pulizia(nickname_tess) 
    nickname_tess = duplicati(nickname_tess) 
    nickname_tess = " ".join([w.capitalize() for w in nickname_tess.split()]) 
    nickname_tess = "".join(c for c in nickname_tess if c.isalpha() or c.isspace()).strip() 
    
    miglior_match = difflib.get_close_matches(nickname_tess, artisti_one, n=1, cutoff=0.75) 
    if miglior_match: 
        return miglior_match[0]
    else:
        return nickname_tess
# _____________________________________________DEFINIZIONI POKEMON_____________________________________________
def artista_pokemon(img): 
    h, w = img.shape[:2] 

    x1 = 0 
    y1 = int(h*0.94) 
    x2 = int(w*0.95) 
    y2 = h 
 
    roi = img[y1:y2, x1:x2] 

    cut_left_percentage = 0.0 
    width_to_keep = int(roi.shape[1] * (1 - cut_left_percentage)) 
    roi_clean = roi[:, int(roi.shape[1]*cut_left_percentage):] 

    roi_zoom = cv2.resize(roi_clean, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) 

    lab = cv2.cvtColor(roi_zoom, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    thresh = cv2.adaptiveThreshold(
        l,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        91,
        40
    )

    roi_inverted = cv2.bitwise_not(lab) 

    # cv2.imshow("ROI pulita", roi_inverted) 
    # cv2.waitKey(0) 
    # cv2.destroyAllWindows()

        # OCR Tesseract
    nickname_tess = pytesseract.image_to_string(thresh, lang='eng+fra+jpn')
    nickname_tess = pulizia(nickname_tess)
    
    # OCR EasyOCR (fallback) 
    if not nickname_tess: # se Tesseract non trova nulla
        results_easy = lingueOCR.readtext(roi_zoom, detail=0) 
        nickname_easy = " ".join(results_easy) 
        nickname_tess = pulizia(nickname_easy) 
        nickname_tess = duplicati(nickname_tess) 
        nickname_tess = " ".join([w.capitalize() for w in nickname_tess.split()]) 

    ban_list = ["lilus","BW","Neel", "XY", "MM", 
        "PoknonNintendo","Niels", "OPES", "td", "ste", "DAT", "yaa", "af", "Niatendo", "PokmonNietend", "ys", "mele", "AV", "PokdmonNinweeds", "PokmonNintende",
        "Pokmentiserls", "Wap", "Tp", "eV", "TeV", "Pokmentiserls"," RUE", "armes"," b", "Pokemonh", "PRE", "PokmonMirteado", "OPBP","co","PokmonNintenda", "TIN","The", 
        "wv","ST","CF","st","CV","Va","P","NV","Vd","Net","kazu", "fukud","br","St","one","Mj","LY","kJ","Mg","VD","NSY","NO","SN", "LIN","GK", "atl","eK", "ik"," RCA", "Rae", "hs", "WY", "Pokmo", "CN",""
        "tres", "Ua", "eu", "KJ", "WS", "WJ", "tts", "THAT", "sh", "BWO", "BW", " ym", "AX","in"," pray", "wir","SIT"," BIKE","PokemorVNintendo", "MMM", "ML", "retrat", "etreat","Sap", "wa", "Kd", "QU","UY", "rt", 
        "PohemonNintenda","eth","nie", "ey","tey","Tey","rer","Sod","PokmonNintenda","FIV","Th", "ess", "PokimonfNintendo","KK", "Z","Poke","simon","Nit","Leone","md","pers",
        "ay", "LYV","Pa","TOUT","DPBPAT","BAIS","GAB","AIA","pes","OOD","Ot", "DEES","AES","tify","thus","Yisards","lilos","Tri","Wasaeds","Wraards","EIS","Vaards","um","GAMFERF","EU","SEIN",
        "Nps","Tw","SSS","yr","Htus","Mrrds","SOF","Nnterdo","CPE","ifllus","Ward","even","yo","canner","Crevaures","Ninrerde","PokemovNintendo","Nistendo","Nirterd","PokemomNinsendo","LAS","Nectar","Wures"
        "vw","VW", "V", "Vv", "ki", "Lf", "MDI", "POKGITION","SA","Era", "YL", "Ul", "shot", "Ye", "SSI", "mot","Nel","MP","Para","ag","DP","kV", "Cetin","eae","aie","PORTE","vr",
        "SEE", "ore", "bsd", "em", "hal", "ben","Wreards", "nm", "ln","Pa", "Fa", "match", "nm","wd", "age", "FB", "PERLE",
        "Photo", "anal", "Pt", "eh","INGO", "RSE", "GAMERE", "rangs", "ue", "K", "su", "Naw","tem", "Nietendo", "rrprm", "essere","whee", "ower", "mare","nd"
        "GA","ga","gA","Ga","Cr","CR","cR","iy","tee","mme", "memamenanmenermemmenemmenmeemvrnnamemerte","GAMEPREAK", "INGO", "It", "Leaf", "all", "SEAR",
        "db", "Forres","GAMEFRCAK", "FSS","Wozards", "hee", "Wiares","GAMEFRE", "vr", "eeu","ore", "gusset", "eos", "reir", "Sia", "By", "Tree","GAMESRE", 
        "raed","GAMEFREEN","Ninon", "uHuis", "sll","tllus","ind", "ullus","jJilus","ivan","F","Nincendo","mars","KG","Winrd","zo","rn","filus","GAMEE","wr","Lee",
        "Nantendo","EERIE","enor", "PokemonNintendo", "Ponxerex","Vire","dy","Lace","Austen","U","Iltus","PokmonNintends","PokmoniNintendo","TOS","Neen","q","filus","meme"
        "so","sre","rere", "di", "GAMEF","EX", "DM", "ads", "Wssrds","San","IERIE","Navcenda","Creavaures", "GAMET", "Fae","Poo","un","NER","Huos","Woods",
        "rendo","DN","DR","G","Winds","Ninterdo","Lit","GAMESBEAN", "EX", "qT", "antsndo", "Y", "Nerzendo", "GAIMEFREAK", "Poo", "un", "Cal", "dries", "so"
        "GAMEFRCAK", "bid","Niorende","Creare","lhus","Sy","oF", "IRIE", "ESE", "LORS","EIV","UV","UVRTITS","QUFSAICU","Nntendo","aq","Nmtereo","dries",
        "Lun","BO","roo","Ege","rev","ort","Hius","GAMEFEESX","Cree","its","FETE","SD","PN","TPN","hd","iv","dius","IS","zards","W","zards","Lenn",
        "Mae","wreee","jilius","uit","LP","ULIVIJ","UG","bg","Nrtendo","GAMEFE","far","aay","bel","baies","WEEE","WINN","ba","mo","Prev","wsrds","NEES",
        "SOOO","flus","GAMLFSEAK","eo","Wires","MOE","GMS","Messe","use","Swe","mF","DES","war","gO","OEM","Eas","Ho","DDR","FT","ZE","Vo","MEG","india",
        "sf","were","GATEESEE","Tn","ARR","irra","wet","Hus","Om","wreew","tvintendo","GAMTEAV","Seammrs","wpe","PR","LD","bene","Vo","Wirrds","za","EB",
        "To","bi","GAMEFRESK","pd","ro","ein","Da","Wares","Ninxendo","jlus","vFRFe","nf","pilus","anne","mu","Lis","t","tltus","GAMESELAK","C","pilus",
        "Wazards","Noacende","Ege","rev","ort","Hius","sere","Feo","aw","FETE","SD","PN","TPN","hd","RO","T","GAMNESRE","GAMETS","GAMEFRES","GAMES","SAC",
        "ORG","DN""Y","SXX","Was","AK","LITE","JO","Words","CERTES","we","Si","fllus","PokmonNintendo","PokmenNnterco","PokmonNintendo","FIND","CEPR",
        "BFE","RIV","ao","vi","ao","TM","PFE","cases","Werards","Wuards","oa","DO","NI","mr","Wieards","QO","vm","nl","GAMETREAX","Wisards","Apneanda",
        "DUMONT","ert","CU","Fr","are","Aus","M","ir","tendo","CSS","CE","GAHEFREAK","lites","Nwrcerdo","MN","Lt","PokmeonNintendo","PokemonioNintersio",
        "BPS","MEEE","VUIIVRTILCIT","SICH","OIE","Led","IVVSpPitlites","PLIS","VIe","wT","TVs","Mi","Wius","GAMERS","yy","nes","SECs","teww","Auss","INS",
        "GE","CS","bid""Wuards","Vvgard","ie","err","GAMEFREAR","MEVEICEIOIU","TT","WEIR","UVRTIT","MEMO","VS","IC","QUFSAIC","JEUIEE","oti","Eg","LV","UT",
          "al","llus","Wusrds","ad","III","IIR","ve","EEN","SMS","OEE","RSS","EINE","PON","ww","BB","garg","wee","IIS","H","FANS","AU","DEDEDE","BEEN","wre",
          "s","UU","gl","teem","e","AB","REE","EIEIO","IEEE","oo","se","did","me","pues","wees","TR","EI","EDIE","SE","mt","NEE","NA","ENED","ur", "Wiards",
          "LM", "VWiords","gi","ea","hi","RD","tus","llius","aaa","Nuitendo","WVinrds","id","lius","Wiaards","IHus", "Wizwds","Mlus","Creanses","Wizuds","Lu",
          "PS","Virards","Vizards","Virarrds","J","fF","ES","RC","Hlus","os","Crerrures","EEO","Iitus","litus","lltus","hall","Nuntenda","int","i","ars",
          "Wlus","INE","IG","IIE","aa","Fe","rw","Wards","LL","ILLUS","Illus","lllus","Creanires","Winards","EYE","eye","Eye","pO","Ulus", "Wauds","o",
          "Wicrds","Naendo","Creansres","SGN","fus","nnn","nn","nS","LES","Ilus","LA","Itlus","Crearures","SR","ae","Mntendo","eds","Wizars","lilus","LS", 
          "Creztures", "Wizunts","IRR","Winrds","Wizards","or","Wirards","Oe","ere","ius","RR","IEE","EER","Er","Weards","WWirards","dd","EES","Illus","-",
          "Mus","lus","Winrds","Li","Waards","eee","ene","ON","ee","Fs","LOS","FW","EEE","EE","D", "GAMEFREAX","TE","RE","RS","R","RÉ","Wizards", "Creanures",
            "GAMEFREAK", "Wids","et", "el", "XY", "SAS", "rm","NE","he", "as","Rie", "ds","Xvai","lilus","Iilus","ii","bd","LE","nt", "Wizarés","lilus", 
            "Nintendo", "Creatures", "GAMEFREAK","N", "Pokémon","x","Pokemon","XY","TAY","illus", "illustrator", "be", "xe", "res", "ss", "ny", "tl", 
            "res ti", "en", "us","JE","TI", "A","an", "Xx","の", "っ","elles","DE","l","Yotémon","LR", "ed", "oer", "TS", "at", "ow","-"," ニ","ン", "ニ", 
            "一 ", "vF", "pee","dilus", "PokemonNinteedo", "Pokmon", "uw", "Pokmon", "Nictendo", "PokemoniNintersio", "kHlus","PokmoniNintesdo", "Hitus", "jus"
            ]

    for bad in ban_list:
        nickname_tess = re.sub(rf"\b{bad}\b", "", nickname_tess, flags=re.IGNORECASE)
    nickname_tess = re.sub(r"[\u3040-\u30FF\u4E00-\u9FFF]+", "", nickname_tess)
    nickname_tess = re.sub(r"[^A-Za-z\s]", "", nickname_tess) 
    nickname_tess = re.sub(r"\breserv(ed)?\b", "", nickname_tess, flags=re.IGNORECASE) 
    nickname_tess = pulizia(nickname_tess) 
    nickname_tess = duplicati(nickname_tess) 
    nickname_tess = " ".join([w.capitalize() for w in nickname_tess.split()]) 
    # dopo il tuo OCR e pulizia... 
    nickname_tess = "".join(c for c in nickname_tess if c.isalpha() or c.isspace()).strip() 
    
    miglior_match = difflib.get_close_matches(nickname_tess, artisti_one, n=1, cutoff=0.75) 
    if miglior_match: 
        return miglior_match[0]
    else:
        return nickname_tess
#__________________________GUI SETUP_____________________________________________
finestra = tk.Tk()
finestra.title("Riconoscimento Carte")
finestra.geometry("880x620")
finestra.configure(bg="black")

font_sub = ("Segoe UI", 8, "italic")
font_title = ("Segoe UI", 16, "bold italic")
font_btn = ("Segoe UI", 12, "bold")
font_risultato = ("Segoe UI", 12, "bold italic")

# _____________________________________________GUI TITOLI E SUBTITOLI_____________________________________________
sottotitolo = tk.Label(finestra, text="BitCamp Presenta:", bg="black", fg="white", font=font_sub)
sottotitolo.pack(anchor="nw", padx=5, pady=5)
titolo = tk.Label(finestra, text="Vuoi sapere la storia e l'artista della carta?", bg="black", fg="white", font=font_title)
titolo.pack(anchor="nw", padx=15, pady=3)

# _____________________________________________FUNZIONE PER CARICARE L’IMMAGINE E PREDIRE_____________________________________________
def carica_immagine():
    percorso_file = filedialog.askopenfilename(filetypes=[("File immagine", "*.jpg;*.jpeg;*.png")])
    if not percorso_file:
        return

    try:
        img_orig = Image.open(percorso_file).convert("RGB")
        disp = img_orig.resize((300, 400))
        img_tk = ImageTk.PhotoImage(disp)
        label_immagine.configure(image=img_tk)
        label_immagine.image = img_tk

        inp = img_orig.resize((224, 224))
        arr = np.array(inp).astype("float32") / 255.0
        arr = arr.reshape(1, 224, 224, 3)

        probs_macro = modello_macro.predict(arr)
        idx_macro = int(np.argmax(probs_macro, axis=1)[0])
        #conf_macro = probs_macro[0, idx_macro]
        nome_macro = nomi_macro.get(idx_macro, f"Indice {idx_macro}")

        testo_risultato = f"Macro: {nome_macro}"
        extra_msg = storie_macro.get(nome_macro, "")
        if extra_msg:
            testo_risultato += f"\n{extra_msg}"

        if idx_macro == 0:
            probs_briscola = modello_briscola.predict(arr)
            idx_briscola = int(np.argmax(probs_briscola, axis=1)[0])
            nome_briscola = nomi_briscola.get(idx_briscola, f"Indice {idx_briscola}")
            testo_risultato += f"\n→ Briscola: {nome_briscola}"
            briscola_extra = storie_briscola.get(nome_briscola, "")
            if briscola_extra:
                testo_risultato += f"\n{briscola_extra}"
        
        if idx_macro == 4:  # Magic
            nickname_artista = artista_mtg(cv2.cvtColor(np.array(img_orig), cv2.COLOR_RGB2BGR))
            testo_risultato += f"\n→ Artista della carta: {nickname_artista}"
        if idx_macro == 1: #Digimon
            nickname_artista = artista_digimon(cv2.cvtColor(np.array(img_orig), cv2.COLOR_RGB2BGR))
            testo_risultato += f"\n→ Artista della carta: {nickname_artista}"
        if idx_macro == 5: #One Piece
            nickname_artista = artista_onepiece(cv2.cvtColor(np.array(img_orig), cv2.COLOR_RGB2BGR))
            testo_risultato += f"\n→ Artista della carta: {nickname_artista}"
        if idx_macro == 6: #PokemoN
            nickname_artista = artista_pokemon(cv2.cvtColor(np.array(img_orig), cv2.COLOR_RGB2BGR))
            testo_risultato += f"\n→ Artista della carta: {nickname_artista}"
            
        label_risultato.configure(state="normal")
        label_risultato.delete("1.0", tk.END)
        label_risultato.insert(tk.END, testo_risultato)
        label_risultato.configure(state="disabled")

    except Exception as e:
        label_risultato.configure(state="normal")
        label_risultato.delete("1.0", tk.END)
        label_risultato.insert(tk.END, f"Errore con immagine o modello:\n{e}")
        label_risultato.configure(state="disabled")

    except Exception as e:
        label_risultato.configure(text=f"Errore con immagine o modello:\n{e}")

#_____________________________________________GUI ICONA + CARICA IMMAGINE_____________________________________________
img = Image.open(r"C:\Users\Calfi\Desktop\Python BitCamp\Python\Progetto Alfio - Riconoscimento Carte\carte.png")
img = img.resize((170, 170)) 
tk_img = ImageTk.PhotoImage(img)
bottone_carica = tk.Button(
    finestra,
    image=tk_img,
    command=carica_immagine,
    bg="black",
    borderwidth=0,
    activebackground="black"
)
bottone_carica.image = tk_img
bottone_carica.place(x=725, y=1)

# _____________________________________________FRAME PRINCIPALE_____________________________________________
frame_principale = tk.Frame(finestra, bg="black")
frame_principale.pack(expand=True, pady=20)

# _____________________________________________LABEL IMMAGINE_____________________________________________
label_immagine = tk.Label(frame_principale, bg="black")
label_immagine.pack(side="left", padx=20, pady=20)

# _____________________________________________LABEL TESTO + RISULTATO TESSERA_____________________________________________
label_risultato = tk.Text(
    frame_principale,
    bg="black",
    fg="white",
    font=font_risultato,
    width=30,      # numero di caratteri
    height=12,     # altezza in righe
    wrap="word"
)
label_risultato.pack(side="left", padx=20)
label_risultato.configure(state="disable")

# _____________________________________________AVVIO GUI_____________________________________________
finestra.mainloop()
# _____________________________________________GRAZIE PER LA VISIONE_____________________________________________