from pycipher import Vigenere
from itertools import product
import string
from collections import Counter

# === Your ciphertext (letters only, no punctuation or spaces) ===

cipher_text = """
tboqj okauj ocduf qyvot aqzmi vsaxd sibif nxump ydqff fyair
atgie btifv ynkgg gsgqq bpxro bnhzp jafbj rotku gexbo cuwoh
ddube wditt utvrs glmfn nebfz ufqyv objhz ftboe agdpv qodxq
fribe xnzoc leqtx cohyq zrdid ztebh nieco gegzm aauun gdbll
zcgfa qzmmv shjsb fugee jsgtg voajs qmmrm pynob ihkgr duqec
kaztk augsg rjafl eazzs oetar inbea feqfe rkaeu fbdpz miabe
kwalk ihpez kcyvg pebez vhkaz ubpup ecnrk guapp jhqci ialeo
hvkug erszq inkrn czmmp nzesz lyvez yckqi afakq ltvql pezkc
yvgpe beoxx sgnbo tvplh rhufh uycoq xlkea taqbf spkgn jubsh
jppbo qtuow ydohi qkgyq geirs axdol zipqj bkfzp emrvs cjqaz
pnsbk uahjs btoqy goqbt jnocz qqfzf kajgf buoqm rczmi qotdh
ofkgs bjgft bxute rkgmf xpabo gtxuo gmdbu psanb esige hnutp
vuecw mqpre bbrpe csqzm nseha ufleb oczez zzqbb lazpa decug
sgkux pmtbf mgygj enons zfzuy cjhzp vvoay dsoha qoddo wmwdi
nblcy ommyn oobad fmual zchpq mzafe pffuk gzigp zreao pkhlr
eakug rrhrp kugpy noqyw slehs hiqfv ymgnj uzrdi zmiro lzqxp
ziwfa rzfje aramr ptboc nokbt rsajg ffhpl pzqrl tebcd dpfai
kgztk ausyt ybkgg wkbom bpkpk glmfa irfpy bbthd krygg tbaql
daase padxu zaifp ffukg ubsbz qblyo alffh lkizl dhaoy rqfff
yaira ppabl tklfv qxpvh kandb fvqqt euhby bsynb ocvar inqxp
zxkon blcii zpemf nkufb neypz gobjh szupb tgmsl zpwfy nezui
fqrhp pecla bufam qnijo lawda pwqfa opwfv uarmr bvjhm hyroa
kufaf ropka fqvep ercap zcocz uzrvo kbjhm tbpka xroxf eflyc
yqjef itheb ifkyn ralpb ygodo qhana tpopt plpcm hftqw paqss
bezfq dkggp lpcjs gihsr hbelt qecjo kgmxs iymzz jerpm gbpep
azoro gbkdi xhmpj imtjh zmeqz lfqnt bxkgl pecfo fqaqp oiezb
dioem qapeo ocumo cnblc ymffx beotb olaco ttqsg ocehi mocnq
jpkpo qdazf hplpj dapmp rpgba tkgec omfnt uscnf ecthu akqsz
upbtg msgtr sgzfe ctqso nbuss rotxu zblqe hnfsb uefnn daxir
oogaf nuuxl djogt xuaku zafek hcuqa jigtl qpafe slasb thpqt
qmfri ahleo zmiiz bqmfy iqzll uzlyv wtzur iipep gmglz izprj
gfups igblp xuzpe bktbg szzqa fhdsl gabpi lqpcb egiif tjddi
mvord idzte bsjbo cvubr raapj hurdc glkrs qjuzl yvsrp gbqev
madbl pmpas aqdfv pzmns dzaup zgqao yrzmn bwfmd nppbo qsvka
zrkqz uzmrz opvre coqzp kpkfe ufqku bcnsz lyvoq rs
"""

# Remove spaces and newlines
cipher_text = ''.join(cipher_text.split())

# === Score plaintext based on English letter frequencies ===
def score_plaintext(text):
    expected_freq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'.lower()
    counter = Counter(text)
    most_common = [c for c, _ in counter.most_common(6)]
    score = sum([expected_freq.index(c) if c in expected_freq else 26 for c in most_common])
    return score

# === Try all keys of a given length ===
def break_vigenere(ciphertext, key_length):
    best_score = float('inf')
    best_plain = ""
    best_key = ""

    for key_tuple in product(string.ascii_lowercase, repeat=key_length):
        key = ''.join(key_tuple)
        plain = Vigenere(key.upper()).decipher(ciphertext)
        score = score_plaintext(plain)
        if score < best_score:
            best_score = score
            best_plain = plain
            best_key = key

    return best_key, best_plain

# === Change this to test different key lengths (3–6 for speed) ===
key_length = 7
best_key, best_plaintext = break_vigenere(cipher_text, key_length)

print(f"\n✅ Best key (length {key_length}): {best_key.upper()}")
print("\n🔓 Decrypted text preview:\n")
print(best_plaintext[:1000])
