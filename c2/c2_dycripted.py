# Step 1: Clean and prepare the ciphertext
ciphertext = """heins tasen ttsif ioreg theuf utteo eftrh nteer insne owtdd
ercln addnu reial civge athat htsob utehs owuty hstei netac
etirv esati fvonc malrt esnth heagk ipnir lecdt toath yeern
icmae ofplp ertih eofst etirm inlce sfeih ngetc orune tinej
uynfl yasot arwsn eoenk todoh eoopt ptuyn irtor eeitt atseh
ritrl onsgh eeldy bieaf tlhou drfte ravlg eornt meena snbuh
rdtah eepch tmern nwhhi ocurr foouh admet nengt rmits rofhf
ednom eader modcc yewea rrarn stcbe odbiy rffor uethc erasn
teure iaggo rserd sleas fytou orken onasw dieno hsasg asius
mtajs llpch aaerl intar gtera srynt hoegh ftbie rewsn ooenp
sadpa reane chenc btsws wsheo ixity smuti esnae dvarr itinn
geafr tigdh nixng eeosd eopnt akbra orsao regiz oatni stcha
ntlla ecota laysn edsoe lnlrp oerus aloin nfman tiros amcoa
mdiet yowen uotrj ttial skgel mania nndcs oacst ltisw terte
lkoin agrmc eduit ihona sbint saada aildy tiivi ctsly esetu
tkhio natoa bdrer einkg issts xafre inagn drusi tmapd eyufa
dfeow retli ecanu dfsrt rdats eorhm efrck teras ethru htsdb
atiao knerr iisga hguin tdues ycion rstif ngsoh onust asomf
cdoan bieps yinng uasen lldio uirpg racay tvove srtdi rsgth
eevee rnomt atndn oerkb rhors gthee veern omtdn oensd rtivt
eisui nhdtr myass chias uwliy nglla ritip catte wpiin hitht
reual egltr ypiai eesat rheer etsrc shear dvier aterd sasnn
teeri nconm ptaes ewhio cogur nasue cheba viioh rnoat sftet
rheti inian fclrn evaee mlodu entli reeup tonyi ixity smuto
esnfe xlamr ppoei netou wthdo hegla trsta daetr ohkeb rsceo
lalte adocn erfag vefth eeinn dtreu ddboi tisin mfofr tinon
aoora etmht wnohn ureld mdiio enalm ictan rsese eahro tpsun
sctee detro trirs buttr saerr evhed atycy izean sihin egtvh
ronnl iidie areis onlds uertn edath iemhw hohut ttirw kneoe
drgel oppar oavas sthli itiua stncs omoeo ltigt hvern feuhe
mrwte stoas ukrse eluvt weoqs utiao nssew aeork hagvi ynuri
onole avctn itine siaco nntde miane tddmi ornep onrtm awhaa
ttcwe bdona utnit oswdn enoao tshed rrghu eattt eheab twoea
spwob ulnda noewe wldei nrtne dtorr riinw ehheo ndctn drene
cptsi oynlu ntioo mahke stmee anesp ldoym eytsh ebnan hdoat
rsoim epsib lse""".replace('\n', ' ').replace(' ', '')

# Step 2: Convert to 7-column matrix (period = 7)
period = 7
rows = len(ciphertext) // period
matrix = [list(ciphertext[i:i+period]) for i in range(0, rows * period, period)]

# Step 3: Decryption function for a column permutation
def decrypt_with_perm(matrix, perm):
    return ''.join(''.join([row[i] for i in perm]) for row in matrix)

# Step 4: Scoring function using common trigrams
def english_score(text, top_trigrams=['the', 'and', 'ing', 'ent']):
    return sum(text.lower().count(t) for t in top_trigrams)

# Step 5: Try all permutations of columns (7! = 5040)
from itertools import permutations
all_perms = list(permutations(range(7)))
results = [(perm, english_score(decrypt_with_perm(matrix, perm)[:500])) for perm in all_perms]
results.sort(key=lambda x: x[1], reverse=True)

# Step 6: Get best permutation and decrypt full text
best_perm = results[0][0]  # best_perm = (5, 0, 1, 3, 4, 6, 2)
plaintext = decrypt_with_perm(matrix, best_perm)

# Step 7: Optional formatting for readability
import re
def format_plaintext(text):
    text = re.sub(r'(?<=[.?!])\s*', '\n', text.lower())
    sentences = re.split(r'(?<=[.?!])\s*', text)
    return '\n'.join(s.capitalize() for s in sentences if s)

# Final output
formatted = format_plaintext(plaintext[:2000])
print(formatted)
