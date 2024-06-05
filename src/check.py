import csv
import json

csv_text = """
名古屋ReNY,Zephyrホール,RAD HALL,TOYS,HOLIDAY NEXT,X-HALL,Dt3F,静かの海,Zion,バーサスホール,ライオンシアター,ライオンカフェ,ライオンリミテッド,シアターZONE,STUDIO 51,DIVA,DEEP,DAYTRIVE
9:50-10:10,10:05-10:30,10:00-10:20,10:05-10:25,10:00-10:20,10:05-10:25,10:00-10:20,14:25-14:45,10:00-10:20,10:05-10:25,10:00-10:20,10:05-10:25,10:00-10:20,10:05-10:25,10:00-10:20,10:05-10:25,10:00-10:20,10:05-10:25
アストリーのうさぎ,凌晨12点,mistress,ヒダリ←イミテイト,RED-i,MiX BeRRY,かるちべいと,MAD JAMIE,you-show,Shupines,neOen,Cassie Te Light,代々木女子音楽院,ブルーなままで,虹色幻想曲 〜プリズム・ファンタジア〜,milu milu!,夢幻スタートレール,MILLE FLEURS
10:10-10:35,10:35-11:00,10:25-10:45,10:30-10:50,10:25-10:45,10:30-10:50,10:20-10:40,14:45-15:05,10:25-10:45,10:25-10:45,10:25-10:45,10:30-10:50,10:20-10:40,10:25-10:45,10:25-10:45,10:30-10:50,10:20-10:40,10:25-10:45
AQA,EMPATHY,アンチテーゼ,NiTRO,ByteSchwarz,make mie,U≠may,禅XENOVA刄,FiDZ,Symdolick,純粋カフェラッテ,YUM!-TUK!,疾風RUN舞,Zero Project,STRAY SHEEP CLAYMORE,WT☆Egret,HIGH HIGH BEAM,acro-A
10:40-11:05,11:05-11:30,10:50-11:10,10:55-11:15,10:50-11:10,10:55-11:15,10:40-11:00,15:05-15:25,10:50-11:10,10:45-11:05,10:50-11:10,10:55-11:15,10:40-11:00,10:45-11:05,10:50-11:10,10:55-11:15,10:40-11:00,10:45-11:05
昼夜逆転,TENRIN,XTEEN,あくしあ,TOROi,ふぇありーているず！,꒰ঌ if ໒꒱,PinkySpice,ALPHACROW,OS☆K,Aのね？Soのね！,えすれある,LEVEL7,PrincessGarden-NAGOYA-,メリーミューズ,KRD8,みらくらんど,DA･BAMBI
11:10-11:35,11:35-12:00,11:15-11:35,11:20-11:40,11:15-11:35,11:20-11:40,11:05-11:25,15:30-15:50,11:15-11:35,11:10-11:30,11:15-11:35,11:20-11:40,11:05-11:25,11:10-11:30,11:15-11:35,11:20-11:40,11:05-11:25,11:10-11:30
アルカナビス,AIBECK,惑星VORTEX,Karman,ADOMIO,にっぽん！真骨頂,CHAAKLiLY,Karman,AiVER.,甘病神℃ロヲム,おむすび娘。,notall,アポストロフィ,WeZ,君とのシナリオ,Gentirover,.BPM,MANACLE
11:40-12:05,12:05-12:30,11:40-12:00,11:45-12:05,11:40-12:00,11:45-12:05,11:25-11:45,15:50-16:10,11:40-12:00,11:30-11:50,11:40-12:00,11:45-12:05,11:25-11:45,11:30-11:50,11:40-12:00,11:45-12:05,11:25-11:45,11:30-11:50
まねきケチャ,神薙ラビッツ,BLACKNAZARENE,AIMIA,POPPiNG EMO,アポロンの翼,Licht,POPPiNG EMO,都の国のアリス,rayray,SEEK PLEASURE-シープレ-,ダブルヴィー,PinkPanda,スーパーマカロニサラダ,プリティチョモランマ組合,XOXO EXTREME,オカシリゾート,OMNI666
12:10-12:35,12:35-13:00,12:05-12:25,12:10-12:30,12:05-12:25,12:10-12:30,11:45-12:05,16:10-16:30,12:05-12:25,11:50-12:10,12:05-12:25,12:10-12:30,11:45-12:05,11:50-12:10,12:05-12:25,12:10-12:30,11:45-12:05,11:50-12:10
ai*ai,椎名ひかり,ガガピエロ,青空の下で手をつなぐ,CHEMICAL X,ESTLINK☆,MEWCATUNE,ZIGA,MAGMAZ,ミリオン！ Million Heaven Tokyo,強くてニューゲーム。,Seven Day'z,アステリア,サークルクラッシャー,アイドル教室NEW,ミラクルファンファーレ！,LOVE IZ DOLL,ONE SHOT ONE KILL
12:40-13:05,13:05-13:30,12:30-12:50,12:35-12:55,12:30-12:50,12:35-12:55,12:10-12:30,16:35-16:55,12:30-12:50,12:15-12:35,12:30-12:50,12:35-12:55,12:10-12:30,12:15-12:35,12:30-12:50,12:35-12:55,12:10-12:30,12:15-12:35
アルテミスの翼,ニーキューオメガ,CALETWOLF,残響ヴァルキリー,Sekaisen,DINKY JUNK,究極人形,ENVY PARANOID,sui sui,Lollipop♡CHU,RESNECT,あおぞらをキミに,Goodbye for First kiss,すたんぴっ！,いざ参らん,theWORLD,24emotions,Re:INCARNATION
13:10-13:35,13:35-14:00,12:55-13:15,13:00-13:20,12:55-13:15,13:00-13:20,12:30-12:50,16:55-17:15,12:55-13:15,12:35-12:55,12:55-13:15,13:00-13:20,12:30-12:50,12:35-12:55,12:55-13:15,13:00-13:20,12:30-12:50,12:35-12:55
Brave Mental Orchestra,LEIWAN,NEO BREAK,BR!OT,NANONI,ぽッぴン☆じゃんピン.com,ピコ☆レボ,AKIARIM,混沌少女,Blancanie,Otto,MAHΩRAMA(まほらま),dela,青色のSKY,モードラ,すてねこキャッツ,Fragrant Drive,戦国アニマル極楽浄土
13:40-14:05,14:05-14:30,13:20-13:40,13:25-13:45,13:20-13:40,13:25-13:45,12:50-13:10,17:15-17:35,13:20-13:40,12:55-13:15,13:20-13:40,13:25-13:45,12:50-13:10,12:55-13:15,13:20-13:40,13:25-13:45,12:50-13:10,12:55-13:15
プエラの絶対値,AdamLiLith,THE＋BETH,キミイロプロジェクト,棘,脳内パステル,ゼロキョリハーツ,ByteSchwarz,lonlium,かるちべいと,PrincessGarden-姫庭-,ヒビコレ,グランダルメ,キミノトナリ,idrip,Epheaile,Bety,MELTЯAGE
14:10-14:35,14:35-15:00,13:45-14:05,13:50-14:10,13:45-14:05,13:50-14:10,13:15-13:35,17:40-18:00,13:45-14:05,13:20-13:40,13:45-14:05,13:50-14:10,13:15-13:35,13:20-13:40,13:45-14:05,13:50-14:10,13:15-13:35,13:20-13:40
Star☆T,プランクスターズ,ミソラドエジソン,RESELA,WONDER SNAKE,神薙-時うさぎ-,木苺FRUCTOSE,acro-A,NiTRO,拍宙夢,MATANAGOYA,トキメロ,ふるふるしっぽ,虹色幻想曲 〜プリズム・ファンタジア〜,No.*Day,新章 大阪☆春夏秋冬,MiX BeRRY,Innocent Lucia
14:40-15:05,15:05-15:30,14:10-14:30,14:15-14:35,14:10-14:30,14:15-14:35,13:35-13:55,18:00-18:20,14:10-14:30,13:40-14:00,14:10-14:30,14:15-14:35,13:35-13:55,13:40-14:00,14:10-14:30,14:15-14:35,13:35-13:55,13:40-14:00
My Dresscode,アンチテーゼ,AZ-ON,乙女座長☆銀河団,高貴な絶対零度,MAD MEDiCINE,NEW POLARIS,AIMIA,MOZU,neOen,きっとずっと青春。,YUM!-TUK!,君とセレンディピティ,覚醒♡ラブビート,IZANAGI,LEVEL7,蛍,Tri-Sphere
15:10-15:35,15:35-16:00,14:35-14:55,14:40-15:00,14:35-14:55,14:40-15:00,13:55-14:15,18:20-18:40,14:35-14:55,14:00-14:20,14:35-14:55,14:40-15:00,13:55-14:15,14:00-14:20,14:35-14:55,14:40-15:00,13:55-14:15,14:00-14:20
きっと大切だった,夢幻のシナリオ,DA･BAMBI,TOROi,どーぴんぐ疑惑,凌晨12点,Cosmoslay,都の国のアリス,Re:LiZE,ヒダリ←イミテイト,milu milu!,夢現シンクレティズム,ぷりしえーる,代々木女子音楽院,みらくる★ふぉーぜ,純粋カフェラッテ,思い出とプレゼント,MAIDEN√DOLL
15:40-16:05,16:05-16:30,15:00-15:20,15:05-15:25,15:00-15:20,15:05-15:25,14:20-14:40,18:45-19:05,15:00-15:20,14:25-14:45,15:00-15:20,15:05-15:25,14:20-14:40,14:25-14:45,15:00-15:20,15:05-15:25,14:20-14:40,14:25-14:45
ふぇありーているず！,究極人形,Caress Van End,SHIROMIZAKANA,NiL,ナト☆カン,YA'ABURNEE,MANACLE,Treble,YURAMEKI Neon Walker,BABY BUBBLE,THE ENCORE,Aim,ぶっとび！パンデミック,SAI-HATE,ぜろから☆すた→と,LUNETTA,カリギュラ
16:10-16:35,16:35-17:00,15:25-15:45,15:30-15:50,15:25-15:45,15:30-15:50,14:40-15:00,19:05-19:25,15:25-15:45,14:45-15:05,15:25-15:45,15:30-15:50,14:40-15:00,14:45-15:05,15:25-15:45,15:30-15:50,14:40-15:00,14:45-15:05
にっぽん！真骨頂,惑星VORTEX,TENRIN,Gentirover,MILLE FLEURS,にっぽんワチャチャ,WANNA,YA'ABURNEE,maleficium,君とのシナリオ,U≠may,#かわいいだけでバズりたい,キミと永遠に,꒰ঌ if ໒꒱,Cassie Te Light,アポストロフィ,レトロレイン,Paradox Risk
16:40-17:05,17:05-17:30,15:50-16:10,15:55-16:15,15:50-16:10,15:55-16:15,15:00-15:20,19:25-19:45,15:50-16:10,15:05-15:25,15:50-16:10,15:55-16:15,15:00-15:20,15:05-15:25,15:50-16:10,15:55-16:15,15:00-15:20,15:05-15:25
LOVE9LOVE,MAGMAZ,ジエメイ,GLIM of GRAND,OMG,エウレカ,恋音クロシェット,MAIDEN√DOLL,CYCLONISTA,ヲドルマヨナカ,ブルーなままで,ミリオン！ Million Heaven Tokyo,WT☆Egret,Ikenai Rouge Magic,超常フォーチュン,ai*ai,BANZAI JAPAN,ZEPANEWT
17:10-17:35,17:35-18:00,16:15-16:35,16:20-16:40,16:15-16:35,16:20-16:40,15:25-15:45,19:50-20:10,16:15-16:35,15:30-15:50,16:15-16:35,16:20-16:40,15:25-15:45,15:30-15:50,16:15-16:35,16:20-16:40,15:25-15:45,15:30-15:50
ANA®KIE,ミソラドエジソン,LØISLOID,NANONI,Absopetus-アブソプ- ,おちゃメンタル☆パーティー,アポロンの翼,Re:LiZE,CHEMICAL X,.Link,Stella!,Goodbye for First kiss,KRD8,Licht,帝都薫風,make mie,BABY-CRAYON〜1361〜,CHERRY GIRLS PROJECT
17:40-18:05,18:05-18:30,16:40-17:00,16:45-17:05,16:40-17:00,16:45-17:05,15:45-16:05,20:10-20:30,16:40-17:00,15:50-16:10,16:40-17:00,16:45-17:05,15:45-16:05,15:50-16:10,16:40-17:00,16:45-17:05,15:45-16:05,15:50-16:10
BLACKNAZARENE,ガガピエロ,.BPM,ピコ☆レボ,MELTЯAGE,ミラクルファンファーレ！,青空の下で手をつなぐ,Absopetus-アブソプ- ,9DayzGlitchClubTokyo,Aqueur,ルチアーズ,神薙ラビッツ,miao,AiVER.,アルカナビス,Bety,疾風RUN舞,FiDZ
18:10-18:35,18:35-19:00,17:05-17:25,17:10-17:30,17:05-17:25,17:10-17:30,16:05-16:25,20:30-20:50,17:05-17:25,16:10-16:30,17:05-17:25,17:10-17:30,16:05-16:25,16:10-16:30,17:05-17:25,17:10-17:30,16:05-16:25,16:10-16:30
NEO BREAK,ALPHACROW,椎名ひかり,Seven Day'z,sui sui,すてねこキャッツ,Agrand×Aglow,GLIM of GRAND,OMNI666 ,あくしあ,theWORLD,グランダルメ,STARRY×NIGHT↗,STRAY SHEEP CLAYMORE,WeZ,AQA,caprice,NO❤AF
18:40-19:05,19:05-19:30,17:30-17:50,17:35-17:55,17:30-17:50,17:35-17:55,16:30-16:50,20:50-21:10,17:30-17:50,16:35-16:55,17:30-17:50,17:35-17:55,16:30-16:50,16:35-16:55,17:30-17:50,17:35-17:55,16:30-16:50,16:35-16:55
夢現シンクレティズム,lonlium,husky,Epheaile,Cosmoslay,まねきケチャ,みらくらんど,Treble,THE＋BETH,RESNECT,CHAAKLiLY,ぽッぴン☆じゃんピン.com,24emotions,アイドル教室NEW,スーパーマカロニサラダ,Sekaisen,道玄坂69,残響ヴァルキリー
19:10-19:35,19:35-20:00,17:55-18:15,18:00-18:20,17:55-18:15,18:00-18:20,16:50-17:10,,17:55-18:15,16:55-17:15,17:55-18:15,18:00-18:20,16:50-17:10,16:55-17:15,17:55-18:15,18:00-18:20,16:50-17:10,16:55-17:15
dela,MAD MEDiCINE,戦国アニマル極楽浄土,Lollipop♡CHU,Otto,OS☆K,Zero project,,Innocent Lucia ,MAHΩRAMA(まほらま),甘病神℃ロヲム,LUNETTA,昼夜逆転,Fragrant Drive,サークルクラッシャー,PinkPanda,あたっちゅ！,AKUMATICA
19:40-20:05,20:05-20:30,18:20-18:40,18:25-18:45,18:20-18:40,18:25-18:45,17:10-17:30,,18:20-18:40,17:15-17:35,18:20-18:40,18:25-18:45,17:10-17:30,17:15-17:35,18:20-18:40,18:25-18:45,17:10-17:30,17:15-17:35
ぜろから☆すた→と,ジエメイ,Re:INCARNATION,木苺FRUCTOSE,混沌少女,アルテミスの翼,Blancanie,,Tri-Sphere,プリンセス物語,MEWCATUNE,ふるふるしっぽ,プリティチョモランマ組合,HIGH HIGH BEAM,覚醒♡ラブビート,ESTLINK☆,すたんぴっ！,CALETWOLF
20:10-20:35,20:35-21:00,18:45-19:05,18:50-19:10,18:45-19:05,18:50-19:10,17:35-17:55,,18:45-19:05,17:40-18:00,18:45-19:05,18:50-19:10,17:35-17:55,17:40-18:00,18:45-19:05,18:50-19:10,17:35-17:55,17:40-18:00
THE ENCORE,MAZE,ADOMIO,恋音クロシェット,メタモル!!!,ダブルヴィー,ONE SHOT ONE KILL,,MOZU,Aのね？Soのね！,神薙-時うさぎ-,脳内パステル,XOXO EXTREME,思い出とプレゼント,Ikenai Rouge Magic,Brave Mental Orchestra,PrincessGarden-NAGOYA-,XTEEN
,21:05-21:30,19:10-19:30,19:15-19:35,19:10-19:30,19:15-19:35,17:55-18:15,,19:10-19:30,18:00-18:20,19:10-19:30,19:15-19:35,17:55-18:15,18:00-18:20,19:10-19:30,19:15-19:35,17:55-18:15,18:00-18:20
,mistress,Paradox Risk,いざ参らん,ZEPANEWT,ニーキューオメガ,キミイロプロジェクト,,禅XENOVA刄,おむすび娘。,YURAMEKI Neon Walker,青色のSKY,アイアール,オカシリゾート,キミノトナリ,DINKY JUNK,EMPATHY,BR!OT
,,19:35-19:55,19:40-20:00,19:35-19:55,19:40-20:00,18:15-18:35,,19:35-19:55,18:20-18:40,19:35-19:55,19:40-20:00,18:15-18:35,18:20-18:40,19:35-19:55,19:40-20:00,18:15-18:35,18:20-18:40
,,AdamLiLith,モードラ,夢幻のシナリオ,新章 大阪☆春夏秋冬,あおぞらをキミに,,AZ-ON,SEEK PLEASURE-シープレ-,idrip,ヲドルマヨナカ,My Dresscode,miao,トキメロ,高貴な絶対零度,君とセレンディピティ,MAD JAMIE
,,20:00-20:20,20:05-20:25,20:00-20:20,20:05-20:25,18:40-19:00,,20:00-20:20,18:45-19:05,20:00-20:20,20:05-20:25,18:40-19:00,18:45-19:05,20:00-20:20,20:05-20:25,18:40-19:00,18:45-19:05
,,NO❤AF,帝都薫風,AKUMATICA,アステリア,カリギュラ,,RESELA,MATANAGOYA,WANNA,SHIROMIZAKANA,プエラの絶対値,No.*Day,ヒビコレ,AIBECK,ぷりしえーる,棘
,,20:25-20:45,20:30-20:50,20:25-20:45,20:30-20:50,19:00-19:20,,20:25-20:45,19:05-19:25,20:25-20:45,20:30-20:50,19:00-19:20,19:05-19:25,20:25-20:45,20:30-20:50,19:00-19:20,19:05-19:25
,,CYCLONISTA,ナト☆カン,maleficium,Star☆T,rayray,,ZIGA,WONDER SNAKE,BABY-CRAYON〜1361〜,きっと大切だった,強くてニューゲーム。,レトロレイン,ゼロキョリハーツ,おちゃメンタル☆パーティー,キミと永遠に,乙女座長☆銀河団
,,20:50-21:10,20:55-21:15,20:50-21:10,20:55-21:15,19:20-19:40,,20:50-21:10,19:25-19:45,20:50-21:10,20:55-21:15,19:20-19:40,19:25-19:45,20:50-21:10,20:55-21:15,19:20-19:40,19:25-19:45
,,どーぴんぐ疑惑,道玄坂69,LØISLOID,みらくる★ふぉーぜ,.Link,,ENVY PARANOID,BANZAI JAPAN,Aim,にっぽんワチャチャ,プランクスターズ,LOVE IZ DOLL,ぶっとび！パンデミック,LEIWAN,PrincessGarden-姫庭-,Caress Van End
,,,,,,19:45-20:05,,,19:50-20:10,,,19:45-20:05,19:50-20:10,,,19:45-20:05,19:50-20:10
,,,,,,SAI-HATE,,,#かわいいだけでバズりたい,,,プリンセス物語,蛍,,,きっとずっと青春。,PinkySpice
,,,,,,20:05-20:25,,,20:10-20:30,,,20:05-20:25,20:10-20:30,,,20:05-20:25,20:10-20:30
,,,,,,caprice,,,Agrand×Aglow,,,LAVi DOLL,メリーミューズ,,,LOVE9LOVE,OMG
,,,,,,20:25-20:45,,,20:30-20:50,,,20:25-20:45,20:30-20:50,,,20:25-20:45,20:30-20:50
,,,,,,拍宙夢,,,超常フォーチュン,,,IZANAGI,GMG-P,,,CHERRY GIRLS PROJECT,NiL
,,,,,,20:45-21:05,,,20:50-21:10,,,20:45-21:05,STARRY×NIGHT↗,,,20:45-21:05,20:50-21:10
,,,,,,あたっちゅ！,,,Stella!,,,AKIARIM,,,,Aqueur,9DayzGlitchClubTokyo
,,,,,,21:05-21:25,,,,,,,,,,,
,,,,,,アストリーのうさぎ,,,,,,,,,,,
"""


# Convert the CSV text into a list of lists
csv_data = list(csv.reader(csv_text.strip().split("\n")))

# Extract the venues, times, and artists
venues = csv_data[0]
times_artists = csv_data[1:]

# Initialize the dictionary to store artist schedules
artist_schedules = {}

# Process the times and artists to build the JSON structure
try:
    for i in range(0, len(times_artists), 2):
        if i + 1 >= len(times_artists):
            print(f"Skipping incomplete pair at line {i + 1}")
            continue

        times = times_artists[i]
        artists = times_artists[i + 1]

        for j in range(len(venues)):
            artist = artists[j].strip()
            if not artist:
                # Skip empty cells
                continue

            if artist not in artist_schedules:
                artist_schedules[artist] = []

            try:
                start_time, end_time = times[j].strip().split('-')
            except ValueError:
                print(f"Error processing time range for artist '{artist}' at venue '{venues[j]}': '{times[j]}'")
                continue

            schedule = {
                "place": venues[j],
                "start": start_time,
                "end": end_time
            }
            artist_schedules[artist].append(schedule)

except Exception as e:
    print(f"Error processing CSV data: {e}")

# Convert to JSON format
json_data = [{"artist": artist, "schedules": schedules} for artist, schedules in artist_schedules.items()]
json_output = json.dumps(json_data, ensure_ascii=False, indent=2)
print(json_output)
