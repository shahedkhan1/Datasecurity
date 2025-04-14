import wordninja
import textwrap
import spacy

# === Load spaCy English model (first time: run `python -m spacy download en_core_web_sm`)
nlp = spacy.load("en_core_web_sm")

decrypted_text = (
    "IAMASICKMANIAMASPITEFULMANIAMANUNATTRACTIVEMANIBELIEVEMYLIVERISDISEASED"
    "HOWEVERIKNOWNOTHINGATALLABOUTMYDISEASEANDDONOTKNOWFORCERTAINWHATAILSME"
    "IDONTCONSULTADOCTORFORITANDNEVERHAVETHOUGHIHAVEARESPECTFORMEDICINEAND"
    "DOCTORSBESIDESIAMENTREMELYSUPERSTITIOUSSUFFICIENTLYSOTORESPECTMEDICINE"
    "ANYWAYIAMWELLEDUCATEDENOUGHNOTTOBESUPERSTITIOUSBUTIAMSUPERSTITIOUSNOIR"
    "EFUSETOCONSULTADOCTORFROMSPITETHATYOUPROBABLYWILLNOTUNDERSTANDWELLIUND"
    "ERSTANDITTHOUGHOFCOURSEICANTENPLAINWHOITISPRECISELYTHATIAMMORTIFYINGIN"
    "THISCASEBY"
)

# === Step 1: Word segmentation ===
split_text = ' '.join(wordninja.split(decrypted_text.lower()))

# === Step 2: Let spaCy split into sentences and correct basic punctuation ===
doc = nlp(split_text)

# === Step 3: Capitalize and format each sentence ===
sentences = [sent.text.capitalize() for sent in doc.sents]
formatted_output = "\n\n".join(textwrap.fill(s, width=80) for s in sentences)

# === Output ===
print(" Formatted Decrypted Text (with estimated punctuation):\n")
print(formatted_output)
