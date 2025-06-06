import os
import pygame
#used edge-tts
voice = 'en-US-AnaNeural'
def speak(data):
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "voicedata/data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("voicedata/data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()

        pygame.mixer.quit()

'''
*****************.  extra voice packs and languages.  .**********************************


ShortName: af-ZA-AdriNeural
Gender: Female
Locale: af-ZA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}
# Name: Microsoft Server Speech Text to Speech Voice (af-ZA, Wi
llemNeural)
ShortName: af-ZA-WillemNeural
Gender: Male
Locale: af-ZA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sq-AL, An
ilaNeural)
ShortName: sq-AL-AnilaNeural
Gender: Female
Locale: sq-AL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sq-AL, Il
irNeural)
ShortName: sq-AL-IlirNeural
Gender: Male
Locale: sq-AL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (am-ET, Am
ehaNeural)
ShortName: am-ET-AmehaNeural
Gender: Male
Locale: am-ET
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (am-ET, Me
kdesNeural)
ShortName: am-ET-MekdesNeural
Gender: Female
Locale: am-ET
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-DZ, Am
inaNeural)
ShortName: ar-DZ-AminaNeural
Gender: Female
Locale: ar-DZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-DZ, Is
maelNeural)
ShortName: ar-DZ-IsmaelNeural
Gender: Male
Locale: ar-DZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-BH, Al
iNeural)
ShortName: ar-BH-AliNeural
Gender: Male
Locale: ar-BH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-BH, La
ilaNeural)
ShortName: ar-BH-LailaNeural
Gender: Female
Locale: ar-BH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-EG, Sa
lmaNeural)
ShortName: ar-EG-SalmaNeural
Gender: Female
Locale: ar-EG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-EG, Sh
akirNeural)
ShortName: ar-EG-ShakirNeural
Gender: Male
Locale: ar-EG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-IQ, Ba
sselNeural)
ShortName: ar-IQ-BasselNeural
Gender: Male
Locale: ar-IQ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-IQ, Ra
naNeural)
ShortName: ar-IQ-RanaNeural
Gender: Female
Locale: ar-IQ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-JO, Sa
naNeural)
ShortName: ar-JO-SanaNeural
Gender: Female
Locale: ar-JO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-JO, Ta
imNeural)
ShortName: ar-JO-TaimNeural
Gender: Male
Locale: ar-JO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-KW, Fa
hedNeural)
ShortName: ar-KW-FahedNeural
Gender: Male
Locale: ar-KW
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-KW, No
uraNeural)
ShortName: ar-KW-NouraNeural
Gender: Female
Locale: ar-KW
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-LB, La
ylaNeural)
ShortName: ar-LB-LaylaNeural
Gender: Female
Locale: ar-LB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-LB, Ra
miNeural)
ShortName: ar-LB-RamiNeural
Gender: Male
Locale: ar-LB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-LY, Im
anNeural)
ShortName: ar-LY-ImanNeural
Gender: Female
Locale: ar-LY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-LY, Om
arNeural)
ShortName: ar-LY-OmarNeural
Gender: Male
Locale: ar-LY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-MA, Ja
malNeural)
ShortName: ar-MA-JamalNeural
Gender: Male
Locale: ar-MA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-MA, Mo
unaNeural)
ShortName: ar-MA-MounaNeural
Gender: Female
Locale: ar-MA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-OM, Ab
dullahNeural)
ShortName: ar-OM-AbdullahNeural
Gender: Male
Locale: ar-OM
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-OM, Ay
shaNeural)
ShortName: ar-OM-AyshaNeural
Gender: Female
Locale: ar-OM
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-QA, Am
alNeural)
ShortName: ar-QA-AmalNeural
Gender: Female
Locale: ar-QA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-QA, Mo
azNeural)
ShortName: ar-QA-MoazNeural
Gender: Male
Locale: ar-QA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-SA, Ha
medNeural)
ShortName: ar-SA-HamedNeural
Gender: Male
Locale: ar-SA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-SA, Za
riyahNeural)
ShortName: ar-SA-ZariyahNeural
Gender: Female
Locale: ar-SA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-SY, Am
anyNeural)
ShortName: ar-SY-AmanyNeural
Gender: Female
Locale: ar-SY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-SY, La
ithNeural)
ShortName: ar-SY-LaithNeural
Gender: Male
Locale: ar-SY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-TN, He
diNeural)
ShortName: ar-TN-HediNeural
Gender: Male
Locale: ar-TN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-TN, Re
emNeural)
ShortName: ar-TN-ReemNeural
Gender: Female
Locale: ar-TN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-AE, Fa
timaNeural)
ShortName: ar-AE-FatimaNeural
Gender: Female
Locale: ar-AE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-AE, Ha
mdanNeural)
ShortName: ar-AE-HamdanNeural
Gender: Male
Locale: ar-AE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-YE, Ma
ryamNeural)
ShortName: ar-YE-MaryamNeural
Gender: Female
Locale: ar-YE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ar-YE, Sa
lehNeural)
ShortName: ar-YE-SalehNeural
Gender: Male
Locale: ar-YE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (az-AZ, Ba
bekNeural)
ShortName: az-AZ-BabekNeural
Gender: Male
Locale: az-AZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (az-AZ, Ba
nuNeural)
ShortName: az-AZ-BanuNeural
Gender: Female
Locale: az-AZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bn-BD, Na
banitaNeural)
ShortName: bn-BD-NabanitaNeural
Gender: Female
Locale: bn-BD
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bn-BD, Pr
adeepNeural)
ShortName: bn-BD-PradeepNeural
Gender: Male
Locale: bn-BD
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bn-IN, Ba
shkarNeural)
ShortName: bn-IN-BashkarNeural
Gender: Male
Locale: bn-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bn-IN, Ta
nishaaNeural)
ShortName: bn-IN-TanishaaNeural
Gender: Female
Locale: bn-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bs-BA, Go
ranNeural)
ShortName: bs-BA-GoranNeural
Gender: Male
Locale: bs-BA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bs-BA, Ve
snaNeural)
ShortName: bs-BA-VesnaNeural
Gender: Female
Locale: bs-BA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bg-BG, Bo
rislavNeural)
ShortName: bg-BG-BorislavNeural
Gender: Male
Locale: bg-BG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (bg-BG, Ka
linaNeural)
ShortName: bg-BG-KalinaNeural
Gender: Female
Locale: bg-BG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (my-MM, Ni
larNeural)
ShortName: my-MM-NilarNeural
Gender: Female
Locale: my-MM
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (my-MM, Th
ihaNeural)
ShortName: my-MM-ThihaNeural
Gender: Male
Locale: my-MM
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ca-ES, En
ricNeural)
ShortName: ca-ES-EnricNeural
Gender: Male
Locale: ca-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ca-ES, Jo
anaNeural)
ShortName: ca-ES-JoanaNeural
Gender: Female
Locale: ca-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-HK, Hi
uGaaiNeural)
ShortName: zh-HK-HiuGaaiNeural
Gender: Female
Locale: zh-HK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-HK, Hi
uMaanNeural)
ShortName: zh-HK-HiuMaanNeural
Gender: Female
Locale: zh-HK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-HK, Wa
nLungNeural)
ShortName: zh-HK-WanLungNeural
Gender: Male
Locale: zh-HK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN, Xi
aoxiaoNeural)
ShortName: zh-CN-XiaoxiaoNeural
Gender: Female
Locale: zh-CN
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Warm']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN, Xi
aoyiNeural)
ShortName: zh-CN-XiaoyiNeural
Gender: Female
Locale: zh-CN
VoiceTag: {'ContentCategories': ['Cartoon', 'Novel'], 'VoiceP
ersonalities': ['Lively']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN, Yu
njianNeural)
ShortName: zh-CN-YunjianNeural
Gender: Male
Locale: zh-CN
VoiceTag: {'ContentCategories': ['Sports', ' Novel'], 'VoiceP
ersonalities': ['Passion']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN, Yu
nxiNeural)
ShortName: zh-CN-YunxiNeural
Gender: Male
Locale: zh-CN
VoiceTag: {'ContentCategories': ['Novel'], 'VoicePersonalitie
s': ['Lively', 'Sunshine']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN, Yu
nxiaNeural)
ShortName: zh-CN-YunxiaNeural
Gender: Male
Locale: zh-CN
VoiceTag: {'ContentCategories': ['Cartoon', 'Novel'], 'VoiceP
ersonalities': ['Cute']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN, Yu
nyangNeural)
ShortName: zh-CN-YunyangNeural
Gender: Male
Locale: zh-CN
VoiceTag: {'ContentCategories': ['News'], 'VoicePersonalities
': ['Professional', 'Reliable']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN-lia
oning, XiaobeiNeural)
ShortName: zh-CN-liaoning-XiaobeiNeural
Gender: Female
Locale: zh-CN-liaoning
VoiceTag: {'ContentCategories': ['Dialect'], 'VoicePersonalit
ies': ['Humorous']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-TW, Hs
iaoChenNeural)
ShortName: zh-TW-HsiaoChenNeural
Gender: Female
Locale: zh-TW
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-TW, Yu
nJheNeural)
ShortName: zh-TW-YunJheNeural
Gender: Male
Locale: zh-TW
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-TW, Hs
iaoYuNeural)
ShortName: zh-TW-HsiaoYuNeural
Gender: Female
Locale: zh-TW
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zh-CN-sha
anxi, XiaoniNeural)
ShortName: zh-CN-shaanxi-XiaoniNeural
Gender: Female
Locale: zh-CN-shaanxi
VoiceTag: {'ContentCategories': ['Dialect'], 'VoicePersonalit
ies': ['Bright']}

# Name: Microsoft Server Speech Text to Speech Voice (hr-HR, Ga
brijelaNeural)
ShortName: hr-HR-GabrijelaNeural
Gender: Female
Locale: hr-HR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (hr-HR, Sr
eckoNeural)
ShortName: hr-HR-SreckoNeural
Gender: Male
Locale: hr-HR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (cs-CZ, An
toninNeural)
ShortName: cs-CZ-AntoninNeural
Gender: Male
Locale: cs-CZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (cs-CZ, Vl
astaNeural)
ShortName: cs-CZ-VlastaNeural
Gender: Female
Locale: cs-CZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (da-DK, Ch
ristelNeural)
ShortName: da-DK-ChristelNeural
Gender: Female
Locale: da-DK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (da-DK, Je
ppeNeural)
ShortName: da-DK-JeppeNeural
Gender: Male
Locale: da-DK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nl-BE, Ar
naudNeural)
ShortName: nl-BE-ArnaudNeural
Gender: Male
Locale: nl-BE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nl-BE, De
naNeural)
ShortName: nl-BE-DenaNeural
Gender: Female
Locale: nl-BE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nl-NL, Co
letteNeural)
ShortName: nl-NL-ColetteNeural
Gender: Female
Locale: nl-NL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nl-NL, Fe
nnaNeural)
ShortName: nl-NL-FennaNeural
Gender: Female
Locale: nl-NL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nl-NL, Ma
artenNeural)
ShortName: nl-NL-MaartenNeural
Gender: Male
Locale: nl-NL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-AU, Na
tashaNeural)
ShortName: en-AU-NatashaNeural
Gender: Female
Locale: en-AU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-AU, Wi
lliamNeural)
ShortName: en-AU-WilliamNeural
Gender: Male
Locale: en-AU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-CA, Cl
araNeural)
ShortName: en-CA-ClaraNeural
Gender: Female
Locale: en-CA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-CA, Li
amNeural)
ShortName: en-CA-LiamNeural
Gender: Male
Locale: en-CA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-HK, Sa
mNeural)
ShortName: en-HK-SamNeural
Gender: Male
Locale: en-HK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-HK, Ya
nNeural)
ShortName: en-HK-YanNeural
Gender: Female
Locale: en-HK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-IN, Ne
erjaNeural)
ShortName: en-IN-NeerjaNeural
Gender: Female
Locale: en-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-IN, Pr
abhatNeural)
ShortName: en-IN-PrabhatNeural
Gender: Male
Locale: en-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-IE, Co
nnorNeural)
ShortName: en-IE-ConnorNeural
Gender: Male
Locale: en-IE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-IE, Em
ilyNeural)
ShortName: en-IE-EmilyNeural
Gender: Female
Locale: en-IE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-KE, As
iliaNeural)
ShortName: en-KE-AsiliaNeural
Gender: Female
Locale: en-KE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-KE, Ch
ilembaNeural)
ShortName: en-KE-ChilembaNeural
Gender: Male
Locale: en-KE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-NZ, Mi
tchellNeural)
ShortName: en-NZ-MitchellNeural
Gender: Male
Locale: en-NZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-NZ, Mo
llyNeural)
ShortName: en-NZ-MollyNeural
Gender: Female
Locale: en-NZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-NG, Ab
eoNeural)
ShortName: en-NG-AbeoNeural
Gender: Male
Locale: en-NG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-NG, Ez
inneNeural)
ShortName: en-NG-EzinneNeural
Gender: Female
Locale: en-NG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-PH, Ja
mesNeural)
ShortName: en-PH-JamesNeural
Gender: Male
Locale: en-PH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-PH, Ro
saNeural)
ShortName: en-PH-RosaNeural
Gender: Female
Locale: en-PH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-SG, Lu
naNeural)
ShortName: en-SG-LunaNeural
Gender: Female
Locale: en-SG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-SG, Wa
yneNeural)
ShortName: en-SG-WayneNeural
Gender: Male
Locale: en-SG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-ZA, Le
ahNeural)
ShortName: en-ZA-LeahNeural
Gender: Female
Locale: en-ZA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-ZA, Lu
keNeural)
ShortName: en-ZA-LukeNeural
Gender: Male
Locale: en-ZA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-TZ, El
imuNeural)
ShortName: en-TZ-ElimuNeural
Gender: Male
Locale: en-TZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-TZ, Im
aniNeural)
ShortName: en-TZ-ImaniNeural
Gender: Female
Locale: en-TZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-GB, Li
bbyNeural)
ShortName: en-GB-LibbyNeural
Gender: Female
Locale: en-GB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-GB, Ma
isieNeural)
ShortName: en-GB-MaisieNeural
Gender: Female
Locale: en-GB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-GB, Ry
anNeural)
ShortName: en-GB-RyanNeural
Gender: Male
Locale: en-GB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-GB, So
niaNeural)
ShortName: en-GB-SoniaNeural
Gender: Female
Locale: en-GB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-GB, Th
omasNeural)
ShortName: en-GB-ThomasNeural
Gender: Male
Locale: en-GB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Ar
iaNeural)
ShortName: en-US-AriaNeural
Gender: Female
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Positive', 'Confident']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, An
aNeural)
ShortName: en-US-AnaNeural
Gender: Female
Locale: en-US
VoiceTag: {'ContentCategories': ['Cartoon', 'Conversation'],
'VoicePersonalities': ['Cute']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Ch
ristopherNeural)
ShortName: en-US-ChristopherNeural
Gender: Male
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Reliable', 'Authority']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Er
icNeural)
ShortName: en-US-EricNeural
Gender: Male
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Rational']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Gu
yNeural)
ShortName: en-US-GuyNeural
Gender: Male
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Passion']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Je
nnyNeural)
ShortName: en-US-JennyNeural
Gender: Female
Locale: en-US
VoiceTag: {'ContentCategories': ['Conversation', 'News'], 'Vo
icePersonalities': ['Friendly', 'Considerate', 'Comfort']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Mi
chelleNeural)
ShortName: en-US-MichelleNeural
Gender: Female
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Friendly', 'Pleasant']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, Ro
gerNeural)
ShortName: en-US-RogerNeural
Gender: Male
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Lively']}

# Name: Microsoft Server Speech Text to Speech Voice (en-US, St
effanNeural)
ShortName: en-US-SteffanNeural
Gender: Male
Locale: en-US
VoiceTag: {'ContentCategories': ['News', 'Novel'], 'VoicePers
onalities': ['Rational']}

# Name: Microsoft Server Speech Text to Speech Voice (et-EE, An
uNeural)
ShortName: et-EE-AnuNeural
Gender: Female
Locale: et-EE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (et-EE, Ke
rtNeural)
ShortName: et-EE-KertNeural
Gender: Male
Locale: et-EE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fil-PH, A
ngeloNeural)
ShortName: fil-PH-AngeloNeural
Gender: Male
Locale: fil-PH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fil-PH, B
lessicaNeural)
ShortName: fil-PH-BlessicaNeural
Gender: Female
Locale: fil-PH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fi-FI, Ha
rriNeural)
ShortName: fi-FI-HarriNeural
Gender: Male
Locale: fi-FI
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fi-FI, No
oraNeural)
ShortName: fi-FI-NooraNeural
Gender: Female
Locale: fi-FI
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-BE, Ch
arlineNeural)
ShortName: fr-BE-CharlineNeural
Gender: Female
Locale: fr-BE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-BE, Ge
rardNeural)
ShortName: fr-BE-GerardNeural
Gender: Male
Locale: fr-BE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-CA, An
toineNeural)
ShortName: fr-CA-AntoineNeural
Gender: Male
Locale: fr-CA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-CA, Je
anNeural)
ShortName: fr-CA-JeanNeural
Gender: Male
Locale: fr-CA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-CA, Sy
lvieNeural)
ShortName: fr-CA-SylvieNeural
Gender: Female
Locale: fr-CA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-FR, De
niseNeural)
ShortName: fr-FR-DeniseNeural
Gender: Female
Locale: fr-FR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-FR, El
oiseNeural)
ShortName: fr-FR-EloiseNeural
Gender: Female
Locale: fr-FR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-FR, He
nriNeural)
ShortName: fr-FR-HenriNeural
Gender: Male
Locale: fr-FR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-CH, Ar
ianeNeural)
ShortName: fr-CH-ArianeNeural
Gender: Female
Locale: fr-CH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fr-CH, Fa
briceNeural)
ShortName: fr-CH-FabriceNeural
Gender: Male
Locale: fr-CH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (gl-ES, Ro
iNeural)
ShortName: gl-ES-RoiNeural
Gender: Male
Locale: gl-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (gl-ES, Sa
belaNeural)
ShortName: gl-ES-SabelaNeural
Gender: Female
Locale: gl-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ka-GE, Ek
aNeural)
ShortName: ka-GE-EkaNeural
Gender: Female
Locale: ka-GE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ka-GE, Gi
orgiNeural)
ShortName: ka-GE-GiorgiNeural
Gender: Male
Locale: ka-GE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-AT, In
gridNeural)
ShortName: de-AT-IngridNeural
Gender: Female
Locale: de-AT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-AT, Jo
nasNeural)
ShortName: de-AT-JonasNeural
Gender: Male
Locale: de-AT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-DE, Am
alaNeural)
ShortName: de-DE-AmalaNeural
Gender: Female
Locale: de-DE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-DE, Co
nradNeural)
ShortName: de-DE-ConradNeural
Gender: Male
Locale: de-DE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-DE, Ka
tjaNeural)
ShortName: de-DE-KatjaNeural
Gender: Female
Locale: de-DE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-DE, Ki
llianNeural)
ShortName: de-DE-KillianNeural
Gender: Male
Locale: de-DE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-CH, Ja
nNeural)
ShortName: de-CH-JanNeural
Gender: Male
Locale: de-CH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (de-CH, Le
niNeural)
ShortName: de-CH-LeniNeural
Gender: Female
Locale: de-CH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (el-GR, At
hinaNeural)
ShortName: el-GR-AthinaNeural
Gender: Female
Locale: el-GR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (el-GR, Ne
storasNeural)
ShortName: el-GR-NestorasNeural
Gender: Male
Locale: el-GR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (gu-IN, Dh
waniNeural)
ShortName: gu-IN-DhwaniNeural
Gender: Female
Locale: gu-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (gu-IN, Ni
ranjanNeural)
ShortName: gu-IN-NiranjanNeural
Gender: Male
Locale: gu-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (he-IL, Av
riNeural)
ShortName: he-IL-AvriNeural
Gender: Male
Locale: he-IL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (he-IL, Hi
laNeural)
ShortName: he-IL-HilaNeural
Gender: Female
Locale: he-IL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (hi-IN, Ma
dhurNeural)
ShortName: hi-IN-MadhurNeural
Gender: Male
Locale: hi-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (hi-IN, Sw
araNeural)
ShortName: hi-IN-SwaraNeural
Gender: Female
Locale: hi-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (hu-HU, No
emiNeural)
ShortName: hu-HU-NoemiNeural
Gender: Female
Locale: hu-HU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (hu-HU, Ta
masNeural)
ShortName: hu-HU-TamasNeural
Gender: Male
Locale: hu-HU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (is-IS, Gu
drunNeural)
ShortName: is-IS-GudrunNeural
Gender: Female
Locale: is-IS
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (is-IS, Gu
nnarNeural)
ShortName: is-IS-GunnarNeural
Gender: Male
Locale: is-IS
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (id-ID, Ar
diNeural)
ShortName: id-ID-ArdiNeural
Gender: Male
Locale: id-ID
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (id-ID, Ga
disNeural)
ShortName: id-ID-GadisNeural
Gender: Female
Locale: id-ID
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ga-IE, Co
lmNeural)
ShortName: ga-IE-ColmNeural
Gender: Male
Locale: ga-IE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ga-IE, Or
laNeural)
ShortName: ga-IE-OrlaNeural
Gender: Female
Locale: ga-IE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (it-IT, Di
egoNeural)
ShortName: it-IT-DiegoNeural
Gender: Male
Locale: it-IT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (it-IT, El
saNeural)
ShortName: it-IT-ElsaNeural
Gender: Female
Locale: it-IT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (it-IT, Is
abellaNeural)
ShortName: it-IT-IsabellaNeural
Gender: Female
Locale: it-IT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ja-JP, Ke
itaNeural)
ShortName: ja-JP-KeitaNeural
Gender: Male
Locale: ja-JP
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ja-JP, Na
namiNeural)
ShortName: ja-JP-NanamiNeural
Gender: Female
Locale: ja-JP
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (jv-ID, Di
masNeural)
ShortName: jv-ID-DimasNeural
Gender: Male
Locale: jv-ID
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (jv-ID, Si
tiNeural)
ShortName: jv-ID-SitiNeural
Gender: Female
Locale: jv-ID
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (kn-IN, Ga
ganNeural)
ShortName: kn-IN-GaganNeural
Gender: Male
Locale: kn-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (kn-IN, Sa
pnaNeural)
ShortName: kn-IN-SapnaNeural
Gender: Female
Locale: kn-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (kk-KZ, Ai
gulNeural)
ShortName: kk-KZ-AigulNeural
Gender: Female
Locale: kk-KZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (kk-KZ, Da
uletNeural)
ShortName: kk-KZ-DauletNeural
Gender: Male
Locale: kk-KZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (km-KH, Pi
sethNeural)
ShortName: km-KH-PisethNeural
Gender: Male
Locale: km-KH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (km-KH, Sr
eymomNeural)
ShortName: km-KH-SreymomNeural
Gender: Female
Locale: km-KH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ko-KR, In
JoonNeural)
ShortName: ko-KR-InJoonNeural
Gender: Male
Locale: ko-KR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ko-KR, Su
nHiNeural)
ShortName: ko-KR-SunHiNeural
Gender: Female
Locale: ko-KR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (lo-LA, Ch
anthavongNeural)
ShortName: lo-LA-ChanthavongNeural
Gender: Male
Locale: lo-LA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (lo-LA, Ke
omanyNeural)
ShortName: lo-LA-KeomanyNeural
Gender: Female
Locale: lo-LA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (lv-LV, Ev
eritaNeural)
ShortName: lv-LV-EveritaNeural
Gender: Female
Locale: lv-LV
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (lv-LV, Ni
lsNeural)
ShortName: lv-LV-NilsNeural
Gender: Male
Locale: lv-LV
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (lt-LT, Le
onasNeural)
ShortName: lt-LT-LeonasNeural
Gender: Male
Locale: lt-LT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (lt-LT, On
aNeural)
ShortName: lt-LT-OnaNeural
Gender: Female
Locale: lt-LT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mk-MK, Al
eksandarNeural)
ShortName: mk-MK-AleksandarNeural
Gender: Male
Locale: mk-MK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mk-MK, Ma
rijaNeural)
ShortName: mk-MK-MarijaNeural
Gender: Female
Locale: mk-MK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ms-MY, Os
manNeural)
ShortName: ms-MY-OsmanNeural
Gender: Male
Locale: ms-MY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ms-MY, Ya
sminNeural)
ShortName: ms-MY-YasminNeural
Gender: Female
Locale: ms-MY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ml-IN, Mi
dhunNeural)
ShortName: ml-IN-MidhunNeural
Gender: Male
Locale: ml-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ml-IN, So
bhanaNeural)
ShortName: ml-IN-SobhanaNeural
Gender: Female
Locale: ml-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mt-MT, Gr
aceNeural)
ShortName: mt-MT-GraceNeural
Gender: Female
Locale: mt-MT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mt-MT, Jo
sephNeural)
ShortName: mt-MT-JosephNeural
Gender: Male
Locale: mt-MT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mr-IN, Aa
rohiNeural)
ShortName: mr-IN-AarohiNeural
Gender: Female
Locale: mr-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mr-IN, Ma
noharNeural)
ShortName: mr-IN-ManoharNeural
Gender: Male
Locale: mr-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mn-MN, Ba
taaNeural)
ShortName: mn-MN-BataaNeural
Gender: Male
Locale: mn-MN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (mn-MN, Ye
suiNeural)
ShortName: mn-MN-YesuiNeural
Gender: Female
Locale: mn-MN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ne-NP, He
mkalaNeural)
ShortName: ne-NP-HemkalaNeural
Gender: Female
Locale: ne-NP
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ne-NP, Sa
garNeural)
ShortName: ne-NP-SagarNeural
Gender: Male
Locale: ne-NP
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nb-NO, Fi
nnNeural)
ShortName: nb-NO-FinnNeural
Gender: Male
Locale: nb-NO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (nb-NO, Pe
rnilleNeural)
ShortName: nb-NO-PernilleNeural
Gender: Female
Locale: nb-NO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ps-AF, Gu
lNawazNeural)
ShortName: ps-AF-GulNawazNeural
Gender: Male
Locale: ps-AF
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ps-AF, La
tifaNeural)
ShortName: ps-AF-LatifaNeural
Gender: Female
Locale: ps-AF
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fa-IR, Di
laraNeural)
ShortName: fa-IR-DilaraNeural
Gender: Female
Locale: fa-IR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (fa-IR, Fa
ridNeural)
ShortName: fa-IR-FaridNeural
Gender: Male
Locale: fa-IR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (pl-PL, Ma
rekNeural)
ShortName: pl-PL-MarekNeural
Gender: Male
Locale: pl-PL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (pl-PL, Zo
fiaNeural)
ShortName: pl-PL-ZofiaNeural
Gender: Female
Locale: pl-PL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (pt-BR, An
tonioNeural)
ShortName: pt-BR-AntonioNeural
Gender: Male
Locale: pt-BR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (pt-BR, Fr
anciscaNeural)
ShortName: pt-BR-FranciscaNeural
Gender: Female
Locale: pt-BR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (pt-PT, Du
arteNeural)
ShortName: pt-PT-DuarteNeural
Gender: Male
Locale: pt-PT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (pt-PT, Ra
quelNeural)
ShortName: pt-PT-RaquelNeural
Gender: Female
Locale: pt-PT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ro-RO, Al
inaNeural)
ShortName: ro-RO-AlinaNeural
Gender: Female
Locale: ro-RO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ro-RO, Em
ilNeural)
ShortName: ro-RO-EmilNeural
Gender: Male
Locale: ro-RO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ru-RU, Dm
itryNeural)
ShortName: ru-RU-DmitryNeural
Gender: Male
Locale: ru-RU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ru-RU, Sv
etlanaNeural)
ShortName: ru-RU-SvetlanaNeural
Gender: Female
Locale: ru-RU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sr-RS, Ni
cholasNeural)
ShortName: sr-RS-NicholasNeural
Gender: Male
Locale: sr-RS
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sr-RS, So
phieNeural)
ShortName: sr-RS-SophieNeural
Gender: Female
Locale: sr-RS
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (si-LK, Sa
meeraNeural)
ShortName: si-LK-SameeraNeural
Gender: Male
Locale: si-LK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (si-LK, Th
iliniNeural)
ShortName: si-LK-ThiliniNeural
Gender: Female
Locale: si-LK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sk-SK, Lu
kasNeural)
ShortName: sk-SK-LukasNeural
Gender: Male
Locale: sk-SK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sk-SK, Vi
ktoriaNeural)
ShortName: sk-SK-ViktoriaNeural
Gender: Female
Locale: sk-SK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sl-SI, Pe
traNeural)
ShortName: sl-SI-PetraNeural
Gender: Female
Locale: sl-SI
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sl-SI, Ro
kNeural)
ShortName: sl-SI-RokNeural
Gender: Male
Locale: sl-SI
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (so-SO, Mu
useNeural)
ShortName: so-SO-MuuseNeural
Gender: Male
Locale: so-SO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (so-SO, Ub
axNeural)
ShortName: so-SO-UbaxNeural
Gender: Female
Locale: so-SO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-AR, El
enaNeural)
ShortName: es-AR-ElenaNeural
Gender: Female
Locale: es-AR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-AR, To
masNeural)
ShortName: es-AR-TomasNeural
Gender: Male
Locale: es-AR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-BO, Ma
rceloNeural)
ShortName: es-BO-MarceloNeural
Gender: Male
Locale: es-BO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-BO, So
fiaNeural)
ShortName: es-BO-SofiaNeural
Gender: Female
Locale: es-BO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CL, Ca
talinaNeural)
ShortName: es-CL-CatalinaNeural
Gender: Female
Locale: es-CL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CL, Lo
renzoNeural)
ShortName: es-CL-LorenzoNeural
Gender: Male
Locale: es-CL
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CO, Go
nzaloNeural)
ShortName: es-CO-GonzaloNeural
Gender: Male
Locale: es-CO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CO, Sa
lomeNeural)
ShortName: es-CO-SalomeNeural
Gender: Female
Locale: es-CO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CR, Ju
anNeural)
ShortName: es-CR-JuanNeural
Gender: Male
Locale: es-CR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CR, Ma
riaNeural)
ShortName: es-CR-MariaNeural
Gender: Female
Locale: es-CR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CU, Be
lkysNeural)
ShortName: es-CU-BelkysNeural
Gender: Female
Locale: es-CU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-CU, Ma
nuelNeural)
ShortName: es-CU-ManuelNeural
Gender: Male
Locale: es-CU
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-DO, Em
ilioNeural)
ShortName: es-DO-EmilioNeural
Gender: Male
Locale: es-DO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-DO, Ra
monaNeural)
ShortName: es-DO-RamonaNeural
Gender: Female
Locale: es-DO
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-EC, An
dreaNeural)
ShortName: es-EC-AndreaNeural
Gender: Female
Locale: es-EC
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-EC, Lu
isNeural)
ShortName: es-EC-LuisNeural
Gender: Male
Locale: es-EC
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-SV, Lo
renaNeural)
ShortName: es-SV-LorenaNeural
Gender: Female
Locale: es-SV
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-SV, Ro
drigoNeural)
ShortName: es-SV-RodrigoNeural
Gender: Male
Locale: es-SV
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-GQ, Ja
vierNeural)
ShortName: es-GQ-JavierNeural
Gender: Male
Locale: es-GQ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-GQ, Te
resaNeural)
ShortName: es-GQ-TeresaNeural
Gender: Female
Locale: es-GQ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-GT, An
dresNeural)
ShortName: es-GT-AndresNeural
Gender: Male
Locale: es-GT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-GT, Ma
rtaNeural)
ShortName: es-GT-MartaNeural
Gender: Female
Locale: es-GT
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-HN, Ca
rlosNeural)
ShortName: es-HN-CarlosNeural
Gender: Male
Locale: es-HN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-HN, Ka
rlaNeural)
ShortName: es-HN-KarlaNeural
Gender: Female
Locale: es-HN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-MX, Da
liaNeural)
ShortName: es-MX-DaliaNeural
Gender: Female
Locale: es-MX
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-MX, Jo
rgeNeural)
ShortName: es-MX-JorgeNeural
Gender: Male
Locale: es-MX
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-MX, Lo
renzoEsCLNeural)
ShortName: es-MX-LorenzoEsCLNeural
Gender: Male
Locale: es-MX
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-NI, Fe
dericoNeural)
ShortName: es-NI-FedericoNeural
Gender: Male
Locale: es-NI
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-NI, Yo
landaNeural)
ShortName: es-NI-YolandaNeural
Gender: Female
Locale: es-NI
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PA, Ma
rgaritaNeural)
ShortName: es-PA-MargaritaNeural
Gender: Female
Locale: es-PA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PA, Ro
bertoNeural)
ShortName: es-PA-RobertoNeural
Gender: Male
Locale: es-PA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PY, Ma
rioNeural)
ShortName: es-PY-MarioNeural
Gender: Male
Locale: es-PY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PY, Ta
niaNeural)
ShortName: es-PY-TaniaNeural
Gender: Female
Locale: es-PY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PE, Al
exNeural)
ShortName: es-PE-AlexNeural
Gender: Male
Locale: es-PE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PE, Ca
milaNeural)
ShortName: es-PE-CamilaNeural
Gender: Female
Locale: es-PE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PR, Ka
rinaNeural)
ShortName: es-PR-KarinaNeural
Gender: Female
Locale: es-PR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-PR, Vi
ctorNeural)
ShortName: es-PR-VictorNeural
Gender: Male
Locale: es-PR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-ES, Al
varoNeural)
ShortName: es-ES-AlvaroNeural
Gender: Male
Locale: es-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-ES, El
viraNeural)
ShortName: es-ES-ElviraNeural
Gender: Female
Locale: es-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-ES, Ma
nuelEsCUNeural)
ShortName: es-ES-ManuelEsCUNeural
Gender: Male
Locale: es-ES
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-US, Al
onsoNeural)
ShortName: es-US-AlonsoNeural
Gender: Male
Locale: es-US
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-US, Pa
lomaNeural)
ShortName: es-US-PalomaNeural
Gender: Female
Locale: es-US
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-UY, Ma
teoNeural)
ShortName: es-UY-MateoNeural
Gender: Male
Locale: es-UY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-UY, Va
lentinaNeural)
ShortName: es-UY-ValentinaNeural
Gender: Female
Locale: es-UY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-VE, Pa
olaNeural)
ShortName: es-VE-PaolaNeural
Gender: Female
Locale: es-VE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (es-VE, Se
bastianNeural)
ShortName: es-VE-SebastianNeural
Gender: Male
Locale: es-VE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (su-ID, Ja
jangNeural)
ShortName: su-ID-JajangNeural
Gender: Male
Locale: su-ID
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (su-ID, Tu
tiNeural)
ShortName: su-ID-TutiNeural
Gender: Female
Locale: su-ID
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sw-KE, Ra
fikiNeural)
ShortName: sw-KE-RafikiNeural
Gender: Male
Locale: sw-KE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sw-KE, Zu
riNeural)
ShortName: sw-KE-ZuriNeural
Gender: Female
Locale: sw-KE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sw-TZ, Da
udiNeural)
ShortName: sw-TZ-DaudiNeural
Gender: Male
Locale: sw-TZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sw-TZ, Re
hemaNeural)
ShortName: sw-TZ-RehemaNeural
Gender: Female
Locale: sw-TZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sv-SE, Ma
ttiasNeural)
ShortName: sv-SE-MattiasNeural
Gender: Male
Locale: sv-SE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (sv-SE, So
fieNeural)
ShortName: sv-SE-SofieNeural
Gender: Female
Locale: sv-SE
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-IN, Pa
llaviNeural)
ShortName: ta-IN-PallaviNeural
Gender: Female
Locale: ta-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-IN, Va
lluvarNeural)
ShortName: ta-IN-ValluvarNeural
Gender: Male
Locale: ta-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-MY, Ka
niNeural)
ShortName: ta-MY-KaniNeural
Gender: Female
Locale: ta-MY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-MY, Su
ryaNeural)
ShortName: ta-MY-SuryaNeural
Gender: Male
Locale: ta-MY
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-SG, An
buNeural)
ShortName: ta-SG-AnbuNeural
Gender: Male
Locale: ta-SG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-SG, Ve
nbaNeural)
ShortName: ta-SG-VenbaNeural
Gender: Female
Locale: ta-SG
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-LK, Ku
marNeural)
ShortName: ta-LK-KumarNeural
Gender: Male
Locale: ta-LK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ta-LK, Sa
ranyaNeural)
ShortName: ta-LK-SaranyaNeural
Gender: Female
Locale: ta-LK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (te-IN, Mo
hanNeural)
ShortName: te-IN-MohanNeural
Gender: Male
Locale: te-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (te-IN, Sh
rutiNeural)
ShortName: te-IN-ShrutiNeural
Gender: Female
Locale: te-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (th-TH, Ni
watNeural)
ShortName: th-TH-NiwatNeural
Gender: Male
Locale: th-TH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (th-TH, Pr
emwadeeNeural)
ShortName: th-TH-PremwadeeNeural
Gender: Female
Locale: th-TH
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (tr-TR, Ah
metNeural)
ShortName: tr-TR-AhmetNeural
Gender: Male
Locale: tr-TR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (tr-TR, Em
elNeural)
ShortName: tr-TR-EmelNeural
Gender: Female
Locale: tr-TR
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (uk-UA, Os
tapNeural)
ShortName: uk-UA-OstapNeural
Gender: Male
Locale: uk-UA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (uk-UA, Po
linaNeural)
ShortName: uk-UA-PolinaNeural
Gender: Female
Locale: uk-UA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ur-IN, Gu
lNeural)
ShortName: ur-IN-GulNeural
Gender: Female
Locale: ur-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ur-IN, Sa
lmanNeural)
ShortName: ur-IN-SalmanNeural
Gender: Male
Locale: ur-IN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ur-PK, As
adNeural)
ShortName: ur-PK-AsadNeural
Gender: Male
Locale: ur-PK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (ur-PK, Uz
maNeural)
ShortName: ur-PK-UzmaNeural
Gender: Female
Locale: ur-PK
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (uz-UZ, Ma
dinaNeural)
ShortName: uz-UZ-MadinaNeural
Gender: Female
Locale: uz-UZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (uz-UZ, Sa
rdorNeural)
ShortName: uz-UZ-SardorNeural
Gender: Male
Locale: uz-UZ
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (vi-VN, Ho
aiMyNeural)
ShortName: vi-VN-HoaiMyNeural
Gender: Female
Locale: vi-VN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (vi-VN, Na
mMinhNeural)
ShortName: vi-VN-NamMinhNeural
Gender: Male
Locale: vi-VN
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalit
ies': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (cy-GB, Al
edNeural)
ShortName: cy-GB-AleVoiceTag: {'ContentCategories': ['General'], 'VoicePersonalities': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (cy-GB, NiaNeural)
ShortName: cy-GB-NiaNeural
Gender: Female
Locale: cy-GB
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalities': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zu-ZA, ThandoNeural)
ShortName: zu-ZA-ThandoNeural
Gender: Female
Locale: zu-ZA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalities': ['Friendly', 'Positive']}

# Name: Microsoft Server Speech Text to Speech Voice (zu-ZA, ThembaNeural)
ShortName: zu-ZA-ThembaNeural
Gender: Male
Locale: zu-ZA
VoiceTag: {'ContentCategories': ['General'], 'VoicePersonalities': ['Friendly', 'Positive']}
'''
