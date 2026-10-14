# ==========================================
# PLAN MYYATRA - TRAVEL ENGINE
# ==========================================

import math


# ==========================================
# 1. CITY COORDINATES
# ==========================================

CITY_COORDINATES = {
    "delhi": (28.6139, 77.2090),
    "new delhi": (28.6139, 77.2090),
    "noida": (28.5355, 77.3910),
    "gurgaon": (28.4595, 77.0266),
    "gurugram": (28.4595, 77.0266),
    "faridabad": (28.4089, 77.3178),
    "ghaziabad": (28.6692, 77.4538),
    "chandigarh": (30.7333, 76.7794),
    "kurukshetra": (29.9695, 76.8783),
    "panipat": (29.3909, 76.9635),
    "hisar": (29.1492, 75.7216),
    "panchkula": (30.6906, 76.8606),
    "morni hills": (30.6995, 77.0834),
    "pinjore": (30.7982, 76.9238),
    "yamunanagar": (30.1290, 77.2800),
    "karnal": (29.6857, 76.9905),
    "surajkund": (28.2667, 77.2167),
    "shimla": (31.1048, 77.1734),
    "manali": (32.2432, 77.1892),
    "dharamshala": (32.2192, 76.3234),
    "mcleod ganj": (32.2428, 76.3215),
    "dalhousie": (32.5361, 75.9731),
    "khajjiar": (32.5289, 75.9788),
    "kullu": (31.9580, 77.1184),
    "kasol": (32.0069, 77.3150),
    "kasauli": (30.8981, 76.9650),
    "spiti valley": (32.1232, 78.1603),
    "kinnaur": (31.5667, 78.4000),
    "kalpa": (31.5496, 78.2670),
    "chitkul": (31.3478, 78.1750),
    "tirthan valley": (31.5514, 77.3570),
    "chamba": (32.5514, 76.1256),
    "manikaran": (32.0451, 77.3474),
    "bir billing": (32.0506, 76.7132),
    "lahaul": (32.5454, 77.0151),
    "keylong": (32.5712, 77.0314),
    "sangla": (31.4217, 78.2482),
    "narkanda": (31.2677, 77.4831),
    "solang valley": (32.3401, 77.1718),
    "kufri": (31.1007, 77.2575),
    "rohtang region": (32.3416, 77.1820),
    "mussoorie": (30.4598, 78.0644),
    "rishikesh": (30.0869, 78.2676),
    "haridwar": (29.9457, 78.1642),
    "dehradun": (30.3165, 78.0322),
    "nainital": (29.3803, 79.4636),
    "auli": (30.5307, 79.5699),
    "badrinath": (30.7433, 79.4937),
    "kedarnath": (30.7340, 79.0665),
    "gangotri": (30.9925, 78.9340),
    "yamunotri": (31.0189, 78.4512),
    "ranikhet": (29.6406, 79.4322),
    "almora": (29.5979, 79.6628),
    "kausani": (29.8451, 79.9517),
    "lansdowne": (29.8386, 78.6933),
    "jim corbett": (29.5319, 78.7704),
    "valley of flowers": (30.7298, 79.9004),
    "chopta": (30.5992, 79.1554),
    "mukteshwar": (29.4817, 79.6459),
    "dhanaulti": (30.4146, 78.2069),
    "tehri": (30.3777, 78.4832),
    "pithoragarh": (29.5800, 80.2180),
    "uttarkashi": (30.7286, 78.4430),
    "binsar": (29.8070, 79.7570),
    "amritsar": (31.6340, 74.8723),
    "jaipur": (26.9124, 75.7873),
    "jaisalmer": (26.9157, 70.9083),
    "udaipur": (24.5854, 73.7125),
    "jodhpur": (26.2389, 73.0243),
    "pushkar": (26.4889, 74.5500),
    "ajmer": (26.4499, 74.6399),
    "mount abu": (24.5924, 72.7080),
    "bikaner": (28.0229, 73.3119),
    "ranthambore": (26.0183, 76.5007),
    "chittorgarh": (24.8887, 74.6269),
    "bundi": (25.4401, 75.6360),
    "kota": (25.2138, 75.8648),
    "alwar": (27.5529, 76.6346),
    "neemrana": (27.9758, 76.2764),
    "bharatpur": (27.2179, 77.4902),
    "sawai madhopur": (26.0229, 76.3515),
    "kumbhalgarh": (25.1472, 73.5824),
    "barmer": (25.7471, 71.3967),
    "osian": (26.7182, 72.9073),
    "mandawa": (28.0558, 75.1455),
    "sariska": (27.3218, 76.3570),
    "mumbai": (19.0760, 72.8777),
    "pune": (18.5204, 73.8567),
    "mahabaleshwar": (17.9307, 73.6477),
    "lonavala": (18.7546, 73.4062),
    "khandala": (19.3886, 73.3674),
    "panchgani": (17.9225, 73.8076),
    "matheran": (19.0090, 73.2673),
    "nashik": (19.9975, 73.7898),
    "aurangabad": (19.8762, 75.3433),
    "chhatrapati sambhajinagar": (19.8762, 75.3433),
    "ajanta caves": (20.5545, 75.7060),
    "ellora caves": (20.0265, 75.1770),
    "alibaug": (18.6414, 72.8724),
    "ratnagiri": (16.9948, 73.3005),
    "tarkarli": (16.0588, 73.4756),
    "ganpatipule": (17.1410, 73.2700),
    "kolhapur": (16.7049, 74.2433),
    "shirdi": (19.7660, 74.4777),
    "nagpur": (21.1458, 79.0882),
    "tadoba": (20.2640, 79.5252),
    "lonar": (19.9738, 76.5127),
    "igatpuri": (19.7035, 73.5629),
    "goa": (15.2993, 74.1240),
    "panaji": (15.4909, 73.8278),
    "north goa": (15.4909, 73.8278),
    "south goa": (15.2893, 74.1235),
    "calangute": (15.5430, 73.7612),
    "baga": (15.5550, 73.7510),
    "anjuna": (15.5975, 73.7448),
    "vagator": (15.6067, 73.7515),
    "candolim": (15.5186, 73.7622),
    "palolem": (15.0055, 74.0255),
    "colva": (15.2817, 74.1337),
    "morjim": (15.6202, 73.7606),
    "old goa": (15.5035, 73.9124),
    "dudhsagar falls": (15.3050, 74.3137),
    "fort aguada": (15.4967, 73.7600),
    "chapora fort": (15.6185, 73.7450),
    "divar island": (15.5287, 73.9211),
    "surat": (21.1702, 72.8311),
    "ahmedabad": (23.0225, 72.5714),
    "statue of unity": (21.8383, 73.7197),
    "vadodara": (22.3072, 73.1812),
    "rajkot": (22.3039, 70.8022),
    "dwarka": (22.2394, 68.9678),
    "somnath": (20.9072, 70.4028),
    "gir national park": (21.1298, 70.8003),
    "kutch": (23.7337, 69.8597),
    "rann of kutch": (23.7337, 69.8597),
    "bhuj": (23.2420, 69.6669),
    "dholavira": (23.8851, 70.2165),
    "modhera": (23.5893, 72.1300),
    "patan": (23.8516, 72.1325),
    "saputara": (20.5735, 73.7294),
    "junagadh": (21.5222, 70.4579),
    "girnar": (21.5195, 70.4673),
    "champaner-pavagadh": (22.4858, 73.5351),
    "porbandar": (21.6417, 69.6093),
    "mandvi": (22.8319, 69.3567),
    "bhopal": (23.2599, 77.4126),
    "indore": (22.7196, 75.8577),
    "ujjain": (23.1793, 75.7849),
    "gwalior": (26.2183, 78.1828),
    "khajuraho": (24.8318, 79.9199),
    "orchha": (25.3516, 78.6411),
    "pachmarhi": (22.4673, 78.4332),
    "jabalpur": (23.1815, 79.9462),
    "sanchi": (23.4828, 77.7377),
    "mandu": (22.3518, 75.4021),
    "maheshwar": (22.1806, 75.5875),
    "omkareshwar": (22.2472, 76.1420),
    "kanha national park": (22.3333, 80.6667),
    "bandhavgarh national park": (23.7000, 80.9500),
    "pench national park": (21.6667, 79.3333),
    "satpura national park": (22.5000, 78.5000),
    "bhimbetka": (22.9333, 77.6000),
    "chanderi": (24.7096, 78.1328),
    "amarkantak": (22.6700, 81.7500),
    "bengaluru": (12.9716, 77.5946),
    "bangalore": (12.9716, 77.5946),
    "mysuru": (12.2958, 76.6394),
    "hampi": (15.3350, 76.4600),
    "coorg": (12.4244, 75.7382),
    "chikmagalur": (13.3160, 75.7754),
    "gokarna": (14.5526, 74.3178),
    "udupi": (13.3409, 74.7421),
    "mangaluru": (12.9141, 74.8560),
    "badami": (15.9220, 75.6813),
    "aihole": (16.0201, 75.8803),
    "pattadakal": (16.0182, 75.8480),
    "jog falls": (14.2263, 74.8127),
    "kabini": (11.9182, 76.0191),
    "bandipur": (11.8065, 76.6140),
    "nagarhole": (12.0950, 76.1145),
    "dandeli": (15.2650, 74.6131),
    "sakleshpur": (12.9446, 75.7862),
    "shivamogga": (13.9299, 75.5681),
    "belur": (13.1621, 75.8643),
    "halebidu": (13.2143, 75.9962),
    "vijayapura": (16.8302, 75.7100),
    "bijapur": (16.8302, 75.7100),
    "bidar": (17.9134, 77.5310),
    "murudeshwar": (14.0941, 74.4920),
    "kudremukh": (13.2054, 75.2668),
    "hyderabad": (17.3850, 78.4866),
    "warangal": (17.9689, 79.5941),
    "karimnagar": (18.4386, 79.1288),
    "nizamabad": (18.6725, 78.0941),
    "khammam": (17.2473, 80.1514),
    "medak": (18.0428, 78.2633),
    "nagarjuna sagar": (16.5317, 79.3277),
    "ananthagiri hills": (17.3188, 78.6652),
    "ramappa temple": (18.1770, 79.9403),
    "thousand pillar temple": (17.3956, 78.4995),
    "charminar": (17.3616, 78.4747),
    "golconda fort": (17.3833, 78.4011),
    "hussain sagar": (17.4065, 78.4730),
    "bhongir": (17.5122, 78.8849),
    "chennai": (13.0827, 80.2707),
    "kochi": (9.9312, 76.2673),
    "munnar": (10.0889, 77.0595),
    "ooty": (11.4064, 76.6932),
    "coimbatore": (11.0168, 76.9558),
    "madurai": (9.9252, 78.1198),
    "rameswaram": (9.2876, 79.3129),
    "kanyakumari": (8.0883, 77.5385),
    "mahabalipuram": (12.6269, 80.1724),
    "pondicherry region": (11.9416, 79.8083),
    "pondicherry": (11.9416, 79.8083),
    "thanjavur": (10.7870, 79.1378),
    "kumbakonam": (10.9600, 79.3881),
    "tiruchirappalli": (10.7905, 78.7047),
    "tirupati": (13.6288, 79.4192),
    "vijayawada": (16.5062, 80.6480),
    "yercaud": (11.7749, 78.2098),
    "coonoor": (11.3527, 76.8155),
    "kanchipuram": (12.8352, 79.7078),
    "chidambaram": (11.3990, 79.6943),
    "dhanushkodi": (9.2317, 79.3967),
    "valparai": (10.3265, 76.9559),
    "mudumalai": (11.5884, 76.5735),
    "courtallam": (8.9345, 77.2760),
    "kolkata": (22.5726, 88.3639),
    "ranchi": (23.3441, 85.3096),
    "rajgir": (25.0260, 85.4217),
    "varanasi": (25.3176, 82.9739),
    "puri": (19.8135, 85.8302),
    "rajahmundry": (16.9900, 81.7800),
    "kakinada": (16.9891, 82.2475),
    "machilipatnam": (16.1875, 81.1353),
    "nellore": (14.4426, 79.9865),
    "visakhapatnam": (17.6868, 83.2185),
    "vizag": (17.6868, 83.2185),
    "gandikota": (14.8127, 78.2743),
    "horsley hills": (13.4852, 78.2671),
    "kurnool": (15.8287, 78.0373),
    "lepakshi": (13.8185, 77.7230),
    "papikondalu": (17.5817, 81.7593),
    "srisailam": (16.0828, 78.8701),
    "borra caves": (18.2720, 82.8930),
    "amravati": (20.9320, 77.7523),
    "nagaon": (26.3479, 92.6901),
    "darjeeling": (27.0410, 88.2663),
    "kalimpong": (27.0590, 88.4685),
    "siliguri": (26.7271, 88.3953),
    "sundarbans": (21.9497, 88.9404),
    "digha": (21.6774, 87.5489),
    "mandarmani": (21.6660, 87.5000),
    "shantiniketan": (23.6818, 87.6846),
    "dooars": (26.7193, 89.1333),
    "jalpaiguri": (26.5245, 88.7359),
    "mirik": (26.8837, 88.1866),
    "kurseong": (26.8786, 88.2788),
    "bishnupur": (23.0718, 87.3189),
    "murshidabad": (24.1822, 88.2732),
    "bankura": (23.2320, 87.0737),
    "bakkhali": (21.5571, 88.2500),
    "guwahati": (26.1445, 91.7362),
    "kaziranga national park": (26.5775, 93.1711),
    "manas national park": (26.6764, 90.9435),
    "majuli": (27.0000, 94.2000),
    "sivasagar": (26.9839, 94.6393),
    "tezpur": (26.6333, 92.8000),
    "jorhat": (26.7500, 94.2167),
    "dibrugarh": (27.4720, 94.9121),
    "haflong": (25.1771, 93.0161),
    "pobitora wildlife sanctuary": (26.2392, 91.8883),
    "hajo": (26.2399, 91.5303),
    "digboi": (27.3838, 95.6128),
    "tinsukia": (27.4900, 95.3621),
    "umananda island": (26.1643, 91.7487),
    "kamakhya temple": (26.1701, 91.7030),
    "patna": (25.5941, 85.1376),
    "bodh gaya": (24.6956, 84.9912),
    "gaya": (24.7955, 85.0002),
    "nalanda": (25.1350, 85.4419),
    "vaishali": (25.9900, 85.1000),
    "pawapuri": (25.6394, 85.4507),
    "muzaffarpur": (26.1209, 85.3647),
    "valmiki nagar": (27.2852, 84.2400),
    "madhubani": (26.3473, 86.0714),
    "bhagalpur": (25.2378, 86.9817),
    "sasaram": (24.9473, 84.0134),
    "vikramshila": (25.2310, 87.4447),
    "kesaria": (26.3088, 84.9140),
    "barabar caves": (25.0269, 85.0228),
    "raipur": (21.2514, 81.6296),
    "jagdalpur": (19.0715, 82.0338),
    "chitrakote falls": (19.3916, 81.8246),
    "tirathgarh falls": (19.1640, 81.7429),
    "bastar": (19.0956, 81.9517),
    "kanger valley national park": (18.9267, 81.9043),
    "mainpat": (22.7200, 83.2200),
    "sirpur": (21.4059, 82.1757),
    "barnawapara wildlife sanctuary": (21.1835, 82.0700),
    "achanakmar": (22.4708, 81.7429),
    "danteshwari temple": (19.1140, 81.9632),
    "dongargarh": (21.1887, 80.7341),
    "bhoramdeo": (22.1437, 81.2013),
    "amarkantak region": (22.6749, 81.7495),
    "agartala": (23.8315, 91.2868),
    "ujjayanta palace": (23.8387, 91.2804),
    "neermahal": (23.8437, 91.2734),
    "unakoti": (24.3171, 91.9601),
    "jampui hills": (24.3068, 92.1847),
    "sepahijala wildlife sanctuary": (23.7214, 91.3155),
    "tripura sundari temple": (23.8330, 91.2864),
    "dumboor lake": (23.4572, 91.4436),
    "pilak": (23.6258, 91.7798),
    "imphal": (24.8170, 93.9368),
    "loktak lake": (24.5150, 93.8125),
    "keibul lamjao national park": (24.6000, 93.8000),
    "ukhrul": (25.1375, 94.3655),
    "shirui hills": (25.1426, 94.3728),
    "moreh": (24.2942, 94.3069),
    "kangla fort": (24.8034, 93.9422),
    "andro": (24.7530, 93.8902),
    "senapati": (25.1704, 94.0918),
    "tamenglong": (24.9862, 93.8355),
    "shillong": (25.5788, 91.8933),
    "cherrapunji": (25.2944, 91.6990),
    "sohra": (25.2944, 91.6990),
    "mawsynram": (25.2998, 91.5852),
    "dawki": (25.2087, 92.0324),
    "nongriat": (25.5110, 91.8442),
    "mawlynnong": (25.2654, 91.7630),
    "jowai": (25.4381, 92.1968),
    "tura": (25.5139, 90.2144),
    "laitlum": (25.4602, 91.7965),
    "nohkalikai falls": (25.2615, 91.7046),
    "seven sisters falls": (25.3488, 91.6632),
    "umiam lake": (25.6519, 91.9063),
    "double decker living root bridge": (25.3167, 91.7000),
    "aizawl": (23.7367, 92.7173),
    "lunglei": (22.8830, 92.7459),
    "champhai": (23.4562, 93.3332),
    "reiek": (23.6417, 92.7561),
    "hmuifang": (23.4630, 92.9090),
    "phawngpui": (22.6509, 93.0280),
    "blue mountain": (22.6509, 93.0280),
    "vantawng falls": (23.6448, 92.9785),
    "tamdil lake": (23.5330, 92.7327),
    "serchhip": (23.3179, 92.8557),
    "kolasib": (24.2222, 92.6665),
    "kohima": (25.6740, 94.1086),
    "dzukou valley": (25.6367, 94.0940),
    "kisama heritage village": (25.6797, 94.1261),
    "mokokchung": (26.3215, 94.5200),
    "mon": (26.7500, 95.0000),
    "tuophema": (26.0153, 94.2268),
    "wokha": (26.1019, 94.2678),
    "khonoma": (25.6697, 94.0412),
    "pfutsero": (25.9187, 94.2394),
    "japfu peak": (25.8868, 94.2506),
    "bhubaneswar": (20.2961, 85.8245),
    "konark": (19.8876, 86.0949),
    "chilika lake": (19.7286, 85.2982),
    "cuttack": (20.4625, 85.8828),
    "gopalpur": (19.2700, 84.9540),
    "daringbadi": (19.3794, 84.1100),
    "simlipal national park": (21.9366, 86.2707),
    "satkosia": (20.8404, 84.6417),
    "baripada": (21.9330, 86.7287),
    "raghurajpur": (20.3860, 85.5550),
    "dhauli": (20.2198, 85.8240),
    "chandipur": (21.4685, 87.0515),
    "sambalpur": (21.4669, 83.9812),
    "koraput": (18.8137, 82.7138),
    "bhitarkanika": (20.7617, 86.8789),
    "amritsar": (31.6340, 74.8723),
    "golden temple": (31.6197, 74.8765),
    "wagah": (31.6060, 74.5730),
    "jalandhar": (31.3260, 75.5762),
    "ludhiana": (30.9009, 75.8573),
    "patiala": (30.3398, 76.3869),
    "anandpur sahib": (31.2367, 76.5000),
    "bathinda": (30.2104, 74.9489),
    "kapurthala": (31.3806, 75.3840),
    "pathankot": (32.2641, 75.6437),
    "harike wetland": (31.1401, 74.9393),
    "sultanpur lodhi": (31.2120, 75.1968),
    "gurugram": (28.4595, 77.0266),
    "faridabad": (28.4089, 77.3178),
    "panipat": (29.3909, 76.9635),
    "hisar": (29.1492, 75.7216),
    "panchkula": (30.6906, 76.8606),
    "morni hills": (30.6995, 77.0834),
    "pinjore": (30.7982, 76.9238),
    "sultanpur national park": (28.5006, 76.8988),
    "damdama lake": (28.4924, 77.1558),
    "surajkund": (28.2667, 77.2167),
    "jyotisar": (29.9869, 76.9500),
    "karnal": (29.6857, 76.9905),
    "yamunanagar": (30.1290, 77.2800),
    "gangtok": (27.3389, 88.6065),
    "tsomgo lake": (27.3664, 88.7463),
    "nathula pass": (27.3734, 88.8026),
    "pelling": (27.3181, 88.2234),
    "lachung": (27.6906, 88.7423),
    "lachen": (27.7194, 88.5513),
    "yumthang valley": (27.8220, 88.7017),
    "ravangla": (27.3110, 88.3656),
    "namchi": (27.1645, 88.3549),
    "zuluk": (27.2179, 88.6083),
    "yuksom": (27.3737, 88.2233),
    "gurudongmar lake": (28.0047, 88.7637),
    "dhanushkodi": (9.2317, 79.3967),
    "valparai": (10.3265, 76.9559),
    "mudumalai": (11.5884, 76.5735),
    "courtallam": (8.9345, 77.2760),
    "bengaluru": (12.9716, 77.5946),
    "bangalore": (12.9716, 77.5946),
    "mysuru": (12.2958, 76.6394),
    "hampi": (15.3350, 76.4600),
    "coorg": (12.4244, 75.7382),
    "chikmagalur": (13.3160, 75.7754),
    "gokarna": (14.5526, 74.3178),
    "udupi": (13.3409, 74.7421),
    "mangaluru": (12.9141, 74.8560),
    "badami": (15.9220, 75.6813),
    "aihole": (16.0201, 75.8803),
    "pattadakal": (16.0182, 75.8480),
    "jog falls": (14.2263, 74.8127),
    "kabini": (11.9182, 76.0191),
    "bandipur": (11.8065, 76.6140),
    "nagarhole": (12.0950, 76.1145),
    "dandeli": (15.2650, 74.6131),
    "sakleshpur": (12.9446, 75.7862),
    "shivamogga": (13.9299, 75.5681),
    "belur": (13.1621, 75.8643),
    "halebidu": (13.2143, 75.9962),
    "vijayapura": (16.8302, 75.7100),
    "bidar": (17.9134, 77.5310),
    "murudeshwar": (14.0941, 74.4920),
    "kudremukh": (13.2054, 75.2668),
    "wayanad": (11.6854, 76.1320),
    "thekkady": (9.6054, 77.1707),
    "kumarakom": (9.6173, 76.4311),
    "varkala": (8.7374, 76.7162),
    "kovalam": (8.3967, 76.9948),
    "thiruvananthapuram": (8.5241, 76.9366),
    "kozhikode": (11.2588, 75.7804),
    "kannur": (11.8745, 75.3704),
    "kollam": (8.8932, 76.6141),
    "bekal": (12.3907, 75.0177),
    "vagamon": (9.6904, 76.9213),
    "athirappilly": (10.2830, 76.5483),
    "thrissur": (10.5276, 76.2144),
    "kasaragod": (12.4996, 74.9870),
    "sabarimala": (9.4324, 76.9389),
    "marari": (9.5902, 76.2930),
    "srinagar": (34.0837, 74.7973),
    "jammu": (32.7266, 74.8570),
    "leh": (34.1526, 77.5771),
    "kargil": (34.5539, 76.1329),
    "gulmarg": (34.0495, 74.3965),
    "sonmarg": (34.2985, 75.2940),
    "pahalgam": (34.0134, 75.3210),
    "patnitop": (33.0580, 75.3380),
    "doodhpathri": (33.8500, 74.6300),
    "yusmarg": (33.8220, 74.7500),
    "gurez valley": (34.6446, 74.7450),
    "anantnag": (33.7315, 75.1467),
    "dal lake": (34.0837, 74.8700),
    "wular lake": (34.2988, 74.5690),
    "betaab valley": (33.5930, 75.3367),
    "aru valley": (33.6953, 75.3126),
    "vaishno devi": (32.9400, 74.9500),
    "nubra valley": (34.9650, 77.4760),
    "pangong lake": (33.7610, 78.7600),
    "tso moriri": (32.9378, 78.3035),
    "khardung la": (34.2856, 77.6042),
    "magnetic hill": (34.1077, 77.5660),
    "zanskar": (33.3820, 77.1540),
    "alchi": (34.1977, 77.1716),
    "lamayuru": (34.2746, 76.7898),
    "diskit": (34.5447, 77.5687),
    "hanle": (32.7833, 78.9640),
    "turtuk": (34.8355, 77.6565),
    "hemis": (33.9183, 77.7173),
    "thiksey": (34.0512, 77.5410),
    "shey palace": (34.0581, 77.5617),
    "kavaratti": (10.5626, 72.6369),
    "agatti": (10.8340, 72.1758),
    "bangaram": (10.9436, 72.2935),
    "kadmat": (11.1537, 72.7772),
    "kalpeni": (10.0940, 73.6389),
    "minicoy": (8.2955, 73.0419),
    "thinnakara": (10.9790, 72.2922),
    "andrott": (10.8280, 73.6685),
    "port blair": (11.6234, 92.7265),
    "havelock island": (11.9721, 92.9786),
    "neil island": (11.8340, 93.0410),
    "baratang": (12.1050, 92.7570),
    "ross island": (11.6667, 92.7470),
    "north bay": (11.6998, 92.7510),
    "long island": (12.0230, 92.9720),
    "rangat": (12.4955, 92.8737),
    "mayabunder": (12.9229, 92.9022),
    "great nicobar": (6.9554, 93.8908),
    "puducherry": (11.9416, 79.8083),
    "french quarter": (11.9398, 79.8156),
    "promenade beach": (11.9139, 79.8119),
    "paradise beach": (11.9230, 79.7942),
    "auroville": (12.0056, 79.8086),
    "sri aurobindo ashram": (11.9353, 79.8303),
    "basilica of the sacred heart of jesus": (11.9348, 79.8304),
    "serenity beach": (11.9194, 79.7766),
    "chunnambar boat house": (11.9565, 79.8097),
    "mahe": (11.7033, 75.5366),
    "yanam": (16.7428, 82.2144),
    "karaikal": (10.9285, 79.8327),
    "silvassa": (20.2739, 73.0160),
    "dudhni": (20.2739, 73.0160),
    "khanvel": (20.1942, 73.1215),
    "tribal cultural museum": (20.2677, 73.0127),
    "daman": (20.4173, 72.8324),
    "devka beach": (20.4033, 72.9000),
    "jampore beach": (20.4023, 72.8764),
    "moti daman fort": (20.4173, 72.8511),
    "nani daman fort": (20.4141, 72.8200),
    "st. jerome fort": (20.4175, 72.8395),
    "diu": (20.7148, 70.9873),
    "diu fort": (20.7187, 70.9977),
    "naida caves": (20.7333, 70.9833),
    "nagoa beach": (20.7305, 70.9715),
    "ghoghla beach": (20.7448, 70.9848),
    "st. paul's church": (20.7147, 70.9896),
    "rock garden": (30.7403, 76.7935),
    "sukhna lake": (30.7420, 76.8120),
    "rose garden": (30.7422, 76.8044),
    "capitol complex": (30.7337, 76.7881),
    "sector 17": (30.7343, 76.7882),
    "government museum and art gallery": (30.7341, 76.7903),
    "sukhna wildlife sanctuary": (30.7264, 76.8017),
    "lucknow": (26.8467, 80.9462),
    "mathura": (27.4924, 77.6737),
    "vrindavan": (27.5740, 77.7032),
    "prayagraj": (25.4358, 81.8463),
    "chitrakoot": (25.1714, 80.8675),
    "jhansi": (25.4484, 78.5685),
    "sarnath": (25.3801, 83.0224),
    "kushinagar": (26.7413, 83.8885),
    "fatehpur sikri": (27.0948, 77.6597),
    "kanpur": (26.4499, 80.3319),
    "meerut": (28.9845, 77.7064),
    "dudhwa national park": (28.5303, 80.6500),
    "greater noida": (28.4744, 77.5030),
    "bareilly": (28.3670, 79.4304),
    "gorakhpur": (26.7606, 83.3692),
    "vindhyachal": (24.5517, 82.9539),
    "mirzapur": (25.1337, 82.5647),
    "ayodhya": (26.7997, 82.2044),
    "allahabad": (25.4358, 81.8463),
    "taj mahal": (27.1751, 78.0421),
    "red fort": (28.6562, 77.2410),
    "india gate": (28.6129, 77.2295),
    "qutub minar": (28.5244, 77.1855),
    "humayun's tomb": (28.5933, 77.2504),
    "lotus temple": (28.5535, 77.2588),
    "akshardham": (28.6127, 77.2773),
    "jama masjid": (28.6507, 77.2330),
    "chandni chowk": (28.6562, 77.2302),
    "purana qila": (28.6148, 77.2409),
    "lodhi garden": (28.5935, 77.2185),
    "national museum": (28.6114, 77.2176),
    "connaught place": (28.6315, 77.2167),
    "rashtrapati bhavan": (28.6142, 77.1990),
    "agrasen ki baoli": (28.6517, 77.2283),
    "national zoological park": (28.6103, 77.2791),
    "tawang": (27.5862, 91.8656),
    "ziro valley": (27.5341, 93.8420),
    "bomdila": (27.2677, 92.4000),
    "dirang": (27.3594, 92.2566),
    "itanagar": (27.1004, 93.6161),
    "mechuka": (28.5915, 94.1787),
    "pasighat": (28.0652, 95.3250),
    "roing": (28.1423, 95.8300),
    "namsai": (27.6933, 95.8577),
    "changlang": (27.1305, 96.6987),
    "sela pass": (27.4925, 92.1032),
    "bum la pass": (28.1119, 93.7750),
    "namdapha national park": (27.5312, 96.6018),
    "yingkiong": (28.6178, 94.8333),
    "pakke": (27.1653, 93.0155),
    "mayudia": (27.1238, 93.8232),
    "sri vijaya puram": (11.6234, 92.7265),
    "swaraj dweep": (11.9721, 92.9786),
    "shaheed dweep": (11.8340, 93.0410),
    "north bay": (11.6998, 92.7510),
    "great nicobar": (6.9554, 93.8908),
    "rangat": (12.4955, 92.8737),
    "mayabunder": (12.9229, 92.9022),
    "ross island": (11.6667, 92.7470),
    "baratang": (12.1050, 92.7570),
    "long island": (12.0230, 92.9720),
    "sri vijaya puram": (11.6234, 92.7265),
    "port blair": (11.6234, 92.7265),
    "havelock island": (11.9721, 92.9786),
    "neil island": (11.8340, 93.0410)
}


# ==========================================
# 2. CITY ALIASES
# ==========================================

CITY_ALIASES = {
    "new delhi": "delhi",
    "ncr": "delhi",
    "bangalore": "bengaluru",
    "bombay": "mumbai",
    "calcutta": "kolkata",
    "poona": "pune",
    "andaman and nicobar islands": "port blair",
    "port blair andaman": "port blair",
    "jammu and kashmir": "srinagar",
    "ladakh": "leh",
    "dnhdd": "silvassa",
    "dadra and nagar haveli": "silvassa",
    "daman and diu": "daman",
    "lakshadweep": "kavaratti",
    "aru valley": "araku valley",
    "araku valley": "araku valley",
    "andhra pradesh": "vizag",
    "arunachal pradesh": "tawang",
    "assam": "guwahati",
    "bihar": "rajgir",
    "chhattisgarh": "bastar",
    "gujarat": "ahmedabad",
    "haryana": "kurukshetra",
    "jharkhand": "ranchi",
    "karnataka": "coorg",
    "kerala": "munnar",
    "madhya pradesh": "khajuraho",
    "maharashtra": "mahabaleshwar",
    "manipur": "imphal",
    "meghalaya": "shillong",
    "mizoram": "aizawl",
    "nagaland": "kohima",
    "odisha": "puri",
    "punjab": "amritsar",
    "rajasthan": "jaisalmer",
    "sikkim": "gangtok",
    "tamil nadu": "ooty",
    "telangana": "hyderabad",
    "tripura": "agartala",
    "uttar pradesh": "varanasi",
    "uttarakhand": "mussoorie",
    "west bengal": "darjeeling",
    "goa": "goa",
    "amravati": "amravati",
    "amaravati": "amravati",
    "amaravathi": "amravati",
    "gandikota": "gandikota",
    "srisailam": "srisailam",
    "borra caves": "borra caves",
    "papikondalu": "papikondalu",
    "tirupati": "tirupati",
    "vijayawada": "vijayawada",
    "visakhapatnam": "visakhapatnam",
    "kakinada": "kakinada",
    "rajahmundry": "rajahmundry",
    "kurnool": "kurnool",
    "lepakshi": "lepakshi",
    "horsley hills": "horsley hills",
    "nellore": "nellore",
    "machilipatnam": "machilipatnam",
    "chittoor": "chittoor",
    "mechuka": "mechuka",
    "roing": "roing",
    "namsai": "namsai",
    "changlang": "changlang",
    "sela pass": "sela pass",
    "bum la pass": "bum la pass",
    "namdapha national park": "namdapha national park",
    "yingkiong": "yingkiong",
    "pakke": "pakke",
    "nagaon": "nagaon",
    "majuli": "majuli",
    "manas national park": "manas national park",
    "pobitora wildlife sanctuary": "pobitora wildlife sanctuary",
    "hajo": "hajo",
    "tezpur": "tezpur",
    "jorhat": "jorhat",
    "haflong": "haflong",
    "digboi": "digboi",
    "kamakhya temple": "kamakhya temple",
    "barabar caves": "barabar caves",
    "rajgir": "rajgir",
    "nalanda": "nalanda",
    "vaishali": "vaishali",
    "pawapuri": "pawapuri",
    "valmiki nagar": "valmiki nagar",
    "bhagalpur": "bhagalpur",
    "kesaria": "kesaria",
    "madhubani": "madhubani",
    "jagdalpur": "jagdalpur",
    "chitrakote falls": "chitrakote falls",
    "tirathgarh falls": "tirathgarh falls",
    "kanger valley national park": "kanger valley national park",
    "sirpur": "sirpur",
    "dongargarh": "dongargarh",
    "bhoramdeo": "bhoramdeo",
    "mainpat": "mainpat",
    "sundarbans": "sundarbans",
    "digha": "digha",
    "mandarmani": "mandarmani",
    "dooars": "dooars",
    "jalpaiguri": "jalpaiguri",
    "mirik": "mirik",
    "kurseong": "kurseong",
    "bishnupur": "bishnupur",
    "murshidabad": "murshidabad",
    "bankura": "bankura",
    "bakkhali": "bakkhali",
    "swaraj dweep": "havelock island",
    "shaheed dweep": "neil island",
    "andrott": "andrott",
    "bangaram": "bangaram",
    "kadmat": "kadmat",
    "kalpeni": "kalpeni",
    "minicoy": "minicoy",
    "thinnakara": "thinnakara",
    "sri vijaya puram": "port blair",
    "great nicobar": "great nicobar",
    "make sure": "" 
}


# ==========================================
# 3. TRANSPORT HUBS
# ==========================================

TRANSPORT_HUBS = {

    "shimla": {
        "rail": "Kalka",
        "airport": "Shimla Airport",
        "rail_city": "kalka",
        "airport_city": "shimla",
    },

    "manali": {
        "rail": "Chandigarh",
        "airport": "Bhuntar Airport",
        "rail_city": "chandigarh",
        "airport_city": "bhuntar",
    },

    "mahabaleshwar": {
        "rail": "Pune",
        "airport": "Pune Airport",
        "rail_city": "pune",
        "airport_city": "pune",
    },

    "lonavala": {
        "rail": "Lonavala",
        "airport": "Pune Airport",
        "rail_city": "lonavala",
        "airport_city": "pune",
    },

    "mussoorie": {
        "rail": "Dehradun",
        "airport": "Dehradun Airport",
        "rail_city": "dehradun",
        "airport_city": "dehradun",
    },

    "rishikesh": {
        "rail": "Rishikesh Railway Station",
        "airport": "Dehradun Airport",
        "rail_city": "rishikesh",
        "airport_city": "dehradun",
    },

    "haridwar": {
        "rail": "Haridwar Junction",
        "airport": "Dehradun Airport",
        "rail_city": "haridwar",
        "airport_city": "dehradun",
    },

    "darjeeling": {
        "rail": "New Jalpaiguri",
        "airport": "Bagdogra Airport",
        "rail_city": "siliguri",
        "airport_city": "siliguri",
    },

    "gangtok": {
        "rail": "New Jalpaiguri",
        "airport": "Bagdogra Airport",
        "rail_city": "siliguri",
        "airport_city": "siliguri",
    },

    "munnar": {
        "rail": "Aluva",
        "airport": "Cochin International Airport",
        "rail_city": "aluva",
        "airport_city": "kochi",
    },

    "ooty": {
        "rail": "Coimbatore",
        "airport": "Coimbatore Airport",
        "rail_city": "coimbatore",
        "airport_city": "coimbatore",
    },

    "wayanad": {
        "rail": "Kozhikode",
        "airport": "Kannur International Airport",
        "rail_city": "kozhikode",
        "airport_city": "kannur",
    },

    "leh": {
        "rail": None,
        "airport": "Kushok Bakula Rimpochee Airport",
        "rail_city": None,
        "airport_city": "leh",
    },

    "jaisalmer": {
        "rail": "Jaisalmer",
        "airport": "Jaisalmer Airport",
        "rail_city": "jaisalmer",
        "airport_city": "jaisalmer",
    },

    "goa": {
        "rail": "Madgaon",
        "airport": "Goa International Airport",
        "rail_city": "madgaon",
        "airport_city": "goa",
    },

    "udaipur": {
        "rail": "Udaipur City",
        "airport": "Maharana Pratap Airport",
        "rail_city": "udaipur",
        "airport_city": "udaipur",
    },

    "jodhpur": {
        "rail": "Jodhpur Junction",
        "airport": "Jodhpur Airport",
        "rail_city": "jodhpur",
        "airport_city": "jodhpur",
    },

    "amritsar": {
        "rail": "Amritsar Junction",
        "airport": "Sri Guru Ram Dass Jee International Airport",
        "rail_city": "amritsar",
        "airport_city": "amritsar",
    },

    "mumbai": {
        "rail": "Mumbai Central",
        "airport": "Chhatrapati Shivaji Maharaj International Airport",
        "rail_city": "mumbai",
        "airport_city": "mumbai",
    },

    "delhi": {
        "rail": "New Delhi Railway Station",
        "airport": "Indira Gandhi International Airport",
        "rail_city": "delhi",
        "airport_city": "delhi",
    },

    "chandigarh": {
        "rail": "Chandigarh Railway Station",
        "airport": "Chandigarh Airport",
        "rail_city": "chandigarh",
        "airport_city": "chandigarh",
    },

    "srinagar": {
        "rail": "Jammu Tawi",
        "airport": "Sheikh ul-Alam International Airport",
        "rail_city": "jammu",
        "airport_city": "srinagar",
    },

    "vizag": {
        "rail": "Visakhapatnam Junction",
        "airport": "Visakhapatnam Airport",
        "rail_city": "visakhapatnam",
        "airport_city": "visakhapatnam",
    },

    "araku valley": {
        "rail": "Visakhapatnam Junction",
        "airport": "Visakhapatnam Airport",
        "rail_city": "visakhapatnam",
        "airport_city": "visakhapatnam",
    },

    "tawang": {
        "rail": "Naharlagun",
        "airport": "Tezu Airport",
        "rail_city": "naharlagun",
        "airport_city": "tezu",
    },

    "kaziranga": {
        "rail": "Guwahati",
        "airport": "Lokpriya Gopinath Bordoloi Airport",
        "rail_city": "guwahati",
        "airport_city": "guwahati",
    },

    "rajgir": {
        "rail": "Patna",
        "airport": "Jay Prakash Narayan Airport",
        "rail_city": "patna",
        "airport_city": "patna",
    },

    "bastar": {
        "rail": "Raipur",
        "airport": "Swami Vivekananda Airport",
        "rail_city": "raipur",
        "airport_city": "raipur",
    },

    "saputara": {
        "rail": "Surat",
        "airport": "Surat Airport",
        "rail_city": "surat",
        "airport_city": "surat",
    },

    "coorg": {
        "rail": "Mysore",
        "airport": "Mysore Airport",
        "rail_city": "mysore",
        "airport_city": "mysore",
    },

    "imphal": {
        "rail": "Dimapur",
        "airport": "Imphal Airport",
        "rail_city": "dimapur",
        "airport_city": "imphal",
    },

    "aizawl": {
        "rail": "Silchar",
        "airport": "Lengpui Airport",
        "rail_city": "silchar",
        "airport_city": "aizawl",
    },

    "kohima": {
        "rail": "Dimapur",
        "airport": "Dimapur Airport",
        "rail_city": "dimapur",
        "airport_city": "dimapur",
    },

    "puri": {
        "rail": "Bhubaneswar",
        "airport": "Biju Patnaik Airport",
        "rail_city": "bhubaneswar",
        "airport_city": "bhubaneswar",
    },

    "agartala": {
        "rail": "Lumding",
        "airport": "Agartala Airport",
        "rail_city": "lumding",
        "airport_city": "agartala",
    },

    "shillong": {
        "rail": "Guwahati",
        "airport": "Shillong Airport",
        "rail_city": "guwahati",
        "airport_city": "guwahati",
    },

    "kavaratti": {
        "rail": None,
        "airport": "Agatti Airport",
        "rail_city": None,
        "airport_city": "agatti",
    },

    "port blair": {
        "rail": None,
        "airport": "Veer Savarkar International Airport",
        "rail_city": None,
        "airport_city": "port blair",
    },

    "puducherry": {
        "rail": "Villupuram",
        "airport": "Puducherry Airport",
        "rail_city": "villupuram",
        "airport_city": "puducherry",
    },

    "silvassa": {
        "rail": "Vapi",
        "airport": "Surat Airport",
        "rail_city": "vapi",
        "airport_city": "surat",
    },

    "daman": {
        "rail": "Vapi",
        "airport": "Daman Airport",
        "rail_city": "vapi",
        "airport_city": "daman",
    },

    "kurukshetra": {
        "rail": "Kurukshetra Junction",
        "airport": "Chandigarh Airport",
        "rail_city": "kurukshetra",
        "airport_city": "chandigarh",
    },

    "netarhat": {
        "rail": "Ranchi",
        "airport": "Ranchi Airport",
        "rail_city": "ranchi",
        "airport_city": "ranchi",
    },

    "warangal": {
        "rail": "Kazipet",
        "airport": "Rajiv Gandhi International Airport",
        "rail_city": "kazipet",
        "airport_city": "hyderabad",
    },

    "mahabalipuram": {
        "rail": "Chennai",
        "airport": "Chennai Airport",
        "rail_city": "chennai",
        "airport_city": "chennai",
    },

    "bhubaneswar": {
        "rail": "Bhubaneswar",
        "airport": "Biju Patnaik Airport",
        "rail_city": "bhubaneswar",
        "airport_city": "bhubaneswar",
    },

    "guwahati": {
        "rail": "Guwahati",
        "airport": "Lokpriya Gopinath Bordoloi Airport",
        "rail_city": "guwahati",
        "airport_city": "guwahati",
    },

    "gwalior": {
        "rail": "Gwalior Junction",
        "airport": "Gwalior Airport",
        "rail_city": "gwalior",
        "airport_city": "gwalior",
    },

    "jabalpur": {
        "rail": "Jabalpur Junction",
        "airport": "Jabalpur Airport",
        "rail_city": "jabalpur",
        "airport_city": "jabalpur",
    },

    "gorakhpur": {
        "rail": "Gorakhpur Junction",
        "airport": "Mahayogi Gorakhnath Airport",
        "rail_city": "gorakhpur",
        "airport_city": "gorakhpur",
    },

    "kolkata": {
        "rail": "Sealdah Railway Station",
        "airport": "Netaji Subhas Chandra Bose International Airport",
        "rail_city": "kolkata",
        "airport_city": "kolkata",
    },

    "ranchi": {
        "rail": "Ranchi Railway Station",
        "airport": "Birsa Munda Airport",
        "rail_city": "ranchi",
        "airport_city": "ranchi",
    },

    "ghaziabad": {
        "rail": "Ghaziabad Junction",
        "airport": "Indira Gandhi International Airport",
        "rail_city": "ghaziabad",
        "airport_city": "delhi",
    },

    "allahabad": {
        "rail": "Prayagraj Junction",
        "airport": "Allahabad Airport",
        "rail_city": "prayagraj",
        "airport_city": "prayagraj",
    },

    "kochi": {
        "rail": "Ernakulam Junction",
        "airport": "Cochin International Airport",
        "rail_city": "kochi",
        "airport_city": "kochi",
    },

    "srinagar": {
        "rail": "Jammu Tawi",
        "airport": "Sheikh ul-Alam International Airport",
        "rail_city": "jammu",
        "airport_city": "srinagar",
    },
}


# ==========================================
# 4. DESTINATION INFORMATION
# ==========================================

DESTINATIONS = {

    "shimla": {
        "name": "Shimla",
        "state": "Himachal Pradesh",
        "type": "hill_station",
        "best_season": "March to June and September to November",
        "hotel_prices": {
            "budget": 800,
            "standard": 2000,
            "premium": 3000,
            "luxury": 5000,
        },
        "food_per_person_day": 700,
        "local_transport_per_person_day": 300,
        "activities_per_person_day": 500,
    },

    "manali": {
        "name": "Manali",
        "state": "Himachal Pradesh",
        "type": "hill_station",
        "best_season": "March to June and October to February",
        "hotel_prices": {
            "budget": 900,
            "standard": 2200,
            "premium": 3500,
            "luxury": 5500,
        },
        "food_per_person_day": 750,
        "local_transport_per_person_day": 350,
        "activities_per_person_day": 800,
    },

    "mahabaleshwar": {
        "name": "Mahabaleshwar",
        "state": "Maharashtra",
        "type": "hill_station",
        "best_season": "October to June",
        "hotel_prices": {
            "budget": 1000,
            "standard": 2200,
            "premium": 3500,
            "luxury": 5500,
        },
        "food_per_person_day": 700,
        "local_transport_per_person_day": 300,
        "activities_per_person_day": 500,
    },

    "goa": {
        "name": "Goa",
        "state": "Goa",
        "type": "beach",
        "best_season": "November to February",
        "hotel_prices": {
            "budget": 1000,
            "standard": 2500,
            "premium": 4000,
            "luxury": 6500,
        },
        "food_per_person_day": 800,
        "local_transport_per_person_day": 400,
        "activities_per_person_day": 800,
    },

    "jaipur": {
        "name": "Jaipur",
        "state": "Rajasthan",
        "type": "heritage",
        "best_season": "October to March",
        "hotel_prices": {
            "budget": 700,
            "standard": 1800,
            "premium": 3000,
            "luxury": 5000,
        },
        "food_per_person_day": 650,
        "local_transport_per_person_day": 300,
        "activities_per_person_day": 500,
    },

    "agra": {
        "name": "Agra",
        "state": "Uttar Pradesh",
        "type": "heritage",
        "best_season": "October to March",
        "hotel_prices": {
            "budget": 700,
            "standard": 1700,
            "premium": 2800,
            "luxury": 4500,
        },
        "food_per_person_day": 600,
        "local_transport_per_person_day": 250,
        "activities_per_person_day": 400,
    },

    "varanasi": {
        "name": "Varanasi",
        "state": "Uttar Pradesh",
        "type": "spiritual",
        "best_season": "October to March",
        "hotel_prices": {
            "budget": 600,
            "standard": 1600,
            "premium": 2800,
            "luxury": 4500,
        },
        "food_per_person_day": 600,
        "local_transport_per_person_day": 250,
        "activities_per_person_day": 400,
    },

    "rishikesh": {
        "name": "Rishikesh",
        "state": "Uttarakhand",
        "type": "adventure",
        "best_season": "March to May and September to November",
        "hotel_prices": {
            "budget": 700,
            "standard": 1800,
            "premium": 3000,
            "luxury": 5000,
        },
        "food_per_person_day": 650,
        "local_transport_per_person_day": 250,
        "activities_per_person_day": 700,
    },

    "udaipur": {
        "name": "Udaipur",
        "state": "Rajasthan",
        "type": "heritage",
        "best_season": "October to March",
        "hotel_prices": {"budget": 800, "standard": 2200, "premium": 3800, "luxury": 6500},
        "food_per_person_day": 700,
        "local_transport_per_person_day": 300,
        "activities_per_person_day": 600,
    },

    "jodhpur": {
        "name": "Jodhpur",
        "state": "Rajasthan",
        "type": "heritage",
        "best_season": "October to March",
        "hotel_prices": {"budget": 700, "standard": 1800, "premium": 3200, "luxury": 5500},
        "food_per_person_day": 650,
        "local_transport_per_person_day": 280,
        "activities_per_person_day": 500,
    },

    "jaisalmer": {
        "name": "Jaisalmer",
        "state": "Rajasthan",
        "type": "desert",
        "best_season": "October to February",
        "hotel_prices": {"budget": 800, "standard": 2000, "premium": 3500, "luxury": 6000},
        "food_per_person_day": 650,
        "local_transport_per_person_day": 350,
        "activities_per_person_day": 850,
    },

    "amritsar": {
        "name": "Amritsar",
        "state": "Punjab",
        "type": "heritage",
        "best_season": "October to March",
        "hotel_prices": {"budget": 700, "standard": 1800, "premium": 3000, "luxury": 5000},
        "food_per_person_day": 650,
        "local_transport_per_person_day": 250,
        "activities_per_person_day": 450,
    },

    "mumbai": {
        "name": "Mumbai",
        "state": "Maharashtra",
        "type": "city_break",
        "best_season": "October to February",
        "hotel_prices": {"budget": 1200, "standard": 3000, "premium": 5000, "luxury": 8500},
        "food_per_person_day": 900,
        "local_transport_per_person_day": 500,
        "activities_per_person_day": 700,
    },

    "kochi": {
        "name": "Kochi",
        "state": "Kerala",
        "type": "coastal",
        "best_season": "October to March",
        "hotel_prices": {"budget": 900, "standard": 2200, "premium": 3800, "luxury": 6500},
        "food_per_person_day": 750,
        "local_transport_per_person_day": 350,
        "activities_per_person_day": 550,
    },

    "ooty": {
        "name": "Ooty",
        "state": "Tamil Nadu",
        "type": "hill_station",
        "best_season": "October to June",
        "hotel_prices": {"budget": 900, "standard": 2200, "premium": 3500, "luxury": 5500},
        "food_per_person_day": 700,
        "local_transport_per_person_day": 350,
        "activities_per_person_day": 550,
    },

    "gangtok": {
        "name": "Gangtok",
        "state": "Sikkim",
        "type": "hill_station",
        "best_season": "March to June and September to November",
        "hotel_prices": {"budget": 900, "standard": 2200, "premium": 3800, "luxury": 6000},
        "food_per_person_day": 700,
        "local_transport_per_person_day": 400,
        "activities_per_person_day": 650,
    },

    "srinagar": {
        "name": "Srinagar",
        "state": "Jammu and Kashmir",
        "type": "valley_escape",
        "best_season": "April to October",
        "hotel_prices": {"budget": 1000, "standard": 2500, "premium": 4500, "luxury": 7500},
        "food_per_person_day": 750,
        "local_transport_per_person_day": 450,
        "activities_per_person_day": 700,
    },

    "leh": {
        "name": "Leh",
        "state": "Ladakh",
        "type": "mountain_adventure",
        "best_season": "May to September",
        "hotel_prices": {"budget": 1000, "standard": 2500, "premium": 4500, "luxury": 7500},
        "food_per_person_day": 800,
        "local_transport_per_person_day": 500,
        "activities_per_person_day": 300,
    },

    "mussoorie": {
        "name": "Mussoorie",
        "state": "Uttarakhand",
        "type": "hill_station",
        "best_season": "March to June and September to November",
        "hotel_prices": {
            "budget": 800,
            "standard": 2000,
            "premium": 3200,
            "luxury": 5000,
        },
        "food_per_person_day": 700,
        "local_transport_per_person_day": 300,
        "activities_per_person_day": 500,
    },

    "darjeeling": {
        "name": "Darjeeling",
        "state": "West Bengal",
        "type": "hill_station",
        "best_season": "March to May and October to November",
        "hotel_prices": {
            "budget": 800,
            "standard": 1900,
            "premium": 3200,
            "luxury": 5000,
        },
        "food_per_person_day": 650,
        "local_transport_per_person_day": 300,
        "activities_per_person_day": 500,
    },

    "munnar": {
        "name": "Munnar",
        "state": "Kerala",
        "type": "hill_station",
        "best_season": "September to May",
        "hotel_prices": {
            "budget": 900,
            "standard": 2000,
            "premium": 3500,
            "luxury": 5500,
        },
        "food_per_person_day": 700,
        "local_transport_per_person_day": 350,
        "activities_per_person_day": 600,
    },
}


# ==========================================
# 5. TRANSPORT SETTINGS
# ==========================================

TRANSPORT_SETTINGS = {

    "road": {
        "fuel_price": 100,
        "mileage": 14,
        "toll_per_km": 0.70,
        "parking_and_misc": 300,
    },

    "train": {
        "rate_per_km": 1.30,
        "base_fare": 150,
    },

    "flight": {
        "rate_per_km": 6.50,
        "base_fare": 2200,
    },

    "bus": {
        "rate_per_km": 1.80,
        "base_fare": 100,
    },
}


# ==========================================
# 6. NORMALIZE CITY
# ==========================================

def normalize_city(city):

    if not city:
        return None

    city = str(city).strip().lower()

    # Normalize common input variations that appear in the UI and manual entries.
    city = city.replace("_", " ")
    city = " ".join(city.split())

    if city in CITY_ALIASES:
        return CITY_ALIASES[city]

    aliases = {
        "new delhi": "delhi",
        "delhi ncr": "delhi",
        "ncr delhi": "delhi",
        "bangalore": "bengaluru",
        "bengaluru city": "bengaluru",
        "bombay": "mumbai",
        "calcutta": "kolkata",
        "poona": "pune",
        "ooty hill station": "ooty",
        "munnar hill station": "munnar",
        "munnar tea gardens": "munnar",
        "varanasi city": "varanasi",
        "puri beach": "puri",
        "goa beach": "goa",
        "leh ladakh": "leh",
        "manali himachal": "manali",
    }

    return aliases.get(city, city)


# ==========================================
# 7. HAVERSINE DISTANCE
# ==========================================

def haversine_distance(lat1, lon1, lat2, lon2):

    earth_radius = 6371.0

    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)

    a = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat1_rad)
        * math.cos(lat2_rad)
        * math.sin(delta_lon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius * c


# ==========================================
# 8. ROAD DISTANCE
# ==========================================

def get_distance(from_city, destination):

    from_city = normalize_city(from_city)
    destination = normalize_city(destination)

    if from_city not in CITY_COORDINATES:
        return None

    if destination not in CITY_COORDINATES:
        return None

    lat1, lon1 = CITY_COORDINATES[from_city]
    lat2, lon2 = CITY_COORDINATES[destination]

    straight_distance = haversine_distance(
        lat1,
        lon1,
        lat2,
        lon2
    )

    # Approximate road distance
    road_distance = straight_distance * 1.20

    return round(road_distance, 1)


# ==========================================
# 9. DESTINATION INFO
# ==========================================

def get_destination_info(destination):

    destination = normalize_city(destination)

    if destination in DESTINATIONS:
        return DESTINATIONS.get(destination)

    fallback_name = destination.replace("-", " ").title()

    return {
        "name": fallback_name,
        "state": "India",
        "type": "travel_destination",
        "best_season": "October to March",
        "hotel_prices": {
            "budget": 1000,
            "standard": 2200,
            "premium": 3500,
            "luxury": 6000,
        },
        "food_per_person_day": 700,
        "local_transport_per_person_day": 350,
        "activities_per_person_day": 500,
    }


# ==========================================
# 10. TRANSPORT HUBS
# ==========================================

def get_nearest_transport_hub(destination, hub_type):
    destination = normalize_city(destination)

    if not destination or destination not in CITY_COORDINATES:
        return None

    destination_lat, destination_lon = CITY_COORDINATES[destination]

    candidates = []

    for hub_data in TRANSPORT_HUBS.values():
        hub_city = hub_data.get(f"{hub_type}_city")

        if not hub_city or hub_city not in CITY_COORDINATES:
            continue

        hub_lat, hub_lon = CITY_COORDINATES[hub_city]
        distance = haversine_distance(
            destination_lat,
            destination_lon,
            hub_lat,
            hub_lon,
        )

        candidates.append((distance, hub_data.get(hub_type), hub_city))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0])
    nearest = candidates[0][1]

    return nearest if nearest else None


def get_transport_hubs(destination):

    destination = normalize_city(destination)

    if destination in TRANSPORT_HUBS:
        hub = TRANSPORT_HUBS.get(destination)
        rail = hub.get("rail")
        airport = hub.get("airport")

        if rail is None:
            rail = get_nearest_transport_hub(destination, "rail")

        if airport is None:
            airport = get_nearest_transport_hub(destination, "airport")

        return {
            "rail": rail,
            "airport": airport,
            "rail_city": hub.get("rail_city"),
            "airport_city": hub.get("airport_city"),
        }

    rail = get_nearest_transport_hub(destination, "rail")
    airport = get_nearest_transport_hub(destination, "airport")

    return {
        "rail": rail,
        "airport": airport,
        "rail_city": None,
        "airport_city": destination,
    }


# ==========================================
# 11. ROAD COST CALCULATION
# ==========================================

def calculate_road_cost(
    one_way_distance,
    travelers
):
    """
    Calculate total road vehicle cost.

    IMPORTANT:
    Fuel/vehicle cost is NOT multiplied by travelers.

    Example:
    A car carrying 4 people still consumes approximately
    the same amount of fuel as the same car carrying 2 people.

    The total vehicle cost is shared between travelers.
    """

    if one_way_distance is None:
        return None

    travelers = max(int(travelers), 1)

    settings = TRANSPORT_SETTINGS["road"]

    # Round trip
    round_trip_distance = one_way_distance * 2

    # Fuel required
    fuel_required = (
        round_trip_distance / settings["mileage"]
    )

    # Fuel cost
    fuel_cost = (
        fuel_required * settings["fuel_price"]
    )

    # Estimated tolls
    toll_cost = (
        round_trip_distance * settings["toll_per_km"]
    )

    # Parking and miscellaneous road charges
    parking_misc = settings["parking_and_misc"]

    # Total vehicle cost
    total_vehicle_cost = (
        fuel_cost
        + toll_cost
        + parking_misc
    )

    # Shared cost
    per_person_cost = (
        total_vehicle_cost / travelers
    )

    return {
        "one_way_distance_km": round(
            one_way_distance,
            1
        ),

        "round_trip_distance_km": round(
            round_trip_distance,
            1
        ),

        "fuel_required_litres": round(
            fuel_required,
            2
        ),

        "fuel_price_per_litre": settings[
            "fuel_price"
        ],

        "fuel_cost": round(
            fuel_cost
        ),

        "toll_cost": round(
            toll_cost
        ),

        "parking_and_misc": round(
            parking_misc
        ),

        "total_vehicle_cost": round(
            total_vehicle_cost
        ),

        "travelers": travelers,

        "shared_cost_per_person": round(
            per_person_cost
        ),
    }


# ==========================================
# 12. TRAIN COST
# ==========================================

def calculate_train_cost(
    one_way_distance,
    travelers
):

    if one_way_distance is None:
        return None

    travelers = max(int(travelers), 1)

    settings = TRANSPORT_SETTINGS["train"]

    # Round trip ticket estimate
    ticket_per_person = (
        settings["base_fare"]
        + (
            one_way_distance
            * settings["rate_per_km"]
        )
    )

    group_cost = (
        ticket_per_person
        * travelers
    )

    return {
        "ticket_cost_per_person": round(
            ticket_per_person
        ),

        "travelers": travelers,

        "total_group_cost": round(
            group_cost
        ),
    }


# ==========================================
# 13. FLIGHT COST
# ==========================================

def calculate_flight_cost(
    one_way_distance,
    travelers
):

    if one_way_distance is None:
        return None

    travelers = max(int(travelers), 1)

    settings = TRANSPORT_SETTINGS["flight"]

    ticket_per_person = (
        settings["base_fare"]
        + (
            one_way_distance
            * settings["rate_per_km"]
        )
    )

    group_cost = (
        ticket_per_person
        * travelers
    )

    return {
        "ticket_cost_per_person": round(
            ticket_per_person
        ),

        "travelers": travelers,

        "total_group_cost": round(
            group_cost
        ),
    }


# ==========================================
# 14. BUS COST
# ==========================================

def calculate_bus_cost(
    one_way_distance,
    travelers
):

    if one_way_distance is None:
        return None

    travelers = max(int(travelers), 1)

    settings = TRANSPORT_SETTINGS["bus"]

    ticket_per_person = (
        settings["base_fare"]
        + (
            one_way_distance
            * settings["rate_per_km"]
        )
    )

    group_cost = (
        ticket_per_person
        * travelers
    )

    return {
        "ticket_cost_per_person": round(
            ticket_per_person
        ),

        "travelers": travelers,

        "total_group_cost": round(
            group_cost
        ),
    }


# ==========================================
# 15. TRANSPORT OPTIONS
# ==========================================

def calculate_all_transport(
    from_city,
    destination,
    travelers
):

    distance = get_distance(
        from_city,
        destination
    )

    if distance is None:
        return None

    return {
        "road": calculate_road_cost(
            distance,
            travelers
        ),

        "train": calculate_train_cost(
            distance,
            travelers
        ),

        "flight": calculate_flight_cost(
            distance,
            travelers
        ),

        "bus": calculate_bus_cost(
            distance,
            travelers
        ),
    }


# ==========================================
# 16. BASIC TRANSPORT RECOMMENDATION
# ==========================================

def recommend_transport(
    from_city,
    destination,
    travelers,
    budget,
    preferred_mode="auto"
):

    distance = get_distance(
        from_city,
        destination
    )

    if distance is None:
        return {
            "mode": None,
            "reason": "Route could not be calculated."
        }

    options = calculate_all_transport(
        from_city,
        destination,
        travelers
    )

    # User specifically selected a mode
    if preferred_mode in options:

        selected = options[preferred_mode]

        return {
            "mode": preferred_mode,
            "reason": "Selected according to your preference.",
            "cost": selected,
            "options": options,
        }

    # Automatic recommendation
    road_cost = options["road"]["total_vehicle_cost"]
    train_cost = options["train"]["total_group_cost"]
    bus_cost = options["bus"]["total_group_cost"]
    flight_cost = options["flight"]["total_group_cost"]

    costs = {
        "road": road_cost,
        "train": train_cost,
        "bus": bus_cost,
        "flight": flight_cost,
    }

    affordable = {
        mode: cost
        for mode, cost in costs.items()
        if cost <= budget
    }

    if affordable:

        recommended_mode = min(
            affordable,
            key=affordable.get
        )

        return {
            "mode": recommended_mode,
            "reason": (
                "Recommended based on the estimated "
                "group transport cost and your budget."
            ),
            "cost": options[recommended_mode],
            "options": options,
        }

    # If nothing fits budget, choose cheapest
    recommended_mode = min(
        costs,
        key=costs.get
    )

    return {
        "mode": recommended_mode,
        "reason": (
            "No estimated transport option fits "
            "the complete budget, so the lowest-cost "
            "transport option is shown."
        ),
        "cost": options[recommended_mode],
        "options": options,
    }


# ==========================================
# 17. TEST
# ==========================================

if __name__ == "__main__":

    print("\n==========================================")
    print("      PLAN MYYATRA TRANSPORT TEST")
    print("==========================================\n")

    from_city = "Delhi"
    destination = "Shimla"
    travelers = 2
    budget = 15000

    distance = get_distance(
        from_city,
        destination
    )

    print("Route:")
    print(
        from_city,
        "→",
        destination
    )

    print(
        "One-way distance:",
        distance,
        "km"
    )

    print("\n--- ROAD ---")

    road = calculate_road_cost(
        distance,
        travelers
    )

    print(road)

    print("\n--- TRAIN ---")

    train = calculate_train_cost(
        distance,
        travelers
    )

    print(train)

    print("\n--- FLIGHT ---")

    flight = calculate_flight_cost(
        distance,
        travelers
    )

    print(flight)

    print("\n--- BUS ---")

    bus = calculate_bus_cost(
        distance,
        travelers
    )

    print(bus)

    print("\n--- RECOMMENDATION ---")

    recommendation = recommend_transport(
        from_city,
        destination,
        travelers,
        budget,
        "auto"
    )

    print(recommendation)

    print("\n==========================================")
    print("Transport test completed.")
    print("==========================================\n")
